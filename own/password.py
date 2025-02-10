import random
import string

def password_generator(lenght = 12):
    charater = string.ascii_letters + string.digits + string.punctuation
    password = " ".join(random.choice(charater) for _ in range(length)) 
    
    
    return password
length = 12
password = password_generator(length)
print(password)

