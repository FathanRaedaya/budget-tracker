from app import app, db
from app.models import Income, Expense, Goal, db
from app.forms import IncomeForm, ExpenseForm, GoalForm, EditGoalForm
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import func


# Create database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    
    # Add up all the incomes and expenses
    total_income = db.session.query(db.func.sum(Income.amount)).scalar() or 0
    total_expense = db.session.query(db.func.sum(Expense.amount)).scalar() or 0

    # See if there is a goal
    temp_goal = Goal.query.first()

    goal_name = ""
    goal_value = ""
    progress = ""

    # If a goal does exist then assign these variables
    if temp_goal:
        goal_name = temp_goal.name
        goal_value = temp_goal.value
        progress = total_income - total_expense

    return render_template('index.html', total_income=total_income, total_expense=total_expense, goal_name=goal_name,
                           goal_value=goal_value, progress=progress)


@app.route('/income', methods=['GET', 'POST'])
def income():

    # Create the form for income
    form = IncomeForm()

    # Enter if there was an input while validating
    if form.validate_on_submit():
        
        name = form.name.data
        amount = form.amount.data

        # Ensure that there are no duplicates in the database
        dupe_income = Income.query.filter(func.lower(Income.name) == func.lower(name)).first()
        if dupe_income:
            flash('Invalid name (duplicate)', 'danger')
            return redirect(url_for('income'))

        # Add the new input to the database
        new_income = Income(name=name, amount=amount)
        db.session.add(new_income)
        db.session.commit()

        flash('Income added successfully', 'success')
        return redirect(url_for('income'))

    incomes = Income.query.all()
    return render_template('income.html', form=form, incomes=incomes)


@app.route('/income/edit/<int:id>', methods=['POST'])
def edit_income(id):

    # Get the id of the income
    temp_income = Income.query.get_or_404(id)

    # Get the newly editted income
    temp_income.name = request.form['name']
    temp_income.amount = request.form['amount']

    # Update the database with the new inputs
    db.session.commit()

    flash('Income updated successfully', 'success')

    return redirect(url_for('income'))


@app.route('/income/delete/<int:id>', methods=['POST'])
def delete_income(id):

    # Get the id of the income
    temp_income = Income.query.get_or_404(id)

    # Delete the income and update the database
    db.session.delete(temp_income)
    db.session.commit()

    flash('Income removed successfully', 'success')
    return redirect(url_for('income'))

'''
All the other functions below work the same as the incomes'
'''

@app.route('/expense', methods=['GET', 'POST'])
def expense():
    form = ExpenseForm()

    if form.validate_on_submit():
        name = form.name.data
        amount = form.amount.data

        # Ensure that there are no duplicates in the database
        dupe_expense = Expense.query.filter(func.lower(Expense.name) == func.lower(name)).first()
        if dupe_expense:
            flash('Invalid name (duplicate)', 'danger')
            return redirect(url_for('expense'))

        new_expense = Expense(name=name, amount=amount)
        db.session.add(new_expense)
        db.session.commit()

        flash('Expense added successfully', 'success')
        return redirect(url_for('expense'))

    expenses = Expense.query.all()
    return render_template('expense.html', form=form, expenses=expenses)


@app.route('/expense/edit/<int:id>', methods=['POST'])
def edit_expense(id):
    temp_expense = Expense.query.get_or_404(id)

    temp_expense.name = request.form['name']
    temp_expense.amount = request.form['amount']

    db.session.commit()

    flash('Expense updated successfully', 'success')

    return redirect(url_for('expense'))


@app.route('/expense/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    temp_expense = Expense.query.get_or_404(id)
    db.session.delete(temp_expense)
    db.session.commit()

    flash('Expense removed successfully', 'success')
    return redirect(url_for('expense'))


@app.route('/goal', methods=['GET', 'POST'])
def goal():
    form = GoalForm()

    if form.validate_on_submit():
        name = form.name.data
        value = form.value.data

        dupe_goal = Goal.query.first()
        if dupe_goal:
            flash('A goal has already been created', 'warning')
            return redirect(url_for('goal'))

        temp_goal = Goal(name=name, value=value)
        db.session.add(temp_goal)
        db.session.commit()

        flash('Goal created successfully', 'success')
        return redirect(url_for('goal'))

    current_goal = Goal.query.first()

    return render_template('goal.html', form=form, current_goal=current_goal)


@app.route('/goal/edit', methods=['POST'])
def edit_goal():
    form = EditGoalForm()

    if form.validate_on_submit():
        name = form.name.data
        value = form.value.data

        temp_goal = Goal.query.first()

        if temp_goal:

            temp_goal.name = name
            temp_goal.value = value

            db.session.commit()

            flash('Goal updated successfully', 'success')


    return redirect(url_for('goal'))


@app.route('/goal/delete', methods=['POST'])
def delete_goal():
    temp_goal = Goal.query.first()

    if temp_goal:
        db.session.delete(temp_goal)
        db.session.commit()
        flash('Goal deleted successfully', 'success')

    return redirect(url_for('goal'))
