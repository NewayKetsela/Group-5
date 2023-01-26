import string

def remove_special_characters(text):
    # remove special characters from the text
    for c in string.punctuation:
        text = text.replace(c, "")
    return text

def word_frequency(text):
    word_freq = {}
    words = text.split() # split the text into words
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    # sort the dictionary by frequency in descending order
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    for word in sorted_words:
        print(word[0], word[1])

def character_frequency(text):
    char_freq = {}
    for c in text:
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    # sort the dictionary by frequency in descending order
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    # print the first five most frequently occurring characters
    for i in range(6):
        if i!=0:
            print(sorted_chars[i][0], sorted_chars[i][1])

def main():
    try:
        with open("MyFile.txt", "r", encoding="utf-8") as f:
           text = f.read()
    except:
        print("File is not found.")
    text = remove_special_characters(text)
    print("Words in decreasing order of frequency: ")
    word_frequency(text)
    print("\nThe first five most frequently occurring characters are:")
    character_frequency(text)

main()