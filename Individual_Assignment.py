# Python Program to Convert Roman Numbers to Integer from 1 to 3999

"""   Name: Neway Ketsela  
      Id number: 3809/12
  """

def romanToDecimal(romanNumber):
    roman_number_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal = 0
    prev_value = 0
    l=v=d=0
    char_freq = []
    N = 4
    current_char, count = None, 0
    for ch in reversed(romanNumber):
        if ch == current_char:
                count += 1
        else:
                current_char,count = ch,1
        if count == N:
                char_freq.append(N * ch)
                return print("Invalid Roman Numeral, It can not be more than 3 Consecutive ->", char_freq[0])
        if(ch=='L'):
            l+=1
        if(ch=='V'):
            v+=1
        if(ch=='D'):
            d+=1
  
    if(l<2 and v<2 and d<2):
       pass
    else:
        return print("The Input is WRONG that is V,L, and D can not be repeated. ")
    
    for char in reversed(romanNumber): # iterate through the Roman numeral string in reverse order
        current_value = roman_number_values[char]
        if current_value >= prev_value:
            decimal += current_value     
        else:   
            decimal -= current_value
        prev_value = current_value
    print(decimal)


while True:

    try:
            n=input("Enter the Roman numeral: ")
            romanToDecimal(n.upper())
    except:
        print("The input is wrong. Please try again")

    choose = input("To Convert Again Press \'Y\' or \'y\' Otherwise Press Anykey: ")

    if choose.upper() != "Y":
        break
