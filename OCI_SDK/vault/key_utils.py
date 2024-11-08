import oci
import base64
import hashlib
import inspect
import os
 
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
            key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljry7luc2femaiojbpk77yn3fzgdcmwbjrhbrkmzq2su7ftmr2oiwpa",
            encryption_algorithm="RSA_OAEP_SHA_256"))

def encrypt_data(text):
    print(f"plaintext = {text}")
    encrypt_response = key_management_client.encrypt(
    encrypt_data_details=oci.key_management.models.EncryptDataDetails(
        #key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljrpdnyrb6ct2snpchu6udwdl5b4e6oodt6ddc66in52qvxdr3nbuea",
        key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljry7luc2femaiojbpk77yn3fzgdcmwbjrhbrkmzq2su7ftmr2oiwpa",
        plaintext=text,
        encryption_algorithm="SHA_256_RSA_PKCS_PSS"))

    # Get the data from response
    print(encrypt_response.data)
    ciphertext = encrypt_response.data.ciphertext

def decode_b64(text):
    decoded_data = base64.b64decode(text.encode('utf-8'))
    print(f"Encoded: {decoded_data}")
    return decoded_data.decode('utf-8')

def encode_b64(text):
    encoded_data = base64.b64encode(text)
    print(f"Encoded: {encoded_data.decode('utf-8')}")
    return encoded_data.decode('utf-8')
def verify_data(text, message):
    verify_response = key_management_client.verify(
    verify_data_details=oci.key_management.models.VerifyDataDetails(
        key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljry7luc2femaiojbpk77yn3fzgdcmwbjrhbrkmzq2su7ftmr2oiwpa",
        signature=text,
        message=message,
        signing_algorithm="SHA_256_RSA_PKCS1_V1_5",
        message_type="DIGEST"))

    # Get the data from response
    print(verify_response.data)

def sign_data(text=None):
    #text="L2FwaS9teWJhbmsvb3NwYXkvZW50ZXJwcmlzZS9nbG9iYWxjYXNobWFuYWdlbWVudC9tb2VnZ2xvYmFscGF5c3VibWl0L1YxP2FwcF9pZD0xMTAwMDAwMDAwMDAwMDAxNTM1MSZiaXpfY29udGVudD17dHJhbnNfY29kZToiR0xPQkFMUEFZIix0cmFuX2RhdGU6IjIwMTkwMTAxIix0cmFuX3RpbWU6IjEwMzIzMTAwMSIsbGFuZ3VhZ2U6InpoX0NOIixmX3NlcV9ubzoiR0xPQkFMUEFZMjAzNzYxMzU5MyIsemlwX2ZsYWc6IjAiLHppcDoiVUVzREJCUUFDQWciLHRvdGFsX251bToxLHRvdGFsX2FtdDoxMDB9bXNnX2lkPXVyY25sMjRjaXV0cjkmZm9ybWF0PWpzb24mY2hhcnNldD11dGYtOCZzaWduX3R5cGU9Q0EmJnRpbWVzdGFtcD0yMDI0LTEwLTMxIDA4OjAwOjAwIg=="
    text="/api/mybank/ospay/enterprise/globalcashmanagement/moegglobalpaysubmit/V1?app_id=11000000000000005251&biz_content={trans_code:GLOBALPAY,tran_date:20190101,tran_time:103231001,language:zh_CN,f_seq_no:GLOBALPAY2037613593,zip_flag:0,zip:UEsDBBQACAg,total_num:1,total_amt:100}&charset=UTF-8&format=json&msg_id=urcnl24ciutr9&sign_type=RSA2&timestamp=2024-11-01 15:51:59"
    hash_object = hashlib.sha256()
    hash_object.update(text.encode('utf-8'))
    digest = hash_object.digest()
    print(u"digest返回的摘要: %s"% digest)

    digest_base64 = encode_b64(digest)
    sign_response = key_management_client.sign(
    sign_data_details=oci.key_management.models.SignDataDetails(
        message=digest_base64,
        key_id="ocid1.key.oc1.ap-singapore-1.gzs6a4j6aabvg.abzwsljry7luc2femaiojbpk77yn3fzgdcmwbjrhbrkmzq2su7ftmr2oiwpa",
        signing_algorithm="SHA_256_RSA_PKCS1_V1_5",
        message_type="DIGEST"))
    # Get the data from response
    print(sign_response.data)
    print("begin verify ===========================================================")
    signature = sign_response.data.signature
    verify_data(signature, digest_base64)


if __name__ == "__main__":
    #results = search_by_user("luka", "OracleCanton10##")
    #origin_text = "abddddkjhyfiakahsfkhakshfkashdfkhasfhkashfkshfdkdahkfddddakfhdddkjhyfiaysfudkhkashfdkahskfhakuhdfkahsfkhakshfkashdfkhasfhkashfkshfdkdahkfhakfhdddddkjhykfhdddddkjhyfiaysfudkhkashfdkahskfhakend"
    #print(json.dumps(results))
    #plaintext = encode_b64(origin_text)
    #plaintext = u"L2FwaS9teWJhbmsvb3NwYXkvZW50ZXJwcmlzZS9nbG9iYWxjYXNobWFuYWdlbWVudC9tb2VnZ2xvYmFscGF5c3VibWl0L1YxP2FwcF9pZD0xMTAwMDAwMDAwMDAwMDAxNTM1MSZiaXpfY29udGVudD17dHJhbnNfY29kZToiR0xPQkFMUEFZIix0cmFuX2RhdGU6IjIwMTkwMTAxIix0cmFuX3RpbWU6IjEwMzIzMTAwMSIsbGFuZ3VhZ2U6InpoX0NOIixmX3NlcV9ubzoiR0xPQkFMUEFZMjAzNzYxMzU5MyIsemlwX2ZsYWc6IjAiLHppcDoiVUVzREJCUUFDQWciLHRvdGFsX251bToxLHRvdGFsX2FtdDoxMDB9bXNnX2lkPXVyY25sMjRjaXV0cjkmZm9ybWF0PWpzb24mY2hhcnNldD11dGYtOCZzaWduX3R5cGU9Q0EmJnRpbWVzdGFtcD0yMDI0LTEwLTMxIDA4OjAwOjAwIg=="
    #decode_b64(plaintext)
    #encrypt_data("L2FwaS9teWJhbmsvb3NwYXkvZW50ZXJwcmlzZS9nbG9iYWxjYXNobWFuYWdlbWVudC9tb2VnZ2xvYmFscGF5c3VibWl0L1YxP2FwcF9pZD0xMTAwMDAwMDAwMDAwMDAxNTM1MSZiaXpfY29udGVudD17dHJhbnNfY29kZToiR0xPQkFMUEFZIix0cmFuX2RhdGU6IjIwMTkwMTAxIix0cmFuX3RpbWU6IjEwMzIzMTAwMSIsbGFuZ3VhZ2U6InpoX0NOIixmX3NlcV9ubzoiR0xPQkFMUEFZMjAzNzYxMzU5MyIsemlwX2ZsYWc6IjAiLHppcDoiVUVzREJCUUFDQWciLHRvdGFsX251bToxLHRvdGFsX2FtdDoxMDB9bXNnX2lkPXVyY25sMjRjaXV0cjkmZm9ybWF0PWpzb24mY2hhcnNldD11dGYtOCZzaWduX3R5cGU9Q0EmJnRpbWVzdGFtcD0yMDI0LTEwLTMxIDA4OjAwOjAwIg==")
    sign_data()




