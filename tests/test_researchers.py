from researchers import add_researcher, find_researcher, count_researchers
from models import Researcher


def test_add_researcher():
    researchers = []
    add_researcher(researchers, "Исследователь", "Область")
    assert len(researchers) == 1
    assert isinstance(researchers[0], Researcher)


def test_find_researcher():
    researchers = []
    add_researcher(researchers, "Исследователь", "Область")
    assert find_researcher(researchers, "исслед")


def test_count_researchers():
    researchers = []
    add_researcher(researchers, "Исследователь", "Область")
    add_researcher(researchers, "Второй", "Область")
    assert count_researchers(researchers) == 2
