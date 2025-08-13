from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    user_message = ""

    if request.method == "POST":
        
        user_message = request.form.get("message", "").strip()

        
        if not user_message:
            user_message = "Please enter a valid message."

    return render_template("index.html", message=user_message)


@app.route("/contact")
def contact():
   
    return render_template("contact.html")


if __name__ == "__main__":
    
    app.run(host="127.0.0.1", port=5000, debug=True)
