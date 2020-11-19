import pyodbc

#Settings
configFilePath = "config.local.txt"

#Get MySQL configuration
configFile = open(configFilePath, "r")
configRaw = []
for line in configFile:
    configRaw.append(line[:-1])
configRaw = configRaw[1:]
dbDriver = configRaw[0]
dbServerName = configRaw[1]
dbSchemaName = configRaw[2]
dbUsername = configRaw[3]
dbPassword = configRaw[4]

conn = pyodbc.connect('DRIVER=' + dbDriver + ';SERVER=' + dbServerName + ';DATABASE=' + dbSchemaName + ';UID=' + dbUsername + ';PWD=' + dbPassword)

try:
    cursor = conn.cursor()
    print("Connection successful")
except:
    print("Connection failed")