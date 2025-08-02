from flask import Flask, render_template, url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Check if trending_items.csv exists
        if os.path.exists('trending_items.csv'):
            # Read trending items from CSV
            trending_items = pd.read_csv('trending_items.csv')
            # Get top 8 trending items
            top_trending = trending_items.to_dict('records')
        else:
            # If file doesn't exist, return empty list
            top_trending = []
        return render_template('index.html', trending_items=top_trending)
    except Exception as e:
        # Log the error (in a production app, use a proper logging system)
        print(f"Error: {e}")
        # Return empty list if there's an error
        return render_template('index.html', trending_items=[])

if __name__ == '__main__':
    app.run(debug=True)