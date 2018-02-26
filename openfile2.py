# Rita Raher 26-02-18
# How to open a file...more advanced 
# creates a block of python code
# with automatically know how to close the file after use
with open("data/iris.csv") as f:
    #contents = f.read()
    #print(contents)

    for line in f:
        print(line.split(',')[0])
