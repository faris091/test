#INSTALLING SMTP

sudo apt-get install ssmtp
cd /etc/ssmtp
vi ssmtp.conf

Config file for sSMTP sendmail

The person who gets all mail for userids < 1000
Make this empty to disable rewriting.
root=postmaster

 The place where the mail goes. The actual machine name is required no
 MX records are consulted. Commonly mailhosts are named mail.domain.com

mailhub=mail
mailhub=smtp.gmail.com:587

AuthUser=gostfaris94@gmail.com
AuthPass=
UseTLS=YES
UseSTARTTLS=YES

# Where will the mail seem to come from?
#rewriteDomain=
rewriteDomain=gmail.com

# The full hostname
hostname=gostfaris94@gmail.com

# Are users allowed to set their own From: address?
# YES - Allow the user to specify their own From: address
# NO - Use the system generated From: address
#FromLineOverride=YES

#SENT EMAIL
ssmtp [receipent email]

INSTALLING KIPPO
wget -q https://raw.githubusercontent.com/faris091/Test/Kippo/Kippo/kippo.py -O /tmp/setup.bash && bash /tmp/setup.bash
