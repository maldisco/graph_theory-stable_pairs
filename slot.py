class Slot:

    def __init__(self, preferences) -> None:
        self.preferences = preferences
        self.available = True
    
    def set_available(self, value):
        self.available = value