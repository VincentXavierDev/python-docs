import sys
# argv in Python
# print ("Number of arguments:", len(sys.argv), "arguments")
# print ("Argument List:", str(sys.argv))

#RUN TEST 
# python .\lesson1.py
# sys.argv[0] = '.\lesson1.py'

# Keyword Arguments
def cheeseshop(kind, *arguments, **keywords):
    print(type(kind))
    print(type *arguments)
    print(type(**keywords))

# cheeseshop("Limburger", "It's very runny, sir.",
#     "It's really very, VERY runny, sir.",
#     shopkeeper="Michael Palin",
#     client="John Cleese",
#     sketch="Cheese Shop Sketch")

# Bài tập
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
result = [x * 2 for x in vec]
result = [(x * 2 + 1) for x in vec]
result = [str(x) for x in vec]
# filter the list to exclude negative numbers
result = [x for x in vec if x > 0]
result = [(x * 2) for x in vec if x > 0]
result = [(x + y) for x in vec if x > 0 for y in vec if y < 0]
result = [(x + y) for x in range(0, 5, 1) for y in range(0, 5, 1) if y < 3]

# for (let i = 0; i < 5; i++)
#     for (let j = 0; j < 5; j++)
#         if (j < 3) i + j
# apply a function to all the elements

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

# create a list of 2-tuples like (number, square)

# the tuple must be parenthesized, otherwise an error is raised