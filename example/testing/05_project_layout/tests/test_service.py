import unittest
from unittest.mock import patch

import pytest

from lab.service import ask_name, build_report


class TestBuildReport(unittest.TestCase):
    # Підміняємо fetch_status там, де її ВИКОРИСТОВУЄ build_report (lab.service),
    # а тестуємо саме build_report
    @patch("lab.service.fetch_status", return_value={"status": "ok", "data": [1, 2, 3]})
    def test_report_uses_status(self, mock_fetch):
        self.assertEqual("Статус: ok, даних: 3", build_report())
        mock_fetch.assert_called_once()

    def test_report_without_mock_fails(self):
        with self.assertRaises(ConnectionError):
            build_report()


@patch("builtins.input", return_value="  марта ")
def test_ask_name_cleans_input(mock_input):
    assert ask_name() == "Марта"
    mock_input.assert_called_once_with("Введіть ім'я: ")


def test_ask_name_with_monkeypatch(monkeypatch):
    # те саме за допомогою вбудованої fixture pytest
    monkeypatch.setattr("builtins.input", lambda prompt: "олег")
    assert ask_name() == "Олег"


@pytest.mark.parametrize("raw, expected", [("іван", "Іван"), ("  ОЛЕНА ", "Олена"), ("", "")])
def test_ask_name_parametrized(monkeypatch, raw, expected):
    monkeypatch.setattr("builtins.input", lambda prompt: raw)
    assert ask_name() == expected
