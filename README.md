# Movie Review Sentiment Analysis and Rating Prediction

## Project Overview

This project focuses on sentiment analysis and rating prediction of movie reviews. Utilizing machine learning and natural language processing techniques, the system analyzes reviews to classify them as positive or negative and predicts numerical ratings. The project also explores review similarity analysis using spaCy.

## Quick Start Guide

To get started with this project, follow the steps below:

1. **Set up a Python Environment**:
   Ensure you have Python 3.8+ installed on your system.

2. **Run the Notebooks**:
   Launch Jupyter Notebook in your environment and open the `.ipynb` files to view the models and visualizations.

3. **Run the Script**:
   Execute `python index.py` to start the sentiment analysis and rating prediction interface.

## Development Environment & Tools

- **Programming Language**: Python
- **Libraries and Frameworks**:
  - `Logistic Regression and Naive Bayes` for sentiment analysis
  - `fasttext` for sentiment analysis
  - `LinearRegression` from `sklearn` for rating prediction
  - `spaCy` for text processing and similarity analysis
  - `TfidfVectorizer` from `sklearn` for feature extraction
  - `pandas`, `numpy`, `matplotlib`, `nltk` for data processing and visualization
- **IDE**: Jupyter Notebook

## Folder Hierarchy
src_folder/
├── .ipynb_checkpoints/ # Jupyter notebook checkpoint files
├── Data_visualization.ipynb # Jupyter notebook for data visualization
├── IMDB_sentimental_model.ipynb # Jupyter notebook for IMDB sentiment analysis
├── logistic&Bayes.ipynb # Jupyter notebook for logistic regression and Naive Bayes models
├── index.py # Python script for sentiment analysis and rating prediction
├── my_senti_model.bin # Trained FastText sentiment analysis model
├── Rating_Cleaned.csv # Cleaned dataset with sentiment labels
├── rating_model.pkl # Trained rating prediction model
├── review_rating_sent.csv # Raw dataset with review texts and ratings
├── review_sent.csv # Raw dataset with review texts for sentiment analysis
├── tfidf_model.pkl # Trained TF-IDF vectorizer model
└── train.txt # Processed training data for FastText model

## Installation Steps

1. Clone the repository.
2. Install required Python packages: `pip install pandas scikit-learn fasttext spacy nltk matplotlib`.
3. Download and install spaCy language model: `python -m spacy download en_core_web_sm`.

## Usage

Run the Python scripts for each specific task:

- FasrText model： `IMDB_sentimental_model.ipynb`
- Logistic regression and naive Bayes model: `logistic&Bayes.ipynb`
- Display interface: `index.py`
- Data_visualization: `Data_visualization.ipynb`

## License

This project uses various tools and libraries, each with their own licenses. Please refer to the respective official documentation for license details.

## Team Member Contributions

- **Team Member Gurnoor**: Focused on initial sentiment analysis using Logistic Regression and Naive Bayes.
- **Team Member Lawrence Qiu**: Worked on sentiment analysis using FastText, rating prediction, and similarity analysis, data visualization.

## References

1. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit*. O'Reilly Media, Inc.
2. Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research, 3*(Jan), 993-1022.
3. Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). Enriching Word Vectors with Subword Information. *Transactions of the Association for Computational Linguistics, 5*, 135-146.
4. FastText. (n.d.). Text classification. Retrieved from https://fasttext.cc/docs/en/supervised-tutorial.html
5. Hutto, C. J., & Gilbert, E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. *Eighth International AAAI Conference on Weblogs and Social Media*.
6. Chodavadiya, N. (2021, March 21). IMDB movie reviews with ratings. *Kaggle*. https://www.kaggle.com/datasets/nisargchodavadiya/imdb-movie-reviews-with-ratings-50k
7. Joulin, A., Grave, E., Bojanowski, P., & Mikolov, T. (2016). Bag of Tricks for Efficient Text Classification. *arXiv preprint arXiv:1607.01759*.
8. Loper, E., & Bird, S. (2002). NLTK: The Natural Language Toolkit. *arXiv preprint cs/0205028*.
9. Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient Estimation of Word Representations in Vector Space. *arXiv preprint arXiv:1301.3781*.
10. Makwana, A. (2022, October 10). Complete Guide to Analyzing Movie Reviews Using NLP. *Analytics Vidhya*. https://www.analyticsvidhya.com/blog/2022/09/complete-guide-to-analyzing-movie-reviews-using-nlp/
11. N, L. (2019, March 9). IMDB dataset of 50K movie reviews. *Kaggle*. https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
12. Ortony, A., & Turner, T. J. (1990). What's basic about basic emotions? *Psychological Review, 97*(3), 315–331. https://doi.org/10.1037/0033-295X.97.3.315
13. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research, 12*(Oct), 2825-2830.
14. SpaCy. (n.d.). Industrial-Strength Natural Language Processing in Python. Retrieved from https://spacy.io/
  
# Acknowledgments

I would like to express my deepest appreciation to my professor, Dr. Russell Campbell, whose invaluable guidance and insightful critiques have been instrumental to the success of this project. His expertise and support throughout this course have not only helped in sharpening my analytical skills but have also encouraged me to explore the field of natural language processing more deeply. Thank you, Dr. Campbell, for your mentorship and for fostering an environment that challenges and inspires your students.


## Demonstration Video

Link to the project demonstration video: https://www.youtube.com/watch?v=aN6St5Tw50Y

*This README was generated as part of the COMP 482 Fall 2023 course project.*
