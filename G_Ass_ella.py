import string

def remove_special_characters(s):
    # remove special characters from the text
    for c in string.punctuation:
        s = s.replace(c, "")
    return s

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
def statistical_info(text):
    lines = text.count("\n") + 1
    words = len(text.split())
    characters = len(text)
    print("Total lines: ", lines)
    print("Total words: ", words)
    print("Total characters: ", characters)
def main():
    try:
       with open("ass.txt", "r", encoding="utf-8") as f:
        text = f.read()
    except:
        print("File is not found.")
    text = remove_special_characters(text)
    print("Words in decreasing order of frequency: ")
    word_frequency(text)
    statistical_info(text)

    
if __name__ == '__main__':
       main()