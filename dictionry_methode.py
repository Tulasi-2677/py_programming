fruites = {
"apple"  : 70,
"orange" : 80,
"grapes" : 60,
}

print(fruites.items())
print(fruites.keys())
print(fruites.values())
print(fruites.update({"apple": 75,"banana" : 60}))
print(fruites)
print(fruites.get("berry"))
print(fruites.get("apple"))
#print(fruites["apple1"])#return an error
print(fruites.get("apple1"))# prints None
