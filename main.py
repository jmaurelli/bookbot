def main():
    book_path = "books/frankenstein.txt"
    full_text = parse_text(book_path)
    numb_words = count_words(full_text)
    print(f"{numb_words} words in this text.")
    numb_characters = count_characters(full_text)
    print(numb_characters)
    loop_through(numb_characters)

def parse_text(path):
    with open(path) as f:
        return f.read()

def count_words(words):
    parsed_words = words.split()
    return len(parsed_words)

def count_characters(text):
    characters_dic = {}
    lowered_text = text.lower()
    for characters in lowered_text:
        if characters not in characters_dic:
            characters_dic[characters] = 0
        characters_dic[characters] += 1
    return characters_dic

def sort_on(dict):
    pass

def loop_through(provided_dict):
    empty_list = []
    for char, value in provided_dict.items():
        temp_dict = {"letter": char, "count": value}
        empty_list.append(temp_dict)
        print(empty_list)

main()