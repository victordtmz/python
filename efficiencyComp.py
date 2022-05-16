
import sys
import timeit
a = (1,2,3,4, 'test', True, False, 'hello', 'trest', 3, 4, 5, 6, 7)
b = [1,2,3,4, 'test', True, False, 'hello', 'trest', 3, 4, 5, 6, 7]
print(sys.getsizeof(a), 'bytes')
print(sys.getsizeof(b), 'bytes')

print(timeit.timeit(stmt="(1,2,3,4, 'test', True, False, 'hello', 'trest', 3, 4, 5, 6, 7)", number=1000000))
print(timeit.timeit(stmt="[1,2,3,4, 'test', True, False, 'hello', 'trest', 3, 4, 5, 6, 7]", number=1000000))
