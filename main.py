from stats import get_book_words_count, get_book_characters_count, sort_characters_count
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main(book_path):
    book_text = get_book_text(book_path)
    words_count = get_book_words_count(book_text)
    characters_count = get_book_characters_count(book_text)
    sorted_characters_count = sort_characters_count(characters_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    
    print("--------- Character Count -------")
    for item in sorted_characters_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    main(sys.argv[1])
        