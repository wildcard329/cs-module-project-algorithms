'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # window spans k elements
    # window increments by one
    # return array containing max element of window
    i = -1
    max_win = []
    # window = arr[i:j]
    for l in range(len(nums) - k + 1):
        i += 1
        j = i + k
        print(i, j)
        print(nums[i:j])
        max_win.append(max(nums[i:j]))
    return max_win
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
