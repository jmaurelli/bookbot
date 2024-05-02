def main():
    book_path = "books/frankenstein.txt"
    full_text = parse_text(book_path)
    numb_words = count_words(full_text)
    numb_characters = count_characters(full_text)
    list_of_dict = loop_through(numb_characters)
    list_of_dict.sort(reverse=True, key=sort_on)
    print_results(book_path, numb_words, list_of_dict)

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
        if characters.isalpha():
            if characters not in characters_dic:
                characters_dic[characters] = 0
            characters_dic[characters] += 1
    return characters_dic

def sort_on(dict):
    return dict["count"]

def loop_through(provided_dict):
    list_of_dict = []
    for char, value in provided_dict.items():
        temp_dict = {"letter": char, "count": value}
        list_of_dict.append(temp_dict)
    return list_of_dict

def print_results(path, count, content_to_print):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the docutment\n")
    for item in content_to_print:
        print(f"The {item["letter"]} character has occured {item["count"]} of times")
    print("--- End Report ---")
            

main()