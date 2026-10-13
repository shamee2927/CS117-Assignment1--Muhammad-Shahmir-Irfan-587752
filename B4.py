# Finds the longest consecutive streak of strictly decreasing battery, voltage readings and prints its length, start voltage and end voltage.
voltages=[12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
best_length=1
best_start=0
current_length=1
current_start=0
for i in range(1,len(voltages)):
    if voltages[i]<voltages[i - 1]:
        current_length=current_length + 1
    else:
        current_length=1
        current_start=i
    if current_length>best_length:
        best_length=current_length
        best_start=current_start
best_end=best_start + best_length - 1
print("Longest continuous drop:",best_length,"minutes")
print("Started at:",voltages[best_start],"V")
print("Ended at:",voltages[best_end],"V")
