name = input("Enter name: ")
out_file = open("name.txt", "w")
print(name, file=out_file) #can also use out_file.write(name)
out_file.close()