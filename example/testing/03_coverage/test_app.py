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