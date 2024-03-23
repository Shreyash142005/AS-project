from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

comments = []

# Validate name and comment inputs
def is_valid_input(input_str):
    # Use regex to check for any script tags
    return not re.search(r'<script.*?>.*?</script.*?>', input_str, re.IGNORECASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']

    # Server-side input validation using regular expression
    if not re.match(r'^[a-zA-Z0-9\s]+$', search_term):
        return "Invalid input! Please enter alphanumeric characters only."

    # Process search query
    # Your search functionality goes here
    return f"Search results for: {search_term}"

@app.route('/submitComment', methods=['POST'])
def submit_comment():
    data = request.get_json()
    name = data.get('name')
    comment = data.get('comment')

    # Validate inputs
    if not is_valid_input(name) or not is_valid_input(comment):
        return jsonify({'error': 'Invalid input!'}), 400

    # Store the comment
    comments.append({'name': name, 'comment': comment})

    return jsonify({'name': name, 'comment': comment})

if __name__ == '__main__':
    app.run(debug=True,port=5006)
