class Concert:
    def __init__(self) -> None:
        self.title = Title()
        self.events = []

    def add_event(self, event):
        if isinstance(event, (Event, Performance, Interval)):
            self.events.append(event)
            return 0
        elif isinstance(event, Title):
            print("Title object detected, use 'Concert.title' to set titlepage")
        else:
            print("Invalid event type")
        return 1

    def remove_event(self, index):
        try:
            self.events.remove(index)
        except IndexError:
            print("Invalid index")
            return 1
        return 0

    def __str__(self):
        return self.title
        
class Container:
    def __init__(self, type: str):
        self.type = type

class Title(Container):
    def __init__(self):
        super().__init__("title")
        self.name = "Untitled Concert"
        self.authors = []
        self.date = "01/01/2001"
    
class Event(Container):
    def __init__(self):
        super().__init__("event")
        self.name = "Untitled Event"
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

class Performance(Container):
    def __init__(self):
        super().__init__("performance")
        self.name = "Untitled Performance"
        self.author = "Untitled Author"

class Interval(Container):
    def __init__(self):
        super().__init__("interval")
        self.name = "Interval"
        self.details = "Refreshments will be served in the Annexe"