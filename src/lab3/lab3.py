from pyDatalog import pyDatalog as PDL
from numpy import random as RND


PDL.create_terms('result, X, average, mult, median, summ, Y')

summ[X] = X + summ[X - 1]
summ[1] = 1

average[X] = X / 2

mult[X] = RND.randint(0, 100) * mult[X - 1]
mult[1] = 1

print(f"Sum [0 - 100]: {(summ[99] == X).v()[0]}")
print(f"Average [0 - 100]: {(average[99] == X).v()[0]}")

print()

print(f"Multiple (rand 100 elems in [0, 100)): {(mult[99] == X).v()[0]}")