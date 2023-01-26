import string

def remove_special_characters(text):
    # remove special characters from the text
    for c in string.punctuation:
        text = text.replace(c, "")
    return text
    
def main():
    try:
        with open("MyFile.txt", "r", encoding="utf-8") as f:
           text = f.read()
    except:
        print("File is not found.")
    text = remove_special_characters(text)

main()