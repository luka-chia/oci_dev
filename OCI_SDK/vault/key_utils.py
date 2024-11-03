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
def decrypt_data(text):
    decrypt_response = key_management_client.decrypt(
        decrypt_data_details=oci.key_management.models.DecryptDataDetails(
            ciphertext=text,
            key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljruq4lh56kweifac52ivi7ospqtn4o4txqaynbn5ibdybexo7uqygq",
            encryption_algorithm="RSA_OAEP_SHA_256"))

def encrypt_data(text):
    print(f"plaintext = {text}")
    encrypt_response = key_management_client.encrypt(
    encrypt_data_details=oci.key_management.models.EncryptDataDetails(
        #key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljrpdnyrb6ct2snpchu6udwdl5b4e6oodt6ddc66in52qvxdr3nbuea",
        key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljruq4lh56kweifac52ivi7ospqtn4o4txqaynbn5ibdybexo7uqygq",
        plaintext=text,
        encryption_algorithm="RSA_OAEP_SHA_256"))

    # Get the data from response
    print(encrypt_response.data)
    ciphertext = encrypt_response.data.ciphertext

def decode_b64(text):
    decoded_data = base64.b64decode(text.encode('utf-8'))
    print(f"Encoded: {decoded_data}")
    return decoded_data.decode('utf-8')

def encode_b64(text):
    encoded_data = base64.b64encode(text.encode('utf-8'))
    print(f"Encoded: {encoded_data.decode('utf-8')}")
    return encoded_data.decode('utf-8')

if __name__ == "__main__":
    #results = search_by_user("luka", "OracleCanton10##")
    #origin_text = "abddddkjhyfiakahsfkhakshfkashdfkhasfhkashfkshfdkdahkfddddakfhdddkjhyfiaysfudkhkashfdkahskfhakuhdfkahsfkhakshfkashdfkhasfhkashfkshfdkdahkfhakfhdddddkjhykfhdddddkjhyfiaysfudkhkashfdkahskfhakend"
    #print(json.dumps(results))
    #plaintext = encode_b64(origin_text)
    #plaintext = u"L2FwaS9teWJhbmsvb3NwYXkvZW50ZXJwcmlzZS9nbG9iYWxjYXNobWFuYWdlbWVudC9tb2VnZ2xvYmFscGF5c3VibWl0L1YxP2FwcF9pZD0xMTAwMDAwMDAwMDAwMDAxNTM1MSZiaXpfY29udGVudD17dHJhbnNfY29kZToiR0xPQkFMUEFZIix0cmFuX2RhdGU6IjIwMTkwMTAxIix0cmFuX3RpbWU6IjEwMzIzMTAwMSIsbGFuZ3VhZ2U6InpoX0NOIixmX3NlcV9ubzoiR0xPQkFMUEFZMjAzNzYxMzU5MyIsemlwX2ZsYWc6IjAiLHppcDoiVUVzREJCUUFDQWciLHRvdGFsX251bToxLHRvdGFsX2FtdDoxMDB9bXNnX2lkPXVyY25sMjRjaXV0cjkmZm9ybWF0PWpzb24mY2hhcnNldD11dGYtOCZzaWduX3R5cGU9Q0EmJnRpbWVzdGFtcD0yMDI0LTEwLTMxIDA4OjAwOjAwIg=="
    #decode_b64(plaintext)
    encrypt_data("L2FwaS9teWJhbmsvb3NwYXkvZW50ZXJwcmlzZS9nbG9iYWxjYXNobWFuYWdlbWVudC9tb2VnZ2xvYmFscGF5c3VibWl0L1YxP2FwcF9pZD0xMTAwMDAwMDAwMDAwMDAxNTM1MSZiaXpfY29udGVudD17dHJhbnNfY29kZToiR0xPQkFMUEFZIix0cmFuX2RhdGU6IjIwMTkwMTAxIix0cmFuX3RpbWU6IjEwMzIzMTAwMSIsbGFuZ3VhZ2U6InpoX0NOIixmX3NlcV9ubzoiR0xPQkFMUEFZMjAzNzYxMzU5MyIsemlwX2ZsYWc6IjAiLHppcDoiVUVzREJCUUFDQWciLHRvdGFsX251bToxLHRvdGFsX2FtdDoxMDB9bXNnX2lkPXVyY25sMjRjaXV0cjkmZm9ybWF0PWpzb24mY2hhcnNldD11dGYtOCZzaWduX3R5cGU9Q0EmJnRpbWVzdGFtcD0yMDI0LTEwLTMxIDA4OjAwOjAwIg==")
    




