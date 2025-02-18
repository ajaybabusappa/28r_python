#Decorators - These are also functions

def example_decorator(func):
    def wrapper():
        print("Check your cartridge")
        print("Check your A4 sheets")
        func()
        print("Thank you..Malli raku")
    return wrapper



@example_decorator
def printer():
    print("Printing in progres...Kasepu distrub cheyaku")

printer()




#P.S - Why?

#3 main things in p.s - Understanding the question properly
#Algorithm
#Coding 
#2 bonus points - Edge cases, code quality