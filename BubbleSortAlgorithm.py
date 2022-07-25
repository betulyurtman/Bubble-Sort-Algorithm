"""
Created on Jul 25 16:37 2022

"""

#Bubble Sort Algorithm

#First, let's create an array.
the_array = [4,2,346,7,63,8,53,354,5253,3]
#Secondly we create a for loop to run n-1 times to sort our array until all the elements are sorted.
#n is the length of the array and n - 1 is the number of comparisions.
for i in range(len(the_array) - 1):
    #s variable is for index number.        
    s = 0
    #We create another for loop to compare 2 numbers and swap them 
    #if the second number is smaller than the first number.
    for j in the_array:
        #Check if the second number is smaller.
        if the_array[s+1] < j:
            #Swap those 2 numbers.
            the_array[s], the_array[s+1] = the_array[s+1], the_array[s]
        #Increase the index number.
        s += 1
        #Break the loop when s equal n - 1.
        if s == len(the_array) - 1:
            break

print(the_array) 