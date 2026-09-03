import json
import sqlite3

import pytest

from app import create_app


@pytest.fixture
def resources(tmp_path):
    db_path = tmp_path / "tasks.db"
    export_path = tmp_path / "tasks.json"
    app = create_app(db_path, export_path)
    return app.test_client(), db_path, export_path


def test_create_task(resources):
    client, db_path, export_path = resources

    response = client.post("/tasks", json={"title": "Вивчити pytest"})

    assert response.status_code == 201
    assert response.get_json()["title"] == "Вивчити pytest"
    with sqlite3.connect(db_path) as connection:
        row = connection.execute("SELECT title FROM tasks").fetchone()
    assert row == ("Вивчити pytest",)
    assert json.loads(export_path.read_text(encoding="utf-8"))[0]["title"] == "Вивчити pytest"


def test_get_tasks(resources):
    client, _, _ = resources
    client.post("/tasks", json={"title": "Перше завдання"})
    client.post("/tasks", json={"title": "Друге завдання"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert [task["title"] for task in response.get_json()] == [
        "Перше завдання",
        "Друге завдання",
    ]


def test_create_task_requires_title(resources):
    client, _, export_path = resources

    response = client.post("/tasks", json={})

    assert response.status_code == 400
    assert not export_path.exists()
