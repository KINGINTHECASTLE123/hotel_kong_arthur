import streamlit as st
import requests
import os

API_GATEWAY_URL = os.getenv('API_GATEWAY_URL', 'http://api_gateway:5500')  # Gateway modtager ALLE requests

st.set_page_config(page_title="Hotel Kong Arthur Dashboard", layout="wide")

st.title("🏨 Hotel Kong Arthur - Administrationsdashboard")


# ----------------- HENT DATA FUNKTION -----------------
def fetch_data(endpoint):
    try:
        response = requests.get(f"{API_GATEWAY_URL}{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Fejl {response.status_code}: {response.text}")
            return []
    except Exception as e:
        st.error(f"Kan ikke forbinde til API Gateway: {e}")
        return []


# ----------------- VIEW MENUER -----------------
menu = st.sidebar.selectbox(
    "Naviger",
    [
        "Gæster",
        "Værelser",
        "Bookinger",
        "Drinks & Bar Salg"
    ]
)

# ----------------- GÆSTER -----------------
if menu == "Gæster":
    st.header("👤 Gæsteliste")

    guests = fetch_data("/api/guests")
    st.write(f"Total gæster: **{len(guests)}**")

    st.dataframe(guests)

# ----------------- VÆRELSER -----------------
elif menu == "Værelser":
    st.header("🛏️ Værelsesoversigt")

    rooms = fetch_data("/api/rooms")
    st.dataframe(rooms)

# ----------------- BOOKINGER -----------------
elif menu == "Bookinger":
    st.header("📅 Bookingoversigt")

    bookings = fetch_data("/api/bookings")
    st.write(f"Antal bookinger: **{len(bookings)}**")
    st.dataframe(bookings)

# ----------------- DRINKSALES -----------------
elif menu == "Drinks & Bar Salg":
    st.header("🍹 Drinks & Bar Salg Statistik")

    drinks = fetch_data("/api/drinks")
    st.write(f"Antal drikkevarer registreret: **{len(drinks)}**")
    st.dataframe(drinks)

    # Simpel omsætning
    try:
        total_revenue = sum(item["price"] * item["units_sold"] for item in drinks)
        st.subheader(f"💰 Total bar omsætning: **{total_revenue} DKK**")
    except:
        pass
