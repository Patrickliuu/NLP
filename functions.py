import os
import zipfile
import re
from nltk.corpus import stopwords
from nltk import FreqDist
import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from matplotlib import pyplot as plt


# function to automate unzipping of files
def unzip_file(file_path, destination_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        # Extract all files to the destination path
        zip_ref.extractall(destination_path)

    print(f"All files have been extracted to {os.path.abspath(destination_path)}")

#unzip_file('Data/Data_450_news_articles.zip', 'Data/Data_450_news_articles')


# function to read a directory with subdirectories!
def read_directory(path, corpus):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # Recursively call the function to read the subdirectory
            read_directory(item_path, corpus)
        else:
            # Read the file's contents and save it to the corpus
            with open(item_path, "r") as file:
                content = file.read()
                corpus.append(content)

corpus = []
read_directory("../Data/Data_25_reviews", corpus)

print(corpus)


def count_reviews(corpus):
    count = 0
    for review in corpus:
        count += 1
    return count

reviews = count_reviews(corpus)
print(reviews)

# function to count chars
def count_characters(corpus):
    count = 0
    for char in corpus:
        count += len(corpus)
    return count

# function call
character_count = count_characters(corpus)
#print(character_count)  # Output: 48k bei 50k reviews

# Function to count the characters occurrences
def count_character_occurrences(corpus):
    character_counts = {}
    for string in corpus:
        for character in string:
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1
    return character_counts
# function call
char_occurrences = count_character_occurrences(corpus)
#print(char_occurrences)

# function to get the character set
def get_character_set(corpus):
    character_set = set()
    for string in corpus:
        for character in string:
            character_set.add(character)
    return character_set

character_set = get_character_set(corpus)
print(character_set)

#Knuth-Morris
def knuth_morris_pratt_algo(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    # Compute the prefix function for the pattern
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j-1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix[i] = j

    # Perform the search using the prefix function
    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = prefix[j-1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            return i - m + 1

    return -1

#text = "string" # Must be a string, cannot be a list!
#my_pattern = "in"
#match_index = knuth_morris_pratt_algo(text, my_pattern)
##print(match_index)

# Oder kann einfach mit .find() gemacht werden!
#text.find(my_pattern)


def list_to_string(corpus):
    text = ''.join(corpus) # specify a seperator if needed!
    return text

text = list_to_string(corpus)
#print(text)

def split_text(text):
    words = text.split()
    return words

tokens = split_text(text)
#print(tokens)

def count_words(tokens):
    num_words = len(tokens)
    num_unique_words = len(set(tokens))
    return num_words, num_unique_words

counted_words = count_words(tokens)
#print(counted_words)

def create_inverted_index(text):
    inverted_index = {}
    words = text.split()
    for i, word in enumerate(words):
        if word not in inverted_index:
            inverted_index[word] = []
        inverted_index[word].append(i)
    return inverted_index

inverted_index = create_inverted_index(text)
# Look up positions of the word 'psychedlic/glam'
#position = inverted_index['psychedlic/glam']
#print(position)  # Output: [17]

def cleaner(text):
    text = text.lower()
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', text)
    return cleantext

clean = cleaner(text)
#print(clean)

cleaner = split_text(clean)


def filter_stopwords(tokens):
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('english')]
    return filtered_words

filter = filter_stopwords(cleaner)
#print(filter)

def frequency_plot(corpus):
    frequency_distribution = FreqDist(corpus)
    frequency_distribution.plot(25, cumulative=True)

freq = frequency_plot(filter)
print(freq)



pos_tags = nltk.pos_tag(tokens)

tag_freq = nltk.FreqDist(tag for (word, tag) in pos_tags)
plt.figure(figsize=(8, 6))
tag_freq.plot(color='green')
plt.title('POS Tag Frequencies')
plt.xlabel('POS Tag')
plt.ylabel('Frequency')
plt.show()

pos_tags