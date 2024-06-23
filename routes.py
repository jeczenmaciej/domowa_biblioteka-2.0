from flask import Blueprint, jsonify, request
from .models import db, Book, Author, Loan
from .schemas import BookSchema, AuthorSchema, LoanSchema

main = Blueprint('main', __name__)

book_schema = BookSchema()
books_schema = BookSchema(many=True)
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
loan_schema = LoanSchema()

@main.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify(books_schema.dump(books))

@main.route('/books', methods=['POST'])
def add_book():
    data = request.json
    authors_data = data.pop('authors', [])
    new_book = Book(**data)
    
    for author_data in authors_data:
        author = Author.query.filter_by(name=author_data['name']).first()
        if not author:
            author = Author(name=author_data['name'])
        new_book.authors.append(author)
    
    db.session.add(new_book)
    db.session.commit()
    return jsonify(book_schema.dump(new_book)), 201

@main.route('/loans', methods=['POST'])
def add_loan():
    data = request.json
    new_loan = Loan(**data)
    db.session.add(new_loan)
    db.session.commit()
    return jsonify(loan_schema.dump(new_loan)), 201

@main.route('/loans/<int:loan_id>/return', methods=['PUT'])
def return_book(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    loan.return_date = datetime.utcnow()
    db.session.commit()
    return jsonify(loan_schema.dump(loan))

# Dodaj więcej endpointów według potrzeb