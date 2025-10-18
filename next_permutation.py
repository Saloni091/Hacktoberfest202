def next_permutation(arr):
    n = len(arr)
    i = n - 2

    # Step 1: Find the first decreasing element from the end
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find element just larger than arr[i]
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Step 3: Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]

    # Step 4: Reverse the elements from i + 1 to end
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
