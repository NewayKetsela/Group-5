# Python Program to Convert Roman Numbers to Integer from 1 to 3999

print("            ==========================================\n")
print("            == Name: Tesfaye Tesema  Id number: 1512/12\n")
print("            ==========================================\n")

                # to create a dictionary of Roman numeral default values
romanN_constant_Values= {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
}

def romanToDecimal(romanNumbers):
    result = 0
    for i in range(len(romanNumbers) - 1):
        left = romanNumbers[i]
        right = romanNumbers[i + 1]
        if romanN_constant_Values[left] < romanN_constant_Values[right]:
            result -= romanN_constant_Values[left]
        else:
            result += romanN_constant_Values[left]
    result += romanN_constant_Values[romanNumbers[-1]]

    if result >3999:
        return print("Number is greater than 3999")
    else:
        return result


print("             ROMAN NUMBER TO ARABIC NUMBERS!              ")



while 1:
    count = 0
    try: 
        print("Please enter roman number between 1 and 3999 ")
        number = input()
        if len(number) <= 3:
            print(number," = ",romanToDecimal(number))
            count=count+1
        elif len(number)>3:
            for i in range(0,len(number),1):
                if i>=3:
                    if number[i] == number[i-1] == number[i-2] == number[i-3]:
                        count=count+1
                        print("Use appropriate ROMAN numbers")
                        break
        if count == 0:
            print(number," = ",romanToDecimal(number))
            count=0
        else:
            
            count=0
    except:
        print("pLEASE ENTER VALID ROMAN NUMBERS!")
    finally:
        print("--------------------------------------------------------")

