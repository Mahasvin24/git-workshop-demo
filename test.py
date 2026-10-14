"""Tests for the intended queue behavior; the starter methods are unfinished."""

import unittest

from doctors_office_queue import DoctorsOfficeQueue


class DoctorsOfficeQueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = DoctorsOfficeQueue()

    def test_add_person(self):
        self.queue.add_person("patient-1")
        self.assertEqual(self.queue.count(), 1)

    def test_remove_person(self):
        self.queue.add_person("patient-1")
        self.queue.add_person("patient-2")
        self.assertEqual(self.queue.remove_person(), "patient-1")
        self.assertEqual(self.queue.remove_person(), "patient-2")
        self.assertIsNone(self.queue.remove_person())

    def test_count(self):
        self.queue.add_person("patient-1")
        self.queue.add_person("patient-2")
        self.queue.remove_person()
        self.assertEqual(self.queue.count(), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
