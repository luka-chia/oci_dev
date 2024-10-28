import oci
import base64
 
config = oci.config.from_file()
config.update({"region": "ap-singapore-1"})


# Initialize service client with default config file
key_management_client = oci.key_management.KmsCryptoClient(
    config, "https://gzs6a4j6aabvg-crypto.kms.ap-singapore-1.oci.oraclecloud.com")


# Send the request to service, some parameters are not required, see API
# doc for more info
data = "Hello, Oracle!"
encoded_data = base64.b64encode(data.encode('utf-8'))
print(f"Encoded: {encoded_data.decode('utf-8')}")


encrypt_response = key_management_client.encrypt(
    encrypt_data_details=oci.key_management.models.EncryptDataDetails(
        #key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljrpdnyrb6ct2snpchu6udwdl5b4e6oodt6ddc66in52qvxdr3nbuea",
        key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljruq4lh56kweifac52ivi7ospqtn4o4txqaynbn5ibdybexo7uqygq",
        plaintext=encoded_data.decode('utf-8'),
        encryption_algorithm="RSA_OAEP_SHA_256"))

# Get the data from response
print(encrypt_response.data)
ciphertext = encrypt_response.data.ciphertext


decrypt_response = key_management_client.decrypt(
    decrypt_data_details=oci.key_management.models.DecryptDataDetails(
        ciphertext=ciphertext,
        key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljruq4lh56kweifac52ivi7ospqtn4o4txqaynbn5ibdybexo7uqygq",
        encryption_algorithm="RSA_OAEP_SHA_256"))

# Get the data from response
print(decrypt_response.data)
decoded_data = base64.b64decode(decrypt_response.data.plaintext.encode('utf-8'))
print(f"Encoded: {decoded_data.decode('utf-8')}")