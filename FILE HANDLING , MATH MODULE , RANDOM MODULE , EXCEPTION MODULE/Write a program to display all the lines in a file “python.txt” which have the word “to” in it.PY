fh=open("python.txt","r")
count=0
lines=fh.readlines()
for a in lines:
    if (a.tolower().count(“to”) > 0) :
          print(a)
fh.close()
