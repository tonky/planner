from typing import List
from collections import namedtuple
import arrow  # type:ignore


sprint = namedtuple('Sprint', ['start', 'end'])("2013-05-27", "2013-06-21")

tonky = [("2013-05-28", "2013-06-04"), "2013-06-06"]
oleg = ["2013-04-02", ("2013-06-03", "2013-06-18")]


print(tonky)
print(oleg)


def adays_range(start: str, end: str) -> arrow.Arrow.range:
    return arrow.Arrow.range('day', arrow.get(start), arrow.get(end))


def adays_vacation(vacation: list) -> List[arrow.Arrow]:
    adays = []

    for item in vacation:
        if type(item) == str:
            adays.append(arrow.get(item))
        else:
            adays.extend(adays_range(*item))

    return adays


def pp(value):
    print("{:^3}".format(value), end=" ")


def availability(start: str, end: str, vacation: list) -> int:
    total = 0

    for aday in adays_range(arrow.get(start), arrow.get(end)):
        if aday.weekday() in [5, 6]:
            continue

        if aday in adays_vacation(vacation):
            continue

        total += 1

    return total


def print_person(vacation: list, adays: List[arrow.Arrow]) -> int:
    for aday in adays:
        if aday.weekday() in [5, 6]:
            pp(" ")
            continue

        if aday in adays_vacation(vacation):
            pp(0)
        else:
            pp(6)

    print("\t%d" % availability(sprint.start, sprint.end, vacation))


sprint_adays = adays_range(sprint.start, sprint.end)

for day in sprint_adays:
    if day.weekday() in [5, 6]:
        pp("-")
    else:
        pp(day.day)

print("\n")

print_person(tonky, sprint_adays)
print_person(oleg, sprint_adays)
