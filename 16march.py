# Sequencial data type
# list
lst = []
print(type(lst))

lst = [1,2,3,4,5,6,6+6j,True,"are tu jaa re"]
print(lst)

lst = [1,1,1,1,1,11]
print(lst)

mylist = ["apple", "banana", "cherry"]
print(mylist)


# tuple
t=(1,2,3,4,5,6)
print(t)
print(type(t))

t1 = (1)
print(type(t1))

t1 = (1,)
print(type(t1))

# sets
s ={1,2,3,4,5,6,7,"amit","anu",True,2,2,2,2}
print(s)
print(type(s))


# dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(thisdict["year"])