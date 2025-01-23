import glob

myfile = glob.glob("D:\python\*.txt")

'''print (myfile)'''

for files in myfile:
    with open(files,'r') as file:
        if(files == "D:\\python\\ideas.txt"):
            print(file.read().upper())
