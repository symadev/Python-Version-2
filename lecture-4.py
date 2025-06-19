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
