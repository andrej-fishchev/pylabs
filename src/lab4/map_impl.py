def map_t(f, iterable):
    return [f(x) for x in iterable]


def test():
    data = [x for x in range(10)]
    print(f"Testing map impl: \n"
          f"Source array: {data} \n"
          f"Func: lambda x: x + x \n"
          f"Use impl: {map_t(lambda x: x + x, data)}")
