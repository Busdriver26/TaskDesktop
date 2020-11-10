a = [1,2,2,3]
b = [5,5,6,7]
temp = []
for i in a:
    if i not in temp:
        temp.append(i)
a = temp
temp = []
for i in b:
    if i not in temp:
        temp.append(i)
b = temp
print(a,b)
#check github