def calculate_monthly_payment(principal, interest_rate, loan_term):
    if interest_rate == 0:
        return principal / loan_term
    return principal * (interest_rate * (1 + interest_rate) ** loan_term) / ((1 + interest_rate) ** loan_term - 1)

def remaining_balance(principal, interest_rate, loan_term, t):
    if interest_rate == 0:
        return principal - (principal / loan_term) * t
    return principal * ((1 + interest_rate) ** loan_term - (1 + interest_rate) ** t) / ((1 + interest_rate) ** loan_term - 1)

def total_cost(t, down_payment, buying_expenses, monthly_payment):
    return down_payment + buying_expenses + monthly_payment * t

def selling_price(t, total_price, hpi_growth_rate):
    return total_price * (1 + hpi_growth_rate) ** (t / 12)

def net_proceeds(t, principal, interest_rate, loan_term, selling_expenses_rate, total_price, hpi_growth_rate):
    selling_price_t = selling_price(t, total_price, hpi_growth_rate)
    selling_expenses = selling_price_t * selling_expenses_rate
    remaining_balance_t = remaining_balance(principal, interest_rate, loan_term, t)
    return selling_price_t - selling_expenses - remaining_balance_t

# def find_break_even_months():
#     t = 0
#     while True:
#         net = net_proceeds(t, principal, interest_rate, loan_term, selling_expenses_rate, total_price, hpi_growth_rate)
#         if net >= total_cost(t):
#             return t
#         t += 1