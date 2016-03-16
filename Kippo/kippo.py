sudo wget https://raw.github.com/andrewmichaelsmith/honeypot-setup-script/master/scripts/iface-choice.py -O /tmp/iface-choice.py

if [ -d "$script_dir" ];
then
	cp /honeypot-setup-script/templates/kippo.cfg.tmpl /tmp/kippo.cfg
else
	
	sudo wget https://raw.github.com/andrewmichaelsmith/honeypot-setup-script/master/templates/kippo.cfg.tmpl -O /tmp/kippo.cfg
fi

if [ $(dpkg-query -W -f='${Status}' sudo 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
  #sudo package is not currently installed on this box
  echo '[Error] Please install sudo before contniuing (apt-get install sudo)'
  exit 1
fi

current_user=$(whoami)

if [ $(sudo -n -l -U ${current_user} 2>&1 | egrep -c -i "not allowed to run sudo|unknown user") -eq 1 ]
then
   echo '[Error]: You need to run this script under an account that has access to sudo'
   exit 1
fi

sudo apt-get update &> /dev/null
sudo apt-get -y install python-pip python-twisted python-dev iptables python-openssl
sudo pip install netifaces

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

sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
sudo iptables-save > /etc/iptables.rules

sudo echo '#!/bin/sh' >> /etc/network/if-up.d/iptablesload 
sudo echo 'iptables-restore < /etc/iptables.rules' >> /etc/network/if-up.d/iptablesload 
sudo echo 'exit 0' >> /etc/network/if-up.d/iptablesload 

sudo chmod +x /etc/network/if-up.d/iptablesload 

sudo wget https://raw.github.com/andrewmichaelsmith/honeypot-setup-script/master/init/kippo -O /etc/init.d/kippo

sudo chmod +x /etc/init.d/kippo

sudo update-rc.d kippo defaults

sudo /etc/init.d/kippo start
