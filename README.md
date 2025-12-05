# Autospare_CLI_Phase3-project

## Description

The Autospare CLI is a command-line application designed to manage an electric vehicle (EV) spare parts inventory system. It allows users to perform full CRUD operations on suppliers, parts, and orders while interacting with an SQLite database through the SQLAlchemy ORM.
This project demonstrates best practices in CLI design, Python OOP, environment management with Pipenv, and relational database modeling.
## Author

Bryan Kiriama

## Setup Instructions

1. Clone the Repository

Start by cloning the project from GitHub:

git clone https://github.com/bryankiriama/Autospare_CLI_Phase3-project
cd Autospare_CLI_Phase3-project

2. Install Dependencies with Pipenv

Make sure you have Pipenv installed:

pip install pipenv


Now install the project dependencies:

pipenv install


Activate the virtual environment:

pipenv shell

3. Set Up the Database

The project uses SQLite.
To initialize and view the database:

sqlite3 ev_inventory.db


Inside the SQLite terminal:

.tables


If tables already exist, you are ready to go.
If not, you can run the model initialization script (if included) or allow SQLAlchemy to create tables on first run.

4. Run the CLI Application

Once dependencies are installed and the environment is active, run the CLI:

python lib/cli.py

## BDD (Behavior Driven Development)

Scenario: Add a new supplier
Given the user is in the Supplier Management menu
When the user enters a supplier name, contact, and address
Then a new supplier record should be created in the database
And the system should display "Supplier added successfully"

Scenario: View all suppliers
Given suppliers exist in the database
When the user selects "View Suppliers"
Then the system should display a list of all suppliers with their IDs, names, and contacts

Scenario: Delete a supplier
Given a supplier record exists
When the user enters the supplier ID to delete
Then the system should remove the supplier from the database
And the system should display "Supplier deleted successfully"

Feature: Parts Management
Scenario: Add a new part
Given the user is in the Parts Management menu
When the user enters the part name, category, price, supplier ID, stock quantity, and minimum stock
Then a new part record should be saved in the database
And the system should show "Part added successfully"

Scenario: View all parts
Given parts exist in the inventory
When the user selects "View Parts"
Then the system should display all parts with their names, categories, prices, stock quantities, and supplier IDs

Scenario: Delete a part
Given a part record exists
When the user enters the part ID to delete
Then the part should be removed from the database
And the system should display "Part deleted successfully"
