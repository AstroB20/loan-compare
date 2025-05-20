from typing import Dict

def calculate_loan_payments(
    principal: float,
    annual_rate: float,
    term_years: float,
    compounding_freq: int,
    repayment_freq: int,
    inflation_rate: float = 0.0,
) -> Dict:

    n = compounding_freq  
    m = repayment_freq    

    r_c = annual_rate / n              
    N = n * term_years                 
    A = principal * (1 + r_c) ** N    

    effective_annual_rate = (1 + r_c) ** n - 1

    i = (1 + effective_annual_rate) ** (1 / m) - 1

    N_p = int(m * term_years)  

    payment = principal * (i / (1 - (1 + i) ** -N_p))  

    total_repayment = payment * N_p
    total_interest = total_repayment - principal

    discount_rate = inflation_rate / m

    if discount_rate > 0:
        pv_factor = (1 - (1 + discount_rate) ** -N_p) / discount_rate
        total_repayment_real = payment * pv_factor
        payment_per_period_real = total_repayment_real / N_p
    else:
        total_repayment_real = total_repayment
        payment_per_period_real = payment

    return {
        "total_repayment": round(total_repayment, 2),
        "total_interest": round(total_interest, 2),
        "payment_per_period": round(payment, 2),
        "number_of_payments": N_p,
        "total_repayment_real": round(total_repayment_real, 2),
        "payment_per_period_real": round(payment_per_period_real, 2),
    }
