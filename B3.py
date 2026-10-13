# Analyses sensor voltage readings in a single loop: count above 3.2 V,highest, lowest and average.
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count_above=0
highest=readings[0]
lowest=readings[0]
total=0
for reading in readings:
    if reading>3.2:
        count_above=count_above + 1
    if reading>highest:
        highest=reading
    if reading<lowest:
        lowest=reading
    total=total + reading
average=total / len(readings)
print("Readings above 3.2 V:",count_above)
print("Highest:",highest,"V")
print("Lowest:",lowest,"V")
print("Average:",round(average,2),"V")
