
#Module output_greeting(string greeting)
#    Display greeting
#End module
#
#Function string calculate_greeting(string name)
#   Declare string greeting
#
#   set greeting = "Hello" + name + ",welcome to python!"
#   Return greeting
#End function
#
#Function string input_name()
#    declare string name
#
#    Display "please enter your name"
#    Input name  
#    Return name
#End function
#
#Module greet_user()
#    Declare string name
#    Declare string greeting
#
#    Name = input_name()
#    greeting = calculate_greeting(name)
#    Call output_greeting(greeting)
# End module

def output_greeting(greeting):
    print(greeting)

def calculate_greeting(name):
    greeting = ""
    greeting = "Hello" + name + ",welcome to python!"
    return greeting

def input_name():
    name = ""

    name = input("please enter your name!")
    return name

def greet_user():
    name = ""
    greeting = ""

    name = input_name()
    greeting = calculate_greeting(name)
    output_greeting(greeting)
    
greet_user()
