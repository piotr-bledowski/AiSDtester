def readinput():
    inp = input()
    return tuple(float(x) for x in inp.split(' ') if not x == '')


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


class Solution:

    def __init__(self, inp_arr):
        self.merge_calls = 0
        self.merge_sort_calls = 0
        self.quicksort_calls = 0
        self.partition_calls = 0
        self.arr = inp_arr

    def bubble_sort(self):
        for i in range(len(self.arr)-1):
            for j in range(len(self.arr)-1, i, -1):
                if self.arr[j-1] > self.arr[j]:
                    self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
            print(self.arr)


    # implementacja inspirowana 4 wydaniem Cormena
    def insertion_sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
            print(self.arr)



    def bucket_sort(self):
        B = [[] for _ in range(len(self.arr))]
        for i in range(len(self.arr)):
            B[int(len(self.arr)*self.arr[i])].append(self.arr[i])
        for i in range(len(B)):
            B[i].sort()
        print(B)
        # Concatenating B in a neat single line
        self.arr = [inner for outer in B for inner in outer]


    def merge(self, l, m, r):
        self.merge_calls += 1
        l_arr = self.arr[l:m+1]
        r_arr = self.arr[m+1:r+1]

        i = 0
        j = 0
        k = l

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] <= r_arr[j]:
                self.arr[k] = l_arr[i]
                i += 1
            else:
                self.arr[k] = r_arr[j]
                j += 1
            k += 1
        
        while i < len(l_arr):
            self.arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            self.arr[k] = r_arr[j]
            j += 1
            k += 1


    def merge_sort(self, l, r):
        self.merge_sort_calls += 1
        if l >= r:
            return
        m = (l + r) // 2
        self.merge_sort(l, m)
        self.merge_sort(m+1, r)
        self.merge(l, m, r)


    # wersja Lomuto według 4 wydania Cormena
    def partition(self, l, r):
        self.partition_calls += 1
        x = self.arr[r]
        i = l - 1
        for j in range(l, r):
            if self.arr[j] <= x:
                i += 1
                swap(self.arr, i, j)
        swap(self.arr, i+1, r)
        return i + 1


    def quick_sort(self, l, r):
        self.quicksort_calls += 1
        if l < r:
            m = self.partition(l, r)
            self.quick_sort(l, m-1)
            self.quick_sort(m+1, r)


inp1 = readinput()

arr = [float(n) for n in list(inp1[2:])]

print(arr)

#arr_copy = arr[:]

# if inp1[1] == 1:
#     insertion_sort(arr_copy)
#     print(arr_copy)
# elif inp1[1] == 2:
#     bubble_sort(arr_copy)
#     print(arr_copy)
# elif inp1[1] == 3:
#     bucket_sort(arr_copy)
#     print(arr_copy)
# elif inp1[1] == 4:
#     merge_sort(arr_copy, 0, len(arr)-1)
#     print(arr_copy)
# else:
#     quick_sort(arr_copy, 0, len(arr)-1)
#     print(arr_copy)

inp = readinput()

sorter = Solution(arr[:])

while inp[0] != -1:
    if inp[0] == 0:
        print(arr)
    else:
        arr_copy = arr[:]
        if inp[0] == 1:
            sorter.arr = arr[:]
            sorter.insertion_sort()
            print(sorter.arr)
        elif inp[0] == 2:
            sorter.arr = arr[:]
            sorter.bubble_sort()
            print(sorter.arr)
        elif inp[0] == 3:
            sorter.arr = arr[:]
            sorter.bucket_sort()
            print(sorter.arr)
        elif inp[0] == 4:
            sorter.arr = arr[:]
            sorter.merge_sort_calls = 0
            sorter.merge_calls = 0
            sorter.merge_sort(0, len(arr)-1)
            print(str(sorter.merge_sort_calls) + ' ' + str(sorter.merge_calls))
            print(sorter.arr)
        else:
            sorter.arr = arr[:]
            sorter.partition_calls = 0
            sorter.quicksort_calls = 0
            sorter.quick_sort(0, len(arr)-1)
            print(str(sorter.quicksort_calls) + ' ' + str(sorter.partition_calls))
            print(sorter.arr)
    
    inp = readinput()

print('koniec')
