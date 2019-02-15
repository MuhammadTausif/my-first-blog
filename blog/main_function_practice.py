mylist = ['a','b','c','d']

for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)):
        print('Forward: '+mylist[i], mylist[j])
        print('Reversed:'+mylist[j], mylist[i])
