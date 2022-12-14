file = open("file.txt", 'r+')
print(file.read())
file.write("\nMizoram")
file.close()

file2 = open("newFile.py", "w")
file2.write("print('This is a new file')")
file2.close();
