from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "responses.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            user_age TEXT,
            user_channel_name TEXT,
            user_subscribers TEXT,
            user_date TEXT,
            user_country TEXT,
            userhighestview TEXT,
            user_service_looking_for TEXT
        )
    """)
    conn.commit()
    conn.close()


init_db()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        user_age = request.form.get("user_age")
        user_channel_name = request.form.get("user_channel_name")
        user_subscribers = request.form.get("user_subscribers")
        user_date = request.form.get("user_date")
        user_country = request.form.get("user_country")
        userhighestview = request.form.get("userhighestview")
        user_service_looking_for = request.form.get("user_service_looking_for")

        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO responses (
                user_name, user_age, user_channel_name, user_subscribers,
                user_date, user_country, userhighestview, user_service_looking_for
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_name, user_age, user_channel_name, user_subscribers,
            user_date, user_country, userhighestview, user_service_looking_for
        ))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("index.html")


@app.route("/admin")
def admin():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM responses ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return render_template("admin.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
