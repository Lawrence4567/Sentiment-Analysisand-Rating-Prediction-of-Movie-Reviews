Project Title: Sentiment Analysisand Rating Prediction of Movie Reviews

Description

This project utilizes machine learning models to analyze movie reviews, predicting both the sentiment (positive or negative) and a numerical rating. It leverages FastText for sentiment analysis and a linear regression model for rating predictions. The project also includes advanced features like similarity analysis using spaCy and data visualization through word clouds and bar charts.

Contents

logistic&Bayes.ipynb: Initial exploration with Logistic Regression and Naive Bayes models.
FastText_Sentiment_Analysis.ipynb: Advanced sentiment analysis using FastText.
Rating_Prediction.ipynb: Rating prediction using Linear Regression model.
Similarity_Analysis.py: Semantic similarity analysis using spaCy.
WordCloud_Visualization.py: Visualization of frequent words in reviews.
README.md: Project documentation.

Phase 1: Initial Modeling

Logistic Regression and Naive Bayes
logistic&Bayes.ipynb contains the initial experimentation with Logistic Regression and Multinomial Naive Bayes models.
Utilized TF-IDF for text vectorization.
Conducted performance evaluation based on accuracy, precision, recall, and F1 score.

Phase 2: Advancement with FastText and Linear Regression

FastText for Sentiment Analysis
Transitioned to FastText for a more nuanced analysis of sentiments.
FastText model trained on cleaned and preprocessed IMDb reviews.
Linear Regression for Rating Prediction
Developed a Linear Regression model to predict numerical ratings from review text.
Employed TF-IDF vectorization for feature extraction.
spaCy for Similarity Analysis
Implemented spaCy to calculate semantic similarity between different movie reviews.
Data Visualization
Generated word clouds for positive and negative reviews using the WordCloud library.
Visualized the most common words in both positive and negative reviews through bar charts.

Installation and Usage

Ensure Python 3.x is installed.
Install necessary libraries: pip install fasttext spacy sklearn pandas matplotlib nltk
Run Jupyter Notebooks for model training and evaluation.
Execute Python scripts for similarity analysis and visualizations.

Results and Observations

Detail the performance metrics of each model and any interesting observations or insights derived from the analysis.

Acknowledgments
Mention any collaborators, data sources, or references used in the project.
