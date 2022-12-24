import encoders
import adapters


with open('./data/data.json', encoding='utf-8') as j:
    lab_node = adapters.jsonToLabNode(encoders.json.load(j))

if lab_node is not None:
    print(encoders.json.dumps(lab_node, ensure_ascii=False, indent=4, cls=encoders.LabNodeJsonEncoder))
