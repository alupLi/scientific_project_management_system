from publications import (
    add_publication,
    find_publications,
    publications_by_author,
)
from models import Researcher


def test_add_publication():
    publications = []
    author = Researcher(1, "Иванов", "Физика")
    add_publication(
        publications, "Публикация", "Журнал", [author],
    )
    assert len(publications) == 1
    assert publications[0].authors[0] is author


def test_find_publications():
    publications = []
    add_publication(publications, "Публикация", "Журнал", "Автор")
    assert find_publications(publications, "публик")


def test_publications_by_author():
    publications = []
    a1 = Researcher(1, "Иванов", "Физика")
    a2 = Researcher(2, "Петров", "Химия")
    add_publication(publications, "Первая", "Журнал", [a1])
    add_publication(publications, "Вторая", "Журнал", [a2])
    assert publications_by_author(publications, "иванов")
