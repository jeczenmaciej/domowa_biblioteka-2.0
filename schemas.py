from marshmallow import Schema, fields

class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    publication_year = fields.Int()
    isbn = fields.Str()
    authors = fields.Nested(AuthorSchema, many=True)

class LoanSchema(Schema):
    id = fields.Int(dump_only=True)
    book_id = fields.Int(required=True)
    borrower_name = fields.Str(required=True)
    loan_date = fields.DateTime(dump_only=True)
    return_date = fields.DateTime()