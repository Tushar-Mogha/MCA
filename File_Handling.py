# For opening file
file=open("example.txt","w")

# # For writing in the file
# file.write("Hello, this is a test.")
filename="example.txt"
file=open(filename,"a")
datastring="Some dummy text data \n newline \t after tab".split()
print(datastring)
filecontent=file.writelines(datastring)
file.close() #Always close the file your are opening

