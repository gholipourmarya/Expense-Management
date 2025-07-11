# Expense Management

**Expense Management with Python (Tkinter)**  
🧮 Simple tool for managing income and expenses with a graphical user interface

## Description

This Python application allows you to easily record income and expenses and visualize them in various charts. The GUI is built with Tkinter and offers two main sections:

- **New Entry:** Input amount, type (income/expense), category, date, and details.
- **Show Chart:** Select and display different chart types for data visualization.

The program includes input validation (e.g., numeric amounts with up to two decimal places) and stores data in a structured CSV file.

## Features

- Intuitive tabbed GUI for data entry and visualization  
- Input validation for amounts and dates  
- Manage categories and additional details  
- Visualize income and expenses using bar, line, and pie charts  
- Filter data by year for chart display  
- Supports detailed notes for each entry  

## Installation

1. Install Python 3.x: https://www.python.org/downloads/  
2. Install dependencies (e.g., Matplotlib):  
   pip install matplotlib
3. Clone the repository or download the ZIP:
    git clone https://github.com/your-username/expense-management.git
4. Navigate to the project folder and run the program:
    cd expense-management
    python main.py

## Usage
- Launch the program with python main.py.
- Use the New Entry tab to add income or expense entries:
- Enter amount (only numbers, max 2 decimals)
- Select type (Income or Expense)
- Choose a category
- Pick a date (format YYYY-MM-DD)
- Add optional details
- Click Save to store the data.
- Switch to the Show Chart tab to:
- Select the chart type
- Select the year of data to visualize
- Click Show Plot to see your financial overview


## Project Structure
    expense-management/
        ├── Code_Expense Management/
        │   ├── Ausgaben_File.csv            # Data file storing entries
        │   ├── Erstellung_CVF.py            # Data handling and storage
        │   ├── Diagram.py                   # Chart creation and plotting logic
        │   ├── Widiget.py                   # GUI components
        │   └── main.py                     # Main program entry point
        ├── README.md                       # This document
        └── requirements.txt                # (optional) list of dependencies

## Future Enhancements for This Project
    1. Database Support
        Instead of storing data in CSV files, use a database like SQLite or more advanced ones to better manage data, allow faster queries, and prevent concurrent access issues.
    2. Improved User Interface
        -Implement a more modern design using Tkinter themes or migrate to frameworks like PyQt or Kivy.
        -Add advanced search and filtering options in the forms.
        -Display financial summaries on the main page (e.g., total income and expenses per month).
    3. Advanced Reporting
        -Generate PDF or Excel reports from the data.
        -Add interactive charts and a financial dashboard.
        -Enable sending reports via email or sharing online.
    4. Multi-user Support
        Allow creating user accounts so multiple users can manage their expenses separately, with login/logout functionality.
    5. Backup and Restore
        Add automatic backup features and data restoration options.
    6. Multi-currency Support
        Support different currencies and automatic currency conversion for users from different countries.
    7. Reminders
        Add reminders for upcoming payments or expected income.
    8. Mobile or Web Version
        Develop a mobile app (Android/iOS) or a web application for easier access.
    9. Security Enhancements
        If the app goes online, add security measures like data encryption and user authentication.


## Author

    `MaryamGholipour Zilabi`
