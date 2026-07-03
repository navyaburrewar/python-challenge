def partition(arr, low, high):
    pivot = arr[high]      # Choose the last element as pivot
    i = low - 1            # i keeps track of the last position of an element <= pivot

    for j in range(low, high):    # Traverse from low to high-1

        if arr[j] <= pivot:       # If current element is smaller than or equal to pivot
            i += 1                # Move i one step forward
            arr[i], arr[j] = arr[j], arr[i]   # Swap

    arr[i+1], arr[high] = arr[high], arr[i+1]  # Place pivot in its correct position
    return i+1                                # Return pivot index


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


arr = [10,7,8,9,1,5]   ##[1,7,8,9,10,5]-->[1,5,8,9,10,7]
quick_sort(arr,0,len(arr)-1)
print(arr)