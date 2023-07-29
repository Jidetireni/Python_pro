#!/usr/bin/python3
# Binary search script 

# Defining a function to take in the parameters list of number and the target you want to find 
def search(listed, target):
    middle, start, steps = 0, 0, 0 # Intailizing the middle, start, steps variable to zero  
    end= len(listed) - 1 # end of the list is the number of values minus one 

    # Looping the entire conditions until the target is found 
    while start <= end:
        print("step", steps, " :", str(listed[start:end+1]))
        steps += 1
        # Middle variable to is to split the list in two
        middle= (start + end) // 2
        # Condition to find where the target is after spliting and to disreguard the unused list
        if target ==  listed[middle]:
            return middle
        if target <= listed[middle]:
            end= middle - 1
        else:
            start= middle + 1
    return -1 
# Assigning variables for the passed parameters and declaring the function
if __name__ == "__main__":
    mylist= [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
    my_target= 32

    search(mylist, my_target)
