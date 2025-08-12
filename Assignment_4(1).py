#if file not found error comes:
# try:
#     file=open('sample.txt','r')
#     read=file.read()
#     file.close()
# except FileNotFoundError:
#     print("Error:the file 'sample.txt' was not found")

#if sample.txt'exists:
file=open('sample.txt','r')
read=file.read()
print(read)




