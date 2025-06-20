# моделі БД
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from db import Base

class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    target_amount = Column(Float, nullable=False)
    link = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    contributions = relationship("Contribution", back_populates="collection")

class Contribution(Base):
    __tablename__ = "contributors"

    id = Column(Integer, primary_key=True, index=True)
    collection_id = Column(Integer, ForeignKey("collections.id"))
    user_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

    collection = relationship("Collection", back_populates="contributions")
