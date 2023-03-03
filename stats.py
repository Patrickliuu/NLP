import os
import nltk
from nltk import FreqDist

# Define the path to the meta folder containing subfolders
meta_path = '../Data/Data_25_reviews'

# Initialize variables to hold corpus statistics
num_files = 0
total_words = 0
unique_words = set()
corpus = []

# Recursive function to compute statistics for all files in a directory
def compute_stats(directory):
    global num_files, total_words, unique_words
    # Iterate over all files and subdirectories in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # If the item is a file, compute statistics for it
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            num_files += 1
            words = nltk.word_tokenize(text.lower())
            total_words += len(words)
            unique_words.update(words)
        # If the item is a directory, recurse into it
        elif os.path.isdir(file_path):
            compute_stats(file_path)

# Compute corpus statistics for the meta folder
compute_stats(meta_path)


# Compute derived statistics
avg_text_length = total_words / num_files
num_unique_words = len(unique_words)

# Print corpus statistics
print("Number of files: ", num_files)
print("Average text length: ", avg_text_length)
print("Total words: ", total_words)
print("Number of unique words: ", num_unique_words)




def frequency_plot(corpus):
    frequency_distribution = FreqDist(corpus)
    frequency_distribution.plot(20, cumulative=True)

freq = frequency_plot(corpus)
print(freq)