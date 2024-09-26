from app import db


# Create classes of each category, create each column in the database
class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.Float, nullable=False)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.Float, nullable=False)


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    value = db.Column(db.Float)

    def __repr__(self):
        return f'<Goal {self.name} >'


# Initialise and create the database
def init_db():
    db.create_all()


if __name__ == '__main__':
    init_db()
