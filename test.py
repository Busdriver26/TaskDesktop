import re
c="2020-10-33"
a = re.compile("(^((19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$)")
b = a.findall(c)
if(len(b)>0):
    print(b[0][0])
else:
    print("INVALID:"+c)

#testupload