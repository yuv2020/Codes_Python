#Bubble sort.
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                
nums=[56,34,24,6,2,89,60]
sort(nums)

print("Sort the element of list: ",nums)

print("\n")
#selection sort
#Bubble sort.
def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[i] < nums[minpos]:
                minpos=j
                
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        
        print("The selection sort is:", nums)
                        
nums=[56,34,24,6,2,89,60]
sort(nums)

print("Sort the element of list: ",nums)
