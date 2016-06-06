sudo apt-get install ssmtp
cd /etc/ssmtp
sudo rm -f ssmtp.conf
sudo wget https://raw.githubusercontent.com/faris091/Test/Kippo/ssmtp.conf
sudo sed -i 's:root=postmaster:root=gostfaris94@gmail.com:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:AuthUser=user:AuthUser=gostfaris94@gmail.com:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:AuthPass=pass:AuthPass=Najiha1:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:rewriteDomain=:rewriteDomain=gmail.com:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:hostname=Ubuntu:hostname=gostfaris94@gmail.com:g' /etc/ssmtp/ssmtp.conf

ssmtp gost_faris@yahoo.com

To: gost_faris@yahoo.com
From: gostfaris94@gmail.com
Subject: test email

Hello World!