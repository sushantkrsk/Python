file=open("hello.txt",'a')
file.write("sam,matt,jhon")
file.close()
f=open("hello.txt","r")
print(f.read())