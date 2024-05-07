

def main() :
    length = input("Lenght: ")   
    width = input("Width: ")
    
    area = int(length) * int(width) 
    print(f"The area is {area}")

def display(area) :
    print(f"the area is {area}")
    display(area)
main()
