import map_impl
import reduce_impl
import requests
import json

map_impl.test()

print()

reduce_impl.test()

print()

data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()

print(json.dumps(data, indent=4) + '\n')

print(f"1 {data['base']} max rate: "
      f"{reduce_impl.reduce_t(lambda x, y: x if x[1] > y[1] else y, data['rates'].items())}" + '\n')

map_impl.map_t(lambda x: print(f"60 {data['base']} = {x[1] * 60} {x[0]}"), data['rates'].items())

