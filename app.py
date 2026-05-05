import streamlit as st

# Tiêu đề
st.title("Pricing Calculator")

# Input
price = st.number_input("Nhập giá bán", value=100.0)
cost = st.number_input("Nhập chi phí", value=60.0)
quantity = st.number_input("Nhập số lượng bán", value=10)

# Nút bấm
if st.button("Tính lợi nhuận"):
    profit = (price - cost) * quantity
    st.write("👉 Lợi nhuận:", profit)