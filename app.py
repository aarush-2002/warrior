"""
100-DAY WARRIOR - Main Flask PWA Application
Minecraft Edition with 100 Days Roadmap
"""

from flask import Flask, render_template, request, jsonify
import sqlite3
import json
from datetime import datetime, timedelta
from ai_engine import (
    calculate_body_stats,
    generate_morning_workout,
    generate_running_plan,
    generate_diet_plan,
    generate_study_plan,
    get_current_phase,
)
from roadmap import get_full_roadmap

app = Flask(__name__)
ROADMAP = get_full_roadmap()


def init_db():
    conn = sqlite3.connect("warrior.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            id INTEGER PRIMARY KEY,
            name TEXT DEFAULT 'Warrior',
            weight REAL DEFAULT 75,
            height_cm REAL DEFAULT 175.26,
            age INTEGER DEFAULT 18,
            target_weight REAL DEFAULT 67,
            start_date TEXT,
            telegram_chat_id TEXT DEFAULT ''
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS daily_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE,
            day_number INTEGER,
            weight REAL,
            morning_workout_done INTEGER DEFAULT 0,
            morning_workout_time REAL DEFAULT 0,
            evening_run_done INTEGER DEFAULT 0,
            running_time REAL DEFAULT 0,
            running_distance REAL DEFAULT 0,
            study_time REAL DEFAULT 0,
            water_glasses INTEGER DEFAULT 0,
            calories_burned REAL DEFAULT 0,
            mood TEXT DEFAULT 'good',
            notes TEXT DEFAULT ''
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS weight_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            weight REAL
        )
    """)

    c.execute("SELECT COUNT(*) FROM user_profile")
    if c.fetchone()[0] == 0:
        today = datetime.now().strftime("%Y-%m-%d")
        c.execute(
            "INSERT INTO user_profile (name, weight, height_cm, age, target_weight, start_date) VALUES (?, ?, ?, ?, ?, ?)",
            ("Warrior", 75, 175.26, 18, 67, today),
        )

    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect("warrior.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_day_number():
    conn = get_db()
    user = conn.execute("SELECT start_date FROM user_profile WHERE id=1").fetchone()
    conn.close()
    if user and user["start_date"]:
        start = datetime.strptime(user["start_date"], "%Y-%m-%d")
        delta = (datetime.now() - start).days + 1
        return max(1, min(delta, 100))
    return 1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/dashboard")
def dashboard():
    day_number = get_day_number()
    conn = get_db()

    user = conn.execute("SELECT * FROM user_profile WHERE id=1").fetchone()
    today = datetime.now().strftime("%Y-%m-%d")
    today_log = conn.execute(
        "SELECT * FROM daily_log WHERE date=?", (today,)
    ).fetchone()

    stats = calculate_body_stats(user["weight"], user["height_cm"], user["age"])
    phase_num, phase_name, phase_desc = get_current_phase(day_number)

    total_study = conn.execute(
        "SELECT COALESCE(SUM(study_time), 0) as total FROM daily_log"
    ).fetchone()["total"]
    total_workouts = conn.execute(
        "SELECT COUNT(*) as total FROM daily_log WHERE morning_workout_done=1"
    ).fetchone()["total"]
    total_runs = conn.execute(
        "SELECT COUNT(*) as total FROM daily_log WHERE evening_run_done=1"
    ).fetchone()["total"]
    total_distance = conn.execute(
        "SELECT COALESCE(SUM(running_distance), 0) as total FROM daily_log"
    ).fetchone()["total"]

    conn.close()

    return jsonify({
        "day_number": day_number,
        "days_remaining": 100 - day_number,
        "phase": phase_num,
        "phase_name": phase_name,
        "phase_desc": phase_desc,
        "progress_percent": day_number,
        "current_weight": user["weight"],
        "target_weight": user["target_weight"],
        "stats": stats,
        "today_log": dict(today_log) if today_log else None,
        "totals": {
            "study_hours": round(total_study / 3600, 1),
            "workouts": total_workouts,
            "runs": total_runs,
            "distance_km": round(total_distance, 1),
        },
    })


@app.route("/api/workout")
def workout():
    day_number = get_day_number()
    workout_plan = generate_morning_workout(day_number)
    running_plan = generate_running_plan(day_number)
    return jsonify({"morning": workout_plan, "evening": running_plan})


@app.route("/api/diet")
def diet():
    day_number = get_day_number()
    diet_plan = generate_diet_plan(day_number)
    return jsonify(diet_plan)


@app.route("/api/study")
def study():
    day_number = get_day_number()
    study_plan = generate_study_plan(day_number)
    return jsonify(study_plan)


@app.route("/api/roadmap")
def roadmap_all():
    day_number = get_day_number()
    days_list = []
    for d in range(1, 101):
        day_data = ROADMAP.get(d, {})
        day_data["is_current"] = (d == day_number)
        day_data["is_completed"] = (d < day_number)
        day_data["is_locked"] = (d > day_number)
        days_list.append(day_data)
    return jsonify({"days": days_list, "current_day": day_number})


@app.route("/api/roadmap/<int:day>")
def roadmap_day(day):
    if day in ROADMAP:
        day_number = get_day_number()
        data = ROADMAP[day].copy()
        data["is_current"] = (day == day_number)
        data["is_completed"] = (day < day_number)
        data["is_locked"] = (day > day_number)
        return jsonify(data)
    return jsonify({"error": "Day not found"}), 404


@app.route("/api/log", methods=["POST"])
def log_data():
    data = request.json
    today = datetime.now().strftime("%Y-%m-%d")
    day_number = get_day_number()
    conn = get_db()

    existing = conn.execute(
        "SELECT id FROM daily_log WHERE date=?", (today,)
    ).fetchone()

    if existing:
        fields = []
        values = []
        for key in [
            "weight", "morning_workout_done", "morning_workout_time",
            "evening_run_done", "running_time", "running_distance",
            "study_time", "water_glasses", "mood", "notes",
        ]:
            if key in data:
                fields.append(f"{key}=?")
                values.append(data[key])

        if fields:
            values.append(today)
            conn.execute(
                f"UPDATE daily_log SET {', '.join(fields)} WHERE date=?",
                values,
            )
    else:
        conn.execute(
            """INSERT INTO daily_log 
            (date, day_number, weight, morning_workout_done, morning_workout_time,
            evening_run_done, running_time, running_distance, study_time, 
            water_glasses, mood, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                today, day_number,
                data.get("weight", 0),
                data.get("morning_workout_done", 0),
                data.get("morning_workout_time", 0),
                data.get("evening_run_done", 0),
                data.get("running_time", 0),
                data.get("running_distance", 0),
                data.get("study_time", 0),
                data.get("water_glasses", 0),
                data.get("mood", "good"),
                data.get("notes", ""),
            ),
        )

    if "weight" in data and data["weight"] > 0:
        conn.execute(
            "INSERT INTO weight_log (date, weight) VALUES (?, ?)",
            (today, data["weight"]),
        )
        conn.execute(
            "UPDATE user_profile SET weight=? WHERE id=1", (data["weight"],)
        )

    conn.commit()
    conn.close()
    return jsonify({"status": "success"})


