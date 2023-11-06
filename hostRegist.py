import pyzabbix
import pandas

# Initialization
url = "http://192.168.3.19/zabbix"
user = "Admin"
password = "zabbix"
csvPath = "./zabbixHostinfo.csv"
templateid=10577
groupid=21

zabbix = pyzabbix.ZabbixAPI(url)
zabbix.login(user,password)
df = pandas.read_csv(csvPath)

# Host interface to register
def createInterface(ip,mainParam):
    interface = {
        "type":1,
        "main":mainParam,
        "useip":1,
        "ip":ip,
        "dns":"",
        "port":"10050"
    }
    return interface

# Run registered host
def createHost(host,interfaces):
    zabbix.host.create(
        host=host,
        interfaces=interfaces,
        groups=[{"groupid":groupid}],
        templates=[{"templateid":templateid}]
    )

def main():
    # read csv file for every one row
    for rows in df.iterrows():
        row = rows[1]
        interfaces = []
        # If "IP1" item isn't nan, 
        # add the interface infomatin to the [interfaces] list and assign 0 to [mainParam]
        if(pandas.notna(row["IP1"])):
            interfaces.append(createInterface(row["IP1"],1))
            mainParam=0
        # If "IP2" item isn't nan and [interfaces] isn't empty, 
        # add the interface infomatin to the [interfaces] list and assign 0 to [mainParam]
        if(pandas.notna(row["IP2"])):
            if(interfaces == []):
                mainParam=1
            interfaces.append(createInterface(row["IP2"],mainParam))
            mainParam=0
        # If "IP3" item isn't nan and [interfaces] isn't empty, 
        # add the interface infomatin to the [interfaces] list and assign 0 to [mainParam]
        if(pandas.notna(row["IP3"])):
            if(interfaces == []):
                mainParam=1
            interfaces.append(createInterface(row["IP3"],mainParam))
            mainParam=0
        # If "IP4" item isn't nan and [interfaces] isn't empty, 
        # add the interface infomatin to the [interfaces] list and assign 0 to [mainParam]
        if(pandas.notna(row["IP4"])):
            if(interfaces == []):
                mainParam=1
            interfaces.append(createInterface(row["IP4"],mainParam))
            mainParam=0
        # If "IP5" item isn't nan and [interfaces] isn't empty, 
        # add the interface infomatin to the [interfaces] list and assign 0 to [mainParam]
        if(pandas.notna(row["IP5"])):
            if(interfaces == []):
                mainParam=1
            interfaces.append(createInterface(row["IP5"],mainParam))
            mainParam=0
        #If "IP6" item isn't nan and [interfaces] isn't empty, 
        # add the interface infomatin to the [interfaces] list and assign 0 to [mainParam]
        if(pandas.notna(row["IP6"])):
            if(interfaces == []):
                mainParam=1
            interfaces.append(createInterface(row["IP6"],mainParam))
            mainParam=0
        # Regist host to zabbix
        createHost(row["hostname"],interfaces)
        # When finish registration host to zabbix, empty [interfaces] list 
        interfaces.clear()

if __name__ == "__main__":
    main()