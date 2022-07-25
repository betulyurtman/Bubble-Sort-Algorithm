#Bubble Sort Algorithm Function

the_array = [4,2,346,7,63,8,53,354,5253,3]


def Bubble_Sort_Algorithm(list):

    
    for i in range(len(the_array) - 1):
        
        s = 0
        for j in the_array:
            
            if the_array[s+1] < j:
                the_array[s], the_array[s+1] = the_array[s+1], the_array[s]
            s += 1
            
            if s == len(the_array) - 1:
                break
            
    print(the_array)
    

Bubble_Sort_Algorithm(the_array)