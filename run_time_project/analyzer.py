import demo
import random

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1, max_val))
    return ran_list

size = int(input("What size list do you want to create?"))
max_val = int(input("What is the max value?"))

print(create_random_list(size, max_val))