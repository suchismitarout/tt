def arrangeOddAndEven(arr, n):
    oddInd = 1
    evenInd = 0
    while (True):

        while (evenInd < n and arr[evenInd] % 2 == 0):
            evenInd += 2

        while (oddInd < n and arr[oddInd] % 2 == 1):
            oddInd += 2

        if (evenInd < n and oddInd < n):
            temp = arr[evenInd]
            arr[evenInd] = arr[oddInd]
            arr[oddInd] = temp;

        else:
            break


# function to print the array
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], "", end="")

    # Driver function


def main():
    arr = [3, 1, 5, 7, 6, 6, 4, 8, 2, 3]
    n = len(arr)

    print("Original Array: ", end="")
    printArray(arr, n)

    arrangeOddAndEven(arr, n)

    print("\nModified Array: ", end="")
    printArray(arr, n)


if __name__ == '__main__':
    main()
    # This code is contributed by 29AjayKumar