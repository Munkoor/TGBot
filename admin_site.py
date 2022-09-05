from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = "SECRET KEY"

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    categories_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    comments = db.relationship("Comment")

    def __repr__(self):
        return self.title   



class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    books = db.relationship("Book")

    def __repr__(self):
        return self.name


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, index=True)
    text = db.Column(db.Text)
    user_chat_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    def __repr__(self):
        return self.text


admin = Admin(app, name='Сайт керування Книжками', template_mode='bootstrap3')

admin.add_view(ModelView(Book, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Comment, db.session))


if __name__ == '__main__':
    app.run()
