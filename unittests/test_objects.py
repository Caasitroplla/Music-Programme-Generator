import unittest
try:
    from objects import Concert, Event, Performance, Interval
except ModuleNotFoundError:
    from src.objects import Concert, Event, Performance, Interval

class test_objects(unittest.TestCase):
    def test_concert(self):
        concert = Concert()
        concert.title = "Test Concert"

        self.assertEqual(str(concert), "Test Concert")
        self.assertEqual(concert.add_event(Event().add_performance(Performance())), 0)
        self.assertEqual(concert.add_event(Interval()), 0)

        self.assertEqual(str(concert.events[0]), "Untitled Event")
        self.assertEqual(str(concert.events[0].performances[0]), "Untitled Performance")

