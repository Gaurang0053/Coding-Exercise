
# Write a function that returns the maximum of two numbers.

n1=int(input("enter the first no:"))
n2=int(input("Enter the second no:"))
max=max(n1,n2)
print(max)

# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fizz_buzz(n):
    if n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    elif n%3==0 and n%5==0:
        print("FizzBuzz")
    else:
        print(n)


# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one
# demerit point and print the total number of demerit points. For example, if the speed is 80,
# it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

#Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# For example, if the limit is 3, it should print:
#0 EVEN
#1 ODD
#2 EVEN
#3 ODD

def showNumber(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print("Even")
        else:
            print("odd")
            
#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def sum(limit):
    sum=0
    for i in range(0,limit+1):
        if i%3==0 or i%5==0:
            sum=sum+i
            print(sum)




