#Multiplication Table

print 'x 1 2 3 4 5 6 7 8 9 10 11 12'
for row in range(1, 12+1):
    display_str = ""
    for column in range(0, 12 + 1):
        if column is 0:
            display_str += '' +str(row)
        else: 
            display_str += '' + str(column * row)
    print display_str