from flask import Flask, request, jsonify, abort
import json
import os

app = Flask(__name__)

#Ruta del archivo JSON
DATA_FILE = "./data/data.json"

#Cargar datos iniciales
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return[]

#Guardar datos en archivo JSON
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

#Cargar datos iniciales
customers = load_data()


# GET (list) /customers/
@app.route("/customer/", methods=["GET"])
def get_customers():
    return jsonify(customers), 200

# GET /customer/{id}
@app.route("/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = next((c for c in customers if c["id"] == customer_id), None)
    if customer is None:
        abort(404, description="Customer not found")
    return jsonify(customer), 200

# POST /customer/
@app.route("/customer/", methods=["POST"])
def create_customer():
    data = request.json
    if not data or "id" not in data or "first_name" not in data:
        abort(400, description="Invalid input")
    if any(c["id"] == data["id"] for c in customers):
        abort(400, description="Customer ID already exists")
    customers.append(data)
    save_data(customers)
    return jsonify(data), 201

# PUT /customer/{id}
@app.route("/customer/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.json
    customer = next((c for c in customers if c["id"] == customer_id), None)
    if customer is None:
        abort(404, description="Customer not found")
    customer.update(data)
    save_data(customers)
    return jsonify(customer), 200

#DELETE /customer/{id}
@app.route("/customer/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    global customers
    customer = next((c for c in customers if c["id"] == customer_id), None)
    if customer is None:
        abort(404, description="Customer not found")
    customers = [c for c in customers if c["id"] != customer_id]
    save_data(customers)
    return jsonify({"message": "Customer deleted"}), 200

if __name__ ==  "__main__":
    app.run(debug=True)