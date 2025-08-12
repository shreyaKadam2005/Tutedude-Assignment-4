file=open('output.txt','r+')
write=file.write(input("Enter text to write to the file: "))
print("Data successfully written to output.txt.")
print(write)
file.close()

file=open('output.txt','a')
append=file.write(" "+input("Enter additional text to append:  "))
print("Data successfully appended")
file.close()

print("final content of output.txt: ")
file=open('output.txt','r+')
read=file.read()
print(read)
file.close()


