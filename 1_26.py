pi = 3.1416

print("Choose shape to calculate area:")
print("1. Triangle")
print("2. Rectangle")
print("3. Circle")
print("4. Sphere")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of Triangle = {area}")

elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print(f"Area of Rectangle = {area}")

elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = pi * radius ** 2
    print(f"Area of Circle = {area}")

elif choice == 4:
    radius = float(input("Enter the radius of the sphere: "))
    area = 4 * pi * radius ** 2
    print(f"Surface Area of Sphere = {area}")

else:
    print("Invalid choice")
