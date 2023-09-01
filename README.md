# flask-authentication


This Flask project demonstrates user authentication using MongoDB as the database. It provides a secure authentication system that allows users to sign up, log in, and access protected routes.

## Project Structure

- `static`: Directory for storing static files (CSS, JavaScript).
- `templates`: Directory for storing HTML templates.
- `app.py`: The main Flask application file.
- `config.py`: Configuration file for storing sensitive information (e.g., MongoDB URI, secret keys).

## Getting Started

### Prerequisites

- Python
- Flask (install via `pip3 install Flask`)
- Flask-PyMongo (install via `pip3 install "pymongo[srv]" `)
- MongoDB (set up and running)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PytechAcademy/flask-authentication.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-authentication
   ```

### Usage

1. Configure MongoDB URI in the `config.py` file:

   ```python
   MONGO_URI = "your url from Atlas"
   ```

2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).
