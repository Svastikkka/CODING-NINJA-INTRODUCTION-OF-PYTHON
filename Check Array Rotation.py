def countRotations(arr, n):
    # We basically find index
    # of minimum element
    min = arr[0]
    for i in range(0, n):

        if (min > arr[i]):
            min = arr[i]
            min_index = i

    return min_index;


# Driver code
num=int(input())
arr = list(map(int,input().split()))
n = len(arr)
print(countRotations(arr, n))
