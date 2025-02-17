import streamlit as st
import pandas as pd

# Set the title of the app
st.title("🎂 Cake Order Form")

# Customer Details
customer_name = st.text_input("Customer Name")
phone_number = st.text_input("Phone Number", max_chars=15)

# Cake Selection
cake_base = st.selectbox("Select Cake Base:", ["Vanilla", "Chocolate"])
cake_filling = st.selectbox("Select Cake Filling:", ["Strawberry", "Chocolate", "Blueberry", "Caramel"])
cake_size = st.selectbox("Select Cake Size:", ["0.5 lbs", "1 lbs", "1.5 lbs"])
cake_color = st.color_picker("Pick a Cake Color")
cake_text = st.text_input("Text on Cake")
candle_type = st.radio("Candle Type:", ["Spiral", "Pink"])

# Other Specifications
add_glitter = st.radio("Add Glitter? (Extra 20 baht)", ["No (+0 baht)", "Yes (+20 baht)"])

# Delivery details
delivery_date = st.date_input("Delivery Date")
delivery_time = st.time_input("Delivery Time")
delivery_location = st.text_input("Delivery Location")

# Submit Button
if st.button("Place Order"):
    # Save order to CSV
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
    df.to_csv("cake_orders.csv", mode="a", index=False, header=False)  # Append data
    
    st.success("🎉 Order Confirmed! Your details have been saved.")

# Button to View Orders
if st.button("View Orders"):
    try:
        orders_df = pd.read_csv("cake_orders.csv")
        st.write(orders_df)
    except FileNotFoundError:
        st.error("No orders found yet.")
