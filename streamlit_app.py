import streamlit as st
import numpy as np
import pandas as pd

import functions as fc

# Constants
PROPERTY_PRICE        = 5350000  # DKK
BUYING_EXPENSES       = 4000 + 55000 + 1825 + 7000 + 7576 + 20569 + 10000  + 30350 + 1750# DKK
TOTAL_PRICE           = PROPERTY_PRICE + BUYING_EXPENSES  # DKK
DOWN_PAYMENT          = TOTAL_PRICE * 0.2 # DKK
PRINCIPAL             = PROPERTY_PRICE - DOWN_PAYMENT  # DKK
INTEREST_RATE         = 0.0506 * 0.67 / 12  # Monthly interest rate
LOAN_TERM             = 30 * 12  # 30 years in months
SELLING_EXPENSES_RATE = 0.02  # 2% of selling price
T_MONTHS              = 5*12 # Time in months before selling
INFLATION_RATE = 0.02  # 2% annual inflation rate

months = np.arange(0, LOAN_TERM + 1) # Time in months
hpi_growth_rate = 0.02 # 2% annual growth rate

# Calculate monthly payment
monthly_payment = fc.calculate_monthly_payment(PRINCIPAL, INTEREST_RATE, LOAN_TERM)

# Remaining balance after t months
remaining_balance_example = fc.remaining_balance(PRINCIPAL, INTEREST_RATE, LOAN_TERM, T_MONTHS)

# Total cost after t months
total_cost_T_MONTHS = fc.total_cost(T_MONTHS, DOWN_PAYMENT, BUYING_EXPENSES, monthly_payment)

# Selling price after t months
selling_price_value = fc.selling_price(T_MONTHS, TOTAL_PRICE, hpi_growth_rate)

# Net proceeds after t months
net_proceeds_value = fc.net_proceeds(T_MONTHS, PRINCIPAL, INTEREST_RATE, LOAN_TERM, SELLING_EXPENSES_RATE, TOTAL_PRICE, hpi_growth_rate)

# Break-even time
# break_even_months = fc.find_break_even_months()

# Create a DataFrame
data = {
    'Time (months)': months,
    'Total cost (DKK)': fc.total_cost(months, DOWN_PAYMENT, BUYING_EXPENSES, monthly_payment),
    'Remaining balance (DKK)': fc.remaining_balance(PRINCIPAL, INTEREST_RATE, LOAN_TERM, months),
    'Net proceeds (DKK)': fc.net_proceeds(months, PRINCIPAL, INTEREST_RATE, LOAN_TERM, SELLING_EXPENSES_RATE, TOTAL_PRICE, hpi_growth_rate)
}

df = pd.DataFrame(data)

# Streamlit
st.title('Mortgage Calculator')

st.write('## Data')
st.write(df)

# Plot
st.write('## Plot')
st.line_chart(df.set_index('Time (months)'))


