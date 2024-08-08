def binary_search_with_upper_bound(arr, target):
    if not isinstance(arr, list):
        raise ValueError("Input array must be a list.")
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements in the array must be numbers.")
    if not isinstance(target, (int, float)):
        raise ValueError("Target must be a number.")
    if len(arr) == 0:
        raise ValueError("Input array must not be empty.")

    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None  # Початкове значення - немає верхньої межі

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return (iterations, arr[mid])

    # Якщо не знайдено точний збіг, перевіряємо верхню межу
    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)

if __name__ == '__main__':
    try:
        # Тестування функції
        arr = [1.1, 1.3, 2.5, 3.8, 4.6]
        print(binary_search_with_upper_bound(arr, 3.5))  # (2, 3.8)
        print(binary_search_with_upper_bound(arr, 4))    # (3, 4.6)
        print(binary_search_with_upper_bound(arr, 6.0))  # (3, None)
        print(binary_search_with_upper_bound(arr, 2.5))  # (1, 2.5)
        print(binary_search_with_upper_bound(arr, 0))    # (1, 1.1)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
