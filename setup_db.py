# setup_db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.base import Base
from lib.models import Customer, Supplier, Part, Order

# Create SQLite database (file-based)
DATABASE_URL = "sqlite:///ev_inventory.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

print("Database and tables created successfully!")
