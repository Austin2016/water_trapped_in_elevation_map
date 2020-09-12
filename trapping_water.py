  #given non-negative integers representing an elevation map 
  #where the width of each bar is 1, 
  #compute how much water it is able to trap after raining.

#algorithm: 

def trapped_water (array):  
	left = "blank"
	total = 0
	max_height = largest_element(array) 
	for x in range(1, max_height + 1):
	    left = index_of_first_example(array,x) 
	    right = index_of_last_example(array,x)
	    for i in range(left + 1, right):
        	if array[i] < x: 
        		total = total +  1  
	return total 
#Helper Methods below:

def index_of_first_example (array,value):
     index = 0
     for element in array:
     	if element >= value:
     		return index
        else: 
        	index += 1

def index_of_last_example (array,value):
     index = 0
     stored_index = "blank"
     for element in array:
     	if element >= value:
     		stored_index = index
     		index += 1 
        else: 
        	index += 1
     return stored_index

def largest_element (array): 
	largest = 0 
	for n in array:    
		if n > largest: 
			largest = n
	return largest 




x = [0,1,0,2,1,0,1,3,2,1,2,1]
print trapped_water(x)






#for each layer the number of values between that layer value and the next layer value of equal or greator that is less

