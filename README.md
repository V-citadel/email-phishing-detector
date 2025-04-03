# email-phishing-detector
# Phishing Email Detector

## Overview
The **Phishing Email Detector** is a Flask-based web application that identifies phishing emails using **Natural Language Processing (NLP)** and **Machine Learning**. The model analyzes email content and provides reasons why an email is classified as phishing or safe.

## Features
- Detects phishing emails using a **Logistic Regression** model.
- Uses **TF-IDF Vectorization** for text processing.
- Identifies key phishing indicators such as **urgent language**, **suspicious links**, and **requests for personal information**.
- Provides a web interface for users to input email content and receive phishing detection results.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phishing-email-detector.git
   cd phishing-email-detector
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open the app in your browser:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Enter email content in the provided text box.
2. Click the **Detect** button.
3. View the result indicating whether the email is phishing or safe, along with reasons.

## Project Structure
```
phishing-email-detector/
│── templates/
│   ├── home.html
│   ├── result.html
│── static/
│── app.py
│── requirements.txt
│── README.md
```

## Technologies Used
- **Python** (Flask, Scikit-learn, SpaCy, Pandas, NumPy, Regex)
- **Machine Learning** (Logistic Regression, TF-IDF Vectorizer)
- **NLP** (Text Preprocessing, Tokenization, Lemmatization)
- **Flask** (Web framework for UI handling)

## Future Improvements
- Integrate with an email API for real-time email scanning.
- Improve model accuracy with a larger dataset.
- Implement a database for storing user submissions and analysis history.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.


