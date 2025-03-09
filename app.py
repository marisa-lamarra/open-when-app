from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# List of letters (No changes to this part)
letters = {
    "Open Monday": "open_monday.txt",
    "Open ASAP (but not if you feel smushed)": "open_recently.txt",
    "Open when you're doubting us": "doubting_us.txt",
    "Open when you feel like pushing me away": "pushing_away.txt",
    "Open when you need to know how much I appreciate you": "appreciate_you.txt",
    "Open when you feel like you don't deserve good love": "deserve_good_love.txt",
    "Open when you've had a stressful day": "stressful_day.txt",
    "Open when you miss me": "miss_me.txt",
    "Open when you're struggling at work": "struggling_at_work.txt",
    "Open when you need a hug": "need_a_hug.txt",
    "Open when you're overthinking": "overthinking.txt",
    "Open when you're angry with me and I've messed up": "angry_with_me.txt",
    "Open when you can't sleep": "cant_sleep.txt",
    "Open when you need hope for the future": "hope_for_future.txt",
    "Open when you're scared of what could go wrong": "scared_of_wrong.txt",
}

# File to store requests
REQUESTS_HTML_FILE = "requests.txt"  # File where requests will be saved

# Home Page with Letter Buttons (No changes)
@app.route("/")
def home():
    return render_template("index.html", letters=letters)

# Route to Display Letter Content (No changes)
@app.route("/letter/<letter_name>")
def open_letter(letter_name):
    filename = letters.get(letter_name, None)
    if filename:
        try:
            with open(filename, "r") as file:
                content = file.read()
            return render_template("letter.html", letter_name=letter_name, content=content)
        except FileNotFoundError:
            return "Sorry, this letter is missing.", 404
    return "Invalid Letter", 400

# Route to Handle Requests (Save the requests to requests.html)
@app.route("/request", methods=["GET", "POST"])
def make_request():
    if request.method == "POST":
        user_request = request.form.get("user_request")
        if user_request:
            # Add the request to the requests.html file in a readable format
            with open(REQUESTS_HTML_FILE, "a") as file:
                # Write the request inside <p> tags for HTML formatting
                file.write(user_request + "\n")
            return redirect("/")  # Redirect back to home after submission
    return render_template("request.html")

if __name__ == "__main__":
    app.run(debug=True)

