# from sys import argv
# print("Script name: ", argv[0])
# print("Command line arguments: ", argv[1:])

# from sys import argv
# print("The Number of Command Line Arguments:", len(argv))
# print("The List of Command Line Arguments:", argv)
# print("Command Line Arguments one by one:")
# for x in argv:
#     print(x)



from sys import argv
sum = 0
args = argv[1:]
for x in args:
    sum=sum+int(x)
print("Sun is: ",sum)    