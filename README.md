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

-1. Supplier Management

As an inventory manager, I want to add new suppliers so that I can track where parts come from.

As an inventory manager, I want to view all suppliers so that I know who provides what.

As an inventory manager, I want to delete a supplier so that I can remove outdated records.

-2. Parts Management

As a store operator, I want to add new parts so that I can update inventory.

As a store operator, I want to view parts and their categories so that I can quickly check availability.

As a store operator, I want to delete parts so that I can clean up inactive items.

-3. Orders Management

As a sales clerk, I want to create orders so that I can record customer purchases.

As a sales clerk, I want to see total prices automatically calculated so that errors are avoided.

As a sales clerk, I want to view all orders so that I can track sales history.