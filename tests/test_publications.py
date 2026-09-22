from publications import (
    add_publication,
    find_publications,
    publications_by_author,
)
from models import Publication


def test_add_publication():
    publications = []
    add_publication(publications, "Публикация", "Журнал", "Автор")
    assert len(publications) == 1
    assert isinstance(publications[0], Publication)


def test_find_publications():
    publications = []
    add_publication(publications, "Публикация", "Журнал", "Автор")
    assert find_publications(publications, "публик")


def test_publications_by_author():
    publications = []
    add_publication(publications, "Публикация", "Журнал", "Автор")
    add_publication(publications, "Вторая", "Журнал", "Второй")
    assert publications_by_author(publications, "автор")
