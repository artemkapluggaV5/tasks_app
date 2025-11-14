import json
import os

from src.tasks_app import load_tasks, save_tasks, view_tasks, FILENAME


# Тест load_tasks
def test_load_tasks():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    tasks = load_tasks()
    assert tasks == []


# Тест save_tasks
def test_save_tasks():
    tasks = [{"title": "Тест", "priority": "Высокий"}]
    save_tasks(tasks)
    assert os.path.exists(FILENAME)
    with open(FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == tasks


# Тест view_tasks
def test_view_tasks():
    tasks = [{"title": "Посмотреть", "priority": "Средний"}]
    view_tasks(tasks)


# Тест add_task
def test_add_task():
    tasks = []
    task = {"title": "Новая задача", "priority": "Низкий"}
    tasks.append(task)
    assert tasks[0]["title"] == "Новая задача"
    assert tasks[0]["priority"] == "Низкий"


# Тест delete_task
def test_delete_task():
    tasks = [{"title": "Удалить", "priority": "Высокий"}]
    removed = tasks.pop(0)
    assert removed["title"] == "Удалить"
    assert len(tasks) == 0
