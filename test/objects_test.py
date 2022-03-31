import unittest
from src.objects import Concert, Event, Performance, Interval

class TestObjects(unittest.TestCase):
    def concert_test(self):
        concert = Concert()
        concert.title = "Test Concert"

        self.assertEqual(str(concert), "Test Concert")
        self.assertEqual(concert.add_event(Event().add_performance(Performance())), 0)
        self.assertEqual(concert.add_event(Interval()), 0)

        self.assertEqual(str(concert.events[0]), "Untitled Event")
        self.assertEqual(str(concert.events[0].performances[0]), "Untitled Performance")