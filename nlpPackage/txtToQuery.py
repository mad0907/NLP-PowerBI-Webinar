from textblob import TextBlob
import pandas as pd

# Create a sample DataFrame
# data = {'text': ['This is a positive sentence.', 
#                 'This is a negative sentence.', 
#                 'This is a neutral sentence.'],
#         'label': [1, -1, 0]}
# df = pd.DataFrame(data)

# Define a function to return the sentiment of a sentence using TextBlob
def get_sentiment(sentence):
    return TextBlob(sentence).sentiment.polarity

# Use the 'text' column and the get_sentiment function to create a new 'sentiment' column
def get_df_with_sentiments(df):
    # df=pd.read_csv(r"C:\Users\munmun.a.das\OneDrive - Accenture\DS_Sessions\PowerBI\FoodFeedback.csv")
    df['sentiment'] = df['feedback'].apply(get_sentiment)
    return(df)

# Use the new 'sentiment' column to filter the DataFrame
# positive_rows = df[df['sentiment'] > 0]
# negative_rows = df[df['sentiment'] < 0]
# neutral_rows = df[(df['sentiment'] >= 0) & (df['sentiment'] <= 0)]

#from nlpPackage import txtToQuery as senti
#dataset['sentiment']=dataset['feedback'].apply(senti.get_sentiment)

