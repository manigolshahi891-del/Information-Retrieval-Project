import re

from collections import Counter

texts = {
    "text1": "Friends, Romans, countrymen, lend me your ears;",

    "text2": "John's new U.S.A. laptop is a state-of-the-art device. The price is high, but the quality is amazing!",

    "text3": "The authorization for this authorized project is pending. He authorizes the payments regularly."
}

stop_words = {
    "the", "is", "a", "an", "of", "to", "for",
    "and", "but", "this", "he", "his", "in",
    "on", "are", "was", "were", "it"
}


# Step 1: Tokenization
def tokenize(text):

    pattern = r"(?:[A-Za-z]\.){2,}|[A-Za-z]+(?:[-'’][A-Za-z]+)*"

    tokens = re.findall(pattern, text)

    result = []

    for token in tokens:

        if token.lower().endswith(("'s", "’s")):
            token = token[:-2]

        result.append(token)

    return result


# Step 2: Normalization
def normalize(tokens):

    result = []

    for token in tokens:

        token = token.lower()
        token = token.replace(".", "")

        result.append(token)

    return result


# Step 3: Stop Words Removal
def remove_stop_words(tokens):

    return [
        word for word in tokens
        if word not in stop_words
    ]

# Step 4: Stemming
def stem_word(word):

    if word.endswith("ation"):
        return word[:-5]

    elif word.endswith("ed"):
        return word[:-2]

    elif word.endswith("es"):
        return word[:-2]

    return word


def stemming(tokens):

    return [stem_word(word) for word in tokens]

# Testing
for name, text in texts.items():

    print("\n", name)

    tokens = tokenize(text)
    print("Tokenization:", tokens)

    normalized = normalize(tokens)
    print("Normalization:", normalized)

    filtered = remove_stop_words(normalized)
    print("Stop Words Removed:", filtered)

    stemmed = stemming(filtered)
    print("Stemming:", stemmed)
    

# Step 5: Gold Standard
gold_standard = {
    "text1": [
        "friends", "romans", "countrymen",
        "lend", "me", "your", "ears"
    ],

    "text2": [
        "john", "new", "usa", "laptop",
        "state-of-the-art", "device", "price",
        "high", "quality", "amazing"
    ],

    "text3": [
        "authoriz", "authoriz", "project",
        "pending", "authoriz", "payments", "regularly"
    ]
} 

print("\nGold Standard:")
for name, words in gold_standard.items():
   print(name, ":", words)

# Step 6: Precision and Recall

print("\nEvaluation Results:")

for name, text in texts.items():

    tokens = tokenize(text)
    normalized = normalize(tokens)
    filtered = remove_stop_words(normalized)
    predicted = stemming(filtered)

    actual = gold_standard[name]

    predicted_set = set(predicted)
    actual_set = set(actual)

    true_positive = len(predicted_set & actual_set)
    false_positive = len(predicted_set - actual_set)
    false_negative = len(actual_set - predicted_set) 
    
    precision = true_positive / (true_positive + false_positive) if true_positive + false_positive else 0

    recall = true_positive / (true_positive + false_negative) if true_positive + false_negative else 0
    f1_score = 2 * precision * recall / (precision + recall) if precision + recall else 0

    print("\n", name)
    print("True Positive:", true_positive)
    print("False Positive:", false_positive)
    print("False Negative:", false_negative)
    print("Precision:", round(precision * 100, 2), "%")
    print("Recall:", round(recall * 100, 2), "%")
    print("F1-Score:", round(f1_score * 100, 2), "%")
    print("Extra Words:", list(predicted_set - actual_set))
    print("Missing Words:", list(actual_set - predicted_set))

 # Custom Text Input
print("\nEnter your own text:")
custom_text = input()

tokens = tokenize(custom_text)
normalized = normalize(tokens)
filtered = remove_stop_words(normalized)
stemmed = stemming(filtered)

print("\nProcessed Result:")
print("Tokenization:", tokens)
print("Normalization:", normalized)
print("Stop Words Removed:", filtered)
print("Stemming:", stemmed)
