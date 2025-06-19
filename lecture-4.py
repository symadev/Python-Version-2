dict={
    "name":"rutu",
     "age":23,
    "height": 56.6,
    list:[34,56,7,78,90],


}
print(dict)
print(type(dict))
print(dict["name"])
print(dict["height"])
print(dict[list])
print(list(dict))
new_dict = {
    "name":"hena",
    "age":34
}
dict.update(new_dict)
print(dict)#just value is replaced



#set in python
collection= { 23,3,4,45,"masha","ritika","monika"}
print(collection)
print(type(collection))
collection.add(49)
collection.remove(49)
collection.pop()#first element  delete  in this pop operation
print(collection)
collection2= {23,45,6789,90,7,2}
print(collection2.union(collection))#print with added the collection2
print(collection2.intersection(collection))#show the common elememnt
# set ignore the duplicate items
