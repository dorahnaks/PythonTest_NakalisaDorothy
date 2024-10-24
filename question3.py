# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.


run = 1
while True:
    number = int(input("Enter number: "))
    total_sum = 0
    
    if number != 0:
        total_sum += number
        print(f"The sum is {total_sum}")
    else:
        print(f"The sum is {total_sum}")
        break



    






# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

for i in range(100):
    if i %2 == 1:
        print(i)
