# link to instructiobns for main code: https://roboticadiy.com/motion-detection-video-captured-email-alert-using-raspberry-pi-4/
# Code to set pi to run program at start up https://www.dexterindustries.com/howto/auto-run-python-programs-on-the-raspberry-pi/
        
from gpiozero import MotionSensor, Button, LED
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from subprocess import call 
import os
import email.mime.application
import datetime
import smtplib
from time import sleep

button2 = Button(20)
button1 = Button(16)
led = LED(17)

#replace the next three lines with your credentials
from_email_addr = 'nemosdream131@gmail.com'
from_email_password = 'dreamingofnemo'
to_email_addr = 'devonriter@gmail.com'

#Create Alarm State by default it is off.
Alarm_state = False
sleep(30)

while True:

    if button1.is_pressed or button2.is_pressed:
        Alarm_state = True
        print('Alarm ON')

    if Alarm_state == True:
        led.on()
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
