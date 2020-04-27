import pytest

from ..models import Guitar


# Connects our tests with our database
pytestmark = pytest.mark.django_db

def test___str__():
    guitar = Guitar.objects.create(
        name="LesPaul",
        description="Semi-sweet guitar that goes well with Rock.",
        genre=Guitar.Genre.HARD_ROCK,
        )
    assert guitar.__str__() == "LesPaul"
    assert str(guitar) == "LesPaul"