
def reduce_t(f, iterable):
    iterator = iter(iterable)

    try:
        value = next(iterator)
    except StopIteration:
        return None

    for x in iterator:
        value = f(value, x)

    return value


def test():
    data = [x for x in range(10)]
    print(f"Testing reduce impl: \n"
          f"Source array: {data} \n"
          f"Func: lambda x, y: x + y \n"
          f"Use impl: {reduce_t(lambda x, y: x + y, data)}")
