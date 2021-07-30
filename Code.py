from gpiozero import MotionSensor, Button, LED
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from subprocess import call 
import os
import email.mime.application
import datetime
import smtplib
from time import sleep

button2 = Button(17)
button1 = Button(16)
sudo tvservice --off
echo 0 | sudo tee /sys/devices/platform/soc/3f980000.usb/buspower >/dev/null
sudo ifconfig wlan0 down

#replace the next three lines with your credentials
from_email_addr = 'nemosdream131@gmail.com'
from_email_password = 'dreamingofnemo'
to_email_addr = 'devonriter@gmail.com'

#Create Alarm State by default it is off.
Alarm_state = False
sleep(3600)

while True:

    if button1.is_pressed or button2.is_pressed:
        Alarm_state = True
        print('Alarm ON')
        sudo ifconfig wlan0 up

    if Alarm_state == True:
        sleep(10)
        #Create the Message
        msg = MIMEMultipart()
        msg[ 'Subject'] = 'HYDROPONICS BIN DANGEROUSLY EMPTY!!'
        msg['From'] = from_email_addr
        msg['To'] = to_email_addr
        #send Mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email_addr, from_email_password)
        server.sendmail(from_email_addr, to_email_addr, msg.as_string())
        server.quit()
        print('Email sent')
        Alarm_state = False
        quit()
