sudo apt-get install ssmtp
cd /etc/ssmtp
sudo rm -f ssmtp.conf
sudo wget https://raw.githubusercontent.com/faris091/Test/Kippo/ssmtp.conf
sudo sed -i 's:root=postmaster:root=MyEmails:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:AuthUser=user:AuthUser=MyEmail:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:AuthPass=pass:AuthPass=MyPassword:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:rewriteDomain=:rewriteDomain=gmail.com:g' /etc/ssmtp/ssmtp.conf
sudo sed -i 's:hostname=Ubuntu:hostname=MyEmail:g' /etc/ssmtp/ssmtp.conf