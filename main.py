def count_words(content):
    words = content.split()

def count_characters(content):
    words = content.split()
    count_list = {}

    for word in words:
        letters = list(word)

        for letter in letters:
            current_letter = letter.lower()

            if current_letter not in count_list:
                count_list[current_letter] = 0

            count_list[current_letter] += 1
    
    return count_list

def sort_on(dict):
    return dict["count"]

def __main__():
    book_path = "books/frankenstein.txt"
    with open(book_path, 'r') as book:
        book_content = book.read()
        count_dict = count_characters(book_content)
        
        count_list = []
        
        for letter, count in count_dict.items():
            count_list.append({"letter": letter, "count": count})

        count_list.sort(reverse=True, key=sort_on)

        print(f"--- Begin report of {book_path} ---")
        for count in count_list:
            if count['letter'].isalpha():
                print(f"The '{count['letter']}' character was found {count['count']} times")

        #print("--- End report ---")
__main__()
