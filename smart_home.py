class Device:
    def __init__(self, name, device_type, id, active, location):
        self.name = name
        self.device_type = device_type
        self.id = id
        self.active = active
        self.location = location

    def __str__(self):
        return f"{self.name} ({self.device_type} {self.id}) is {'active' if self.active else 'inactive'} and located in {self.location}"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_device_type(self):
        return self.device_type

    def get_active(self):
        return self.active

    def get_location(self):
        return self.location

    def set_name(self, name):
        self.name = name

    def set_active(self, active):
        self.active = active

    def set_location(self, location):
        self.location = location


class Actor(Device):
    def __init__(self, name, device_type, id, active, location, state):
        super().__init__(name, device_type, id, active, location)
        self.state = state

    def __str__(self):
        return f"{self.name} ({self.device_type} {self.id}) is {'active' if self.active else 'inactive'}, located in {self.location} state = {self.state}"

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False


class Sensor(Device):
    def __init__(self, name, device_type, id, active, location, value):
        super().__init__(name, device_type, id, active, location)
        self.value = value

    def __str__(self):
        return super().__str__() + f", value = {self.value}"

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class Button(Sensor):
    def __init__(self, name, id, active, location, state, value):
        super().__init__(name, "Button", id, active, location, state)
        self.value = value

    def __str__(self):
        return super().__str__() + f", button_value = {self.button_value}"


class Led(Actor):
    def __init__(self, name, id, active, location, state, candela):
        super().__init__(name, "LED", id, active, location, state)
        self.candela = candela

    def __str__(self):
        return super().__str__()


class RgbLed(Actor):
    def __init__(self, name, id, active, location, state, candela, color):
        super().__init__(name, "RGB LED", id, active, location, state)
        self.candela = candela
        self.color = color

    def __str__(self):
        return super().__str__() + f", color = {self.color}"

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
