
f= open ("output.txt",'w')
import math

def calculate_core_area(power, current_density, secondary_voltage):
    return round(power / (current_density * secondary_voltage), 7)

def calculate_primary_secondary_turns(primary_voltage, secondary_voltage):
    primary_turns = round(primary_voltage / math.sqrt(2), 7)
    secondary_turns = round(secondary_voltage / math.sqrt(2),7)
    return primary_turns, secondary_turns

power = float(input("transformer power (watts): "))
current_density = float(input("current density (A/cm²): "))
primary_voltage = float(input("primary voltage (volts): "))
secondary_voltage = float(input("secondary voltage (volts): "))


core_area = calculate_core_area(power, current_density, secondary_voltage)
primary_turns, secondary_turns = calculate_primary_secondary_turns(primary_voltage, secondary_voltage)

print(f"area: {core_area}")
print(f"turns in primary coil: {primary_turns}")
print(f"turns in secondary coil: {secondary_turns}")


print(f"area: {core_area}",file=f)
print(f"turns in primary coil: {primary_turns}",file=f)
print(f"turns in secondary coil: {secondary_turns}",file=f)
f.write(f"area: {core_area}")
f.write(f"turns in primary coil: {primary_turns}")
f.write(f"turns in secondary coil: {secondary_turns}")    
f.close()    