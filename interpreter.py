import re

def remove_spaces(txt):
    txt = re.sub(r';\s*\n', ';', txt)  
    def replacer(match):
        if match.group(1): 
            return match.group(1)
        else:
            return re.sub(r'\s+', '', match.group(2)) 
    txt = re.sub(r'(".*?")|([^"]+)', replacer, txt)
    
    return txt

def extract_reserved_symbols(txt):
    reserve_words = ["integer", "double", "output", "if"]
    operators = [':', ':=', '+', '-', '<<', '>', '<', '==', '!=']
    
    found_words = []
    for word in reserve_words:
        if word in txt:
            found_words.append(word)
    
    found_symbols = []
    for operator in operators:
        if operator in txt:
            found_symbols.append(operator)
    
    return found_words, found_symbols

def check_syntax(lines):
    errors = []
    variable_decl_pattern = re.compile(r'^\w+:(integer|double);$')
    assignment_pattern = re.compile(r'^\w+:=\s*[\d.]+;$')
    output_pattern = re.compile(r'^output<<(.+);$')
    if_pattern = re.compile(r'^if\((.+)\)$')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Variable declaration
        if ":" in line and ":=" not in line:  # Detect variable declarations
            if not variable_decl_pattern.match(line):
                errors.append(f"Syntax error on line {i+1}: Invalid variable declaration.")
        
        elif ":=" in line:  # Detect assignment statements
            if not assignment_pattern.match(line):
                errors.append(f"Syntax error on line {i+1}: Invalid assignment statement.")
        
        elif "output<<" in line:
            if not output_pattern.match(line):
                errors.append(f"Syntax error on line {i+1}: Invalid output statement.")
        
        elif line.startswith("if"):
            if not if_pattern.match(line):
                errors.append(f"Syntax error on line {i+1}: Invalid if statement.")
        
        elif not line.endswith(";"):
            errors.append(f"Syntax error on line {i+1}: Missing semicolon.")
        
        else:
            if line and not any([variable_decl_pattern.match(line), assignment_pattern.match(line), 
                                output_pattern.match(line), if_pattern.match(line)]):
                errors.append(f"Syntax error on line {i+1}: Unknown syntax.")
    
    return errors

def main():
    testNum = input("Input Test Number: ")
    path = f"tests/PROG{testNum}.HL"

    try:
        with open(path, 'r') as file:
            content = file.readlines() 
    except FileNotFoundError:
        print(f"File {path} not found.")
        return

    no_spaces_content = remove_spaces("".join(content))
    with open("NOSPACES.TXT", 'w') as nospaces_file:
        nospaces_file.write(no_spaces_content)

    found_words, found_symbols = extract_reserved_symbols(no_spaces_content)
    with open("RES_SYM.TXT", 'w') as ressym_file:
        ressym_file.write("Reserved Words:\n" + ', '.join(found_words) + "\n")
        ressym_file.write("Symbols:\n" + ', '.join(found_symbols) + "\n")

    errors = check_syntax(content)
    
    if errors:
        print("ERROR(S) FOUND:")
        for error in errors:
            print(error)
    else:
        print("NO ERROR(S) FOUND")

if __name__ == "__main__":
    main()
