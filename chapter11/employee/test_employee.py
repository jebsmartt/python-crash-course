import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee('Bill','Shakespeare',50_000)
    return employee

def test_give_default_raise(employee):
    """Test that an employee can receive the default raise ammount"""
    employee.give_raise()
    assert employee.annual_salary == 55_000

def test_give_custom_raise(employee):
    """Test that an employee can recieve a custom raise ammount"""
    employee.give_raise(30_000)
    assert employee.annual_salary == 80_000
