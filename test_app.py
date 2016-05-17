import arrow
from app import adays_vacation, availability


vacation = [("2013-05-28", "2013-06-04"), "2013-06-06"]


def test_availability():
    assert availability("2013-01-01", "2013-01-14", vacation) == 10
    assert availability("2013-05-28", "2013-05-29", vacation) == 0
    assert availability("2013-05-27", "2013-05-29", vacation) == 1
    assert availability("2013-05-28", "2013-06-06", vacation) == 1
    assert availability("2013-06-05", "2013-06-08", vacation) == 2  # weekend


def test_adays_vacation():
    assert arrow.get("2013-05-27") not in adays_vacation(vacation)
    assert arrow.get("2013-06-01") in adays_vacation(vacation)
    assert arrow.get("2013-06-05") not in adays_vacation(vacation)
    assert arrow.get("2013-06-06") in adays_vacation(vacation)
    assert arrow.get("2013-06-07") not in adays_vacation(vacation)
