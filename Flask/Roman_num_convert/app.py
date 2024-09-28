from flask import Flask, render_template, request

app = Flask(__name__)

def int_to_roman(num):
    roman_numerals = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    
    roman_result = []
    
    for symbol, value in roman_numerals:
        count = num // value
        roman_result.append(symbol * count)
        num %= value
    
    return ''.join(roman_result)

@app.route("/", methods=["GET", "POST"])
def index():
    roman_numeral = ""
    if request.method == "POST":
        number = request.form.get("number")
        if number.isdigit() and 1 <= int(number) <= 3999:
            roman_numeral = int_to_roman(int(number))
        else:
            roman_numeral = "Ungültige Eingabe! Bitte eine Zahl zwischen 1 und 3999 eingeben."
    
    return render_template("index.html", roman_numeral=roman_numeral)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
