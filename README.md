# CS145 Lab Exercise: A Simple Interpreter

## Overview

This lab exercise involves building a simple interpreter called `HLInt.XXX`, which processes source code written in a hypothetical language called **HL**. The interpreter reads the source code and performs basic operations defined by the language.

## HL Language Features

The **HL** language supports the following features:

### 1. Variable Declaration
```hl
x: integer;
y: double;
```
- `integer`, `double` – Data types

### 2. Assignment Statements
```hl
x := 5;
y := 2.35;
```

### 3. Mathematical Operations
- Addition and subtraction of single-digit integers and double values with precision of 2 decimal places.
```hl
x = 3 + 2;
y = 4 + 2.56;
```

### 4. Output to Screen
```hl
output << "<string>";
output << value;
```
Examples:
```hl
output << "hello";
output << x;
```

### 5. Conditional Statement (One-way `if`)
```hl
if (<condition>)
    <statement>;
```
- Supports relational operators: `>`, `<`, `==`, `!=`

Example:
```hl
x := 6;
if (x < 5)
    output << x;
```

## Program Examples

### PROG1.HL
```hl
x: integer;
x := 5;
output << x;
```

### PROG2.HL
```hl
x: integer;
y: double;
x := 3;
y := 1.25;
output << x + y;
```

### PROG3.HL
```hl
x: integer;
y: double;
x := 3;
if (x < 5)
    output << x;
```

## Interpreter Workflow

When `HLInt.XXX` is executed, it follows these steps:

1. Opens a source code file (`PROG1.HL`, `PROG2.HL`, or `PROG3.HL`).
2. Removes all spaces from the program and writes the output to `NOSPACES.TXT`.
3. Sends reserved words and symbols found in the program to `RES_SYM.TXT`.
4. Checks for syntax errors:
    - Prints **ERROR** if any syntax error is found.
    - Prints **NO ERROR(S) FOUND** if the program is syntactically correct.

## Due Date
- This exercise is due by **Sept. 21, 2024**.
