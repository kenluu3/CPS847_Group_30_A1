from flask import Flask, jsonify, request, Response, render_template

app = Flask(__name__)

items = {
    "cheese": 12,
    "hamburger": 13,
    "hotdog": 10,
    "fries": 25
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

# Retrieves items
@app.route('/getItems', methods=["GET"])
def get_items():
    return jsonify({"items": items})

# Run app on debug mode if this is main script.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")