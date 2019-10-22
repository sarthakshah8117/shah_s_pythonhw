# look at the temperature and figure out what state water is in -solid, liquid, gas
# #set the temperature first- and turn our text input into a number => that's what int() does
temp =int(input("enter a temperatre"))

if temp < 4:
	print("water is frozen -a soid")

elif temp >4 and temp <100:	
	print("water is liquid")

elif temp >= 100:
	print("water is gas")		
