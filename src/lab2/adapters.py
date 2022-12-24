import entities


def toObjectList(f, elements: list):
    output = []

    for x in elements:
        buffer = f(x)

        if buffer is not None:
            output.append(buffer)

    return output


def jsonToLabTaskActionAdapter(json_obj: dict):
    obj = entities.LabTaskAction(0, "", "", "")

    if json_obj.keys() != obj.__dict__.keys():
        return None

    obj.__dict__ = json_obj

    return obj


def jsonToLabTaskAdapter(json_obj: dict):
    obj = entities.LabTask(0, "", "", [])

    if json_obj.keys() != obj.__dict__.keys():
        return None

    json_obj['actions'] = toObjectList(jsonToLabTaskActionAdapter, json_obj['actions'])

    obj.__dict__ = json_obj

    return obj


def jsonToLabAdapter(json_obj: dict):
    obj = entities.Lab(0, "", "", [])

    if json_obj.keys() != obj.__dict__.keys():
        return None

    json_obj['tasks'] = toObjectList(jsonToLabTaskAdapter, json_obj['tasks'])

    obj.__dict__ = json_obj

    return obj


def jsonToLabNode(json_obj: dict):
    obj = entities.LabNode(0, "", "", [])

    if json_obj.keys() != obj.__dict__.keys():
        return None

    json_obj['labs'] = toObjectList(jsonToLabAdapter, json_obj['labs'])

    obj.__dict__ = json_obj

    return obj
