# Overview
This script is registration Host to zabbix with csv file.
csv file has host and host's interface information.
script read csv file every one row and regist host to zabbix.

# Execution environment
- Zabbix 6.0
- python 3.11
- pyzabbix
- pandas

# Environmental preparation 
Build zabbix enviroment refer below url

https://www.zabbix.com/download?zabbix=6.0&os_distribution=alma_linux&os_version=9&components=server_frontend_agent&db=mysql&ws=apache

Once zabbix is finished building , run the command below

```
dnf install python
pip install pyzabbix pandas
git clone <url>
```

Once the above command is executed, prepare csvFile.
the structure of csv file is as follows.
```
hostname,IP1,IP2,IP3,IP4,IP5,IP6
```

example:
```
hostname,IP1,IP2,IP3,IP4,IP5,IP6
test01,,192.168.4.2,1.1.1.102,172.231.4.10,10.176.3.56,
test02,10.1.1.2,,1.1.1.103,,10.176.3.57,
```

Once the above is complete , run hostRegist.py









