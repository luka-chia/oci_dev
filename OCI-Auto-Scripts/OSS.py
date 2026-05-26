from flask import Flask, render_template, request, jsonify
import requests
import os
import datetime
import hashlib
import hmac
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


# Create a requests session with SSL verification disabled for testing
session = requests.Session()
session.verify = False

app = Flask(__name__)


def load_private_key(private_key_path):
    password = os.getenv('PRIVATE_KEY_PASSWORD',
                         SAMPLE_ENV.get('PRIVATE_KEY_PASSWORD'))
    if password:
        password = password.encode('utf-8')
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=password,
        )
    return private_key


def oracle_sign_request(private_key, signing_string):
    signature = private_key.sign(
        signing_string.encode('utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')


def oracle_create_authorization_header(tenancy_ocid, user_ocid, fingerprint, signature, headers_list='date (request-target) host'):
    return f'Signature version="1",headers="{headers_list}",keyId="{tenancy_ocid}/{user_ocid}/{fingerprint}",algorithm="rsa-sha256",signature="{signature}"'


def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()


def get_signature_key(key, date_stamp, region_name, service_name):
    k_date = sign(('AWS4' + key).encode('utf-8'), date_stamp)
    k_region = sign(k_date, region_name)
    k_service = sign(k_region, service_name)
    k_signing = sign(k_service, 'aws4_request')
    return k_signing


def create_aws_authorization_header(access_key, secret_key, region, service, method, canonical_uri, canonical_querystring, canonical_headers, signed_headers, body_hash, date_header):
    date_stamp = date_header[:8]
    credential_scope = date_stamp + '/' + region + '/' + service + '/aws4_request'
    canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + \
        '\n' + canonical_headers + '\n' + signed_headers + '\n' + body_hash
    string_to_sign = 'AWS4-HMAC-SHA256\n' + date_header + '\n' + credential_scope + \
        '\n' + hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
    signing_key = get_signature_key(secret_key, date_stamp, region, service)
    signature = hmac.new(signing_key, string_to_sign.encode(
        'utf-8'), hashlib.sha256).hexdigest()
    authorization = 'AWS4-HMAC-SHA256 Credential=' + access_key + '/' + \
        credential_scope + ', SignedHeaders=' + \
        signed_headers + ', Signature=' + signature
    print(f"AWS Authorization: {authorization}")
    return authorization


def get_namespace(region, tenancy_ocid, user_ocid, fingerprint, private_key_path):
    # Get namespace requires authentication too
    # For simplicity, use a known endpoint or assume namespace is tenancy name or something
    # Actually, namespace can be derived or call the API
    # For now, let's assume it's the tenancy OCID part after the last dot or something
    # Better to call the get namespace API
    url = f'https://objectstorage.{region}.oraclecloud.com/n/'
    headers = {}
    # Sign the request
    date_header = datetime.datetime.now(
        datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
    headers['date'] = date_header
    headers['host'] = f'objectstorage.{region}.oraclecloud.com'

    signing_string = f'date: {date_header}\n(request-target): get /n/\nhost: {headers["host"]}'

    private_key = load_private_key(private_key_path)
    signature = oracle_sign_request(private_key, signing_string)
    headers['Authorization'] = oracle_create_authorization_header(
        tenancy_ocid, user_ocid, fingerprint, signature, 'date (request-target) host')

    print(f"Proxies for {url}: {requests.utils.get_environ_proxies(url)}")
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        namespace = response.text.strip().strip('"')
        print(f"Retrieved namespace: {namespace}")
        return namespace
    else:
        raise Exception(f'Failed to get namespace: {response.text}')


# Sample environment variables - replace with your actual values
SAMPLE_ENV = {
    'TENANCY_OCID': 'ocid1.tenancy.oc1..aaaaaaaaro7aox2fclu4urtpgsbacnrmjv46e7n4fw3sc2wbq24l7dzf3kba',
    'USER_OCID': 'ocid1.user.oc1..aaaaaaaaclzuo4gdptw7dmbkjpeplmwoyzxjijd5t3jr55we567vcak6mkmq',
    'FINGERPRINT': '50:a0:2b:1f:32:ee:15:0a:92:0f:91:54:85:be:37:f3',
    'PRIVATE_KEY_PATH': '/Users/stevli/Code/sshkey/cli/oci_api_key.pem',
    'REGION': 'us-ashburn-1',
    'COMPARTMENT_OCID': 'ocid1.compartment.oc1..aaaaaaaapzb3jds7nb5it4t5aoq2ytpyalfm7hidjashb7jmbgz3qboeuugq',
    'PRIVATE_KEY_PASSWORD': 'Oracle123',
    'AWS_ACCESS_KEY_ID': '7a7dd3b6d8cd97cc75a992174299d32a0977b06b',
    'AWS_SECRET_ACCESS_KEY': 'wcwiWwQSes1jUWOlHxav3p9Q4RqaC0E+c4YQYQ4Mw0A='
}


@app.route('/')
def index():
    return render_template('index.html', env=SAMPLE_ENV)


@app.route('/create_bucket', methods=['POST'])
def create_bucket():
    try:
        # Get form data
        bucket_name = request.form['bucket_name']
        compartment_ocid = request.form['compartment_ocid']
        method = int(request.form.get('method', 1))

        # Use sample env vars or override with actual ones if set
        tenancy_ocid = os.getenv('TENANCY_OCID', SAMPLE_ENV['TENANCY_OCID'])
        user_ocid = os.getenv('USER_OCID', SAMPLE_ENV['USER_OCID'])
        fingerprint = os.getenv('FINGERPRINT', SAMPLE_ENV['FINGERPRINT'])
        private_key_path = os.getenv(
            'PRIVATE_KEY_PATH', SAMPLE_ENV['PRIVATE_KEY_PATH'])
        region = os.getenv('REGION', SAMPLE_ENV['REGION'])
        aws_access_key = os.getenv(
            'AWS_ACCESS_KEY_ID', SAMPLE_ENV['AWS_ACCESS_KEY_ID'])
        aws_secret_key = os.getenv(
            'AWS_SECRET_ACCESS_KEY', SAMPLE_ENV['AWS_SECRET_ACCESS_KEY'])

        # Get namespace first - use standard Oracle endpoint
        namespace = get_namespace(
            region, tenancy_ocid, user_ocid, fingerprint, private_key_path)
        print(f"Using namespace: {namespace}, method: {method}")

        if method == 1:
            # OCI S3 Virtual Style API (vhcompat) with AWS SigV4
            region_full = f'{region}.oci.customer-oci.com'
            url = f'https://{bucket_name}.vhcompat.objectstorage.{region_full}/'
            host = f'{bucket_name}.vhcompat.objectstorage.{region_full}'
            method_http = 'PUT'
            body_str = ''
            use_aws_auth = True
        elif method == 2:
            # OCI S3 Path Style API (compat) with AWS SigV4
            region_full = f'{region}.oci.customer-oci.com'
            url = f'https://{namespace}.compat.objectstorage.{region_full}/{bucket_name}'
            host = f'{namespace}.compat.objectstorage.{region_full}'
            method_http = 'PUT'
            body_str = ''
            use_aws_auth = True
        elif method == 3:
            # OCI Native API (oraclecloud.com) with Oracle auth
            url = f'https://objectstorage.{region}.oraclecloud.com/n/{namespace}/b/'
            host = f'objectstorage.{region}.oraclecloud.com'
            method_http = 'POST'
            body = {
                "name": bucket_name,
                "compartmentId": compartment_ocid,
                "publicAccessType": "NoPublicAccess"
            }
            import json
            body_str = json.dumps(body)
            use_aws_auth = False
        else:
            return jsonify({'success': False, 'message': 'Invalid method'})

        headers = {}
        if use_aws_auth:
            # AWS SigV4
            date_header = datetime.datetime.now(
                datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
            headers['host'] = host
            headers['x-amz-date'] = date_header
            body_hash = hashlib.sha256(body_str.encode('utf-8')).hexdigest()
            headers['x-amz-content-sha256'] = body_hash

            canonical_uri = '/' if method == 1 else f'/{bucket_name}'
            canonical_querystring = ''
            canonical_headers = 'host:' + \
                headers['host'] + '\n' + 'x-amz-content-sha256:' + \
                body_hash + '\n' + 'x-amz-date:' + date_header + '\n'
            signed_headers = 'host;x-amz-content-sha256;x-amz-date'
            authorization = create_aws_authorization_header(aws_access_key, aws_secret_key, region, 's3', method_http,
                                                            canonical_uri, canonical_querystring, canonical_headers, signed_headers, body_hash, date_header)
            headers['Authorization'] = authorization
        else:
            # Oracle auth
            date_header = datetime.datetime.now(
                datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
            headers['date'] = date_header
            headers['host'] = host
            headers['content-type'] = 'application/json'
            headers['content-length'] = str(len(body_str))
            content_md5 = base64.b64encode(hashlib.md5(
                body_str.encode('utf-8')).digest()).decode('utf-8')
            headers['Content-MD5'] = content_md5
            headers['x-content-sha256'] = base64.b64encode(hashlib.sha256(
                body_str.encode('utf-8')).digest()).decode('utf-8')

            request_target = f'post /n/{namespace}/b/'
            signing_string = f'date: {date_header}\n(request-target): {request_target}\nhost: {headers["host"]}\ncontent-type: {headers["content-type"]}\nx-content-sha256: {headers["x-content-sha256"]}\ncontent-length: {headers["content-length"]}'

            private_key = load_private_key(private_key_path)
            signature = oracle_sign_request(private_key, signing_string)
            headers['Authorization'] = oracle_create_authorization_header(
                tenancy_ocid, user_ocid, fingerprint, signature, 'date (request-target) host content-type x-content-sha256 content-length')

        response = session.request(
            method_http, url, headers=headers, data=body_str)

        if response.status_code == 200:
            return jsonify({'success': True, 'message': f'Bucket "{bucket_name}" created successfully using method {method}!'})
        else:
            request_id = response.headers.get('opc-request-id', 'N/A')
            return jsonify({'success': False, 'message': f'Failed to create bucket: {response.status_code} {response.text} (Request ID: {request_id})'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5003)
