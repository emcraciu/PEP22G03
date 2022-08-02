"""
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and time worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""
import time
import datetime


class Kronos:

    employees = {}

    def __init__(self, day: float):
        self.day = datetime.datetime.now()

    def __iter__(self):
        return KronosIterator(self.employees)

    def add_start_time(self, name, start_time):
        hours, minutes, seconds = start_time.split(":")
        self.employees[name] = [datetime.datetime(
            year=self.day.year, month=self.day.month, day=self.day.day,
            hour=int(hours), minute=int(minutes), second=int(seconds)
        )]

    def add_end_time(self, name, end_time):
        hours, minutes, seconds = end_time.split(":")
        self.employees[name].append(datetime.datetime(
            year=self.day.year, month=self.day.month, day=self.day.day,
            hour=int(hours), minute=int(minutes), second=int(seconds)
        ))


class KronosIterator():

    working_hours = []

    def __init__(self, employees: dict):
        self.employees = employees
        for name, hours in self.employees.items():
            self.working_hours.append((name, hours[1] - hours[0]))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.working_hours:
            raise StopIteration
        return self.working_hours.pop()






k = Kronos(time.time())
k.add_start_time('Joe', "09:01:20")
k.add_end_time('Joe', "09:01:30")

for emp in k:
    print(emp)