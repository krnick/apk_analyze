git clone https://github.com/radare/radare2.git
radare2/sys/install.sh
#
sudo apt install python-pip
pip install pipenv


#install java
sudo apt install default-jre -y


#install apktool
sudo cp apktool/* /usr/local/bin/ 
sudo chmod +x /usr/local/bin/apktool.jar
sudo chmod +x /usr/local/bin/apktool

