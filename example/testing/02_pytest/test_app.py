import pytest

from app import Figure


@pytest.fixture
def square():
    return Figure("квадрат", 5)


def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    assert Figure(figure_type, 1).type == figure_type


def test_square_length(square):
    assert square.get_figure_length == 5


def test_invalid_figure():
    with pytest.raises(AssertionError):
        Figure("коло", 1)