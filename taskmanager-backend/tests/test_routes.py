def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={"title": "My First Task"}
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "My First Task"
    assert data["completed"] is False


def test_get_tasks(client):
    client.post("/api/tasks", json={"title": "Task 1"})
    client.post("/api/tasks", json={"title": "Task 2"})

    response = client.get("/api/tasks")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2


def test_update_task(client):
    create = client.post("/api/tasks", json={"title": "Old Title"})
    task_id = create.get_json()["id"]

    response = client.put(
        f"/api/tasks/{task_id}",
        json={"title": "New Title", "completed": True}
    )

    data = response.get_json()
    assert data["title"] == "New Title"
    assert data["completed"] is True


def test_delete_task(client):
    create = client.post("/api/tasks", json={"title": "To Delete"})
    task_id = create.get_json()["id"]

    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 204
