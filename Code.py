from gpiozero import MotionSensor, Button, LED
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from subprocess import call 
import os
import email.mime.application
import datetime
import smtplib
from time import sleep

led = LED(17)
button = Button(16)

#replace the next three lines with your credentials
from_email_addr = 'nemosdream131@gmail.com'
from_email_password = 'dreamingofnemo'
to_email_addr = 'devonriter@gmail.com'

#Create Alarm State by default it is off.
Alarm_state = False

while True:

    if button.is_pressed:
        Alarm_state = True
        print('Alarm ON')

    if Alarm_state == True:
        led.on()
        sleep(10)

            #Create the Message
            msg = MIMEMultipart()
            msg[ 'Subject'] = 'INTRUDER ALERT..!!'
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
