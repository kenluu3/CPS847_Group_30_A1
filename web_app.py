from flask import Flask, jsonify, request, Response, render_template

app = Flask(__name__)

items = {
    "cheese": 12,
    "hamburger": 13,
    "hotdog": 10,
    "fries": 25
}

customers = {
    "kingly": 10,
    "danny": 21,
    "ken": 5,
    "nathalie": 21,
    "billy": 21
}

@app.route('/', methods=["GET"])
def hello_world():
    return render_template("index.html")

# URL Format: /add?n1=10&n2=20
@app.route('/add', methods=["GET"])
def add():
    n1 = request.args.get("n1")
    n2 = request.args.get("n2")

    if (n1 == None or n2 == None):
        return Response("Missing parameters: number 1 or number 2", status=400)
    
    result = int(n1) + int(n2)

    return f"The sum of {n1} and {n2} is: {str(result)}."

# URL Format: /mult?n1=10&n2=20
@app.route('/mult', methods=["GET"])
def multiply():
    n1 = request.args.get("n1")
    n2 = request.args.get("n2")

    if (n1 == None or n2 == None):
        return Response("Missing parameters: number 1 or number 2", status=400)
    
    mult = int(n1) * int(n2)
    return f"The multiplication of {n1} and {n2} is: {str(mult)}."

# URL Format: /diff?n1=10&n2=20
@app.route('/diff', methods=["GET"])
def subtract():
    n1 = request.args.get("n1")
    n2 = request.args.get("n2")

    if (n1 == None or n2 == None):
        return Response("Missing parameters: number 1 or number 2", status=400)
    
    diff = int(n1) - int(n2)
    return f"The difference between {n1} and {n2} is: {str(diff)}."

# URL Format: /power?n1=2&n2=3
@app.route('/power', methods=["GET"])
def power():
    n1 = request.args.get("n1")
    n2 = request.args.get("n2")

    if (n1 == None or n2 == None):
        return Response("Missing parameters: number 1", status=400)
    
    power = int(n1) ** int(n2)
    return f"{n1} to the power of {n2} is: {str(power)}."

# Retrieves items
@app.route('/getItems', methods=["GET"])
def get_items():
    return jsonify({"items": items})


# Retrieve the age of customers
@app.route('/getCustomers', methods=["GET"])
def get_customers():
    return jsonify({"customers": customers})

# Retrieve the names of the customers
@app.route('/getCustomerAge', methods=["GET"])
def get_age():
    ages = []
    for c in customers:
        ages.append(customers.get(c))

    return jsonify(ages);

# Run app on debug mode if this is main script.
if __name__ == "__main__":
    app.run(debug=True)