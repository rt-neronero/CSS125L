import re

def remove_spaces(txt):
    try:
        txt = re.sub(r';\s*\n', ';', txt)  

        def replacer(match):
            if match.group(1): 
                return match.group(1)
            else:
                return re.sub(r'\s+', '', match.group(2))
        txt = re.sub(r'(".*?")|([^"]+)', replacer, txt)

        return txt
    except Exception as e:
        print(f"Error in remove_spaces: {e}")
        return ""

def process_output(line, variables):
    match = re.match(r'output\s*<<\s*(.*);', line)
    if match:
        value = match.group(1).strip()
        if value.startswith('"') and value.endswith('"'):
            return value.strip('"') 
        elif value in variables:
            return str(variables[value])
        else:
            try:
                result = eval(value, {}, variables)
                return str(result)
            except Exception as e:
                return f"Error evaluating expression: {value}"
    return None

def extract_reserved_symbols(lines):
    reserve_words = ["integer", "double", "output", "if"]
    operators = [':', ':=', '+', '-', '>', '<', '==', '!=', '<<']

    symbols = set()
    for line in lines:
        line = line.strip()
        
        for word in reserve_words:
            if word in line:
                symbols.add(word)

        for operator in operators:
            if operator in line:
                if operator == '<<' and line.count('<<') > 0:
                    symbols.add('<<')
                elif operator == '<' and line.count('<') > 0:
                    if '<<' not in line:
                        symbols.add('<')
                else:
                    symbols.add(operator)

    print(f"Extracted reserved symbols: {symbols}") #debugger

    return symbols

def check_syntax_and_output(lines):
    variables = {}
    outputs = []
    errors = []

    variable_decl_pattern = re.compile(r'^\s*(\w+)\s*:\s*(integer|double)\s*;$')
    assignment_pattern = re.compile(r'^\s*(\w+)\s*:=\s*([\d.]+)\s*;$')
    output_pattern = re.compile(r'^\s*output\s*<<\s*.+\s*;$')
    if_pattern = re.compile(r'^\s*if\s*\(.+\)\s*$')

    for i, line in enumerate(lines):
        line = line.strip()

        # Variable declaration
        if ":" in line and ":=" not in line:
            match = variable_decl_pattern.match(line)
            if match:
                var_name, var_type = match.groups()
                variables[var_name] = 0 if var_type == "integer" else 0.0
            else:
                errors.append(f"Syntax error on line {i+1}: Invalid variable declaration.")

        elif ":=" in line:
            match = assignment_pattern.match(line)
            if match:
                var_name, value = match.groups()
                if var_name in variables:
                    if isinstance(variables[var_name], int):
                        variables[var_name] = int(float(value))
                    elif isinstance(variables[var_name], float):
                        variables[var_name] = float(value)
                else:
                    errors.append(f"Syntax error on line {i+1}: Undefined variable '{var_name}'")
            else:
                errors.append(f"Syntax error on line {i+1}: Invalid assignment statement.")

        elif output_pattern.match(line):
            output_result = process_output(line, variables)
            if output_result:
                outputs.append(output_result)
            else:
                errors.append(f"Syntax error on line {i+1}: Invalid output statement.")

        elif if_pattern.match(line):
            condition = re.search(r'\((.+)\)', line).group(1)
            try:
                if eval(condition, {}, variables):
                    continue  # If condition is true, proceed to the next statement
            except Exception as e:
                errors.append(f"Syntax error on line {i+1}: Invalid condition in if statement.")

        else:
            if line != "" and not any([variable_decl_pattern.match(line), assignment_pattern.match(line), output_pattern.match(line), if_pattern.match(line)]):
                errors.append(f"Syntax error on line {i+1}: Unknown syntax.")

    return errors, outputs

def main():
    path = input("Enter file name: ")
    
    try:
        with open(path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File {path} not found!")
        return

    print(f"File content before removing spaces:\n{content}\n") #debugger

    no_spaces_content = remove_spaces(content)
    with open("NOSPACES.TXT", 'w') as no_spaces_file:
        no_spaces_file.write(no_spaces_content)

    print(f"Content after removing spaces:\n{no_spaces_content}\n")

    lines = content.splitlines()
    errors, outputs = check_syntax_and_output(lines)

    with open("NOSPACES.TXT", 'a') as no_spaces_file:
        no_spaces_file.write("\n\nOutput/s:\n")
        if outputs:
            no_spaces_file.write("\n".join(outputs))
        else:
            no_spaces_file.write("No outputs.")

    reserved_symbols = extract_reserved_symbols(lines)
    with open("RES_SYM.TXT", 'w') as res_sym_file:
        res_sym_file.write("\n".join(sorted(reserved_symbols)))

    if errors:
        print("ERROR(S) FOUND:")
        for error in errors:
            print(error)
    else:
        print("NO ERROR(S) FOUND")

if __name__ == "__main__":
    main()
