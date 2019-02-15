f = open("E:/1.txt", "r+")
f.write("快乐风男\n")
f.write("托儿所 亚索\n")
f.seek(0)
f.readline()
f.seek(f.tell())
print(f.read())

f.close()