from flask import Flask, request, jsonify, render_template
from frequencies import parse_frequency
from calculator import calculate_loan_payments
app = Flask(__name__)

def validate_loan_input(loan: dict):
    required_keys = [
        "principal", "annual_rate", "term_years",
        "compounding_freq", "repayment_freq", "inflation_rate"
    ]
    for key in required_keys:
        if key not in loan:
            raise ValueError(f"Missing key in loan data: {key}")

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/compare_loans", methods=["POST"])
def compare_loans():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400

        loan1 = data.get("loan1")
        loan2 = data.get("loan2")

        if not loan1 or not loan2:
            return jsonify({"error": "Missing loan1 or loan2 data"}), 400

        validate_loan_input(loan1)
        validate_loan_input(loan2)

        loan1_result = calculate_loan_payments(
            principal=loan1["principal"],
            annual_rate=loan1["annual_rate"],
            term_years=loan1["term_years"],
            compounding_freq=parse_frequency(loan1["compounding_freq"]),
            repayment_freq=parse_frequency(loan1["repayment_freq"]),
            inflation_rate=loan1.get("inflation_rate", 0.0),
        )

        loan2_result = calculate_loan_payments(
            principal=loan2["principal"],
            annual_rate=loan2["annual_rate"],
            term_years=loan2["term_years"],
            compounding_freq=parse_frequency(loan2["compounding_freq"]),
            repayment_freq=parse_frequency(loan2["repayment_freq"]),
            inflation_rate=loan2.get("inflation_rate", 0.0),
        )

        if loan1_result["total_repayment_real"] < loan2_result["total_repayment_real"]:
            better_loan = "loan1"
        elif loan2_result["total_repayment_real"] < loan1_result["total_repayment_real"]:
            better_loan = "loan2"
        else:
            better_loan = "equal"

        return jsonify({
            "loan1": loan1_result,
            "loan2": loan2_result,
            "better_loan": better_loan
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
