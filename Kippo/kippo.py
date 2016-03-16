sudo apt-get update &> /dev/null

sudo sed -i 's:Port 22:Port 65534:g' /etc/ssh/sshd_config
sudo service ssh reload

sudo mkdir /opt/kippo/
sudo git clone https://github.com/desaster/kippo.git /opt/kippo/
sudo cp /tmp/kippo.cfg /opt/kippo/

sudo useradd -r -s /bin/false kippo

sudo mkdir -p /var/kippo/dl
sudo mkdir -p /var/kippo/log/tty
sudo mkdir -p /var/run/kippo

sudo rm -rf /opt/kippo/dl
sudo rm -rf /opt/kippo/log

sudo chown -R kippo:kippo /opt/kippo/
sudo chown -R kippo:kippo /var/kippo/
sudo chown -R kippo:kippo /var/run/kippo/

sudo wget https://raw.github.com/andrewmichaelsmith/honeypot-setup-script/master/init/kippo -O /etc/init.d/kippo

sudo chmod +x /etc/init.d/kippo

sudo update-rc.d kippo defaults

sudo /etc/init.d/kippo start