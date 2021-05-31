from os import write


text = "This is my first test.\nThis is next line."
my_file=open('my file.txt','w')
my_file.write(text)
my_file.close()
