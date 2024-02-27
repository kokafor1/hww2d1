#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
num = 1

while num ** 3 <= 1000:
    cube = num ** 3
    print(cube)
    num += 1


#Get first prime numbers up to 100
def prime(pn):
    if pn < 2:
        return False
    for i in range(2, int(pn**0.5) + 1):
        if pn % i == 0:
            return False
    return True

for num in range(2, 101):
    if prime(num):
        print(num)



#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int(input('Enter Age: '))

if age < 18:
    print(' Your a Kid')
elif 18 <= age <= 65:
    print('Your an Adult')
else: print(' Your a Senior')