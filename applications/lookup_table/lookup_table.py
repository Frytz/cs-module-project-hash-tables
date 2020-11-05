# Your code here
import math
import random

import time

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v
table = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if str((x,y)) not in table:
        
        val = math.pow(x,y)
        val = math.factorial(val)
        val //= (x + y)
        val %= 982451653
        table[str((x,y))] = val
        return val
    else:
        val = table[str((x,y))]
        return y


# Do not modify below this line!
start_time = time.time()
for i in range(50000):
    
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
    # print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')
end_time =time.time()
print(f" the runtime is {end_time - start_time} seconds")