#List 
# l=[]
# print(l,type(l))
#ordered 
# PS C:\Users\AKSHATHA\Desktop\Vamshi\class2> python a.py
# [] <class 'list'>
# PS C:\Users\AKSHATHA\Desktop\Vamshi\class2> 
#creating
# l=[1,2,3,"Akshatha"]
# print(l,type(l))

# #modify 1 to 10 --mutable/updating 
# #indexing---address
# #fecting/reading
# print(l[0])
# #updaint
# l[0]="vamshi"
# print(l)
# #del
# del l
# print(l)
#list allows duplicates 
# l=[1,2,2,3]
# pr
# l=[10,20,30,40]
# print(l[0])
# print(l[1])
# print(l[-1])
# print(l[5])

# Traceback (most recent call last):
#   File "C:\Users\AKSHATHA\Desktop\Vamshi\class2\a.py", line 29, in <module>
#     print(l[5])
# IndexError: list index out of range

#L[start:end:step]
# L=[1,2,3,4,5,6]
# #  0 1 2 3 4 5-->position
# #output:[1,2,3]
# #print(L[0::2])
# #reverse 
# print(L)
# print(L[::-1])
# l=list(["hello",10,20,30])
# print(l)

#print(dir(list))


# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#reverse 
l=[1,2,3]
#print(l)
l.reverse()
print(l)
print(l[::-1])

#sort 
l=[1,2,3,4]
print(l)
l.sort(reverse=True)
print(l)

#copy 
#deep copy
l1=[100,500]
l2=l1
print(l1)
print(l2)
l2.append("akshatha")
print(l1)
print(l2)
#shallow copy 
print("------------------")
x1=[100,500]
x2=x1.copy()
print(x1)
print(x2)
x1.append("vamshi")
print(x1)
print(x2)





