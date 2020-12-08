import mysql.connector
from mysql.connector import errorcode
import sshtunnel

#Settings
configFilePath = "config.local.txt"

#Get MySQL configuration
configFile = open(configFilePath, "r")
configRaw = []
for line in configFile:
    configRaw.append(line[:-1])
configRaw = configRaw[1:]
sshHost = configRaw[0]
sshUser = configRaw[1]
sshKey = configRaw[2]
dbUser = configRaw[3]
dbPass = configRaw[4]
dbSchema = configRaw[5]
print("Setup: Finished reading config")

with sshtunnel.SSHTunnelForwarder(
    ssh_address_or_host = sshHost,
    ssh_username = sshUser,
    ssh_pkey = sshKey,
    remote_bind_address = ('localhost', 3306)
) as tunnel:
    print("Setup: SSH Binding successful")
    conn = mysql.connector.connect(
        user = dbUser,
        password = dbPass,
        host = 'localhost',
        database = dbSchema,
        port = tunnel.local_bind_port,
    )

try:
    cursor = conn.cursor()
    print("Setup: Connection successful")
    cursor.execute('SELECT * FROM db_name.tableName;')
    arr = cursor.fetchall()
    print(arr)
    cursor.close()
except:
    print("Setup: Connection failed")