with open("hii.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fineee")
myfile.close()
