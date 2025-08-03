# Naive_Bayes_classifier

# IMDb Sentiment Analysis - Flask + Naive Bayes Classifier
```
This project is a simple web application that uses a **Naive Bayes Classifier** to predict whether a movie review expresses a **positive** or **negative** sentiment. It is built using **Flask**, **Scikit-learn**, and **Pandas**, and is trained on a sample of IMDb-like reviews.
```
---

##  Features
```
- Binary sentiment classification (positive or negative)
- Uses **Multinomial Naive Bayes** with **TF-IDF vectorization**
- Simple and clean web interface using Flask
- Input a custom review and get the prediction instantly
```
---

##  Project Structure
```
Naive_Bayes_classifier/
├── app.py # Flask web app
├── naive_model.py # Trains and saves the Naive Bayes model
├── reviews.csv # Sample dataset (30 labeled reviews)
├── vectorizer.pkl # TF-IDF vectorizer (serialized)
├── naive_model.pkl # Trained Naive Bayes model (serialized)
├── templates/
│ └── index.html # HTML form for input and output
```
---

# Install dependencies:
```
pip install -r requirements.txt
```
# Train the model:
```
python naive_model.py
```
Run the Flask app:
```
python app.py
```


# Example Inputs
```
Review Text	Predicted Sentiment
"This was a beautifully acted and emotionally powerful film."	 Positive
"A complete waste of time. I hated every minute."	 Negative
```
# Dependencies
```
Flask
scikit-learn
pandas
joblib
```
# ScreenShots
![alt text](<Screenshot 2025-08-03 145451.png>)
![alt text](<Screenshot 2025-08-03 145500.png>)
![alt text](<Screenshot 2025-08-03 145510.png>)
