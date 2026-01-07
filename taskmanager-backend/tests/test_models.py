from app.models import Task

def test_task_creation(app):
    task = Task(title="Test Task")

    assert task.title == "Test Task"
    assert task.completed is False
    assert task.description is None
