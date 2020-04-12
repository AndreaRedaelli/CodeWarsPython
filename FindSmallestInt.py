def find_smallest_int(arr):
    return min_recursive(arr)

def min_recursive(arr):
    if(len(arr) == 0):
        return None
    if(len(arr) == 1):
        return arr[0]
    if(len(arr) == 2):
        if(arr[0] < arr[1]):
            return arr[0]
        else:
            return arr[1]
    else:
        min = min_recursive(arr[:len(arr)-1])
        if(min < arr[len(arr)-1]):
            return min
        else:
            return arr[len(arr)-1]

if __name__ == "__main__":
    find_smallest_int([0, 1-2**64, 2**64])
    print(min([78, 56, -2, 12, 8, -33]))
