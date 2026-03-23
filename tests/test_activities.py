def test_get_activities(client):
    """Test retrieving all activities."""
    response = client.get("/activities")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9  # All activities present

    # Check that Chess Club is present with correct structure
    assert "Chess Club" in data
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_get_activities_has_all_activities(client):
    """Test that all expected activities are returned."""
    response = client.get("/activities")
    data = response.json()

    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Soccer Club",
        "Art Club",
        "Drama Club",
        "Debate Club",
        "Science Club"
    ]

    for activity in expected_activities:
        assert activity in data