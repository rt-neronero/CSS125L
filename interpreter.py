import re

def remove_spaces(txt):
    txt = re.sub(r';\s*\n', ';', txt)  # combine ; and newlines without spaces
    
    def replacer(match):
        # This function is called on each match (either quoted or unquoted text)
        if match.group(1): 
            return match.group(1)
        else:
            return re.sub(r'\s+', '', match.group(2)) 

    txt = re.sub(r'(".*?")|([^"]+)', replacer, txt)
    
    return txt

def main():
    reserve_words = ["integer", "double", "output", "if"]
    operators = [':', ':=', '+', '-', '<<', '>', '<', '==', '!=']

    testNum = input("Input Test Number: ")
    path = f"tests/PROG{testNum}.HL"

    with open(path, 'r') as file:
        content = file.read()
    
    print(remove_spaces(content))

if __name__ == "__main__":
    main()