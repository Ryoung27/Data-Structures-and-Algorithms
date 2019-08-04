# #List

# node_1 = "Custom Object"

# my_data_type = [1,2, False, 4, "Young", None, node_1, 5.0, 1]
# print(my_data_type)
# print(type(my_data_type))

# #Dict

# my_data_type = {1: "hello", 2: "Young"}
# print(my_data_type[2])
# print(type(my_data_type))

# #Sets
# my_data_type = {1,2, False, 4, "Young", None, node_1, 5.0, 1}
# print(my_data_type)
# print(type(my_data_type))

# #Tuples
# my_data_type = (1,2, False, 4, "Young", None, node_1, 5.0, 1)
# print(my_data_type)
# print(type(my_data_type))

#Lists
# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# my_strings_list = ["comp sci", "history", "physics", "law"]
# print(f"Ints: {my_list}")
# print(f"Strings: {my_strings_list}")
# print("Sorting...")
# my_list.sort()
# sorted_list = sorted(my_list)
# print(sorted_list)
# print(f"Sorted Ints: {my_list}")

#Functions

arr_1 = [5,9,3]
arr_2 = [2,16,4]

def func_0(arr_1, arr_2):
    index = 0
    arr_3 = []
    for i in arr_1:
        if i < arr_2[index]:
          arr_3.append(i)
        else:
          arr_3.append(arr_2[index])
        index += 1
    return arr_3

print(func_0(arr_1, arr_2))

arr_1 = [6,3,9]
arr_2 = [11,2,4]

def func_1(arr_1, arr_2):
    arr_1 == arr_1.sort()
    arr_2 == arr_2.sort()
    return func_0(arr_1, arr_2)
print(func_1(arr_1, arr_2))

def func_2(my_string):
    new_string = ''
    for i in my_string:
        new_string += i
        if i != my_string[-1]:
            new_string += '->'
    return(new_string)


print(func_2('hello'))