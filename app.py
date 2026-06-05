import streamlit as st
import json
import random
import string
from pathlib import Path


# --------- SAME LOGIC CLASS (UI-FRIENDLY) ---------
class Bank:
    database = 'data.json'
    data = []

    @classmethod
    def load(cls):
        if Path(cls.database).exists():
            with open(cls.database) as f:
                try:
                    cls.data = json.load(f)
                except:
                    cls.data = []
        else:
            cls.data = []

    @classmethod
    def update(cls):
        with open(cls.database, 'w') as f:
            json.dump(cls.data, f, indent=4)

    @classmethod
    def account_generate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)


# Load data
Bank.load()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox("Menu", [
    "Create Account",
    "Deposit",
    "Withdraw",
    "View Details",
    "Update Details",
    "Delete Account"
])

# -------- CREATE ACCOUNT --------
if menu == "Create Account":
    st.subheader("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        if age < 18 or len(pin) != 4:
            st.error("Invalid age or PIN")
        else:
            account = {
                "name": name,
                "age": age,
                "email": email,
                "pin": int(pin),
                "accountNo.": Bank.account_generate(),
                "balance": 0
            }
            Bank.data.append(account)
            Bank.update()

            st.success("Account Created!")
            st.write("Account Number:", account["accountNo."])


# -------- DEPOSIT --------
elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        try:
            user = [i for i in Bank.data if i.get("accountNo.") == acc and i.get("pin") == int(pin)]

            if not user:
                st.error("User not found")
            elif amount > 10000:
                st.error("Amount should be below 10000")
            else:
                user[0]["balance"] += amount
                Bank.update()
                st.success("Amount Deposited Successfully")
        except:
            st.error("Invalid input")


# -------- WITHDRAW --------
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        try:
            user = [i for i in Bank.data if i.get("accountNo.") == acc and i.get("pin") == int(pin)]

            if not user:
                st.error("User not found")
            elif user[0]["balance"] < amount:
                st.error("Insufficient balance")
            else:
                user[0]["balance"] -= amount
                Bank.update()
                st.success("Amount Withdrawn Successfully")
        except:
            st.error("Invalid input")


# -------- VIEW DETAILS --------
elif menu == "View Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        try:
            user = [i for i in Bank.data if i.get("accountNo.") == acc and i.get("pin") == int(pin)]

            if not user:
                st.error("User not found")
            else:
                st.json(user[0])
        except:
            st.error("Invalid input")


# -------- UPDATE DETAILS --------
elif menu == "Update Details":
    st.subheader("Update Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        try:
            user = [i for i in Bank.data if i.get("accountNo.") == acc and i.get("pin") == int(pin)]

            if not user:
                st.error("User not found")
            else:
                if name:
                    user[0]["name"] = name
                if email:
                    user[0]["email"] = email
                if new_pin:
                    if len(new_pin) != 4:
                        st.error("PIN must be 4 digits")
                        st.stop()
                    user[0]["pin"] = int(new_pin)

                Bank.update()
                st.success("Details Updated")
        except:
            st.error("Invalid input")


# -------- DELETE ACCOUNT --------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        try:
            user = [i for i in Bank.data if i.get("accountNo.") == acc and i.get("pin") == int(pin)]

            if not user:
                st.error("User not found")
            else:
                Bank.data.remove(user[0])
                Bank.update()
                st.success("Account Deleted")
        except:
            st.error("Invalid input")