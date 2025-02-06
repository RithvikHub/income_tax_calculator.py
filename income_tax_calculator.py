import streamlit as st

def calculate_income_tax(income):
    # Standard Deduction for salaried individuals
    standard_deduction = 75000
    taxable_income = max(0, income - standard_deduction)  # Ensure taxable income is not negative

    # Initialize tax
    tax = 0

    # Income slabs and rates (FY 2025-26)
    slabs = [
        (400000, 0),
        (800000, 0.05),
        (1200000, 0.10),
        (1600000, 0.15),
        (2000000, 0.20),
        (2400000, 0.25),
        (float('inf'), 0.30)
    ]

    previous_limit = 0
    for limit, rate in slabs:
        if taxable_income > previous_limit:
            taxable_amount = min(taxable_income, limit) - previous_limit
            tax += taxable_amount * rate
            previous_limit = limit
        else:
            break

    # Adding Health & Education Cess (4%)
    cess = tax * 0.04
    total_tax = tax + cess

    return standard_deduction, tax, cess, total_tax


# Streamlit App
st.title("Income Tax Calculator (FY 2025-26)")
st.write("Calculate your income tax under the new tax regime!")

income = st.number_input("Enter your annual income (in ₹):", min_value=0, step=1000)

if income:
    standard_deduction, tax, cess, total_tax = calculate_income_tax(income)
    
    st.write("### Tax Calculation Breakdown:")
    st.write(f"**Standard Deduction:** ₹{standard_deduction:,.2f}")
    st.write(f"**Income Tax (Before Cess):** ₹{tax:,.2f}")
    st.write(f"**Cess (4% on tax):** ₹{cess:,.2f}")
    st.success(f"**Total Tax Payable (Grand Total): ₹{total_tax:,.2f}**")
