'''Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters
anything other than a valid number catch it with a try/except and put out an appropriate message
and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

Invalid input
Maximum is 10
Minimum is 2'''


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    else:
        
        try:
            user_input = int(num)
        except:
            print("Invali input")
            continue
            
        if largest is None :
            largest = user_input
        if user_input > largest:
            largest = user_input
            
            
        if smallest is None:
            smallest = user_input
        if user_input < smallest:
            smallest = user_input

print("Maximum is", largest)
print("Minimum is", smallest)
