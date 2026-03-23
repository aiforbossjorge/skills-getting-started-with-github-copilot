def test_unregister_success(client):
    """Test successful unregistration from an activity."""
    # First sign up
    client.post("/activities/Gym%20Class/signup?email=unreg@example.com")

    # Then unregister
    response = client.delete("/activities/Gym%20Class/signup?email=unreg@example.com")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "unreg@example.com" in data["message"]
    assert "Gym Class" in data["message"]

    # Verify the participant was removed
    response2 = client.get("/activities")
    activities = response2.json()
    assert "unreg@example.com" not in activities["Gym Class"]["participants"]


def test_unregister_not_signed_up(client):
    """Test unregistering when not signed up."""
    response = client.delete("/activities/Chess%20Club/signup?email=notsigned@example.com")
    assert response.status_code == 400

    data = response.json()
    assert "detail" in data
    assert "not signed up" in data["detail"]


def test_unregister_invalid_activity(client):
    """Test unregistering from non-existent activity."""
    response = client.delete("/activities/NonExistent/signup?email=test@example.com")
    assert response.status_code == 404

    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]