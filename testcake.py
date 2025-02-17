import streamlit as st
import pandas as pd
import os
import requests

# LINE Notify Token (Replace with your actual token)
LINE_NOTIFY_TOKEN = "gF2wiELf5fMoOnRdTMud8dJ0xpMrh3mo7oPevPifUVB"

def send_line_notification(message):
    """Send order notification to LINE Notify."""
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_NOTIFY_TOKEN}"}
    data = {"message": message}
    requests.post(url, headers=headers, data=data)

# Streamlit App Title
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

            # Generate Order Summary
            order_summary = f"""
            **💌K.{customer_name}**
            - **Phone Number:** {phone_number}

            **🎂Cake Details**
            - **Cake Base:** {cake_base}
            - **Cake Filling:** {cake_filling}
            - **Cake Size:** {cake_size}
            - **Cake Color:** {cake_color}
            - **Text on Cake:** {cake_text}

            **🕯️Candle**
            - **Candle Type:** {candle_type}

            **🚗Delivery Information**
            - **Delivery Date:** {delivery_date}
            - **Delivery Time:** {delivery_time}
            - **Delivery Location:** {delivery_location}
            """

            # Generate Order Summary for LINE
            order_summaryforLINE = f"""
💌 K.{customer_name} {phone_number}

🎂Cake Details
    - Cake Base: {cake_base}
    - Cake Filling: {cake_filling}
    - Cake Size: {cake_size}
    - Cake Color: {cake_color}
    - Text on Cake: {cake_text}

🕯️Candle
    - Candle Type: {candle_type}

🚗Delivery Information
    - Delivery Date: {delivery_date}
    - Delivery Time: {delivery_time}
    - Delivery Location: {delivery_location}
            """

            # Send order notification to LINE
            send_line_notification(order_summaryforLINE)

            # Show Order Summary Immediately
            st.subheader("📋 Order Summary")
            st.write(order_summary.replace("🎂", ""))  # Remove emoji for Streamlit display

        except Exception as e:
            st.error(f"⚠️ Error saving order: {e}")

# Admin Section (Hidden from customers)
st.divider()
st.subheader("🔒 Admin Access")

admin_password = st.text_input("Enter Admin Password", type="password")

if admin_password == "mysecret123":  # Change this password!
    if st.button("View Orders"):
        try:
            orders_df = pd.read_csv(ORDER_FILE)
            st.write(orders_df)
        except FileNotFoundError:
            st.error("No orders found yet.")
else:
    st.warning("🔐 Enter the admin password to view orders.")




