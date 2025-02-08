#Calculate the Perimeter and Area of different Shapes using functions

def circle():
    radius=float(input("Enter radius:"))
    perimeter = 2 * 3.142 * radius
    area= 3.142 * radius**2
    print(f"For circle, the perimeter will be: {perimeter:.2f} and area will be: {area:.2f}")

def square():
    side=float(input("Enter side of a square:"))
    perimeter = 4 * side
    area = side**2
    print(f"For square, the perimeter will be: {perimeter:.2f} and area will be: {area:.2f}")

def triangle():
    base=float(input("Enter base:"))
    height=float(input("Enter height:"))
    a=float(input("Enter side 1 of triangle:"))
    b=float(input("Enter side 2 of triangle:")) 
    c=float(input("Enter side 3 of triangle:"))
    perimeter = a+b+c
    area = 0.5 * base * height
    print(f"For triangle, the perimeter will be: {perimeter:.2f} and area will be: {area:.2f}")

def rectangle():
    base=float(input("Enter base:"))
    height=float(input("Enter height:"))
    perimeter = 2 * (base+height)
    area=base*height
    print(f"For rectangle, the perimeter will be: {perimeter:.2f} and area will be: {area:.2f}")


while True:
    print('''To calculate the perimeters and areas of different shapes, select a option:
         1.Circle
         2.Square
         3.Triangle
         4.Rectangle
         5.Exit''')
    n = int(input("Enter your choice:"))
    
    if n==1:
        circle();
        
    elif n==2:
        square();
       
    elif n==3:
        triangle();
    
    elif n==4:
        rectangle();

    elif n==5:
        print("Exiting...")
        break
    
    else:
        print("Invalid Choice!")
