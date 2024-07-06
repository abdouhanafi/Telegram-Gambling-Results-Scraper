from flask import Flask, request, render_template, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Load the data
data = pd.read_csv('telegram_leaked_data.csv')

# Route to serve images if they are stored locally
@app.route('/images/<path:filename>')
def download_file(filename):
    return send_from_directory('images', filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_data(query)
    return render_template('results.html', query=query, results=results.to_dict(orient='records'), result_count=len(results))

def search_data(query):
    # Perform the search
    return data[data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]

if __name__ == '__main__':
    app.run(debug=True)
