#Program to calculate the area of circle
def areaofcircle():
        ch = 'y'
        while ch == 'y' or ch =='Y':
                pi = 3.141592653589793238
                r = float(input("Enter the radius of the circle: "))
                area = pi*r*r
                print("Area of circle is =  ",area)
                ch = input("Do you wish to continue??(y/n):")
areaofcircle()
