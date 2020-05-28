"""
NOTE: Add to start up sequence once notes are completed
"""

#!/usr/bin/python3
import smtplib, ssl, datetime, time, os, random
from random import randrange
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Simply file path
programPath = "/home/connor/Documents/Projects/PythonServer/PlankEmailer/"
etcPath = "/home/connor/Documents/Etc/"

# Picks random set of lecture notes and finds date
files = list(os.listdir(programPath + "Notes"))
file = random.choice(files)
day = datetime.today().weekday()

# Compare with most recent send data
with open(etcPath + "mostRecentSendNotes.txt", "r") as lastDateSent:
    data = lastDateSent.read().splitlines()
    
    # Check for matching dates
    if (str(day) == data[0]):
        exit(0)
    else:
        # Checks for matching notes file
        while(str(data[1]) == str(file)):
            file = random.choice(files)

        # Write over file with new date and poem entry
        with open(etcPath + "mostRecentSendNotes.txt", "w") as writeNewDate:
            writeNewDate.write(str(day) + '\n')
            writeNewDate.write(str(file))

# Set up server and login
sender = "PlankByteSizeNotes@gmail.com"
passwordFile = open(etcPath + "plankEmailerPassword.txt", "r")
password = passwordFile.read()
server = smtplib.SMTP_SSL("smtp.gmail.com")
server.login(sender, str(password))

# Set up message headers
message = MIMEMultipart("alternative")
message["Subject"] = "Byte Sized Notes"
message["From"] = sender

# Set up message body
htmlFile = open(programPath + "Notes/" + str(file) + ".html", "r")

# Convert message to object
htmlObject = MIMEText(htmlFile.read(), "html")

# Attach to objects to message
message.attach(htmlObject)

# Loops and sends email per person
with open(etcPath + "students.txt", "r") as recieverFile:
    for person in recieverFile.readlines():
        message["To"] = person
        server.sendmail(sender, person, message.as_string())

# Turn off the server and close files
server.quit()
htmlFile.close()
exit(0)