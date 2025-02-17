# -*- coding: utf-8 -*-
"""Testcake.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lV4BBksPFeeOZAhcr0uDvProS6PH2LGO
"""



import streamlit as st

# Title of the app
st.title("Cake Order Form")

# Cake Base Selection
cake_base = st.selectbox("Select Cake Base", ["Vanilla", "Chocolate"])

# Cake Filling Selection
cake_filling = st.selectbox("Select Cake Filling", ["Strawberry", "Chocolate", "Blueberry", "Caramel"])

# Cake Size Selection
cake_size = st.selectbox("Select Cake Size", ["0.5 lbs", "1 lbs", "1.5 lbs"])

# Delivery Date & Time
delivery_date = st.date_input("Select Delivery Date")
delivery_time = st.time_input("Select Delivery Time")

# Delivery Location
delivery_location = st.text_input("Enter Delivery Location")

# Telephone Number
phone_number = st.text_input("Enter Your Telephone Number")

# Submit Button
if st.button("Place Order"):
    st.success(f"Order Confirmed! 🎉\n\nCake: {cake_base} with {cake_filling} filling.\nSize: {cake_size}\nDelivery: {delivery_date} at {delivery_time}\nLocation: {delivery_location}\nPhone: {phone_number}")