numbers = [23 , 5 , 89 , 12 , 45 , 12 , 67]

# len() used to find length 
print("Length = ",len(numbers))

# .append() added a number or text at the end 
numbers.append(100)
print("After Adding 100 at the end : ", numbers)

# .insert() add a number of text to a specific index
numbers.insert(2,99)
print("After adding 99 on index 2 : ",numbers)

# .pop() remove the last element 
print("using pop function it gives the last deleted element like : ",numbers.pop())
print("After removing last element the list looks like : ",numbers)

# .remove() delete a specific value
numbers.remove(5)
print("After removing 5 : ",numbers)

# .reverse() used to reverse a list
numbers.reverse() 
print("After reversing a list : ",numbers)

# .count() used to find a specific value or character 
print("After Counting 12 : ",numbers.count(12))

# .index() used to find index of a number or character 
print("The Index of 45 is : ",numbers.index(45))

# max() used to see the max value of list
print("The max value of list is : ",max(numbers))

# min() used to see least value of list
print("The least value of list is : ",min(numbers))

# sum() used to sum the numbers in the list
print("Sum of list is : ",sum(numbers))

# .sort()
numbers.sort()
print("After sorting :",numbers)

# sorted() create a new list and sort 

new_List= sorted(numbers)