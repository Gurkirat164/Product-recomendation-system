# Product Recommendation System

A modern web-based product recommendation system built with Flask that provides intelligent product suggestions using content-based filtering and machine learning techniques.

## 🌟 Features

### Core Functionality
- **Content-Based Recommendations**: Advanced product recommendations using TF-IDF vectorization and cosine similarity
- **Real-time Search**: Smart search functionality with autocomplete suggestions
- **Trending Products**: Display of trending and popular items on the homepage
- **Responsive Design**: Modern, mobile-friendly UI with Bootstrap 4
- **Theme Switching**: Dark/Light mode toggle with localStorage persistence

### Technical Features
- **Machine Learning**: Scikit-learn powered recommendation engine
- **Data Processing**: Pandas-based data manipulation and analysis
- **Interactive UI**: Dynamic search suggestions and smooth animations
- **Error Handling**: Robust error handling throughout the application
- **Performance Optimized**: Efficient data loading and caching

## 🛠️ Technology Stack

### Backend
- **Python 3.x**
- **Flask** - Web framework
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **TF-IDF Vectorizer** - Text feature extraction
- **Cosine Similarity** - Recommendation calculations

### Frontend
- **HTML5/CSS3** - Modern responsive design
- **Bootstrap 4** - UI framework
- **JavaScript (ES6+)** - Interactive features
- **jQuery** - DOM manipulation and AJAX

### Data Science Tools
- **Jupyter Notebook** - Data exploration and model development
- **NumPy** - Numerical computations
- **Data Visualization** - Analysis and insights

## 📊 Dataset

**Source**: [Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)

The dataset contains comprehensive product information including:
- Product names and descriptions
- Pricing information (actual price, discounted price, discount percentage)
- Product images and ratings
- Category and tag information
- Sales data and trends

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Gurkirat164/Product-recomendation-system.git
cd Product-recomendation-system
```

### Step 2: Install Dependencies
```bash
pip install flask pandas scikit-learn numpy
```

### Step 3: Prepare Data Files
Ensure these CSV files are in the root directory:
- `train_data.csv` - Main product dataset
- `trending_items.csv` - Trending products data
- `amazon.csv` - Original dataset (optional)

### Step 4: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
Product-recomendation-system/
│
├── app.py                        # Main Flask application
├── system.ipynb                  # Jupyter notebook for data analysis
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── start.py          # Pterodactyl startup script
│
├── Data Files/
│   ├── train_data.csv           # Processed training data
│   ├── trending_items.csv       # Trending products
│   └── amazon.csv              # Original dataset
│
├── templates/
│   ├── index.html              # Homepage template
│   └── products.html           # Products/search results page
│
└── static/
    ├── css/
    │   └── style.css           # Custom styling
    └── js/
        └── script.js           # Frontend JavaScript
```

## 🔍 How It Works

### 1. Content-Based Filtering
The recommendation system uses TF-IDF (Term Frequency-Inverse Document Frequency) to analyze product descriptions and tags:

```python
def content_based_recommendations(train_data, item_name, top_n=10):
    # Create TF-IDF vectorizer for item descriptions
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    
    # Apply TF-IDF vectorization to item descriptions
    tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['tags'])
    
    # Calculate cosine similarity between items
    cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)
    
    # Find and return similar items
    # ... (similarity calculation and ranking)
```

### 2. Search Functionality
- **Exact Match**: Finds products with exact name matches
- **Partial Match**: Uses string containment for similar products
- **Fallback**: Shows random products when no matches found
- **Auto-suggestions**: Real-time search suggestions via AJAX

### 3. Data Flow
1. User enters search query or browses trending products
2. Flask backend processes the request
3. Machine learning algorithm calculates similarities
4. Results are ranked and returned to frontend
5. Dynamic UI updates with recommendations

## 🎨 UI Features

### Design Elements
- **Modern Gradient Backgrounds**: Eye-catching visual design
- **Card-Based Layout**: Clean product presentation
- **Smooth Animations**: Enhanced user experience
- **Responsive Grid**: Works on all device sizes

### Interactive Features
- **Theme Toggle**: Switch between dark and light modes
- **Search Autocomplete**: Real-time search suggestions
- **Hover Effects**: Interactive product cards
- **Loading States**: User feedback during operations

## 📈 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage with trending products |
| `/products` | GET | All products page |
| `/search` | GET | Search results with recommendations |
| `/api/search-suggestions` | GET | JSON API for search autocomplete |

### Example API Usage
```javascript
// Get search suggestions
fetch('/api/search-suggestions?q=laptop')
  .then(response => response.json())
  .then(suggestions => {
    // Display suggestions in UI
  });
```

## 🔧 Configuration

### Environment Variables
The application can be configured through the following variables:
- `DEBUG`: Set to `True` for development mode
- `DATA_PATH`: Custom path for CSV data files

### Data Requirements
Ensure your CSV files contain these columns:
- `product_name`: Product title
- `discounted_price`: Current selling price
- `actual_price`: Original price
- `discount_percentage`: Discount amount
- `rating`: Product rating
- `img_link`: Product image URL
- `tags`: Product description/tags for ML

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Pterodactyl Panel Deployment

This application is fully compatible with Pterodactyl Panel hosting. Follow these steps:

#### Prerequisites
- Pterodactyl Panel with Python 3.11 egg support
- Server with at least 1GB RAM (2GB recommended for ML operations)
- Access to upload files to your Pterodactyl server

#### Step 1: Prepare Your Files
Ensure these files are in your project directory:
- `requirements.txt` - Python dependencies
- `pterodactyl_start.py` - Startup script for Pterodactyl
- `Procfile` - Process file for web server
- `pterodactyl-egg.json` - Custom egg configuration (optional)
- All your CSV data files (`train_data.csv`, `trending_items.csv`)

#### Step 2: Upload to Pterodactyl
1. **Zip your project**: Create a zip file containing all project files
2. **Upload via File Manager**: Use Pterodactyl's file manager to upload and extract
3. **Alternatively**: Use SFTP to transfer files directly

#### Step 3: Configure Server Settings
- **Docker Image**: `ghcr.io/parkervcp/yolks:python_3.11` (recommended) or `ghcr.io/parkervcp/yolks:python_3.13`
- **Startup Command**: `python pterodactyl_start.py` (or `python simple_start.py` for minimal setup)
- **Server Port**: Use the allocated port (usually 25565 for Pterodactyl)

#### Step 4: Environment Variables
Set these environment variables in your Pterodactyl server:
```bash
SERVER_PORT=25565  # Your allocated port
PYTHONUNBUFFERED=1
```

#### Step 5: Installation Process
The startup script will automatically:
1. Install Python dependencies from `requirements.txt`
2. Check for required data files
3. Start the Flask application with Gunicorn

#### Pterodactyl-Specific Files

**requirements.txt** - Python dependencies:
```txt
Flask==2.3.3
pandas==2.1.1
scikit-learn==1.3.0
numpy==1.24.3
Werkzeug==2.3.7
gunicorn==21.2.0
```

**Procfile** - Web server configuration:
```
web: gunicorn app:app --bind 0.0.0.0:$PORT --workers 2
```

**pterodactyl_start.py** - Custom startup script that handles:
- Dependency installation
- File validation
- Server startup with proper port binding

#### Troubleshooting Pterodactyl Deployment

**Common Issues & Solutions:**

1. **Disk Space Issues** (ERROR: [Errno 28] No space left on device):
   - **Solution**: Use minimal requirements: `pip install --no-cache-dir flask pandas scikit-learn numpy`
   - **Alternative**: Use `requirements-minimal.txt` instead of `requirements.txt`
   - **Startup Command**: Try `python simple_start.py` for minimal setup

2. **Python 3.13 Compatibility Issues**:
   - Some packages may not have pre-built wheels for Python 3.13
   - **Solution**: Use Python 3.11 docker image: `ghcr.io/parkervcp/yolks:python_3.11`
   - **Alternative**: Use flexible version ranges in requirements.txt

3. **Memory Issues**: Increase server RAM allocation if you see memory errors during pandas/sklearn operations

4. **Port Binding**: Ensure the application binds to `0.0.0.0` and uses the `SERVER_PORT` environment variable

5. **File Permissions**: Make sure all files have proper read permissions

6. **Data Files**: Verify that `train_data.csv` and `trending_items.csv` are uploaded and accessible

**Quick Fix for Disk Space:**
```bash
# Manual installation if startup fails
pip install --no-cache-dir --user flask pandas scikit-learn numpy
python simple_start.py
```

#### Performance Optimization for Pterodactyl
- Use **2+ workers** in Gunicorn for better performance
- Consider **caching** recommendations for frequently searched items
- **Optimize data loading** by using smaller datasets if needed
- Monitor **memory usage** during ML operations

### Traditional Production Deployment
For production deployment on VPS/dedicated servers:
- Using a WSGI server like Gunicorn
- Setting up a reverse proxy with Nginx
- Configuring environment variables
- Implementing proper logging
- Setting up database connections

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

If you have any questions or run into issues:
- Open an issue on GitHub
- Check the documentation
- Review the code comments for implementation details

## 🔮 Future Enhancements

- **Collaborative Filtering**: User-based recommendations
- **Deep Learning**: Neural network-based recommendations
- **User Accounts**: Personalized recommendations
- **Shopping Cart**: E-commerce functionality
- **Admin Panel**: Content management system
- **Analytics Dashboard**: Usage insights and metrics

---

**Dataset Source**: [Amazon Sales Dataset on Kaggle](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)