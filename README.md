# Movie Review Sentiment Analysis and Rating Prediction

## Project Overview

This project focuses on sentiment analysis and rating prediction of movie reviews. Utilizing machine learning and natural language processing techniques, the system analyzes reviews to classify them as positive or negative and predicts numerical ratings. The project also explores review similarity analysis using spaCy.

## Development Environment & Tools

- **Programming Language**: Python
- **Libraries and Frameworks**: 
  - `fasttext` for sentiment analysis
  - `LinearRegression` from `sklearn` for rating prediction
  - `spaCy` for text processing and similarity analysis
  - `TfidfVectorizer` from `sklearn` for feature extraction
  - `pandas`, `numpy`, `matplotlib`, `nltk` for data processing and visualization
- **IDE**: Jupyter Notebook

## Folder Hierarchy


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

- IMDB Movie Review Dataset: [Kaggle](https://www.kaggle.com/datasets/nisargchodavadiya/imdb-movie-reviews-with-ratings-50k)
- N, L. (2019, March 9). IMDB dataset of 50K movie reviews. Kaggle. https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- spaCy: [Official Documentation](https://spacy.io/api/span)
- FastText: [Official Repository](https://github.com/facebookresearch/fastText)
-  A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, Bag of Tricks for Efficient Text Classification https://arxiv.org/abs/1607.01759
-  Makwana, A. (2022, October 10). Complete Guide to Analyzing Movie Reviews Using NLP. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2022/09/complete-guide-to-analyzing-movie-reviews-using-nlp/

## Demonstration Video

Link to the project demonstration video: https://www.youtube.com/watch?v=aN6St5Tw50Y

*This README was generated as part of the COMP 482 Fall 2023 course project.*
