# create text file
with open("test.txt",'w') as file:
    file.write("Hello, this is a test file.\nThis is the second line of the file.")

myfile = open('test.txt')
myfile = open("C:\\Users\\002CL0744\\Desktop\\py\\test.txt")
myfile.read()
# sets cursor to the index 0 of text file
myfile.seek(0)
myfile.close()

# .seek(), readlines(), close(), open(), w+, a+, read(), 
# w+ overwrite the existing content of file, read and write
# a+ create new file if not present instead of error, append and write
# readlines() goes through line by line, creates list of all the lines in file
