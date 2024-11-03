from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Define Zodiac signs and their date ranges
ZODIAC_SIGNS = [
    ("Capricorn", (datetime.strptime("12-22", "%m-%d"), datetime.strptime("01-19", "%m-%d"))),
    ("Aquarius", (datetime.strptime("01-20", "%m-%d"), datetime.strptime("02-18", "%m-%d"))),
    ("Pisces", (datetime.strptime("02-19", "%m-%d"), datetime.strptime("03-20", "%m-%d"))),
    ("Aries", (datetime.strptime("03-21", "%m-%d"), datetime.strptime("04-19", "%m-%d"))),
    ("Taurus", (datetime.strptime("04-20", "%m-%d"), datetime.strptime("05-20", "%m-%d"))),
    ("Gemini", (datetime.strptime("05-21", "%m-%d"), datetime.strptime("06-20", "%m-%d"))),
    ("Cancer", (datetime.strptime("06-21", "%m-%d"), datetime.strptime("07-22", "%m-%d"))),
    ("Leo", (datetime.strptime("07-23", "%m-%d"), datetime.strptime("08-22", "%m-%d"))),
    ("Virgo", (datetime.strptime("08-23", "%m-%d"), datetime.strptime("09-22", "%m-%d"))),
    ("Libra", (datetime.strptime("09-23", "%m-%d"), datetime.strptime("10-22", "%m-%d"))),
    ("Scorpio", (datetime.strptime("10-23", "%m-%d"), datetime.strptime("11-21", "%m-%d"))),
    ("Sagittarius", (datetime.strptime("11-22", "%m-%d"), datetime.strptime("12-21", "%m-%d"))),
]

# Define birthstones by month
BIRTHSTONES = {
    1: "Garnet",
    2: "Amethyst",
    3: "Aquamarine",
    4: "Diamond",
    5: "Emerald",
    6: "Pearl",
    7: "Ruby",
    8: "Peridot",
    9: "Sapphire",
    10: "Opal",
    11: "Topaz",
    12: "Turquoise"
}

def get_zodiac_sign(birth_date):
    # Remove year from birth_date for comparison
    birth_date = birth_date.replace(year=1900)
    for sign, (start, end) in ZODIAC_SIGNS:
        start = start.replace(year=1900)
        end = end.replace(year=1900)
        if start <= birth_date <= end:
            return sign
    return "Unknown"

def get_birthstone(birth_date):
    return BIRTHSTONES.get(birth_date.month, "Unknown")

@app.route("/", methods=["GET", "POST"])
def index():
    sign = None
    birthstone = None

    if request.method == "POST":
        try:
            # Get date from form
            date_str = request.form["birth_date"]
            birth_date = datetime.strptime(date_str, "%Y-%m-%d")
            sign = get_zodiac_sign(birth_date)
            birthstone = get_birthstone(birth_date)
        except ValueError:
            sign = "Invalid date format"
            birthstone = "Invalid date format"

    return render_template("index.html", sign=sign, birthstone=birthstone)

if __name__ == "__main__":
    app.run(debug=True)
