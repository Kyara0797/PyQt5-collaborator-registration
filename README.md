# PyQt5 Collaborator Registration App

This is a desktop application built with Python and PyQt5 that allows you to register collaborators, calculate their net salary, display the information in a table, and export it to Excel.

## 📌 Features

- Input fields for:
  - Name
  - Last Name
  - Profession
  - Salary
- Calculates **net salary** based on the following rules:
  - Salary ≤ 1000: 20% deduction
  - 1000 < Salary ≤ 4000: 25% deduction
  - Salary > 4000: 35% deduction
- Displays all collaborators in a table
- Exports all data to `data_collaborators.xlsx`

## 🖥️ GUI Preview

The app uses a simple, clean PyQt5 interface with:
- A title label
- A horizontal input form
- Two buttons: "Add Collaborator" and "Export Excel"
- A table with 5 columns

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kyara0797/PyQt5-collaborator-registration.git
   cd PyQt5-collaborator-registration
2. **Create a virtual environment (optional but recommended)**:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. **Install dependencies**:
   pip install -r requirements.txt

4. **Run the app**:
python collaborator_form.py
