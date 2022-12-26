# Create Environment 
Ubuntu, t2micro, generate key (or select existing), select default security group, configure storage: 20, 
modify IAM role > select AmazonS3fullaccess, user must have SSH security access, connect with putty, log into server as user: ubuntu

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

aws key

aws secret key

us-east-1

json
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

touch nppes_archive_s3.sh
nano nppes_archive_s3.sh

#!/bin/bash
aws s3 sync nppesdump/ s3://viquity-database-import-us-east-1/Jobs/nppes/nppes_archive/nppesdump-"$(date +%d-%m-%y-%H-%M)"/

ctrl X
Y

---------------------------------
touch nppes_clean.sh
nano nppes_clean.sh

#!/bin/bash
rm -rf nppesdump

ctrl X
Y
---------------------------------
touch nppes_cron.sh
nano nppes_cron.sh

#!/bin/bash
cd /home/ubuntu/nppes
python3 nppes_cron.py

ctrl X
Y
---------------------------------

touch nppes_dump_to_s3.sh
nano nppes_dump_to_s3.sh

#!/bin/bash
aws s3 sync nppesdump/ s3://viquity-database-import-us-east-1/Jobs/nppes/nppes_current_dump/nppesdump/

ctrl X
Y
---------------------------------

touch nppes_remove_old_dump.sh
nano nppes_remove_old_dump.sh

#!/bin/bash
aws s3 rm s3://viquity-database-import-us-east-1/Jobs/nppes/nppes_current_dump --recursive

ctrl X
Y
```

# Delete Original bash files
```
rm archive_s3.sh  clean.sh  cron.sh  dump_to_s3.sh  remove_old_dump.sh 
```

# Change Permissions of bash Files
```
chmod +x   nppes_archive_s3.sh  nppes_clean.sh  nppes_cron.sh  nppes_dump_to_s3.sh  nppes_remove_old_dump.sh     

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

pip install -r nppes_requirements.txt 

nano /etc/crontab
```
# Create Cron Job ~ https://crontab.guru/examples.html
```
0 0 17 * *  root bash /home/ubuntu/nppes/nppes_cron.sh
!!!CARRIAGE RETURN after line above!!!!!

ctrl x

y

enter
```
