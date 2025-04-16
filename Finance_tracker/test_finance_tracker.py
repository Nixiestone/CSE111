import pytest
from Finance_tracker.finance_tracker import *

# Fixture for test data
@pytest.fixture
def sample_transactions():
    return [
        Transaction(1000, "salary", "2023-01-01", "income"),
        Transaction(500, "rent", "2023-01-01", "expense"),
        Transaction(200, "food", "2023-01-05", "expense")
    ]

def test_load_transactions():
    test_data = load_transactions('test_data.csv')
    assert len(test_data) == 3
    assert isinstance(test_data[0], Transaction)
    assert test_data[1].category == "rent"

def test_categorize_spending(sample_transactions):
    categories = categorize_spending(sample_transactions)
    assert "rent" in categories
    assert "food" in categories
    assert len(categories["food"]) == 1

def test_calculate_budget(sample_transactions):
    income = [t for t in sample_transactions if t.type == 'income']
    expenses = [t for t in sample_transactions if t.type == 'expense']
    assert calculate_budget(income, expenses) == 300

def test_progress_toward_goal():
    assert progress_toward_goal(750, 1000) == 75
    assert progress_toward_goal(0, 500) == 0
    assert progress_toward_goal(100, 0) == 0

def test_report_generation(sample_transactions):
    report = generate_report(sample_transactions)
    assert report['total_income'] == 1000
    assert report['total_expenses'] == 700
    assert report['net_savings'] == 300

def test_save_goals(tmp_path):
    test_goals = {"vacation": 5000}
    save_goals(test_goals)
    with open('financial_goals.txt') as f:
        content = f.read()
    assert "vacation:5000" in content