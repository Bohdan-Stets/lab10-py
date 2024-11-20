def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = list(filter(lambda x: x < pivot, arr))
    middle = list(filter(lambda x: x == pivot, arr))
    right = list(filter(lambda x: x > pivot, arr))
    return quick_sort(left) + middle + quick_sort(right)

def search_element(arr, value):
    return value in arr

def find_five_minimums(arr):
    sorted_arr = quick_sort(arr)
    return sorted_arr[:5] if len(arr) >= 5 else sorted_arr

def average(arr):
    return sum(arr) / len(arr) if arr else 0

def remove_duplicates(arr):
    return list(set(arr))

work_list = [10, 3, 5, 3, 8, 3, 2, 9, 6, 7]

print("Швидке сортування:", quick_sort(work_list))
print("Пошук елементу (3):", search_element(work_list, 3))
print("Пошук перших п'яти мінімальних елементів:", find_five_minimums(work_list))
print("Середнє арифметичне:", average(work_list))
print("Список без повторів:", remove_duplicates(work_list))
