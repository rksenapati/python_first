file_write = open('output.txt', 'w')
userInput =  str(input("Enter text tot write to the file: "))
file_write.write(userInput + "\n")
print("Data Successfully written to output.txt")
file_write.close()

file_append = open('output.txt', 'a')
userInput2 = str(input("Enter additional text to append: "))
file_append.write(userInput2 + "\n")
print("Data Successfully appended")
file_append.close()

file_read = open('output.txt', 'r')
print("Final Content of output.txt")
lines =file_read.readlines()
for line in lines:
        print(line)
file_read.close()