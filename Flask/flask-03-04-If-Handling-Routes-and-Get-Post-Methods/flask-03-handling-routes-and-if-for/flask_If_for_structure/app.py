from flask import Flask, render_template, request
app = Flask(__name__)

# Route for the index page with a message form
@app.route("/", methods=["GET", "POST"])
def head():
    if request.method == "POST":
        first = request.form.get("message")
        if first:  # Check if the message is provided
            return render_template("index.html", message=first)
        else:
            error = "Please enter a message!"
            return render_template("index.html", error=error)
    else:
        return render_template("index.html")

# Route for the list page
@app.route("/list")
def header():
    numbers = range(1, 11)
    return render_template("body.html", object=numbers)

# Run the app
if __name__== "__main__":
    # app.run(debug=True, port=3000)

    app.run(host='0.0.0.0', port=80)

