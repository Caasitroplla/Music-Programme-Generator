class Concert:
    def __init__(self) -> None:
        self.title = Title()
        self.events = []

    def add_event(self, event=None):
        if isinstance(event, (Event, Performance, Interval)):
            self.events.append(event)
            return 0
        elif isinstance(event, Title):
            print("Title object detected, use 'Concert.title' to set titlepage")
        else:
            print("Invalid event type")
        return 1

    def remove_event(self, index=None):
        if index is None:
            index = input("Input Index")
        try:
            self.events.remove(index)
        except IndexError:
            print("Invalid index")
            return 1
        return 0

    def __str__(self):
        return self.title.name

    def to_dict(self) -> dict:
        return {
            "concert_details": self.title.to_dict(),
            "events": [
                event.to_dict() for event in self.events
            ]
        }

class Container:
    def __init__(self, type: str, name: str):
        self.type = type
        self.name = name

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "name": self.name
        }

class Title(Container):
    def __init__(self):
        super().__init__("title", "Untitled Concert")
        self.authors = []
        self.date = "01/01/2001"

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "name": self.name,
            "authors": self.authors,
            "date": self.date
        }
    
class Event(Container):
    def __init__(self):
        super().__init__("event", "Untitled Event")
        self.performances = []

    def add_performance(self, performance):
        if isinstance(performance, Performance):
            self.performances.append(performance)
        else:
            print("Invalid performance type")
            return 1
        return 0

    def remove_performance(self, index):
        try:
            self.performances.remove(index)
        except IndexError:
            print("Invalid index")
            return 1
        return 0

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "name": self.name,
            "performances": [
                performance.to_dict() for performance in self.performances
            ]
        }

class Performance(Container):
    def __init__(self):
        super().__init__("performance", "Untitled Performance")
        self.composer = "Untitled Composer"
    
    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "name": self.name,
            "composer": self.composer
        }

class Interval(Container):
    def __init__(self):
        super().__init__("interval", "Interval")
        self.details = "Refreshments will be served in the Annexe"

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "name": self.name,
            "details": self.details
        }