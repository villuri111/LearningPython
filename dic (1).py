#dict 
s={
    "name":"Akshatha",
    "marks":85
}
#s-->variable holding dict 
#name and marks-->key 
#Akshatha and 85-->value 
#key and value-->items 

#for key try with list,tuple and str if any error capture it
#for value try with list,tuple and str if any error capture it
#give a try with nested dict 
#print(s) 

# d1=dict(name="vamsi",marks=95)
# print(d1)

#acceing the elements 
#1)bracket 2)get

#print(s)
#print(s["name"])
#print(s.name)
#print(s.get("name"))

#print(dir(dict()))

print(s)
print("get:",s.get("marks"))
print("items->",s.items())
print("values->",s.values())