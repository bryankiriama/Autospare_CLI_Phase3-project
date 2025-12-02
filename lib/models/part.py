# lib/models/part.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String)
    stock_quantity = Column(Integer, default=0)
    min_stock = Column(Integer, default=5)
    price = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    # Relationships
    supplier = relationship("Supplier", back_populates="parts")
    orders = relationship("Order", back_populates="part")

    def __repr__(self):
        return f"<Part(id={self.id}, name={self.name}, stock={self.stock_quantity})>"
