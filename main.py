import string
def sort_on(d):
    return d["num"]
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def read_book(path):
    with open(path) as f:
         file_contents = f.read()
         return file_contents

def convertbook_letters(file_contents):
    words=file_contents.lower()
    return words

def create_letterdic(lower_list):
    a = list(string.ascii_lowercase)
    answer_dic={}

    for item in lower_list:
            count=1
            if(item.isalpha() and item in a):
                if item in answer_dic:
                    count=answer_dic[item]+1
                    answer_dic[item]=count
                else:
                    answer_dic[item]=count
    return answer_dic
                    



def main():
    book_data=read_book("books/frankenstein.txt")
    lower_list=convertbook_letters(book_data)
    letter_dic=create_letterdic(lower_list)
    new_list=chars_dict_to_sorted_list(letter_dic)
    
    for item in new_list:
     print(f"The '{item['char']}' character was found {item['num']} times")
    
    
                 

    
             


main()
