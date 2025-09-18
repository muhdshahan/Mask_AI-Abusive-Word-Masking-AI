from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


model_name = "unitary/toxic-bert"
# Tokenizer converts raw text to token then IDs that the model understands
# "You idiot -> [101, 1128, 7543, 102]"
# The tokenizer also handles padding, truncation and special tokens.
tokenizer = AutoTokenizer.from_pretrained(model_name)
# AutoModelForSequenceClassification is the correct Hugging Face Wrapper for models that output classification scores.
# It pulls pretrained weights from Hugging Face Hub(if not cached locally)
# once loaded, can pass tokenized input into it and outputs toxicity probabities
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline for classification
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, truncation=True)

def is_toxic(text: str, threshold: float):
    """ check if text is toxic based on threshold """
    result = classifier(text)[0]
    return result["label"].lower() == "toxic" and result["score"] >= threshold


def mask_abusive_words(text: str, threshold: float):
    """
    Step 1: Check if line is toxic
    Step 2: If toxic, check each word and mask abusive ones
    """
    # If line is clean then return as it is
    if not is_toxic(text, threshold):
        return text
    
    words = text.split()
    masked_words = []

    for word in words:
        if is_toxic(word, threshold):
            masked_words.append("[")
            masked_words.append("*" * len(word)) 
            masked_words.append("]")
        else:
            masked_words.append(word)

    return " ".join(masked_words)

# sentences = [
#     "I hate you idiot!",
#     "What a beautiful day my friend.",
#     "You are such a loser.",
# ]

# for s in sentences:
#     print(f"Original: {s}")
#     print(f"Cleaned : {mask_abusive_words(s)}")
#     print("-" * 50)