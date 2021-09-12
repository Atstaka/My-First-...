#A basic program for creating a strong password.
import random
import string
numbers = 1,2,3,4,5,6,7,8,9,0
words = string.ascii_letters + string.punctuation + ''.join(str(v)for v in numbers) 
print("".join(random.choice(words) for i in range(16)))

