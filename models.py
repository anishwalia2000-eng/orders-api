from dataclasses import dataclass

@dataclass
class Customer:
    id: str
    name: str
    is_premium: bool
    order_count: int

# In-memory customer "database" seeded with sample records
customers_db = {
    "1": Customer(id="1", name="Alice Smith (Premium, 10 orders)", is_premium=True, order_count=10),
    "2": Customer(id="2", name="Bob Jones (Non-Premium, 20 orders)", is_premium=False, order_count=20),
    "3": Customer(id="3", name="Charlie Brown (Premium, 5 orders)", is_premium=True, order_count=5),
    "4": Customer(id="4", name="Diana Prince (Non-Premium, 2 orders)", is_premium=False, order_count=2),
}
