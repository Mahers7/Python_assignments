def get_input() :
    length = input("Lenght: ")   
    width = input("Width: ")

def main() :
   get_input()

   return(length, width)

area = int(length) * int(width) 
print(f"The area is {area}")

def display(area) :
    print(f"the area is {area}")
    display(area)
main()
