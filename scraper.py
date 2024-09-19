# MVP: A web scraper that will tell me the name of positions at all hospitals in my list that list 80% of REDCap jobs in Canada

import requests 
import hospitals
import os
from datetime import datetime

# Helper functions

# Create unique timestamp label for output file name
def createTimeStampString():
    now = datetime.now()
    return str(now.month) + "." + str(now.day) +  "." + str(now.year) + "." + str(now.hour) + "." + str(now.minute) + "." + str(now.second)

# Print output
def printOutput(timestamp, content):
    new_filename = "output.file.for." + timestamp + ".txt"
    with open("outputFile.txt", "a") as outputFile:
        # print("Data for: ", timestamp, content, file=outputFile)
        outputFile.write("Jobs for " + timestamp)
        outputFile.write(content)

# get test object from hospitals.py
from hospitals import UHN

# Get URL from hospitals property
url = UHN.url

# Send HTTP request to UHN jobs page
response = requests.get(url)

fileTimeStamp = createTimeStampString()

if response.status_code == 200:
    webpage_content = response.text
    fileTimeStamp = createTimeStampString()
    printOutput(fileTimeStamp, webpage_content)

else:
    print("Error")





