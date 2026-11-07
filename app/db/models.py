
from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from app.db.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, nullable=False)

    books = relationship(
        "Book",
        back_populates="category",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Category(id={self.id}, title='{self.title}')"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    url = Column(String(500), nullable=True)

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )

    category = relationship("Category", back_populates="books")

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', price={self.price})"
