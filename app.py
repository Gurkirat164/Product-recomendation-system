from flask import Flask, render_template, url_for, request
import pandas as pd
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Check if trending_items.csv exists
        if os.path.exists('trending_items.csv'):
            # Read trending items from CSV
            trending_items = pd.read_csv('trending_items.csv')
            # Get top 8 trending items
            top_trending = trending_items.head(8).to_dict('records')
        else:
            # If file doesn't exist, return empty list
            top_trending = []
        return render_template('index.html', trending_items=top_trending)
    except Exception as e:
        # Log the error (in a production app, use a proper logging system)
        print(f"Error: {e}")
        # Return empty list if there's an error
        return render_template('index.html', trending_items=[])

@app.route('/search')
def search():
    query = request.args.get('query', '')
    
    try:
        if os.path.exists('train_data.csv'):
            # Read product data from CSV
            products = pd.read_csv('train_data.csv')
            
            # Filter products based on search query
            # Using case-insensitive partial matching
            results = products[products['product_name'].str.contains(query, case=False, na=False)]
            
            # Convert to list of dictionaries for the template
            search_results = results.head(20).to_dict('records')
        else:
            search_results = []
            
        return render_template('products.html', 
                               products=search_results, 
                               query=query,
                               is_search=True)
    except Exception as e:
        print(f"Search error: {e}")
        return render_template('products.html',
                               products=[], 
                               query=query,
                               is_search=True)

@app.route('/products')
def products():
    try:
        if os.path.exists('train_data.csv'):
            # Read product data from CSV
            products_df = pd.read_csv('train_data.csv')
            
            # Get 50 random products
            if len(products_df) > 50:
                random_products = products_df.sample(n=50).to_dict('records')
            else:
                random_products = products_df.to_dict('records')
                
            return render_template('products.html', 
                                   products=random_products,
                                   is_search=False)
        else:
            return render_template('products.html', 
                                   products=[],
                                   is_search=False)
    except Exception as e:
        print(f"Products page error: {e}")
        return render_template('products.html', 
                               products=[],
                               is_search=False)

if __name__ == '__main__':
    app.run(debug=True)