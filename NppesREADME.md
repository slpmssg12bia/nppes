# Update Environment 

```
sudo apt update 

sudo apt install unzip

sudo apt install python3-pip -y
```
# Install AWS CLI 
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install
```

# Configure AWS CLI
```
aws configure

AKIA6CZ442HWM64HSD7R

tnrbtyMG2j+iYOiXP2BiBwpwWCvfe77FDuQndsBM

us-east-1

json
```
Check the Buckets
```
aws s3 ls
```

# Clone Git Repository
```
git clone https://github.com/slpmssg12bia/nppes.git
```
# cd into the repository
```
cd nppes
```
# Recreate bash Files
```
touch nppes_clean.sh
nano nppes_clean.sh

#!/bin/bash
rm -rf dump
rm db.zip

ctrl X
Y
---------------------------------
touch nppes_dump_to_s3.sh
nano nppes_dump_to_s3.sh

#!/bin/bash
mkdir dump
mv *.csv *.pdf dump
aws s3 sync dump/ s3://viquity-database-import-us-east-1/Jobs/nppes/dump-"$(date +%d-%m-%y-%H-%M)"/

ctrl X
Y
------------------------
touch nppes_cron.sh
nano nppes_cron.sh

#!/bin/bash
cd /home/ubuntu/nppes
python3 /home/ubuntu/nppes/nppes_cron.py

ctrl X
Y
```
# Delete Original bash files
```
rm clean.sh  dump_to_s3.sh  cron.sh
```

# Change Permissions of .sh Files
```
chmod +x   nppes_clean.sh  nppes_dump_to_s3.sh  nppes_cron.sh
```

# install pip dependencies
```
pip install -r nppes_requirements.txt 
```
# install Cron jobs for Parsing
```
pwd

sudo apt-get install cron
```
# Open Cron Tab
```
sudo su

nano /etc/crontab
```
# Create Cron Job ~ https://crontab.guru/examples.html
```
0 0 1 * *  root bash /home/ubuntu/nppes/nppes_cron.sh
!!!CARRIAGE RETURN after line above!!!!!

ctrl x

y

enter
```