@app.route("/api/progress")
def progress():
    conn = get_db()

    weight_data = conn.execute(
        "SELECT date, weight FROM weight_log ORDER BY date"
    ).fetchall()

    daily_data = conn.execute(
        "SELECT * FROM daily_log ORDER BY date"
    ).fetchall()

    conn.close()

    return jsonify({
        "weight_history": [
            {"date": w["date"], "weight": w["weight"]} for w in weight_data
        ],
        "daily_history": [dict(d) for d in daily_data],
    })


@app.route("/api/water", methods=["POST"])
def update_water():
    today = datetime.now().strftime("%Y-%m-%d")
    conn = get_db()

    existing = conn.execute(
        "SELECT water_glasses FROM daily_log WHERE date=?", (today,)
    ).fetchone()

    if existing:
        new_count = existing["water_glasses"] + 1
        conn.execute(
            "UPDATE daily_log SET water_glasses=? WHERE date=?",
            (new_count, today),
        )
    else:
        day_number = get_day_number()
        conn.execute(
            "INSERT INTO daily_log (date, day_number, water_glasses) VALUES (?, ?, 1)",
            (today, day_number),
        )
        new_count = 1

    conn.commit()
    conn.close()
    return jsonify({"water_glasses": new_count})


@app.route("/api/setup", methods=["POST"])
def setup():
    data = request.json
    conn = get_db()
    conn.execute(
        """UPDATE user_profile SET 
        name=?, weight=?, height_cm=?, age=?, start_date=?, telegram_chat_id=?
        WHERE id=1""",
        (
            data.get("name", "Warrior"),
            data.get("weight", 75),
            data.get("height_cm", 175.26),
            data.get("age", 18),
            data.get("start_date", datetime.now().strftime("%Y-%m-%d")),
            data.get("telegram_chat_id", ""),
        ),
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)