# Rita Raher 26-02-18
# Topic 5 
# Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.



import pandas as pd
#Column names = petal length, petal width, sepal length and sepal width
columns = ['Petal Length' , 'Petal Width' , 'Sepal Length', 'Sepal Width' , 'Type']

df = pd.read_csv("data/iris.csv", names=columns)

print(df)









"""with open("data/iris.csv") as f:
    #contents = f.read()
    #print(contents)
    print('Petal length',)
    for line in f:
        #print(""line.split(',')[0],  line.split(',')[1])
        #print(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3], line.split(',')[4])
        print(line[1])
        #print('{:2d} {:2d} {:3d} {:4d} {:5d}'.format(line[0], line[1], line[2], line[3], line[4]))
  
"""