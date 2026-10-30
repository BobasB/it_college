import pytest

from app import Figure


@pytest.mark.parametrize(
    ("figure_type", "expected_angles"),
    [("квадрат", 4), ("прямокутник", 4), ("трикутник", 3)],
)
def test_get_angles(figure_type, expected_angles):
    assert Figure(figure_type, 1).get_angles == expected_angles


def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


def test_unknown_type_uses_fallback():
    figure = Figure("квадрат", 1)
    figure.type = "коло"

    assert figure.get_angles == 0