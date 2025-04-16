## old version

#import math
#radius = float(input("What is the radius of the circle?"))
#area = math.pi * radius ** 2
#circumference = 2 * math.pi * radius
#print(f"The area of the circle is: {area}")
#print(f"The circumference of the circle is: {circumference}")

## new version
import sys
import math

if len(sys.argv) != 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

radius = float(sys.argv[1])
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")
