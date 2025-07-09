from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration
usernames = []

# Route to insert a username
@app.route('/add-username', methods=['POST'])
def add_username():
    try:
        # Get JSON data from the request
        data = request.get_json()
        username = data.get('username')

        # Validate input
        if not username:
            return jsonify({"error": "Username is required"}), 400

        # Add username to the list
        usernames.append(username)
        return jsonify({"message": "Username added successfully", "usernames": usernames}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
