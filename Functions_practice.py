# def add(num1, num2):
#     return num1 + num2

#A function is defined in four parts:
# • Using the def keyword
# • Naming the function
# • Declaring parameters ("ingredients")
# • Providing the body of the function as a code block 

#After defining a function you run the function by using its name, with a pair of ()
#When you run a function, each sstatement in the function's body is run

#REFACTORING CODE FROM LAST LESSON WITH FUNCTIONS

# todos = []

# # Create a constant for our main menu.
# # This saves us from having to type it out twice.
# MAIN_MENU = """
# Choose an action:
# P: Print your to-do list
# A: Add a to-do item
# R: Replace a to-do item
# C: Complete a to-do item
# (Or press Enter to exist the program.)
# """

# def print_todos():
#     # Print the current list of to-do items
#     print("\n\n\nTo do:")
#     print("====================")
#     count = 1
#     for todo in todos:
#         print("%d: %s" % (count, todo))
#         count += 1

# choice = input(MAIN_MENU)
# choice = choice.upper() # Simplifies our if-conditions

# # As long as they type something, keep prompting
# while len(choice) > 0:
#     if choice == "P":
#         print_todos()
#     elif choice == "A":
#         new_todo = input("What do you need to do? ")
#         if len(new_todo) > 0:
#             todos.append(new_todo)
#     elif choice == "R":
#         print_todos()
        
#         which_index = input("Which to-do number? ")
#         try:
#             which_index = int(which_index)
#             which_index -= 1 # Convert from human-readable to 0-based index
            
#             if which_index >= 0 and which_index < len(todos):
#                 new_todo = input("What do you need to do? ")
#                 todos[which_index] = new_todo
#         except ValueError:
#             print("\n\n***Please enter a number.***")
#     elif choice == "C":
#         print_todos()
        
#         which_index = input("Which to-do number? ")
#         if which_index != -1:
#             completed_todo = todos[which_index]
#             del todos[which_index]
#             print("%s has been marked complete!" % completed_todo)        
#     else:
#         print("\n\n***Please enter a valid menu option.***")    

#     choice = input(MAIN_MENU)
#     choice = choice.upper() # Simplifies our if-conditions

# print("Have a nice day!")

#YOU ARE ONLY ALLOWED TO RETURN A SINGLE VALUE FROM A FUNCTION. TO GET AROUND THIS, YOU CAN RETURN A SEQUENCE INSTEAD.

#Here's an example of a divide() function that returns both the quotient and the remainder:
# def divide(dividend, divisor):
#     quotient = dividend // divisor # The // operator rounds
#     remainder = dividend % divisor
#     return (quotient, remainder) # Return a tuple

# result = divide(5, 3)
# print(result)

#Does any code run after a return statement?
# When Python encounters the return keyword while running a function, it exits the functions. This means that none of the statements after return will run.

# def does_not_print():
#     print("This prints")
#     return
#     print("This does not print")
#     print("Nor does this")

#     print("Third time is not a charm")
#     print(":)")
    
# does_not_print()
# # The first print() runs, but the rest do not:

# # This prints

# Does the order of arguments matter?
# When you call a function, the order of the arguments must be the same as the function definition.

# Here is a variation of our "greeter" program:

# def make_formal_greeting(name, title):
#     return "This is %s, the %s!" % (name, title)

# result = make_formal_greeting("Rob Stark", "King in the North")
# print(result)

# oops = make_formal_greeting("King in the North", "Rob Stark")
# print(oops)

# What is scope?
# Scope is the amount of code where a variable can be accessed.

# The two main kinds of scope are local and global

# #What is local scope?
# Local scope is when a variable is defined as part of a function body, or as one of its arguments.
# A local variable (i.e., one with local scope) can only be accessed inside of the function where it is defined.

# def dance():
#     kind = "silly"
#     print("I am doing a %s dance" % kind)

# dance()

# # print(kind)

# def dance():
#     kind = "silly"
#     print("I am doing a %s dance" % kind)

# def dance2():
#     print("I want to do a %s dance" % kind)    
    
# dance()
# dance2() <=== This will return an error since kind is not in dance2

#Every function has its own local scope

#WHAT IS GLOBAL SCOPE?

# The other kind of scope is the scope of the entire program file, known as global scope.

# kind = "mesmerizing"
# def dance():
#     print("I am doing a %s dance" % kind)

# dance() # Totally OK.
# print(kind) # Also totally OK.
# # Therefore, the scope of a parameter and a local variable are the same.

# # # I am doing a mesmerizing dance
# # # mesmerizing

#TIP
# It is best to use local variables instead of global variables. Overuse of global variables is a sign of poor organization and can lead to buggy programs.

#### WHAT IS RECURSION ####

#A function that calls itself is a recursive function. Recursion is an alternative for using a loop.

#Here is a loop that we can convert to a recursive function:

# def calculate_sum(number_list):
#     result = 0
#     for number in number_list:
#         result += number
#     return result

# the_sum = calculate_sum(range(100))
# print(the_sum)

# # When using a loop, your function goes like this:

# # Create a variable for the result and set it to 0
# # For each number in the list add it to result
# # Then return result
# # With recursion, you would approach the problem differently. Your function description is:
# # • The sum of the list is the first number plus the sum of the rest of the list
# # • If there are no more items in the list, we're finished

# # This is what that description looks like in code:

# def calculate_sum(number_list):
#     if len(number_list) == 0:
#         return 0
#     else:
#         return number_list[0] + calculate_sum(number_list[1:]) #This is the recursive definition
    
# the_sum = calculate_sum(range(100))
# print(the_sum)

# On line 2, we check for the base case - this is how the function knows that it is finished.

# On line 5 is the recursive definition: the first number plus the sum of the rest of the list. We return the result of adding number_list[0] to the result of calling calculate_sum() again. But when we call calculate_sum(), we pass it everything except number_list[0].

# That is, each time we call calculate_sum(), we pass it a shorter List. Eventually, the final time we call calculate_sum(), it receives a List whose len() is 0.

# To write recursive functions, make sure that:

# • You define the base case
# • Your alternate case includes a recursive function call
# • The set of values gets smaller each time

# Summary
# In this lesson, you learned how to:

# • Define reusable functions
# • Return values
# • Specify arguments
# • Work with local and global scope
# • Do basic recursion

# TIP

# Besides serving as building blocks for your programs, it is useful to think of functions as communicating with each other via arguments and return values.