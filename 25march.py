 # Question pratical

# Print numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i)

# Print the multiplication table of a given number (e.g., 5).

# num =int(input('enter the number :'))
# for i in range(1,11):
#     print(num,'X',i,'=',num*i)

# for i in range(10,0,-1):
#     print(i)

# Count how many numbers between 1 and 50 are divisible by 3.   

count =0
for i in range(1,100):
    if i % 3==0:
        count +=1
print(count)