using System;

using MailKit.Net.Smtp;
using MailKit;
using MimeKit;
using MailKit.Security;

namespace Program {
    class TestOCIEmail
    {
        public static void Main (string[] args)
        {
            var message = new MimeMessage ();
            message.From.Add (new MailboxAddress ("Lujia_Oracle_CS", "luka@bydmail.hw69.cn"));
            message.To.Add (new MailboxAddress ("714250945", "714250945@qq.com"));
            message.Subject = "Mail from OCI ED service";

            message.Body = new TextPart ("Html") {
                Text = @"
                <h1>OCI Email Delivery test</h1>
                <p>This email was sent with OCI Email Delivery using the 
                <a href='https://github.com/jstedfast/MailKit'>MailKit Package</a>
                for .Net .</p>"
            };

            using (var client = new SmtpClient ()) {

                var host = "smtp.email.ap-singapore-1.oci.oraclecloud.com";
                var port = 465;
                var username = "ocid1.user.oc1..aaaaaaaafkg344hepfwbzyrdzbi334q2ncyjforez3pw7kegmyqut5l7eorq@ocid1.tenancy.oc1..aaaaaaaaro7aox2fclu4urtpgsbacnrmjv46e7n4fw3sc2wbq24l7dzf3kba.xs.com";
                var password = "+x7ZbDYxcSV}xd$#{PbM";
                
                client.Connect (host, port, true);

                client.Authenticate (username, password);

                client.Send (message);
                client.Disconnect (true);
            }
           Console.WriteLine("Email send successfully !!");
        }
    }
}