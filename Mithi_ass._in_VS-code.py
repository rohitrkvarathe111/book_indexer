#This line defines the class BookIndexGenerator.
class BookIndexGenerator:
    def __init__(self, pages, exclude_words_file):
        self.pages = pages
        self.exclude_words = self.load_exclude_words(exclude_words_file)
        self.index = {}


#This method reads words from the exclude_words_file and returns a set of words after stripping any leading or trailing whitespaces.
    def load_exclude_words(self, exclude_words_file):
        with open(exclude_words_file, 'r', encoding='utf-8') as file:
            return set(word.strip() for word in file.readlines())


#This method processes each page by calling the  method for every page in .process_pageself.pages
    def process_pages(self):
        for page_number, page_file in self.pages.items():
            self.process_page(page_number, page_file)


#This method processes a single page.
#It opens the  and reads its contents.page_file
#The contents are split into a list of words using .split()

    def process_page(self, page_number, page_file):
        with open(page_file, 'r', encoding='utf-8') as file:
            words = file.read().split()
            unique_words = set(word for word in words if word not in self.exclude_words)
            for word in unique_words:
                if word in self.index:
                    self.index[word].add(page_number)
                else:
                    self.index[word] = {page_number}


#This method generates the index file with the provided index_file name.
#sorted_words is a sorted list of keys from self.index.
#It opens the index_file in write mode

    def generate_index_file(self, index_file):
        sorted_words = sorted(self.index.keys())
        with open(index_file, 'w', encoding='utf-8') as file:
            for word in sorted_words:
                pages = ','.join(str(page) for page in sorted(self.index[word]))
                file.write(f"{word} : {pages}\n")





pages = {
    1: 'Page1.txt',
    2: 'Page2.txt',
    3: 'Page3.txt'
}
exclude_words_file = 'exclude-words.txt'
index_file = 'Answer_Index_file/VSCode_Output_index1.txt'

index_generator = BookIndexGenerator(pages, exclude_words_file)
index_generator.process_pages()
index_generator.generate_index_file(index_file)







'''

Summary for the given Python script:

The provided Python script defines a class called BookIndexGenerator that generates an index for a collection of pages. The class takes in the pages dictionary and the exclude_words_file as arguments.

The BookIndexGenerator class has the following methods:

__init__: Initializes the pages, exclude_words, and index attributes of the class. It also calls the load_exclude_words method to load the excluded words from the provided file.
load_exclude_words: Reads the words from the given file and returns them as a set after stripping any leading or trailing whitespace.
process_pages: Iterates over the pages dictionary and calls the process_page method for each page.
process_page: Reads the content of a page file, splits it into words, and filters out the words that are present in the exclude_words set. It then updates the index dictionary by associating each word with the page number.
generate_index_file: Sorts the keys of the index dictionary (words) and writes them along with the sorted page numbers to the specified index file.
The script also includes an example usage where a pages dictionary, exclude_words_file, and index_file are defined. An instance of BookIndexGenerator is created, the pages are processed, and the index file is generated.
'''