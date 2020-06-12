'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    pos = 0
    for i in range(len(arr)): # O(n)
        element = arr[i] # O(n)
        if element != 0: # O(n)
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    return arr # Overall O(n)

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")