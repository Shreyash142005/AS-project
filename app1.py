
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

comments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']
    # Process search query without validation (vulnerable to XSS)
    return f"Search results for: {search_term}"

@app.route('/submitComment', methods=['POST'])
def submit_comment():
    data = request.get_json()
    name = data.get('name')
    comment = data.get('comment')

    # Store the comment
    comments.append({'name': name, 'comment': comment})

    return jsonify({'name': name, 'comment': comment})

if __name__ == '__main__':
    app.run(debug=True,port=5006)
