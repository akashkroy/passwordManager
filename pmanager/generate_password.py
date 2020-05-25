import random
import string

# length = int(input("Enter the length of password: "))

def gen_pass(length=10):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = []
    for i in range(length):
        _ = random.choice(chars)
        password.append(_)
    final = "".join(password)
    print(final)
     
