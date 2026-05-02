import json
import os
from datetime import datetime

DB_FILE = "data.json"


def load_data():
    """Load data from JSON file."""
    if not os.path.exists(DB_FILE):
        return {"players": {}}

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """Save data to JSON file."""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def create_tables():
    """Compatibility function (does nothing now)."""
    if not os.path.exists(DB_FILE):
        save_data({"players": {}})


def get_or_create_player(username):
    """Ensure player exists."""
    data = load_data()

    if username not in data["players"]:
        data["players"][username] = []

    save_data(data)
    return username


def save_result(username, score, level):
    """Save game result."""
    data = load_data()

    if username not in data["players"]:
        data["players"][username] = []

    data["players"][username].append({
        "score": score,
        "level": level,
        "played_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    save_data(data)


def get_personal_best(username):
    """Get best score of player."""
    data = load_data()

    if username not in data["players"]:
        return 0

    scores = [game["score"] for game in data["players"][username]]
    return max(scores) if scores else 0


def get_top_scores(limit=10):
    """Get leaderboard."""
    data = load_data()

    all_scores = []

    for username, games in data["players"].items():
        for game in games:
            all_scores.append((
                username,
                game["score"],
                game["level"],
                game["played_at"]
            ))

    # сортировка как в SQL
    all_scores.sort(key=lambda x: (-x[1], -x[2], x[3]))

    return all_scores[:limit]