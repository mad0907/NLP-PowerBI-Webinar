from textblob import TextBlob

def translate_to_french(text):
    blob=TextBlob(text)
    return str(blob.translate(from_lang="en", to="fr"))

def translate_to_spanish(text):
    blob=TextBlob(text)
    return str(blob.translate(from_lang="en", to="es"))

def translate_to_Japanese(text):
    blob=TextBlob(text)
    return str(blob.translate(from_lang="en", to="ja"))

def translate_to_hindi(text):
    blob=TextBlob(text)
    return str(blob.translate(from_lang="en", to="hi"))




#print(translate("hello"))

#dataset['spanish_desc']=dataset['description'].apply(translate)