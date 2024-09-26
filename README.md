# CSS125L
Hypothetical Language Interpreter using Python

CS145 Lab Exercise
A Simple “Interpreter”
Your simple interpreter called “HLInt.XXX” reads a source code written in our hypothetical language 
“HL.” Then, it performs operations based on the source code.
Our hypothetical language has the following:
1) Variable declaration 
x:integer; <br/>
y:double; <br/>
integer, double – data types
1) Assignment statements
x:= 5;
y:= 2.35;
1) Mathematical operations
Addition and subtraction of single digit integers and double values with precision of 2
x = 3 + 2;
y = 4 + 2.56;
4) Sending output to screen
output<<” <string>”; 
output<<value;
output<<”hello”;
output<<x;
5) Conditional statement
One-way if
If(<condition>)
 <statement>
>,<,==.!=
Example:
x:= 6;
If(x<5)
 Output<<X;
Program Listing
PROG1.HL
x: integer;
x:= 5;
output<<x;
PROG2.HL
x: integer;
y: double;
x:= 3;
y:= 1.25;
output<<x+y;
PROG3.HL
x: integer;
y: double;
x:= 3;
if(x<5)
 output<<x;
The Process:
When HLInt.XXX runs, it opens a source code [PROG1.HL or PROG2.HL or PROG3.HL], then it removes all 
spaces in the program and sends the contents “without spaces” to an output file named 
“NOSPACES.TXT” Then, it sends reserved words and symbols found in the program to “RES_SYM.TXT” 
Finally, it prints on the screen “ERROR” if it finds any syntax error in the program or “NO ERROR(S) 
FOUND” if there are no errors.
Due date:
This is due by Sept. 21, 2024.