class Engine:
    def __init__(self):
        pass

    def start(self):
        return "Engine started"

class Driver:
    def __init__(self):
        pass

# Car has an engine
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()
