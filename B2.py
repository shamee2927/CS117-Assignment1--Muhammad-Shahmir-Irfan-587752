# Reads the value of each series resistor and prints the total resistance.
count=int(input("How many resistors?"))
total_resistance=0
for number in range(1,count + 1):
    resistance=float(input("Enter R" + str(number) + ":"))
    total_resistance=total_resistance + resistance
print("Total resistance =",total_resistance,"ohm")
