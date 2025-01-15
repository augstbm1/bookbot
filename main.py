def main():
    dict_list = []
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    num = num_words(file_contents)
    number_of_chars = num_chars(file_contents)

    for char, count in number_of_chars.items():
        dict_list.append({'char': char, 'count': count})
    dict_list.sort(reverse=True, key=sort_on)
    
    gen_report(num, dict_list)



def num_words(str):
    return len(str.split())

def num_chars(str):
    
    str_dict = {}
    for char in str:
        if char.isalpha():
            char = char.lower()
            if char in str_dict:
                str_dict[char] += 1
            else:
                str_dict[char] = 1
    return str_dict

def sort_on(dict):
    return dict["count"]

def gen_report(num, lst):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num} words found in the document')
    print()
    for line in lst:
        print(f"The '{line['char']}' character was found {line['count']} times")
    print('--- End report ---')


if __name__ == '__main__':
    main()