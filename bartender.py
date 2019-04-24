import time
import sys
import RPi.GPIO as GPIO
from guizero import App, PushButton


GPIO.setmode(GPIO.BCM)
#Motor 1 Whiskey
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
#Motor 2 Rum
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
#Motor 3 Tequila
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
#Motor 4 Coke
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
#Motor 5 Sour Mix
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
#Motor 6 Pineapple
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

def pour(whiskey_time,rum_time,tequila_time,coke_time,sour_time,pineapple_time):
	start_time = time.time()
	numrunning=0
	turnon=True
	turnon2=True
	turnon3=True
	turnon4=True
	turnon5=True
	turnon6=True
	if(whiskey_time!=0):
		GPIO.output(17,GPIO.HIGH)
		numrunning+=1
	if(rum_time!=0):
		GPIO.output(27,GPIO.HIGH)
		numrunning+=1
	if(tequila_time!=0):
		GPIO.output(22,GPIO.HIGH)
		numrunning+=1
	if(coke_time!=0):
		GPIO.output(23,GPIO.HIGH)
		numrunning+=1
	if(sour_time!=0):
		GPIO.output(24,GPIO.HIGH)
		numrunning+=1
	if(pineapple_time!=0):
		GPIO.output(25,GPIO.HIGH)
		numrunning+=1
	print(numrunning)
	while(numrunning>0):
		current_time=time.time()
		if (whiskey_time!=0 and whiskey_time < current_time - start_time and turnon):
			GPIO.output(17,GPIO.LOW)
			numrunning-=1
			turnon=False;
		if (rum_time!=0 and rum_time < current_time - start_time and turnon2):
			GPIO.output(27,GPIO.LOW)
			numrunning-=1
			turnon2=False;
		if (tequila_time!=0 and tequila_time < current_time- start_time and turnon3):
			GPIO.output(22,GPIO.LOW)
			numrunning-=1
			turnon3=False;
		if (coke_time!=0 and coke_time < current_time- start_time and turnon4):
			GPIO.output(23,GPIO.LOW)
			numrunning-=1
			turnon4=False;
		if (sour_time!=0 and sour_time < current_time- start_time and turnon5):
			GPIO.output(24,GPIO.LOW)
			numrunning-=1
			turnon5=False;
		if (pineapple_time!=0 and pineapple_time < current_time- start_time and turnon6):
			GPIO.output(25,GPIO.LOW)
			numrunning-=1
			turnon6=False;
		#print(numrunning)
		
	

def rum_and_coke():
	pour(0,68,0,300,6,0)
	
def whiskey_and_coke():
	pour(68,0,0,300,0,0)
	
def tequila_and_coke():
	pour(0,0,68,300,0,0)
	
def whiskey_and_sour():
	pour(80,0,0,0,120,0)
	
def rum_and_sour():
	pour(0,80,0,0,120,0)
	
def tequila_and_sour():
	pour(0,0,80,0,120,0)
	
def the_special():
	pour(34,34,34,34,34,34)
	
def pineapple_whiskey_sour():
	pour(80,0,0,0,80,80)
	
def rum_and_pineapple():
	pour(0,68,0,0,0,160)

def tequila_and_pineapple():
	pour(0,0,68,0,0,160)
	
def whiskey_and_pineapple():
	pour(68,0,0,0,0,160)
	
def horsemen():
	pour(20,20,20,0,0,0)
	
def black_mamba():
	pour(40,0,14,106,0,0)
	
def rum():
	pour(0,30,0,0,0,0)

def coke():
	pour(0,0,0,300,0,0)
	
def whiskey():
	pour(30,0,0,0,0,0)
	


if __name__ == '__main__':
	app = App(layout='grid')
	h=7
	w=22
	button = PushButton(app, text="Rum & Coke", command=rum_and_coke,grid=[1,1],height=h,width=w )
	button1 = PushButton(app, text="Whiskey & Coke", command=whiskey_and_coke,grid=[2,1],height=h,width=w   )
	button2= PushButton(app, text="Tequila & Coke", command=tequila_and_coke,grid=[3,1],height=h,width=w  )
	button3 = PushButton(app, text="Whiskey & Sour", command=whiskey_and_sour,grid=[4,1],height=h,width=w  )
	button4 = PushButton(app, text="Rum & Sour", command=rum_and_sour,grid=[1,2],height=h,width=w  )
	button5 = PushButton(app, text="Tequila & Sour", command=tequila_and_sour ,grid=[2,2],height=h,width=w )
	button6 = PushButton(app, text="Rum & Pineapple", command=rum_and_pineapple,grid=[3,2],height=h,width=w )
	button7 = PushButton(app, text="Tequila & Pineapple", command=tequila_and_pineapple ,grid=[4,2],height=h,width=w )
	button8 = PushButton(app, text="Whiskey & Pineapple", command=whiskey_and_pineapple ,grid=[1,3],height=h,width=w )
	button9 = PushButton(app, text="3 Horsemen", command=horsemen ,grid=[2,3],height=h,width=w )
	button10 = PushButton(app, text="Black Mamba", command=black_mamba,grid=[3,3],height=h,width=w )
	button11 = PushButton(app, text="Rum", command=rum ,grid=[4,3],height=h,width=w )
	button12 = PushButton(app, text="Coke", command=coke ,grid=[1,4],height=h,width=w )
	button13 = PushButton(app, text="The Special", command=the_special,grid=[2,4],height=h,width=w )
	button14 = PushButton(app, text="Pineapple Whiskey Sour", command=pineapple_whiskey_sour,grid=[3,4],height=h,width=w )
	button15 = PushButton(app, text="Whiskey", command=whiskey ,grid=[4,4],height=h,width=w )
	app.set_full_screen()
	app.display()
	
