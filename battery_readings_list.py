voltage_readings = [12.6,12.4,12.8,11.9,12.5]
additional_reading= 12.7
corrected_fourth_reading = 12.1

voltage_readings.append(additional_reading)
voltage_readings[3] = corrected_fourth_reading

total = sum(voltage_readings)
average = total/len(voltage_readings)

print("Updated readings:",voltage_readings)
print("First three readings:",voltage_readings[:3])
print("total voltage:",total)
print("Average volatge:", average)