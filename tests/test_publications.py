from publications import add_publication, find_publications
from models import Publication


def test_add_publication():
    publications = []
    add_publication(publications, "Публикация", "Журнал")
    assert len(publications) == 1
    assert isinstance(publications[0], Publication)


def test_find_publications():
    publications = []
    add_publication(publications, "Публикация", "Журнал")
    assert find_publications(publications, "публик")
