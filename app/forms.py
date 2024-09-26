from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DecimalField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange


# Create class forms, initialise variables while validating them

class IncomeForm(FlaskForm):
    name = StringField('Income Name', validators=[DataRequired(), Length(max=30)])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0, max=9999999999999.99)])


class ExpenseForm(FlaskForm):
    name = StringField('Expense Name', validators=[DataRequired(), Length(max=30)])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0, max=9999999999999.99)])


class GoalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    value = DecimalField('Value', validators=[InputRequired(), NumberRange(min=0, max=9999999999999.99)])


class EditGoalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    value = DecimalField('Value', validators=[InputRequired(), NumberRange(min=0, max=9999999999999.99)])
