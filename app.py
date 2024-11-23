from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        employee_id = request.form.get("employeeID")
        part_number = request.form.get("partNumber")
        defect = request.form.get("defect")
        additional_details = request.form.get("additionalDetails")

        # Just for demonstration, no database involved
        print(f"Name: {name}")
        print(f"Employee ID: {employee_id}")
        print(f"Part Number: {part_number}")
        print(f"Defect: {defect}")
        print(f"Additional Details: {additional_details}")

        return "Thanks for your submission. A representative will be in touch soon."

    parts = [
        "10008 - Circuit XS",
        '10009 - 12" Cable',
        "10003 - Camera Lens",
        "14007 - Camera Battery",
    ]
    defects = [
        "Part Malfunctioning",
        "Part Missing Components",
        "Need Specs Re-adjustment",
        "Missing Part",
        "Something else",
    ]
    return render_template("form.html", parts=parts, defects=defects)


if __name__ == "__main__":
    app.run(debug=True)
