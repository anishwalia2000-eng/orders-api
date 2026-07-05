def qualifies_for_free_shipping(customer):
    """
    Determines if a customer qualifies for free shipping.

    Business Rule:
    A customer qualifies for free shipping if they are a premium member,
    or they have placed 5 or more orders.
    """
    return customer.is_premium and customer.order_count >= 5
