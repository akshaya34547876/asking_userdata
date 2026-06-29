from flask import Flask, request, render_template

app = Flask(__name__)

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

        return f"""
        PRINTING USER DATA<br><br>
        USER NAME --> {user_name}<br><br>
        USER AGE --> {user_age}<br><br>
        USER CHANNEL NAME --> {user_channel_name}<br><br>
        USER SUBSCRIBERS --> {user_subscribers}<br><br>
        USER CHANNEL CREATION DATE --> {user_date}<br><br>
        USER COUNTRY --> {user_country}<br><br>
        USER HIGHEST VIEW COUNT --> {userhighestview}<br><br>
        USER SERVICE LOOKING FOR --> {user_service_looking_for}<br><br>
        """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)