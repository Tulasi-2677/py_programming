list = ["apple","orange","56","sila","7.9"]
print(list) 

list.append("sila")

print(list)

numbers = [2,56,45,33,1,8,9]
numbers.sort()#it sort the list in increasing order [1, 2, 8, 9, 33, 45, 56] 
print(numbers)

numbers.reverse()#it revers the list [56, 45, 33, 9, 8, 2, 1]
print(numbers)

numbers.insert(4,567)#insert the elemet at index 4
print(numbers)

print(numbers.pop(4))#return the index value


numbers.remove(45)
print(numbers)

