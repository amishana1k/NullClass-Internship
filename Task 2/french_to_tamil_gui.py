import tkinter as tk
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

# Load the trained model and tokenizers
model = load_model("french_to_tamil_model.h5")

with open("french_tokenizer.pkl", "rb") as f:
    french_tokenizer = pickle.load(f)

with open("tamil_tokenizer.pkl", "rb") as f:
    tamil_tokenizer = pickle.load(f)

# Create a reverse mapping for Tamil tokenizer
reverse_tamil_tokenizer = {v: k for k, v in tamil_tokenizer.word_index.items()}

# GUI function for translation
def translate_word():
    input_word = entry.get().strip()
    if len(input_word) != 5:
        output_label.config(text="Please enter a 5-letter French word!")
        return
    
    # Convert input word to sequence
    input_sequence = french_tokenizer.texts_to_sequences([input_word])
    input_padded = pad_sequences(input_sequence, maxlen=6, padding='post')
    
    # Predict using the model
    prediction = model.predict(input_padded)
    tamil_indices = np.argmax(prediction, axis=-1)
    
    # Convert indices to Tamil characters
    tamil_word = ''.join([reverse_tamil_tokenizer.get(idx, '') for idx in tamil_indices.flatten()])
    if not tamil_word.strip():
        tamil_word = "Translation not available."
    
    output_label.config(text=f"Tamil Translation: {tamil_word}")


# GUI setup
root = tk.Tk()
root.title("French to Tamil Translator")

tk.Label(root, text="Enter a 5-letter French word:").pack()
entry = tk.Entry(root)
entry.pack()

translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
