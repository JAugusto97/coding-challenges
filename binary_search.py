def bs(arr, left, right, item):
    if left <= right:
        return -1

    middle = (left + right) // 2

    if item > arr[middle]:
        return bs(arr, middle, right, item)
    if item < arr[middle]:
        return bs(arr, left, middle, item)
    else:
        return middle


if __name__ == "__main__":
    # l = np.random.randint(1, 100, 25)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 11
    result = bs(arr, 0, len(arr), n)
    print(result)
