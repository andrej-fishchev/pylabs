import json
import entities


class LabTaskActionJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, entities.LabTaskAction):
            return obj.__dict__

        return json.JSONEncoder.default(self, obj)


class LabTaskJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, entities.LabTask):
            return obj.__dict__

        if isinstance(obj, entities.LabTaskAction):
            return LabTaskActionJsonEncoder().default(obj)

        return json.JSONEncoder.default(self, obj)


class LabJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, entities.Lab):
            return obj.__dict__

        if isinstance(obj, entities.LabTask):
            return LabTaskJsonEncoder().default(obj)

        if isinstance(obj, entities.LabTaskAction):
            return LabTaskActionJsonEncoder().default(obj)

        return json.JSONEncoder.default(self, obj)


class LabNodeJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, entities.LabNode):
            return obj.__dict__

        if isinstance(obj, entities.Lab):
            return LabJsonEncoder().default(obj)

        if isinstance(obj, entities.LabTask):
            return LabTaskJsonEncoder().default(obj)

        if isinstance(obj, entities.LabTaskAction):
            return LabTaskActionJsonEncoder().default(obj)

        return json.JSONEncoder.default(self, obj)
