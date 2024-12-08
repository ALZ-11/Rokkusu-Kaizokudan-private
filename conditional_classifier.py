from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
import numpy as np
from helper import produce_brut
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords') 
french_stop_words = stopwords.words('french') #We deal with french reports

def classify_elements(df):
    tfidf = TfidfVectorizer(
        max_features=100,  
        stop_words=french_stop_words,
        ngram_range=(1, 2)
    )
    text_features = tfidf.fit_transform(df['text']).toarray()
    pca = PCA(n_components=5)
    text_features_reduced = pca.fit_transform(text_features)
    
    # 2. Feature engineering
    df['char_density'] = df['chars'] / df['area']
    df['relative_size'] = df['char_size'] / df.groupby('num_page')['char_size'].transform('mean')
    df['vertical_position'] = (df['pos_y'] - df.groupby('num_page')['pos_y'].transform('min')) / \
                             (df.groupby('num_page')['pos_y'].transform('max') - df.groupby('num_page')['pos_y'].transform('min'))
    df.drop("layout", axis=1)
    numerical_features = df[[
        'char_size',
        'char_density',         #Features
        'relative_size',
        'width',
        'vertical_position',
        'aspect',
        'area',
        'chars'
    ]].values
    # combined_features = np.hstack([numerical_features, text_features_reduced]) #numerical and textual features
    # scaler = StandardScaler() #Normalization
    # features_scaled = scaler.fit_transform(combined_features)
    # kmeans = KMeans(n_clusters=3, random_state=42) #K-Means for 3 clusters
    # clusters = kmeans.fit_predict(features_scaled)
    # df['cluster'] = clusters
    # print(df['cluster']) #Visualizing clusters
    
    labels = []
    for idx, row in df.iterrows():
        # Extraction des caractéristiques du texte
        text = row['text'].strip().lower()
        text_length = len(text.split())
        has_punctuation = any(p in text for p in '.!?')
        #Classification using if/else statements
        if (row['char_size'] > df['char_size'].mean() * 1.2 and 
            row['width'] > df['width'].mean() * 0.3 and 
            text_length < 20):  #Tiles are genrally short
            labels.append('Titre')
        
        elif (text_length > 5 and  #Minimum words for paragraphs
              row['width'] > df['width'].mean() * 0.4 and
              has_punctuation and  #Paragraphs have generally punctuation
              row['chars'] > 30):
            labels.append('Paragraphe')
        
        else:
            labels.append('Inutile')
    
    df['label'] = labels
    columns_to_keep = [
        'num_page', 'text', 'width', 'height', 'area', 'chars',
        'char_size', 'pos_x', 'pos_y', 'aspect', 'layout',
        'x0', 'x1', 'y0', 'y1', 'label'
    ]
    
    return df[columns_to_keep]

df = produce_brut("axa-output-1-to-71")
df = classify_elements(df)
df.to_excel("axa_conditional.xlsx", index=False, engine="openpyxl")