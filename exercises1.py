# Write a Python program to sum all the items in a list
list_a = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

sum_list = 0
for x in list_a:
    sum_list += x

#Write a Python program to multiply all the items in a list
list_b = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
multi_list = 1
for x in list_b:
    multi_list *= x

#Write a Python program to get the largest number from a list
list_b = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
#Write a Python program to get the smallest number from a list
list_b = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
list_c = ['abc', 'xyz', 'aba', '1221']
result = [x for x in list_c if x[0].__eq__(x[-1])]

#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
list_d = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sorted(list_d, key = lambda x: x[-1])

#Write a Python program to remove duplicates from a list
list_e = [1, 1, 2, 3, 3, 4, 5]
result = []
for x in list_e:
    if x not in result:
        result.append(x)

#Write a Python function that takes two lists and returns True if they have at least one common member
def check_list(list_a, list_b):
    check = [x for x in list_a if x in list_b]
    return check

list_a = [1, 2, 3, 4]
list_b = [4, 5, 6, 7, 8]

# Write a Python program to shuffle and print a specified list
from random import shuffle

from matplotlib.pyplot import flag
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)

# Write a Python program to generate all permutations of a list in Python (permutations: hoán vị)
import itertools
# print(list(itertools.permutations([1,2,3])))

#Write a Python program to get unique values from a list
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
my_set = set(my_list) #return dict

#Write a Python program to get the frequency of the elements in a list. Đếm tần số xuất hiện
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
ctr = collections.Counter(my_list)

#Write a Python program to check whether a list contains a sublist
my_list = [1, 2, 3, 6, 7, 8]
list_a = [2, 3]
list_b = [3, 8]

def check_contains(list_a, list_b):
    flag = 0
    if(all(x in list_b for x in list_a)):
        flag = 1

check_contains(list_a, my_list)
