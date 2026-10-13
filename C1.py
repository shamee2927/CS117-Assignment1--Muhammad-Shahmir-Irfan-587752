# Functions to calculate current (Ohm's law) and power dissipated.
def ohms_current(v,r):
    return v / r
def power_dissipated(i,r):
    return i**2 * r
current=ohms_current(12,6)
power=power_dissipated(current,6)
print("Current =",current,"A")
print("Power =",power,"W")
