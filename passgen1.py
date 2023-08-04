import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$_"
pass_length = int(input("Please enter the length of the password needed: "))
pass_count  = int(input("Please enter the number of password needed :"))


for i in range (0, pass_count):
    password= ""
    for j in range(0, pass_length):
        pass_char = random.choice(characters)
        password= password+pass_char
    print("The obtained password is ",password)    
