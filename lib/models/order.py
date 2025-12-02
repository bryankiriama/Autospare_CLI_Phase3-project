# lib/models/order.py
from datetime import datetime
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    part_id = Column(Integer, ForeignKey("parts.id"))
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    part = relationship("Part", back_populates="orders")

    # Calculate total price
    def calculate_total(self):
        self.total_price = self.quantity * self.part.price

    def __repr__(self):
        return f"<Order(id={self.id}, customer_id={self.customer_id}, part_id={self.part_id}, quantity={self.quantity})>"
