import sys
from past.builtins import xrange
x = xrange(1, 10)
y = range(1, 10)

print(sys.getsizeof(x))
print(sys.getsizeof(y))
