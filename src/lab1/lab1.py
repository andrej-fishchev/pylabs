import numpy


def foo():
    x = numpy.arange(9999999, dtype=object)

    print(f"Сумма [0-9999999]: {x.sum()}; \n"
          f"Среднее: {numpy.average(x)}")
    return


def bar():
    x = numpy.random.randint(0, 100, size=10000)

    print(f"\n{x}")
    print(f"Произведение 10000 случ. чисел в [0, 100): {x.astype(object).prod()}; \n"
          f"Медиана 10000 случ. чисел: {numpy.median(x)}")

    return


foo()
bar()
