import math
multiline = '''
this is line     1     

this is line 2 
this is line 2.    5'''
#print("start")
#print(multiline)
#print("end")

print(multiline.title())
print(multiline.upper())
print(multiline.lower())

print(len(multiline))
multiline += "         "
multiline = "          " +multiline
print(multiline)
print(len(multiline))

print(multiline.strip())
print("\n\n")

#build a menu

title= "menu".upper()
print(title.center(21 , "-"))
print("Coffee".ljust(16, ".")+"$1.0".rjust(6," "))
print("Tea".ljust(16)+"$1.5".rjust(6," "))

print(title[2])

print("")

test = "012345"
print(test[4:])

print()

print(int(math.sqrt(4)))
