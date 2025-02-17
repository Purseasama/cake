import streamlit as st
import pandas as pd
import os

st.title("🎂 Cake Order Form")

# Customer Details
customer_name = st.text_input("Customer Name", placeholder="Enter your full name")
phone_number = st.text_input("Phone Number", max_chars=15, placeholder="Enter your phone number")

# Cake Selection
cake_base = st.selectbox("Select Cake Base:", ["Vanilla", "Chocolate"])
cake_filling = st.selectbox("Select Cake Filling:", ["Strawberry", "Chocolate", "Blueberry", "Caramel"])
cake_size = st.selectbox("Select Cake Size:", ["0.5 lbs", "1 lbs", "1.5 lbs"])

# Cake Color Selection
cake_color_options = ["Pink", "Blue", "White", "Black", "Purple", "Other (Please Specify)"]
cake_color_choice = st.selectbox("Select Cake Color:", cake_color_options)

if cake_color_choice == "Other (Please Specify)":
    custom_cake_color = st.text_input("Enter Your Preferred Color")
    cake_color = custom_cake_color if custom_cake_color else "Not Specified"
else:
    cake_color = cake_color_choice

cake_text = st.text_input("Text on Cake", placeholder="Enter text to be written on the cake")
candle_type = st.radio("Candle Type:", ["Spiral", "Pink","No candle"])

# Other Specifications
add_glitter = st.radio("Add Glitter? (Extra 20 baht)", ["No (+0 baht)", "Yes (+20 baht)"])

# Delivery details
delivery_date = st.date_input("Delivery Date")
delivery_time = st.time_input("Delivery Time")
delivery_location = st.text_input("Delivery Location", placeholder="Enter delivery address")

# File to store orders
ORDER_FILE = "cake_orders.csv"

# Order Placement
if st.button("Place Order"):
    if not customer_name or not phone_number or not delivery_location:
        st.error("⚠️ Please fill in all required fields (Customer Name, Phone Number, and Delivery Location).")
    else:
        order_data = {
            "Customer Name": [customer_name],
            "Phone Number": [phone_number],
            "Cake Base": [cake_base],
            "Cake Filling": [cake_filling],
            "Cake Size": [cake_size],
            "Cake Color": [cake_color],
            "Cake Text": [cake_text],
            "Candle Type": [candle_type],
            "Add Glitter": [add_glitter],
            "Delivery Date": [delivery_date],
            "Delivery Time": [delivery_time],
            "Delivery Location": [delivery_location],
        }

        df = pd.DataFrame(order_data)

        try:
            if os.path.exists(ORDER_FILE):
                df.to_csv(ORDER_FILE, mode="a", index=False, header=False)
            else:
                df.to_csv(ORDER_FILE, mode="w", index=False, header=True)

            st.success("🎉 Order Confirmed! Your details have been saved.")

            # Show Order Summary Immediately
            st.subheader("📋 Order Summary")
            st.write(f"**Customer Name:** {customer_name}")
            st.write(f"**Phone Number:** {phone_number}")
            st.write(f"**Cake Base:** {cake_base}")
            st.write(f"**Cake Filling:** {cake_filling}")
            st.write(f"**Cake Size:** {cake_size}")
            st.write(f"**Cake Color:** {cake_color}")
            st.write(f"**Text on Cake:** {cake_text}")
            st.write(f"**Candle Type:** {candle_type}")
            st.write(f"**Add Glitter:** {add_glitter}")
            st.write(f"**Delivery Date:** {delivery_date}")
            st.write(f"**Delivery Time:** {delivery_time}")
            st.write(f"**Delivery Location:** {delivery_location}")

        except Exception as e:
            st.error(f"⚠️ Error saving order: {e}")

# Admin Section (Hidden from customers)
st.divider()
st.subheader("🔒 Admin Access")

admin_password = st.text_input("Enter Admin Password", type="password")

if admin_password == "PurseAdmin":  # Change this password!
    if st.button("View Orders"):
        try:
            orders_df = pd.read_csv(ORDER_FILE)
            st.write(orders_df)
        except FileNotFoundError:
            st.error("No orders found yet.")
else:
    st.warning("🔐 Enter the admin password to view orders.")



