import RPI>GPIO as GPIO
import time

#setup for soil sensor
channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


# setup for motor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
DC_Motor_Pin1=11
DC_Motor_Pin2=13
GPIO.setup(DC_Motor_Pin1,GPIO.OUT)
GPIO.setup(DC_Motor_Pin2,GPIO.OUT)

#setup for led,buzzer
GPIO.setmode(GPIO.BCM)
buzzer=25
pirpin=26
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(pirpin,GPIO.IN)

#set up for temprature and humidity sensor
GPIO.setmode(GPIO.BCM)
greenled=24
redled=23
temp=4
GPIO.setup(greenled,GPIO.OUT)
GPIO.setup(redled,GPIO.OUT)
GPIO.setup(temp,GPIO.IN)

#code for soil sensor module


def callback1(channel):
	if GPIO.input(channel):
		print("no water detected")
		print("Motor clockwise")
		GPIO.output(DC_Motor_Pin1, GPIO.HIGH)
		GPIO.output(DC_Motor_Pin2, GPIO.LOW)
		endtime=time.time()+60 			# runs motor for 60 seconds
	else:
	print("water detected")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback1)


#code for motion detection module

def buzz(pirpin):
	print("motion detected")
	print("buzzer on")
	GPIO.output(buzzer,GPIO.HIGH)
	time.sleep(10)
	GPIO.output(buzzer,GPIO.LOW)
GPIO.add_event_detect(pirpin, GPIO.RISING, callback=buzz)

#code for temprature and humidity sensor

def temphum(temp)
	if GPIO.input(temp<20)
		GPIO.output(greenled,HIGH)
		time.sleep(10)
		GPIO.output(greenled,LOW)
	elif GPIO.input(temp>35)
		GPIO.output(redled,HIGH)
		time.sleep(10)
		GPIO.output(redled,LOW)
	else
		time.sleep(1)
 while True:
	time.sleep(10)