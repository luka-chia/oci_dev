import boto3

'''
s3 = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    endpoint_url=endpoint,
    config=Config(s3={"addressing_style": "virtual", "signature_version": 's3v4'}))
    us-ashburn-1
    ap-singapore-1
'''

s3 = boto3.resource(
    's3',
    aws_access_key_id="dab86fbac2ea5f22f6272de8b98648c12029e332",#"21d2908825241c2447fc43163cf13e3e04b91988",
    aws_secret_access_key="H8dCfP+ANWoENHwQcF0eYIVPezgYrgI4Rcfg/brwk/M=",#"PP8M7cDO88EUw7+IFsn9TUxwjqr2JNNkS6RGSvGzFE8=",
    region_name="us-ashburn-1", # Region name here that matches the endpoint
    endpoint_url="https://sehubjapacprod.compat.objectstorage.us-ashburn-1.oraclecloud.com" # Include your namespace in the URL
)
  
# Print out the bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
