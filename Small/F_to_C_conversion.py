# The formula to convert a temperature from Fahrenheit to Celsius is:
# C = (F - 32) * 5/9
# Write a function that takes a temperature in Fahrenheit, converts it to Celsius, and returns the value.

def f_to_c(f):
    c = (f -32) * 5/9
    print("The temperature is %d degrees Fahrenheit, %d degrees Celsius." % (f, c))

f_to_c(32)

#solved
