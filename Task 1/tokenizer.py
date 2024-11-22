import re

def basic_tokenizer(text):
    """
    Tokenizes the given text by:
    1. Converting to lowercase
    2. Removing punctuation
    3. Splitting into words
    Args:
        text (str): The input text to tokenize.
    Returns:
        list: A list of tokens (words).
    """
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens


if __name__ == "__main__":
    sample_text = input("Enter input text: ")
    print("Original Text:", sample_text)
    print("Tokens:", basic_tokenizer(sample_text))
