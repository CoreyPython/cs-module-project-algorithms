'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Understand
    ## Every number but one in the array shows up twice.
    ## We need to find out what number is the single occurence.

    # Plan
    ## We can use a set to get the duplicates and maybe compare the original array with the set?


    # Execute
    return 2 * sum(set(arr)) - sum(arr)



    # Reflect


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")