import math

# Input radius with units
radius = float(input('Enter radius of circle in cm: ').strip())

# Calculate area
area = math.pi * radius ** 2

# Print result with units (cm²)
print(f'The area of circle having radius {radius} cm = {area:.2f} cm²')