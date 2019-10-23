# Michael Calhoun
# Shape Size Calculations (Redux)
# 9/11/2019

# Get side lengths for square/rectangle
def intro():
    print("""
    Hello user welcome to geometry :)
    choose which shape you would like to solve
    1. Square
    2. Circle
    3. Triangle
    4. Cube
    5. Quit """)

def option1():
    print("What is the length of the square?")
    sqrLength = float(input(": "))
    print("What is the width of the square?")
    sqrWidth = float(input(": "))
# Calculate perimeter and area
    sqrPer = (sqrLength +sqrWidth) * 2
    sqrArea = sqrLength * sqrWidth
# Print the calculations
    print(str.format("The perimeter of the square is {0:.2f}", sqrPer))
    print(str.format("The area of the square is {0:.2f}", sqrArea))
# ASCII with side lengths
    print(str.format("""
            {0:^10.2f}
    _________________________
    |                         |
    |                         |
    |                         |
    |                         |
    |                         | {1:^10.2f}
    |                         |
    |                         |
    |                         |
    |                         |
    |_________________________|
    """, sqrLength, sqrWidth))
def option2():
# Get the radius of the circle
        print("What is the radius of the circle?")
        radius = float(input(": "))
# Calculate the circumference
        circumference = 2 * 3.14 * radius
        print(str.format("The circumference of the circle is {0:.2f}", circumference))
# ASCII art with radius
        print(str.format("""
               %%%    %%%
          %%%              %%%

      %%%                      %%%
            {0:^12.2f}    
    %%% __________0             %%%
       
    %%%                         %%%

    %%%                        %%%

        %%%                  %%%

              %%%     %%%
    """, radius))

def option3():
# Get the base and height of the triangle
    print("What is the base length of the triangle?")
    triBase = float(input(": "))
    print("What is the height of the triangle?")
    triHeight = float(input(": "))
# Calculate the area of the triangle
    triArea = (triBase * triHeight) / 2
    print(str.format("The area of the triangle is {0:.2f}",triArea))
# ASCII are with base and height
    print(str.format("""
           /|
          / |
         /  |
        /   |
       /    | {0:<12.2f}
      /     |
     /      |
    /_______|
    {1:^12.2f} 
    """, triHeight, triBase))

def option4():
# Get the measurements of the cube/rectangular prism
    print("What is the height of the cube?")
    cubeHeight = float(input(": "))
    print("What is the length of the cube?")
    cubeLength = float(input(": "))
    print("What is the width of the cube?")
    cubeWidth = float(input(": "))
# Calculate and print the volume
    cubeVol = cubeHeight * cubeLength * cubeWidth
    print(str.format("The volume of the cube is {0:.2f}", cubeVol))
 # ASCII art with measurements
    print(str.format("""
    {0:^15.2f}
       +--------+
      /        /|
     /        / | {1:<15.2f}
    +--------+  |
    |        |  |
    |        |  +
    |        | /
    |        |/{2:<14.2f}
    +--------+
    """, cubeLength, cubeHeight, cubeWidth))
def option5():
    while True:
        varify = input("are you sure you want to quit?")
        if varify == "yes":
            return True
        elif varify == "no":
            return False
        else:
            print("okay then")
            continue

def menu():
    while True:
        intro()
        choice = input("pick which one you want")
        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()
            
        elif choice == "5":
            response = option5()
            if response:
                break

menu()
input("press enter to close")





