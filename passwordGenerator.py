import random, string

passwordLength = int(input("How long do you want you'r pasword to be: "))

password_characters = string.ascii_letters + string.digits + string.punctuation

password = []
for i in range(passwordLength):
    password.append(random.choice(password_characters))

print(''.join(password))
