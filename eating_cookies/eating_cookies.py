'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # input is size n
    # output varies on how many ways 
    # 1, 2,  and three can be added to 
    # equal n

    # if n is 0, return 0, if n is 1, 
    # return 1, if n is 2, return 2, 
    # if n is 3, return 4
    if n == 1 or n ==0:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
