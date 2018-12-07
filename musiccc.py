import os
path = 'C:\\Users\\hrc\\Videos\\Flvto Downloads\\music'
sa = os.listdir(path)
ss = str(sa)
ss = ss.replace(',', '\n')
print(ss)
sc = input("Enter the song name: ")
for sc in sa:
    alist = []
    afile = open(a, "r")
    aline - afile.readline()
    while aline != "" and aline != "\n":
        alist.append(aline)
        aline = afile.readline()
    for i in range(0, len(alist)):
        print("Index:", i, alist[i])
