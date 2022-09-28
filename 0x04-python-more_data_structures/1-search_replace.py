#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)

# other methods

# def search_replace(my_list, search, replace):
#     search = search
#     replace = replace
#     new_list = my_list.copy()
#     for i in range(len(my_list)):
#         if new_list[i] == search:
#             new_list[i] = replace
#     return new_list


# def search_replace1(my_list, search, replace):
#     new_list = my_list.copy()
#     search = search
#     replace = replace
#     return [replace if new_list[i] == search else
# new_list[i] for i in range(len(my_list))]


# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)
