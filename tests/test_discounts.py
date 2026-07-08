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

def test_premium_customer_with_one_order():
    # A customer who IS premium but has only 1 order
    # Correct rule: qualifies (True) - premium status alone qualifies
    # Buggy code: does not qualify (False) - would require BOTH conditions
    # BUG CATCH: This test would fail with the buggy code!
    customer = Customer(id="test_3", name="Test Premium Few Orders", is_premium=True, order_count=1)
    assert qualifies_for_free_shipping(customer) is True

def test_non_premium_customer_with_exactly_five_orders():
    # A customer who is NOT premium but has exactly 5 orders
    # Correct rule: qualifies (True) - 5 or more orders qualifies
    # Buggy code: does not qualify (False) - would require BOTH conditions
    # BUG CATCH: This test would fail with the buggy code!
    customer = Customer(id="test_4", name="Test Regular Five Orders", is_premium=False, order_count=5)
    assert qualifies_for_free_shipping(customer) is True

def test_non_premium_customer_with_many_orders():
    # A customer who is NOT premium but has 20+ orders
    # Correct rule: qualifies (True) - 5 or more orders qualifies
    # Buggy code: does not qualify (False) - would require BOTH conditions
    # BUG CATCH: This test would fail with the buggy code!
    customer = Customer(id="test_5", name="Test Regular Many Orders", is_premium=False, order_count=20)
    assert qualifies_for_free_shipping(customer) is True

def test_premium_customer_with_zero_orders():
    # A customer who IS premium with zero orders
    # Correct rule: qualifies (True) - premium status alone qualifies
    # Buggy code: does not qualify (False) - would require BOTH conditions
    customer = Customer(id="test_6", name="Test Premium No Orders", is_premium=True, order_count=0)
    assert qualifies_for_free_shipping(customer) is True
