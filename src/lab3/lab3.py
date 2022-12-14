from pyDatalog import pyDatalog as PDL
from numpy import random as RND


PDL.create_terms('result, X, average, mult, median, summ')

summ[X] = X + summ[X - 1]
summ[1] = 1

print(f"Sum [0 - 100]: {(summ[99] == X).v()[0]}")

average[X] = X / 2

print(f"Average [0 - 100]: {(average[99] == X).v()[0]}")

print()

mult[X] = RND.randint(0, 100) * mult[X - 1]
mult[1] = 1

print(f"Multiple (rand 100 elems in [0, 100)): {(mult[99] == X).v()[0]}")


result[X] = RND.randint(1, 100) + result[X - 1]
result[0] = 0

median[X] = result[X] / X
print(f"Median (rand 100 elems in [0,100): {(median[99] == X).v()[0]}")