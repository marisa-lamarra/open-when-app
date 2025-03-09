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
REQUESTS_FILE = "requests.txt"

# Route to Display the Request Form
@app.route("/request", methods=["GET", "POST"])
def make_request():
    if request.method == "POST":
        # Get the request submitted by the user
        user_request = request.form.get("user_request")
        
        # Check if the user_request is not empty
        if user_request:
            # Make sure the file can be written to (create it if it doesn't exist)
            if not os.path.exists(REQUESTS_FILE):
                with open(REQUESTS_FILE, "w") as file:
                    file.write("")  # Create an empty file if it doesn't exist

            # Append the request to the file
            with open(REQUESTS_FILE, "a") as file:
                file.write(user_request + "\n")  # Save the request in the file
            
            return redirect("/")  # Redirect to the home page after submission

    return render_template("request.html")  # Render the request form

# Home Page Route (Optional - you already have this)
@app.route("/")
def home():
    return render_template("index.html")  # Modify as needed

if __name__ == "__main__":
    app.run(debug=True)
