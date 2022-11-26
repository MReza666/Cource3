import re
#
while True:
    fname=input("Enter File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        print("The file could not be found, please try again")
#
alltxt=fhandle.read()
strnums=re.findall('[0-9]+',alltxt)
sum=0
for i in range(len(strnums)):
    sum+=int(strnums[i])
print('Total sum:', sum)
