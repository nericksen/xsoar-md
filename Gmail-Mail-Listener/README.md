
# Mail Listener Integration with Gmail
You can use a gmail account to test the XSOAR mail listener and run phishing excursuses.
You will need to set insecure apps in the gmail account.  

<img src="account-settings.png" alt="alt text" width="500px">

The security settings are located on the left hand menu.

<img src="account-security-settings.png" alt="alt text" width="500px">

The insecure apps feature can then be turned on to enable testing.
This should only be done with a testing account!

<img src="insecure-apps.png" alt="alt text" width="500px">

The integration settings are then as follows


## GMAIL Listener
```
Mail server hostname: imap.gmail.com
IMAP Port: 993

Use TLS for connection
Don't verify certificate
```

## GMAIL Sender
```
Hostname: smtp.gmail.com
Port: 587

Don't verify certificate
STARTTLS for connection type
```

