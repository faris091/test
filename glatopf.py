sudo wget https://raw.githubusercontent.com/faris091/Test/Kippo/Kippo/scripts/iface-choice.py -O /tmp/iface-choice.py

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
sudo apt-get install -y python2.7 python-openssl python-gevent libevent-dev python2.7-dev build-essential make
sudo apt-get install -y python-chardet python-requests python-sqlalchemy python-lxml
sudo apt-get install -y python-beautifulsoup mongodb python-pip python-dev python-setuptools
sudo apt-get install -y g++ git php5 php5-dev liblapack-dev gfortran libmysqlclient-dev
sudo apt-get install -y libxml2-dev libxslt-dev
sudo apt-get dist-upgrade -y
sudo pip install --upgrade distribute

cd /opt
sudo git clone https://github.com/mushorg/glastopf.git
cd glastopf
sudo python setup.py install

cd /opt
sudo mkdir myhoneypot
cd myhoneypot
sudo glastopf-runner

sudo service apache2 stop
sudo sed -i 's:host = 0.0.0.0:host = 172.212.101.14:g' /opt/myhoneypot/glastopf.cfg

cd /opt/glastopf/
python /usr/local/bin/glastopf-runner > /dev/null 2>&1 &
