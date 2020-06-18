'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the answer is in our cache 
    elif cache[n] > 0:
        return cache[n]
    else:
        # otherwise, our cache doesn't contain the answer, so we'll use our 
        # recursive logic to calculate it, and then save the answer in our 
        # cache for future uses 
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache)+ eating_cookies(n-1, cache) 
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50
    cache = {i: 0 for i in range(num_cookies+1)}

    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to eat {num_cookies} cookies")
