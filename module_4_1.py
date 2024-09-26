from fake_math import divide as error
from true_math import divide as inf

result1 = error(69, 3)
result2 = error(3, 0)
result3 = inf(49, 7)
result4 = inf(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)