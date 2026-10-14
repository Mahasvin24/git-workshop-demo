"""A simple first-in, first-out queue for a doctor's office."""

from collections import deque

class DoctorsOfficeQueue:
    def __init__(self):
        self._people = deque()

    def add_person(self, person_id):
        """Add a person's ID to the end of the queue."""
        print("1")
        return self._people.append(person_id)

    def remove_person(self):
        """Remove and return the next person's ID, or None if empty."""
        if not self._people:
            return None
        return self._people.popleft()

    def count(self):
        """Return how many people are waiting."""
        return len(self._people)
