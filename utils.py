def validate_loan_data(loan_data: dict):
    required_keys = [
        "principal",
        "annual_rate",
        "term_years",
        "compounding_freq",
        "repayment_freq",
        "inflation_rate"
    ]
    for key in required_keys:
        if key not in loan_data:
            raise ValueError(f"Missing field: {key}")
