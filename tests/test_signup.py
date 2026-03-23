def test_signup_success(client):
    """Test successful signup for an activity."""
    response = client.post("/activities/Chess%20Club/signup?email=test@example.com")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "test@example.com" in data["message"]
    assert "Chess Club" in data["message"]

    # Verify the participant was added
    response2 = client.get("/activities")
    activities = response2.json()
    assert "test@example.com" in activities["Chess Club"]["participants"]


def test_signup_duplicate(client):
    """Test that duplicate signup returns error."""
    # First signup
    client.post("/activities/Programming%20Class/signup?email=dup@example.com")

    # Second signup should fail
    response = client.post("/activities/Programming%20Class/signup?email=dup@example.com")
    assert response.status_code == 400

    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"]


def test_signup_invalid_activity(client):
    """Test signup for non-existent activity."""
    response = client.post("/activities/NonExistent/signup?email=test@example.com")
    assert response.status_code == 404

    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]