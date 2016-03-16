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

sudo sed -i 's:Port 22:Port 65534:g' /etc/ssh/sshd_config
sudo service ssh reload

sudo mkdir /opt/kippo/
sudo svn checkout http://kippo.googlecode.com/svn/trunk/ /opt/kippo/
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