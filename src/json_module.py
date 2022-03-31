from objects import Concert, Title, Event, Performance, Interval

import json

def construct_concert_object(data: dict):
    concert = Concert()
    concert.title = Title()
    concert.title.name = data.get("name", "Unnamed Event")
    concert.title.authors = data.get("authors", [])
    concert.title.date = data.get("date", "01/01/2001")
    return concert

def construct_event_object(event: dict):
    if event.get("type") in ["ensemble", "solo"]:
            event_object = Event()
            event_object.name = event.get("name", "Untitled Event")
            for performance in event.get("performances", []):
                performance_object = Performance()
                performance_object.name = performance.get("name", "Untitled Song")
                performance_object.author = performance.get("author", "Untitled Author")
                event_object.add_performance(performance_object)
    elif event.get("type") == "interval":
        event_object = Interval()
        event_object.name = event.get("name", "Interval")
        event_object.details = event.get("details", "")
    else:
        print(f"Event {event} type not recognised")
        return (1, None)
    return (0, event_object)

def open_concert(filepath):
    with open(filepath) as jsonfile:
        dict = json.load(jsonfile)
    concert = construct_concert_object(dict.get("concert_details", {}))
    for event in dict.get("events", []):
        skip, event_object = construct_event_object(event)
        if not skip:
            concert.add_event(event_object)
    return concert

# def save_concert(filepath, concert):
#     with open(filepath) as jsonfile: