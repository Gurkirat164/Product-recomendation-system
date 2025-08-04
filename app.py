from flask import Flask, render_template, url_for, request, jsonify
import pandas as pd
import os
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

# Load train_data.csv once when the app starts
def load_data():
    if os.path.exists('train_data.csv'):
        return pd.read_csv('train_data.csv')
    return None

train_data_global = load_data()

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


def content_based_recommendations(train_data, item_name, top_n=10):

    # Create a TF-IDF vectorizer for item descriptions
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # Apply TF-IDF vectorization to item descriptions
    tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['tags'])

    # Calculate cosine similarity between items based on descriptions
    cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)

    # Find the index of the item
    item_index = train_data[train_data['product_name'] == item_name].index[0]

    # Get the cosine similarity scores for the item
    similar_items = list(enumerate(cosine_similarities_content[item_index]))

    # Sort similar items by similarity score in descending order
    similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)

    # Get the top N most similar items (excluding the item itself)
    top_similar_items = similar_items[1:top_n+1]

    # Get the indices of the top similar items
    recommended_item_indices = [x[0] for x in top_similar_items]

    # Get the details of the top similar items
    recommended_items_details = train_data.iloc[recommended_item_indices][['product_name', 'discounted_price', 'actual_price', 'discount_percentage', 'img_link', 'rating']]

    return recommended_items_details

@app.route('/api/search-suggestions', methods=['GET'])
def search_suggestions():
    query = request.args.get('q', '').lower()
    if not query or len(query) < 3 or train_data_global is None:
        return jsonify([])
    
    # Search for products that contain the query in their name
    matches = train_data_global[train_data_global['product_name'].str.lower().str.contains(query, regex=False)]
    
    # Get the top 10 matching product names
    suggestions = matches.head(10)['product_name'].tolist()
    
    return jsonify(suggestions)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if not query or train_data_global is None:
        # If no query provided, redirect to products page
        return render_template('products.html', products=[], is_search=True, query='', show_random=False)
    
    # Check if the exact product name exists
    exact_match = train_data_global[train_data_global['product_name'] == query]
    
    if not exact_match.empty:
        # If exact match found, get content-based recommendations
        recommendations = content_based_recommendations(train_data_global, query)
        return render_template('products.html', 
                              products=recommendations.to_dict('records'),
                              is_search=True,
                              query=query,
                              show_random=False)
    else:
        # Try to find similar product names
        similar_products = train_data_global[train_data_global['product_name'].str.lower().str.contains(query.lower(), regex=False)]
        
        if not similar_products.empty:
            # Use the first similar product for recommendations
            first_match = similar_products.iloc[0]['product_name']
            recommendations = content_based_recommendations(train_data_global, first_match)
            return render_template('products.html', 
                                 products=recommendations.to_dict('records'),
                                 is_search=True,
                                 query=query,
                                 show_random=False)
        else:
            # If no similar product found, show random products
            if len(train_data_global) > 20:
                random_products = train_data_global.sample(n=20).to_dict('records')
            else:
                random_products = train_data_global.to_dict('records')
                
            return render_template('products.html', 
                                 products=random_products,
                                 is_search=True,
                                 query=query,
                                 show_random=True)

if __name__ == '__main__':
    # Ensure data is loaded
    if train_data_global is None:
        print("Warning: Could not load train_data.csv. Search functionality may not work correctly.")
    else:
        print(f"Loaded {len(train_data_global)} products from train_data.csv")
    
    app.run(debug=True)