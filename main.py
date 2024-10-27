def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    nice_print_report(character_count, word_count, book_path)

def get_book_text(file):
    with open("books/frankenstein.txt") as f:
        return f.read()


def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    text = text.lower()
    characters_count = {}
    for character in text:
        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1
    return characters_count

def nice_print_report(character_count, word_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for character in character_count:
        if character.isalpha():
            print(f"The '{character}' character was found {character_count[character]} times")
    print("--- End report ---")
main()