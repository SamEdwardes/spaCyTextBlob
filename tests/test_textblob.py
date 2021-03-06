import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")


def test_types():
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    
    # Check types
    assert type(doc._.polarity) is float
    assert type(doc._.subjectivity) is float
    assert type(doc._.assessments) is list


def test_negative_sentiment():
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    # Check polarity
    assert doc._.polarity == -1.0
    assert doc[4]._.polarity == -1.0
    [span._.polarity for span in doc.sents] == [-1.0 , -1.0]
    # Check polarity
    assert doc._.subjectivity == 1.0
    assert doc[4]._.subjectivity == 1.0
    assert [span._.subjectivity for span in doc.sents] == [1.0 , 1.0]
    
    
def test_positive_sentiment():
    text = "I had a really amazing day. It was the best day ever!"
    doc = nlp(text)
    # Check polarity
    assert doc._.polarity == 0.8
    assert round(doc[4]._.polarity, 1) == 0.6
    [round(span._.polarity, 1) for span in doc.sents] == [0.6 , 1.0]
    # Check polarity
    assert doc._.subjectivity == 0.6
    assert doc[4]._.subjectivity == 0.9
    assert [span._.subjectivity for span in doc.sents] == [0.9 , 0.3]
    
    
def test_compare_to_text_blob():
    # Text example 1
    text = "It is a very fun thing how happy puppies can make you."
    blob = TextBlob(text)
    doc = nlp(text)
    assert blob.polarity == doc._.polarity
    assert blob.subjectivity == doc._.subjectivity
    assert blob.sentiment_assessments[2] == doc._.assessments
    
    # Text example 2
    text = "My favourite food is Italian food. I love it."
    blob = TextBlob(text)
    doc = nlp(text)
    assert blob.polarity == doc._.polarity
    assert blob.subjectivity == doc._.subjectivity
    assert blob.sentiment_assessments[2] == doc._.assessments
