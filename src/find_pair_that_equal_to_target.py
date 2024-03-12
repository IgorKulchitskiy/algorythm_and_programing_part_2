def find_pair_which_equal_target(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None

numbers = [2, 7, 11, 15]
target = 9
result = find_pair_which_equal_target(numbers, target)
if result is not None:
    print("Пара знайдена для такого target", result)
else:
    print('Нема пари для target', target)
