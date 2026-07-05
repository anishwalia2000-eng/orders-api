from flask import Flask, jsonify, abort
from models import customers_db
from discounts import qualifies_for_free_shipping

app = Flask(__name__)

@app.route("/customers", methods=["GET"])
def get_customers():
    result = []
    for c_id, customer in customers_db.items():
        result.append({
            "id": customer.id,
            "name": customer.name,
            "is_premium": customer.is_premium,
            "order_count": customer.order_count,
            "qualifies_for_free_shipping": qualifies_for_free_shipping(customer)
        })
    return jsonify(result)

@app.route("/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    if customer_id not in customers_db:
        abort(404, description="Customer not found")
    customer = customers_db[customer_id]
    return jsonify({
        "id": customer.id,
        "name": customer.name,
        "is_premium": customer.is_premium,
        "order_count": customer.order_count,
        "qualifies_for_free_shipping": qualifies_for_free_shipping(customer)
    })

@app.route("/customers/<customer_id>/place-order", methods=["POST"])
def place_order(customer_id):
    if customer_id not in customers_db:
        abort(404, description="Customer not found")
    customer = customers_db[customer_id]
    customer.order_count += 1
    return jsonify({
        "id": customer.id,
        "name": customer.name,
        "is_premium": customer.is_premium,
        "order_count": customer.order_count,
        "qualifies_for_free_shipping": qualifies_for_free_shipping(customer)
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
