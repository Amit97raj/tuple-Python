 # Python Basics Chapter 6:
# ========================

# 1. Introduction To Tuple

# tuple data structure
# tuple can store any data type
# most important tuples are immutable, once tuple is created you can't
# update
# data inside tuple
# tuples are faster than lists
# we use tuples when we know that our data will not be change in 
# future.

# days = ('mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun')

# no append, no insert, no pop, no remove

# print(days)
# print(type(days))
# print(days[0])
# print(days[0:3])
# print(days[-1])

# Methods -
# count()
# index()
# len()
# slicing

# print(days.count('mon'))
# print(days.index('sun'))
# print(len(days))

# 2. More About Tuples

# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

# mixed = (1, 2, 3, 4.0)

# for loop and tuple

# for i in mixed:
#     print(i)

# Note- You can use while loop too

# i = 0
# while i < len(mixed):
#     print(mixed[i])
#     i += 1 

# tuple with one element

# nums = (1)
# words = ('one')

# nums = (1, )
# words = ('one', )

# print(type(nums))
# print(type(words))

# tuple without parenthesis

days = 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun'
print(type(days))

# tuple unpacking

# days = ('mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun')

# mon, tues, wed, thurs, fri, sat, sun = days

# print(mon)
# print(sun)

# list inside tuples

# year = (2021, ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun'])

# print(year)
# print(year[1])
# year[1].pop()
# print(year)
# year[1].append('sun')
# print(year)

# some functions that you can use with tuples

# min()
# max()
# sum()

# mixed = (1, 2, 3, 4.0)

# print(min(mixed))
# print(max(mixed))
# print(sum(mixed))

# 3. Function Returning Two Values

# def func(a, b):
#     add = a + b
#     mul = a * b

#     return add, mul

# print(func(2, 4))

# addResult, mulResult = func(2, 4)

# print(addResult)
# print(mulResult)

# 4. Something more about tuples, list, str

# nums = tuple(range(1, 11))

# nums = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# nums = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# nums = str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(nums)
# print(type(nums))
