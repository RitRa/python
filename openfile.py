# Rita Raher 26-02-18
# How to open a file
f = open("data/iris.csv")

# prints some info about the file
print(f)

# reads the file and prints it
print(f.read())

#closes the file
f.close()
