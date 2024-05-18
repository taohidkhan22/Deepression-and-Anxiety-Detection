# -*- coding: utf-8 -*-
"""svm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H080Wj-gnhZGwv4FgWX7iRUfv5jSzKLt
"""

#svm without punctuation and stop word removal
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_excel('/content/myFinalDataset(edited version).xlsx')

# Remove rows with NaN labels
df = df.dropna(subset=['label'])

# Ensure labels are integers
df['label'] = df['label'].astype(int)

# Extract the texts and labels
texts = df['text'].tolist()
labels = df['label'].tolist()

# Split the dataset into training and test sets
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Vectorize the texts using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

# Train an SVM model
model = SVC(kernel='linear', C=1.0)  # Using a linear kernel
model.fit(X_train, train_labels)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(test_labels, predictions)
print(f'Accuracy: {accuracy:.4f}')
print(classification_report(test_labels, predictions))

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_excel('/content/myFinalDataset(edited version).xlsx')

# Remove rows with NaN labels
df = df.dropna(subset=['label'])

# Ensure labels are integers
df['label'] = df['label'].astype(int)

# Define Bengali stop words
bengali_stop_words = {'আমি', 'তুমি', 'সে', 'আমাদের', 'তোমাদের', 'করে', 'তা', 'কিছু', 'কিছুই', 'এই', 'যে', 'এক',
                      'এটা', 'এ', 'হয়', 'কি', 'ও', 'এবং', 'করতে', 'হয়ে', 'থেকে', 'হয়েছে', 'হয়েছিল', 'থাকে',
                      'থাকা', 'যায়', 'যা', 'নিয়ে', 'না', 'বলে', 'এমন', 'করা', 'জন্য', 'মাধ্যমে', 'কিন্তু', 'আপনি', 'আমার', 'তার', 'এখন',
                      'সঙ্গে', 'তারা', 'করছে', 'এইটা', 'তাদের', 'সেটা', 'সম্পর্কে', 'হতে', 'যেতে', 'সেখান', 'সেটি', 'তারেকে', 'এইচেসে', 'করবেন',
                      'অন্য', 'অন্যান্য', 'বার', 'বা', 'প্রায়', 'আবার', 'আগে', 'এস', 'আগেই', 'যেমন', 'হলে', 'এটি', 'মাত্র', 'কিছুদিন', 'তাহলে',
                      'সেও', 'কেউ', 'মোটামুটি', 'হলো', 'জানা', 'হচ্ছে', 'সব', 'আসে', 'কয়েক', 'বেশি', 'সমস্ত', 'মোটেই', 'যান', 'সহ', 'তিনি',
                      'অথবা', 'যদি', 'দিয়ে', 'আবার', 'পারে', 'কারণ', 'কম', 'হল', 'হলেও', 'কেন', 'বাংলা', 'এখানে', 'কোনো', 'পরে', 'গেল',
                      'সেই', 'দেখা', 'হয়েছে', 'হলেই', 'এসে', 'বিশেষ', 'ওঁরা', 'করি', 'মোট', 'হতেই', 'চেয়ে', 'সম্প্রতি',
}

# Preprocess the text data
def preprocess_text(text):
    # Remove non-Bengali characters and numbers
    text = re.sub(r'[^\u0980-\u09FF\s]', '', text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize the text using space
    tokens = text.split()

    # Remove stop words
    tokens = [word for word in tokens if word not in bengali_stop_words]

    # Join the tokens back into text
    text = ' '.join(tokens)

    return text

df['text'] = df['text'].apply(preprocess_text)

# Extract the texts and labels
texts = df['text'].tolist()
labels = df['label'].tolist()

# Split the dataset into training and test sets
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Vectorize the texts using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

# Train an SVM model
model = SVC(kernel='linear', C=1.0)  # Using a linear kernel
model.fit(X_train, train_labels)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(test_labels, predictions)
print(f'Accuracy: {accuracy:.4f}')
print(classification_report(test_labels, predictions))