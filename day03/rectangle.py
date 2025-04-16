##old version
#height = float(input("What is the height of the rectangle?"))
#width = float(input("What is the width of the rectangle?"))
#area = height * width
#perimeter = 2 * (height + width)
#print(f"The area of the rectangle is: {area}")
#print(f"The perimeter of the rectangle is: {perimeter}")


## new version
import sys

if len(sys.argv) != 3:
    print("Usage: python rectangle.py <height> <width>")
    sys.exit(1)

height = float(sys.argv[1])
width = float(sys.argv[2])

area = height * width
perimeter = 2 * (height + width)

print(f"The area of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")
