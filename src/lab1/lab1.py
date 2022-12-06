import numpy


def foo():
    x = range(9999999)
    print(f"Сумма [0-9999999]: {numpy.sum(x)}; "
          f"Среднее: {numpy.average(x)}")
    return


def bar():
    x = numpy.random.randint(0, 100, size=10000)

    print(f"\n{x}")
    print(f"Произведение 10000 случ. чисел в [0, 100): {numpy.prod(x)}; "
          f"Медиана 10000 случ. чисел: {numpy.median(x)}")

    return


foo()
bar()
