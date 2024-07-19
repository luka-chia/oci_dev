# python script for sending SMTP configuration with Oracle Cloud Infrastructure Email Delivery
import smtplib 
import email.utils
from email.message import EmailMessage
import ssl

# Replace sender@example.com with your "From" address.
# This address must be verified.
# this is the approved sender email
SENDER = 'luka@byd.hw69.cn'
SENDERNAME = 'luka_byd'
 
# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = '714250945@qq.com'
 
# Replace the USERNAME_SMTP value with your Email Delivery SMTP username.
USERNAME_SMTP = 'ocid1.user.oc1..aaaaaaaafkg344hepfwbzyrdzbi334q2ncyjforez3pw7kegmyqut5l7eorq@ocid1.tenancy.oc1..aaaaaaaaro7aox2fclu4urtpgsbacnrmjv46e7n4fw3sc2wbq24l7dzf3kba.tf.com'
 
# Put the PASSWORD value from your Email Delivery SMTP password into the following file.
PASSWORD_SMTP_FILE = 'ociemail.config'
 
# If you're using Email Delivery in a different region, replace the HOST value with an appropriate SMTP endpoint.
# Use port 25 or 587 to connect to the SMTP endpoint.
HOST = "smtp.email.ap-singapore-1.oci.oraclecloud.com"
PORT = 587
 
# The subject line of the email.
SUBJECT = 'Email Delivery Test (Python smtplib)'
 
# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Email Delivery Test\r\n"
             "This email was sent through the Email Delivery SMTP "
             "Interface using the Python smtplib package."
            )
 
# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Email Delivery SMTP Email Test</h1>
  <p>This email was sent with Email Delivery using the
    <a href='https://www.python.org/'>Python</a>
    <a href='https://docs.python.org/3/library/smtplib.html'>
    smtplib</a> library.</p>
</body>
</html>"""

# get the password from a named config file ociemail.config
with open(PASSWORD_SMTP_FILE) as f:
    password_smtp = f.readline().strip()

# create message container
msg = EmailMessage()
msg['Subject'] = SUBJECT
msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
msg['To'] = RECIPIENT

# make the message multi-part alternative, making the content the first part
msg.add_alternative(BODY_TEXT, subtype='text')
# this adds the additional part to the message
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.add_alternative(BODY_HTML, subtype='html')

# Try to send the message.
try: 
    server = smtplib.SMTP(HOST, PORT)
    server.ehlo()
    # most python runtimes default to a set of trusted public CAs that will include the CA used by OCI Email Delivery.
    # However, on platforms lacking that default (or with an outdated set of CAs), customers may need to provide a capath that includes our public CA.
    server.starttls(context=ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None))
    # smtplib docs recommend calling ehlo() before & after starttls()
    server.ehlo()
    server.login(USERNAME_SMTP, password_smtp)
    # our requirement is that SENDER is the same as From address set previously
    server.sendmail(SENDER, RECIPIENT, msg.as_string())
    server.close()
# Display an error message if something goes wrong.
except Exception as e:
    print(f"Error: {e}")
else:
    print("Email successfully sent!")