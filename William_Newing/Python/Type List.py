#Type List
mixed_list = ['magical unicorns ',19,'hello ',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff ", "Moon ", "Robot"]

def identify_list_type(lst):
    new_str = ""
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_str += value

    if new_str and total:
        print "The array you entered is of mixed type"
        print "String:", new_str
        print "Total:", total

    elif new_str:
        print "The array you enetered is of string type"
        print "String:",new_str

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)

# my_list = ["hi",19,'hello',98.98,'world',9]
# sum=0
# my_string = ""
# output_type = ""
# for item in my_list:
#     if isinstance(item, int):
#         sum =sum + item
        
#         if output_type == "string":
#            output_type = "mixed"
#         else:
#             output_type = "number"
#     elif isinstance(item, str):
#         my_string = my_string + item
#         if output_type == "number":
#             output_type = "mixed"
#         else:
#             output_type = "string"
# print sum
# print my_string
# print output_type