import zipfile
import os

class Corpus:
    def __init__(self, path):
        self.corpus = []
        self.path = path
        self.num_files = 0
        self.total_words = 0
        self.unique_words = set()
        self.file_lengths = {}
        self.inverted_index = {}

    def unzip_file(self, dest_path):
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            # Extract all files to the destination path
            zip_ref.extractall(dest_path)

        print(f"All files have been extracted to {os.path.abspath(dest_path)}")

    def read_directory(self):
        for item in os.listdir(self.path):
            item_path = os.path.join(self.path, item)
            if os.path.isdir(item_path):
                # Recursively call the function to read the subdirectory
                self.read_directory()
            else:
                # Read the file's contents and save it to the corpus
                with open(item_path, "r") as file:
                    content = file.read()
                    self.corpus.append(content)


c1 = Corpus("../Data/Data_25_reviews")
#c1.unzip_file("../Data/Data_25_reviews")
c1.read_directory()
