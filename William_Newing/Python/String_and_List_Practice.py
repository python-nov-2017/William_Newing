String and List Practice#
find and replace

words = "It's thanksgiving day. It's my birthday, too!"
# for position, i in enumerate(words):
#     if i == "day":
#         print("Found it")
#         print (position)
print words.find("day")
words = words.replace("day", "month")
print words

#min and max
x = [2,54,-2,7,12,98,"world"]
print x
print min(x)
print max(x)

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

#New list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_half = x[:len(x)/2]
second_half = x[len(x)/2:]
print "first half", first_half
print "second_half", second_half
second_half.insert(0,first_half)
print second_half