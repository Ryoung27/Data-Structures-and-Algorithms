import time
from demo import quicksort, bubble_sort
import random

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1, max_val))
    return ran_list

size = int(input("What size list do you want to create?"))
max_val = int(input("What is the max value?"))

l = create_random_list(size, max_val)
print(l)
tic = time.time()
print(quicksort(l))
toc = time.time()
print("Elapsed time -> ", toc-tic)
tic = time.time()
print(bubble_sort(l))
toc = time.time()
print("Elapsed time -> ", toc-tic)