import ntplib
from datetime import datetime
from time import ctime, sleep
import os

def cls():
    os.system("clear");

logfile = "log.txt"
ntpServer = "lul1.ntp.se"
referenceServer = "ntp.se"
ntpClient = ntplib.NTPClient()
oldStratum = 2;
while 1:
    try:
        responseNtp = ntpClient.request(ntpServer, version=4)
        responseReference = ntpClient.request(referenceServer, version=4)
    except:
        print("No response from NTP server")
    stratumNtp = responseNtp.stratum
    receivedNtp = responseNtp.ref_time
    receivedReference = responseReference.ref_time
    file = open(logfile, "a")
    file.write(str(datetime.now()) + ": Stratum " + str(stratumNtp) + " | Received time: " + str(datetime.fromtimestamp(receivedNtp)) + " | Reference time: " + str(datetime.fromtimestamp(receivedReference)) + "\n")
    cls();
    print(str(datetime.now()), ": Stratum", stratumNtp, "| Received time:", str(datetime.fromtimestamp(receivedNtp)), "| Reference time:", str(datetime.fromtimestamp(receivedReference)))
    if oldStratum != stratumNtp:
        file.write(str(datetime.now()) + ": WARNING - STRATUM CHANGE | PREVIOUS STRATUM " + str(oldStratum) + " | CURRENT STRATUM " + str(stratumNtp) + "\n")
    oldStratum = stratumNtp;
    file.close()
    sleep(1)