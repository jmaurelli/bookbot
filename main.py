def main():
    book_path = "books/frankenstein.txt"
    full_text = parse_text(book_path)
    numb_words = count_words(full_text)
    print(f"{numb_words} words in this text.")
    numb_characters = count_characters(full_text)
    print(numb_characters)

def parse_text(path):
    with open(path) as f:
        return f.read()

def count_words(words):
    parsed_words = words.split()
    return len(parsed_words)

def count_characters(text):
    characters_dic = {}
    for characters in text:
        lowered_text = text.lower()
        if lowered_text in characters_dic:
            characters_dic[characters] += 1
        else:
            characters_dic[characters] = 1
    return characters_dic
main()