#Initiliaze a emply list

myList = []

#Append the following numbers in to the list

myList.append(10) #add 10
myList.append(20) #add 20
myList.append(30) #add 30
myList.append(40) #add 40

#add 15 in the second element

myList.insert(1, 15)

#Extend the list with another list

myList.extend([50,60,70])

#Sort the list in ascending order

myList.sort()

#Remove the last element from the list

myList.pop()

#find and print the index of 30 in myList

indexThirty = myList.index(30)

print (indexThirty) #Print 30's index in the list

