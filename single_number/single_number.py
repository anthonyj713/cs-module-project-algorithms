'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    s = set()
    # sets: holding onto unique elements
    # loop through our array
    for x in arr:
        # for each element
        # check if it is already in our set
        # if it is, then thats not our out element out
        if x in s:
            s.remove(x)
        else:
            s.add(x)
        # the odd element out will be the only element in the set
    return list(s)[0]



        
        
  


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")