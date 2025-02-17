from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        data = request.json
        if not data:
            return Response("Failed: No data provided", status=400)

        # print(f"Creating item: {data}")
        return Response("Request successful", status=200)

    return Response("Create endpoint is ready", status=200)


@app.route('/read/<int:item_id>', methods=['GET'])
def read(item_id):
    # print(f"Fetching item with ID: {item_id}")
    return Response("Request successful", status=200)


@app.route('/update/<int:item_id>', methods=['PUT', 'GET'])
def update(item_id):
    if request.method == 'PUT':
        data = request.json
        if not data:
            return Response("Failed: No data provided", status=400)

        # print(f"Updating item {item_id} with data: {data}")
        return Response("Request successful", status=200)

    return Response(f"Update endpoint for item {item_id} is ready", status=200)


@app.route('/delete/<int:item_id>', methods=['DELETE', 'GET'])
def delete(item_id):
    if request.method == 'DELETE':
        # print(f"Deleting item with ID: {item_id}")
        return Response("Request successful", status=200)

    return Response(f"Delete endpoint for item {item_id} is ready", status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

