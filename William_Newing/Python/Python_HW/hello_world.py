#print "Hello World"

# commenting a single line
# we can even comment out code

#print "this is a sample string"

#name = "Zen"
#print "My name is", name

# first_name = "William"
# last_name = "Coder"
# print "My name is {} {}".format(first_name, last_name)

# fruits = ['apple', 'banna', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']

# fruits_and_vegetables = fruits + vegetables
# # print fruits_and_vegetables
# # salad = 3 * vegetables 
# # print salad 
# # print fruits[3]
# fruits.append(kiwi)
# print fruits

# x = [99,4,2,5,-3]
# print x[1:4]

# my_list = [1,'Zen', 'hi']
# print sorted(my_list)

# age = 17
# if age >= 18:
#     print 'Legal age'
# elif age == 17:
#     print 'You are seventeen.'
# else: 
#     print 'You are so young!'

# for count in range(0, 5):
#     print "loopoing -", count

# my_list = [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world!']
# for element in my_list:
#     print element

# for val in "string":
#     if val == "i":
#         break
#     print val

# number = 25

# x='1'
# y = 2
# print int(x) + y

# name = "Charles"

# x = [5,34,10,16]
# if x not exists: #do something

# def say_hi():
#     return "Hi"
# greeting = say_hi()
# print greeting

# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4,5)
# sum2 = add(1,4)
# sum3 = sum1 + sum2

# def multiply(arr,num):
#     for x in range(len(arr)):
#         arr[x] *= num
#     return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b

def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi * r * r 
    return (c, a)
print (c, a)
