#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_circ=False
button_tri=False
button_x=False
button_sq=False
button_up=False
button_down=False
button_right=False
button_left=False
button_l1=False
button_l2=False
button_r1=False
button_r2=False
try: 
	while True:
		button_circ=GPIO.input(4)
		button_tri=GPIO.input(5)
		button_x=GPIO.input(6)
		button_r1=GPIO.input(12)
		button_left=GPIO.input(13)
		button_r2=GPIO.input(16)
		button_sq=GPIO.input(17)
		button_down=GPIO.input(22)
		button_l1=GPIO.input(23)
		button_l2=GPIO.input(24)
		button_right=GPIO.input(26)
		button_up=GPIO.input(27)
		
		if not button_up:  #added not due to pull_up
			bU="U"
		else:
			bU="-"
			
		if not button_circ :
			bC="C"
		else:
			bC="-"
			
		if not button_tri :
			bT="T"
		else:
			bT="-"
			
		if not button_sq :
			bS="S"
		else:
			bS="-"
		
		if not button_x :
			bX="X"
		else:
			bX="-"
			
		if not button_down :
			bD="D"
		else:
			bD="-"
			
		if not button_left :
			bL="L"
		else:
			bL="-"
		
		if not button_right :
			bR="R"
		else:
			bR="-"
			
		if not button_l1 :
			bL1="L1"
		else:
			bL1="-"
			
		if not button_l2 :
			bL2="L2"
		else:
			bL2="-"
			
		if not button_r1 :
			bR1="R1"
		else:
			bR1="-"
			
		if not button_r2 :
			bR2="R2"
		else:
			bR2="-"
			
	
		print(bU+bC+bD+bL+bS+bT+bX+bL+bR+bL1+bR1+bL2+bR2) 
		time.sleep(0.1)

finally:
	GPIO.cleanup()
