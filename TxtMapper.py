import os
#import pandas as pd
from helper import produce_brut
from ConditionalClassifier import classify_elements

def rag_texts(df, output_dir='MappedTexts'):
    """
    Export text from a DataFrame to separate text files based on their labels.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing 'label' and 'text' columns
    output_dir : str, optional
        Directory to save the text files (default is 'MappedTexts')
    
    Returns:
    --------
    None
        Creates text files in the specified output directory
    
    Raises:
    -------
    ValueError
        If 'label' or 'text' columns are missing from the DataFrame
    """
    
    if 'label' not in df.columns or 'text' not in df.columns:  #debugging 
        raise ValueError("DataFrame must contain 'label' and 'text' columns")
    
    
    os.makedirs(output_dir, exist_ok=True) #output directory
    
    MappedTexts = df[df['label'].isin(['Titre', 'Paragraphe'])] #Filter the "Inuutile" part   
    output_file = os.path.join(output_dir, "mapped_texts.txt")
    with open(output_file, 'w', encoding='utf-8') as f:  #write texts to .txt file
        for _, row in MappedTexts.iterrows():
            f.write(f"{row['text'].strip()}\n\n") #map text only  
                                                  #or we can map text and its corresponding label by :
                                                  #f.write(f"[{row['label']}]\n{row['text'].strip()}\n\n")
    print(f"Exported {len(MappedTexts)} texts to {output_dir}")

df = produce_brut("axa-output-1-to-71")
df = classify_elements(df)
rag_texts(df)
