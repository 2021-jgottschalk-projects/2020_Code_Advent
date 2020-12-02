# Python3 program to find a triplet 
  
# returns true if there is triplet 
# with sum equal to 'sum' present 
# in A[]. Also, prints the triplet 
def find3Numbers(A, arr_size, sum): 
  
    # Sort the elements  
    A.sort() 
  
    # Now fix the first element  
    # one by one and find the 
    # other two elements  
    for i in range(0, arr_size-2): 
      
  
        # To find the other two elements, 
        # start two index variables from 
        # two corners of the array and 
        # move them toward each other 
          
        # index of the first element 
        # in the remaining elements 
        l = i + 1 
          
        # index of the last element 
        r = arr_size-1 
        while (l < r): 
          
            if( A[i] + A[l] + A[r] == sum): 
                print("Triplet is", A[i],  
                     ', ', A[l], ', ', A[r]); 
                return True
              
            elif (A[i] + A[l] + A[r] < sum): 
                l += 1
            else: # A[i] + A[l] + A[r] > sum 
                r -= 1
  
    # If we reach here, then 
    # no triplet was found 
    return False


f = open("2020_advent_01_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

num_list = []
for item in content_list:
  item = int(item)
  num_list.append(item)
  num_list.sort()



  
# Driver program to test above function  
sum = 2020
arr_size = len(num_list) 
  
find3Numbers(num_list, arr_size, 2020) 
  
# This is contributed by Smitha Dinesh Semwal 
