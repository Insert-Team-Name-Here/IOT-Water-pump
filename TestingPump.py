from gpiozero import LED
import time
#this will import the relevant modules we need for this code

relay = LED(14)
relay2 = LED(15)
#assigning the relays an LED

while True:
	relay.on()
	#you guessed it… turning the relay on
	relay.off()
	#you guessed it… turning the relay off
	time.sleep(1)
	#sleeping for 1 second
	relay.on()
	#relay on
	relay.off()
	#relay off
	time.sleep(1)
	#sleeping
