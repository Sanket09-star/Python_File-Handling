file = open("hello.c", "r")
s1 = file.read()
s2 = s1.replace("stdio", "iostream")
s2 = s2.replace("printf(", "cout<<")
s2 = s2.replace('")', '"')
file.close()
file1 = open("hello.c" + "pp", "w")
file1.writelines(s2)
file.close()
print("file converted..............")
