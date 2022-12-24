class LabEntity:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class LabTaskAction(LabEntity):
    def __init__(self, id, name, description, method_sig: str):
        super().__init__(id, name, description)
        self.signature = method_sig


class LabTask(LabEntity):

    def __init__(self, id, name, description, actions: [LabTaskAction] = None):
        super().__init__(id, name, description)

        if actions is None:
            actions = []

        self.actions = actions


class Lab(LabEntity):

    def __init__(self, id, name, description, tasks: [LabTask] = None):
        super().__init__(id, name, description)

        if tasks is None:
            tasks = []

        self.tasks = tasks


class LabNode(LabEntity):
    def __init__(self, id, name, description, labs: [Lab] = None):
        super().__init__(id, name, description)

        if labs is None:
            labs = []

        self.labs = labs
