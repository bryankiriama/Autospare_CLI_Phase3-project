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