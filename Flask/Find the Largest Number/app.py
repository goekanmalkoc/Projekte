from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the numbers entered from the form
        try:
            numbers = [int(request.form[f'number{i+1}']) for i in range(5)]
            numbers.sort()
            smallest = numbers[0]
            largest = numbers[-1]
            return render_template("index.html", numbers=numbers, smallest=smallest, largest=largest)
        except ValueError:
            return "Please enter valid numbers."
    return render_template("index.html")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
