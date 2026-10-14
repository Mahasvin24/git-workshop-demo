# Doctor's Office Queue — Git Workshop

A small Python project for practicing Git. Requires Python 3; no extra packages
are needed.

## Queue

`doctors_office_queue.py` contains `DoctorsOfficeQueue`. Its methods currently
return `None`; the exercise is to implement this behavior:

- `add_person(person_id)` adds an ID to the end of the queue.
- `remove_person()` removes and returns the first ID added. Returns `None` when
  the queue is empty.
- `count()` returns the number of people waiting.

Once implemented, the queue should work like this:

```python
from doctors_office_queue import DoctorsOfficeQueue

queue = DoctorsOfficeQueue()
queue.add_person("patient-1")
queue.add_person("patient-2")
print(queue.count())          # 2
print(queue.remove_person())  # patient-1
print(queue.count())          # 1
```

## Run the tests

From this directory, run:

```sh
python3 test.py
```

**All three tests currently fail.** The tests assert the intended behavior, but
the queue methods are unfinished. The runner prints each result and a summary,
and exits with a nonzero status while tests fail.

## Git exercise

1. Run the tests and read the failures.
2. Create a branch with `git switch -c implement-queue`.
3. Implement a queue method, then run the tests again.
4. Review your change with `git diff`.
5. Stage and commit it with `git add doctors_office_queue.py` and
   `git commit -m "Implement queue method"`.
6. Continue implementing the queue until all three tests pass.
