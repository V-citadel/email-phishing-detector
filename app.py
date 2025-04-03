from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import re

app = Flask(__name__)

# Dataset
emails = [
    "Free money!!! Click here to claim your prize",
    "Your invoice is attached. Please review it.",
    "Win a free trip to the Bahamas by clicking this link",
    "Please update your account information",
    "WINNER!! As a valued network customer you have been selected to receive a 900 prize reward! To claim...",
    "Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera f...",
    "England v Macedonia - don't miss the goals/team news. Txt ur national team to 87077 eg ENGLAND to 870...",
    "Thanks for your subscription to Ringtone UK your mobile will be charged 5/month. Please confirm by replying 'YES'.",
    "As a valued Equity customer, you are invited to a special event on financial planning, remember to RSVP.",
    "Urgent: Verify your account details to avoid suspension (KCB). Please respond immediately",
    "Important: Your account will be closed if you do not update your details immediately via the provided link. Yours truly KCB BANK",
    "Limited time offer: Increase your Fuliza limit today. Click on the link below.",
    "Jambo customer, we have changed our banking portal. Please update your details to continue enjoying our services - Yours truly Family Bank.",
    "Congratulations! You have won a free trip to Malindi. To verify, fill in your details in the link below.",
    "Hello Team, attached is the report for last month's performance. Regards, John",
    "Reminder: The team meeting is scheduled for 10 AM tomorrow.",
    "Your order has been shipped and will arrive by the end of the week.",
    "Welcome to our service! We are excited to have you with us."
]
labels = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]

# Preprocess Emails
def preprocess_email(email):
    email = email.lower()
    email = re.sub(r'\W+', ' ', email)  # Remove special characters
    email = re.sub(r'\d+', ' ', email)  # Remove numbers
    email = email.strip()  # Remove extra spaces
    return email

processed_emails = [preprocess_email(email) for email in emails]

# Vectorize Emails
vectorizer = TfidfVectorizer(min_df=2, max_df=0.9, ngram_range=(1, 2))
X = vectorizer.fit_transform(processed_emails)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

# Detect Phishing
def detect_phishing(email_content):
    processed_email = preprocess_email(email_content)
    vectorized_email = vectorizer.transform([processed_email])
    prediction = model.predict(vectorized_email)
    
    # Phishing Indicators
    reasons = []
    if "update your account" in processed_email or "verify your details" in processed_email:
        reasons.append("Request for personal information")
    if "free" in processed_email or "limited time" in processed_email:
        reasons.append("Sense of urgency")
    if "click here" in processed_email or "link below" in processed_email:
        reasons.append("Suspicious links or attachments")
    if "winner" in processed_email or "congratulations" in processed_email:
        reasons.append("Unexpected prize or generic greetings")
    
    if prediction == 1:
        result = "This might be a phishing email."
        details = f"Reasons: {', '.join(reasons) if reasons else 'General phishing characteristics detected.'}"
    else:
        result = "This email is safe."
        details = "No phishing indicators detected."
    
    return result, details

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email_content = request.form['email_content']
        result, details = detect_phishing(email_content)
        return render_template('result.html', result=result, details=details)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
