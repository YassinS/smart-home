class Action:
    def __init__(self, id, content):
        self.id = id
        self.content = content

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def set_id(self, id):
        self.id = id


class Group:
    def __init__(self, group_id) -> None:
        self.group_id = group_id
        self.device_ids = []
        self.actions = []

    def __str__(self) -> str:
        return f"Group {self.group_id}"

    def add_device(self, device_id):
        self.device_ids.append(device_id)

    def remove_device(self, device_id):
        self.device_ids.remove(device_id)

    def add_action(self, action):
        self.actions.append(action)

    def remove_action(self, action):
        self.actions.remove(action)


class Program:
    def __init__(self):
        self.devices = []
        self.rooms = []
        self.groups = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device):
        self.devices.remove(device)

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        self.rooms.remove(room)

    def add_group(self, group):
        self.groups.append(group)

    def remove_group(self, group):
        self.groups.remove(group)


class Room:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id


class WebGui:
    def __init__(self, port):
        self.port = port

    def start(self):
        print(f"Web GUI started on port {self.port}")

    def stop(self):
        print("Web GUI stopped")
