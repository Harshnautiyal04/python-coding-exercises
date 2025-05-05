#find area and perimeter of a square using function a=l**2,p=4a

# num = int(input("Enter a number : "))

# def square(a):
#     perimeter = 4*a
#     area = a**2
#     print(f"Perimeter of a square is {perimeter}.")
#     print(f"Area of a Square is {area}.")
# square(num)

#find area and perimeter of a square using function a=l**2,p=4a
import math

num = int(input("Enter a number : "))

def square(a):
    perimeter = 4*a
    area = a**2
    sqrta = math.sqrt(area)
    sqrtp=math.sqrt(perimeter)
    add = sqrta+sqrtp
    print(f"Perimeter of a square is {perimeter}.")
    print(f"Area of a Square is {area}.")
    print(f"Square root of {perimeter} is {sqrtp}.") 
    print(f"Square root of {area} is {sqrta}.")
    print(f"Sum of {sqrta} and {sqrtp} is {add}.")
square(num)
