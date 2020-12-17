# Self Signed Certs with XSOAR

## Generate Certificate Authority (CA)

```
openssl req -x509 -nodes -new -sha256 -days 1024 -newkey rsa:2048 -keyout RootCA.key -out RootCA.pem -subj "/C=US/CN=Example-Root-CA"

openssl x509 -outform pem -in RootCA.pem -out RootCA.crt
```

You can change the name of the files as well as the Common Name or `CN=<your-cn-here>`.


## Create Domain Certificate

Create a file called `domains.ext` configured with the `alt_names`.

```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = fake1.local
IP.1 = 100.x.y.z
```

You can add DNS entries or IP addresses to the `domains.ext` file.
An example IP entry is listed above.
A domain would have to be either a valid public domain, or you will need to modify your `/etc/hosts` file to point the IP address to the required domain. 

Example `/etc/hosts` for `fake1.local`

```
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost

52.x.y.z fake1.local
```


## Generate the Domain Certificate, Key and CSR

```
openssl req -new -nodes -newkey rsa:2048 -keyout localhost.key -out localhost.csr -subj "/C=US/ST=YourState/L=YourCity/O=Example-Certificates/CN=localhost.local"

openssl x509 -req -sha256 -days 1024 -in localhost.csr -CA RootCA.pem -CAkey RootCA.key -CAcreateserial -extfile domains.ext -out localhost.crt
```

## Create the Domain Certificate PEM File
```
cat localhost.crt >> cert.pem
cat RootCA.crt >> cert.pem
```

## Replace Existing Keys on XSOAR Server

```
sudo cp localhost.key /usr/local/demisto/cert.key
sudo cp cert.pem /usr/local/demisto/cert.pem
```

## XSOAR Notes
You can change the location of the certificate by modifying the `/etc/demisto.conf` file with the following properties
```
{  
  "Security":{  
    "CertFile":"",
    "KeyFile":""
  }
}
```

If the private key is encrypted you can store the password in a one time configuration file and restart the server for the changes to take effect

```
echo "{\"keypass\":\"certpassword\"}" >> /var/lib/demisto/otc.conf.json
```
where `certpassword` is the private key password.

The server can be restarted on RHEL based linux systems with 

`systemctl restart demisto`


## Testing on Mac Locally
You can now go to the url of your XSOAR server. For instance in the Chrome browser on Mac OS.

![Chrome untrusted](invalid-cert-chrome.png =500x)

The CA you created in the first step can be trusted by adding it to the Mac keychain.  For Windows see the links in the References section.

Copy the `RootCA.pem` file from the XSOAR server to your local machine and add it to the keychain.  Open the Keychain Access app and select File >> Import Items.  

![custom cert](import-cert.png =500x)

Select the RootCA.pem file you just created. Once it is imported double click on the certificate to open up its settings in Keychain Access.  Select to Trust Always and then exit.  You will be prompted for your password.

![trust cert](always-trust.png =500x) 

You should now be able to navigate to the XSOAR page and see a secure lock for HTTPS served with your new custom cert.

### References
https://gist.github.com/cecilemuller/9492b848eb8fe46d462abeb26656c4f8
https://docs.paloaltonetworks.com/cortex/cortex-xsoar/5-5/cortex-xsoar-admin/installation/post-installation-checklist/https-with-a-signed-certificate
