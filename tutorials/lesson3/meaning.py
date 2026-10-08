meaning = 42
nofm = int(input("Enter the number of modules you have: "))
modules = [""] * nofm
for i in range(nofm):
    #print("Enter the module "+str(i+1)+" : ")
    modules[i] = input("Enter the module "+str(i+1)+" : ")

for i in range(nofm):
    #print(f"The module number {i+1} is : {modules[i]} ")
    print("The module number", i+1,"is :", modules[i] )
    
