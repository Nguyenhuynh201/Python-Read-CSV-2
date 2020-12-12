import random
import statistics
random.seed(2020)

List_A = [random.randrange(100,121) for x in range(20)]

List_A_sorted = sorted(List_A)

list_median = statistics.median(List_A_sorted)

def find_mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))

list_mode = find_mode(List_A_sorted)

print(f'The median is {list_median}')
print(f'The mode is {list_mode}')


