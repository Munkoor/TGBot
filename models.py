from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    categories_id = Column(Integer, ForeignKey("categories.id"))
    comments = relationship("Comment")

    def __repr__(self):
        return self.title   


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    books = relationship("Book")

    def __repr__(self):
        return self.name


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    user_chat_id = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id"))

    def __repr__(self):
        return self.text
