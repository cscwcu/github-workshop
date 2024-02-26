import ast
import sys


def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[smallest]:
        smallest = left
    if right < n and arr[right] > arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def buildMinHeap(arr):
    n = len(arr)
    startIdx = n // 2 - 1
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)

def heapify_arrays_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            arr = line.strip()

            buildMinHeap(arr)

            print("Min Heap:", arr)


def main():
    file = sys.argv[0]
    heapify_arrays_from_file(file)

if __name__ == "__main__":
    main()
