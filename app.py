from flask import Flask, render_template, request, redirect, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyser = SentimentIntensityAnalyzer()

# Temporarily storing blocked users in memory
blocked_users = set()
temp_user_to_unblock = ""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    username = ""
    comment = ""

    if request.method == "POST":
        username = request.form["username"].strip()
        comment = request.form["comment"].strip()

        sentiment = analyser.polarity_scores(comment)
        compound_score = sentiment['compound']

        if username in blocked_users:
            result = f"🚫 User '{username}' is blocked from commenting due to harassment."
        else:
            if compound_score <= -0.5:
                result = f"⚠️ Harassment Detected! User '{username}' has been blocked."
                blocked_users.add(username)
            else:
                result = f"✅ Comment seems fine. Welcome, {username}!"

        username = ""
        comment = ""

    return render_template("index.html", result=result)

@app.route("/processing", methods=["POST"])
def processing():
    global temp_user_to_unblock
    temp_user_to_unblock = request.form["unblock_user"].strip()
    return render_template("processing.html")

@app.route("/unblock_result")
def unblock_result():
    global temp_user_to_unblock
    user = temp_user_to_unblock
    if user in blocked_users:
        blocked_users.remove(user)
        message = f"✅ User '{user}' has been unblocked!"
    else:
        message = f"ℹ️ User '{user}' was not blocked."

    return render_template("unblock.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
