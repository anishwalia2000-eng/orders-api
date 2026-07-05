from models import Customer
from discounts import qualifies_for_free_shipping

def test_premium_customer_with_many_orders():
    # A customer who is premium AND has > 5 orders (e.g., 10 orders)
    # Correct rule: qualifies (True)
    # Buggy code: qualifies (True)
    # This test passes, masking the bug!
    customer = Customer(id="test_1", name="Test Premium", is_premium=True, order_count=10)
    assert qualifies_for_free_shipping(customer) is True

def test_non_premium_customer_with_few_orders():
    # A customer who is NOT premium and has < 5 orders (e.g., 2 orders)
    # Correct rule: does not qualify (False)
    # Buggy code: does not qualify (False)
    # This test also passes!
    customer = Customer(id="test_2", name="Test Regular", is_premium=False, order_count=2)
    assert qualifies_for_free_shipping(customer) is False
