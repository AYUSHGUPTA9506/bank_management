Bank Management System
A lightweight, secure, console-based Banking Management application built with Python. The system utilizes Object-Oriented Programming (OOP) principles and acts as a localized transaction layer by storing and modifying persistent data using a JSON database (data.json).

📌 Project Overview
Instead of passing complex parameters repeatedly through deep functions, this system maintains a centralized runtime collection (Bank.data) that automatically serializes and updates state modifications back into a localized file-system storage container.

🛠️ Key Architectural Features & OOP Concepts
1. Encapsulation & Secure State Management
Private Class Methods: The system protects algorithmic generation flows using double-underscore prefixes (__). Method __accountgenerate acts as an isolated background token utility, hidden from external instances.

Controlled Serialization: Database writes are tightly channeled through __update(), preventing unvalidated background components from accidentally corrupting the persistent layer.

2. Algorithmic Configurations
Dynamic Account Generation: Generates a randomized, mixed 7-character identifier string using combined subsets of alphabetic sequences, numeric strings, and safe special characters (!@#$%^&*).

Efficient Query Profiling: Leverages inline List Comprehensions across data lookups to immediately capture user scope matches on unique matching combinations of accountNo. and secure security pin keys.

📂 Data Structure Model (JSON Schema)
User profiles are securely captured, dynamically mapped, and stored into data.json following this structured schema:

JSON
[
  {
    "name": "John Doe",
    "age": 24,
    "email": "johndoe@example.com",
    "pin": 1234,
    "accountNo.": "aB1!xY9",
    "balance": 1500
  }
]
🚀 Execution Guide & System Capabilities
Prerequisites
Make sure you have Python 3.x installed on your system.

Running the Application
Clone this repository or download your source script (main.py).

Open your terminal in the script directory and run:

Bash
python main.py
Application Menu & Flow Control
When launched, the program exposes a transactional prompt interface:

1 Create Account: Performs systemic age validation (restricting signups to ages ≥18) and checks PIN structural lengths (enforcing exactly 4 characters) before appending information arrays.

2 Deposit Money: Authenticates records and processes transactions capped inside a safe range (>0 and ≤10,000).

3 Withdraw Money: Evaluates available funds to prevent negative balances and updates the file system upon successful withdrawal.

4 Show Details: Prints user account statistics to the console.

5 Update Details: Allows modifications to explicit fields (name, email, pin) via custom bypass options while safely preserving immutable properties (age, accountNo., balance).

6 Delete Account: Safely deletes active data array instances from indices following a targeted confirmation constraint.
