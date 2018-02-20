# Rita Raher 19-02-18
# Loops through a list

squares = [1, 4, 9, 16, 25]
i = 0 

#while i is less than the length of the list
while i < len(squares):
    #prints the index
    print(i, squares[i])
    #increases i by 1
    i += 1



#for loops
words = ['cat', 'window', 'defenestrate']

for i in words:
    print(i, len(i))

for i in range(len(words)):
    print(i, words[i], len(words[i]))