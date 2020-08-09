# The formula to convert a temperature from Celsius to Fahrenheit is:
# F = (C * 9/5) + 32
# Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value.

def c_to_f(c):
    f = (c * 9/5) +32
    print("The temperature is %d degrees Celsius, %d degrees Fahrenheit." % (c, f))

c_to_f(40)

#solved