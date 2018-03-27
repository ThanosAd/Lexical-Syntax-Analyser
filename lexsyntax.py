
# PAPAIOANNOU GIANNIS A.M 2794 , username : cse42794
# ANTAMIS THANASIS A.M 2639, username : cse42639


import sys
import fileinput

print "\n**** LEXICAL/SYNTAX ANALYSER ****\n\nPlease enter a file name: ",
filename = raw_input()
myfile = open(filename)
temp = myfile.read(1)
line = 0
if(temp == '\n'):
        line = line + 1
token = ""
tk = ""

### lex() function for the lexical analysis

def lex():
    global temp
    phrase = ""
    global line
    global token
    while(temp == "\n" or temp == ' ' or temp == '\t'):     ## Pass the tabs, spaces and new line characters
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    if(temp == "/"):                                       ## Check for comments
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
        
        if(temp == "*"):
            temp = myfile.read(1)
            if(temp == "\n"):
                line = line + 1
            while(temp != "*"):
                temp = myfile.read(1)
                if(temp == "\n"):
                    line = line + 1
                if not temp:
                    print("ERROR: EOF reached :  '*/' expected")
                    sys.exit()
            if(temp == "*"):
                temp = myfile.read(1)
                if(temp == "\n"):
                    line = line + 1
                if(temp == "/"):
                    temp = myfile.read(1)
                    if(temp == "\n"):
                        line = line + 1
                else:
                    print("ERROR:'/' expected")
        elif(temp == "/"):
            myfile.readline()
            temp = myfile.read(1)
            if(temp == "\n"):
                line = line + 1
    
        else:
            token = "divtk"
            return token
     
    while(temp == '\n' or temp == ' ' or temp == '\t'):
        
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    if(temp.isalpha()):                                     ## State 1: Check for alphabetical symbol
        phrase = phrase + temp
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
        count = 2
        while(temp.isalpha() or temp.isdigit()):
            if(count <= 30):
                phrase = phrase + temp
                temp = myfile.read(1)
                if(temp == "\n"):
                    line = line + 1
                count += 1
            else:
                while(temp.isalpha() or temp.isdigit()):
                    temp = myfile.read(1)
                    if(temp == "\n"):
                        line = line + 1
                print("WARNING: length of variable greater than 30 characters")
        if(phrase == "program"):                                                           ## Check for keywords
            token = "programtk"

        elif(phrase == "endprogram"):    
            token = "endprogramtk"

        elif(phrase == "declare"):    
            token = "declaretk"

        elif(phrase == "enddeclare"):    
            token = "enddeclaretk"

        elif(phrase == "if"):    
            token = "iftk"

        elif(phrase == "then"):    
            token = "thentk"

        elif(phrase == "else"):    
            token = "elsetk"

        elif(phrase == "endif"):    
            token = "endiftk"

        elif(phrase == "while"):    
            token = "whiletk"

        elif(phrase == "endwhile"):    
            token = "endwhiletk"

        elif(phrase == "repeat"):    
            token = "repeattk"

        elif(phrase == "endrepeat"):    
            token = "endrepeattk"

        elif(phrase == "exit"):    
            token = "exittk"

        elif(phrase == "switch"):    
            token = "switchtk"

        elif(phrase == "case"):    
            token = "casetk"

        elif(phrase == "endswitch"):    
            token = "endswitchtk"

        elif(phrase == "forcase"):    
            token = "forcasetk"

        elif(phrase == "when"):    
            token = "whentk"

        elif(phrase == "endforcase"):   
            token = "endforcasetk"

        elif(phrase == "procedure"):    
            token = "proceduretk"

        elif(phrase == "endprocedure"):    
            token = "endproceduretk"

        elif(phrase == "function"):    
            token = "functiontk"

        elif(phrase == "endfunction"):    
            token = "endfunctiontk"

        elif(phrase == "call"):    
            token = "calltk"

        elif(phrase == "return"):    
            token = "returntk"

        elif(phrase == "in"):    
            token = "intk"

        elif(phrase == "inout"):    
            token = "inouttk"

        elif(phrase == "and"):    
            token = "andtk"

        elif(phrase == "or"):    
            token = "ortk"

        elif(phrase == "not"):    
            token = "nottk"

        elif(phrase == "true"):    
            token = "truetk"

        elif(phrase == "false"):    
            token = "falsetk"

        elif(phrase == "input"):    
            token = "inputtk"

        elif(phrase == "print"):    
            token = "printtk"
            
        else:
            token = "idtk"                                     ## If not keyword, then id of variable
    
    elif(temp.isdigit()):                                     ## Check for digit
        phrase = phrase + temp
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
        while(temp.isdigit()):
            phrase = phrase + temp
            if(-32767 <= int(phrase) <= 32767):
                temp = myfile.read(1)
                if(temp == "\n"):
                    line = line + 1
            elif(int(phrase) > 32767):
                print("ERROR: number out of bounds(number bigger than 32767)"+phrase)
                sys.exit()
            elif(int(phrase) < -32767):
                print("ERROR: number out of bounds(number smaller than -32767)")
                sys.exit()
        if(temp.isalpha()):
            print("ERROR:letter after number")
            sys.exit()
        token= "constanttk"
    elif(temp == "+"):                                     ## Check for the remaining symbols of the language
        token = "plustk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == "-"):
        token = "minustk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == "*"):
        token = "multk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == "="):
        token = "equaltk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == "<"):
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
        if(temp == "="):
            token = "lessequaltk"
            temp = myfile.read(1)
            if(temp == "\n"):
                line = line + 1
        elif(temp == ">"):
            token = "morelesstk"
            temp = myfile.read(1)
        else:
            token = "lesstk"
            if(temp == "\n"):
                line = line + 1
    elif(temp == ">"):
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
        if(temp == "="):
            token = "moreequaltk"
            temp = myfile.read(1)
            if(temp == "\n"):
                line = line + 1
        else:
            token = "moretk"
            temp = myfile.read(1)
            if(temp == "\n"):
                line = line + 1
    elif(temp == ":"):
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
        if(temp == "="):
            token = "assignmenttk"
            temp = myfile.read(1)
            if(temp == "\n"):
                line = line + 1
        else:
            token = "colontk"
            temp = myfile.read(1)
            if(temp == "\n"):
                line = line + 1
    elif(temp == ","):
        token = "commatk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == ";"):
        token = "semicolontk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == "("):
        token = "rightbrackettk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == ")"):
        token = "leftbrackettk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == "["):
        token = "rightsqbrackettk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif(temp == "]"):
        token = "leftsqbrackettk"
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    elif not temp:
        print ("WARNING : EOF ")                                  ## End of file reached
        token = "eoftk"
    else :                                                       ## Not known character
        print ("ERROR : invalid character: "+ temp + " : line : "+str(line))
        sys.exit()
        temp = myfile.read(1)
        if(temp == "\n"):
            line = line + 1
    return token





### FUNCTIONS FOR SYNTAX ANALYSIS



def program():
    
    global tk 
    if(tk == "programtk"):
        tk = lex()
        if (tk== "idtk") :
          
	    tk=lex()
           
	    block()
	
            if ( tk == "endprogramtk"):
		
                tk = lex()
                print("*** LEXICAL/SYNTAX ANALYSIS COMPLETED SUCCCESSFULLY ***")
            else:
                print("ERROR : keyword 'endprogram' expected or ';' after statement "+": line: "+str(line))
                sys.exit()
        else:
            print("ERROR : program name expected"+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : keyword 'program' expected"+": line: "+str(line))
        sys.exit()
        
def block():
    
    declarations()
    subprograms()
    statements()

def declarations():
    global tk 
    if(tk == "declaretk"):
        tk = lex()
        varlist()
        if(tk == "enddeclaretk"):
            tk = lex()
        else:
            print ("ERROR : keyword 'enddeclare' expected"+": line: "+str(line))
            sys.exit()
		

def varlist():
    global tk 
    if(tk == "idtk"):
        tk = lex()
        while(tk == "commatk"):
            tk = lex()
            if(tk == "idtk"):
                    tk = lex()		
            else:
                print("ERROR : name of variable expected after ',' "+": line: "+str(line))
                sys.exit()
    				

def subprograms():
    global tk 
    while(tk == "proceduretk" or tk == "functiontk"):
        
        procorfunc()
        

def procorfunc():
    global tk
    if(tk == "proceduretk"):
        tk = lex()
        if( tk == "idtk"):
            tk = lex()
            procorfuncbody()
            if(tk == "endproceduretk"):
                tk = lex()
            else:
                print("ERROR : keyword 'endprocedure' or ';' expected "+": line: "+str(line))
                sys.exit()
        else:
            print("ERROR : name of procedure expected"+": line: "+str(line))
            sys.exit()
    elif(tk == "functiontk"):
        tk = lex()
        
        if(tk == "idtk"):
            tk = lex()
           
            procorfuncbody()
            if(tk == "endfunctiontk"):
                tk = lex()
            else:
                print("ERROR : keyword 'endfunction' or ';' expected "+": line: "+str(line))
                sys.exit()
        else:
            print("ERROR : name of function expected"+": line: "+str(line))
            sys.exit()

def procorfuncbody():
    formalpars()
    block()

def formalpars ():
    global tk
    if( tk == "rightbrackettk"):
        tk = lex()
        formalparlist()
        if(tk == "leftbrackettk"):
            tk = lex()
        else:
            print("ERROR : ')' expected after formal parameters of procedure or function "+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : '(' expected before formal parameters of procedure or function "+": line: "+str(line))
        sys.exit()
	
def formalparlist():
    formalparitem()
    global tk
    while(tk == "commatk"):
       tk = lex()
       formalparitem()

def formalparitem():
    global tk
    if(tk == "intk" or tk == "inouttk"):
        tk = lex()
        if(tk == "idtk"):
            tk = lex()
        else:
            print("ERROR: name of formal parameter expected "+": line: "+str(line))
            sys.exit()
			    
    else:
        print("ERROR: 'in' or 'inout' keyword expected before the name of formal parameter "+": line: "+str(line))
        sys.exit()
		

def statements():
    global tk
    statement()
    while( tk == "semicolontk"):
        tk = lex()
        statement()

def statement():
	if(tk == "idtk"):
		assignmentstat()
	elif(tk == "iftk"):
		ifstat()
	elif(tk == "whiletk"):
		whilestat()
	elif(tk == "repeattk"):
		repeatstat()
	elif(tk == "exittk"):
		exitstat()
	elif(tk == "switchtk"):
		switchstat()
	elif(tk == "forcasetk"):
		forcasestat()
	elif(tk == "calltk"):
		callstat()
	elif(tk == "returntk"):
		returnstat()
	elif(tk == "inputtk"):
		inputstat()
	elif(tk == "printtk"):
		printstat()
    
def assignmentstat():
    global tk
    if(tk =="idtk"):
        tk = lex()
        if(tk == "assignmenttk"):
            tk =lex()
            expression()
        else:
            print("ERROR : ':=' expected"+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : name of variable expected before assignment token "+": line: "+str(line))
        sys.exit()

def ifstat():
    global tk
    if(tk == "iftk"):
        tk = lex()
        condition()
        if(tk == "thentk"):
            tk = lex()
            statements()
            elsepart()
            if(tk == "endiftk"):
                tk = lex()
            else:
                print ("ERROR : keyword 'endif' or ';' expected "+": line: "+str(line))
                sys.exit()
        else:
            print("ERROR : keyword 'then' expected"+": line: "+str(line))
            sys.exit()
    else:
        print ("ERROR : keyword 'if' expected"+": line: "+str(line))
        sys.exit()

def elsepart():
    global tk
    if(tk == "elsetk"):
        tk = lex()
        statement()
    
def repeatstat():
    global tk
    if(tk == "repeattk"):
        tk = lex()
        statements()
        if(tk == "endrepeattk"):
            tk = lex()
        else:
            print("ERROR : keyword 'endrepeat' or ';' expected"+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : keyword 'repeat' expected"+": line: "+str(line))
        sys.exit()

def exitstat():
    global tk
    if(tk == "exittk"):
        tk = lex()
    else:
        print("ERROR : keyword 'exit' or ';' expected "+": line: "+str(line))
        sys.exit()

def whilestat():
    global tk
    if(tk == "whiletk"):
        tk = lex()
        condition()
        statements()
        if(tk == "endwhiletk"):
               tk = lex()
        else:
            print("ERROR : keyword 'endwhile' or ';' expected "+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : keyword 'while' expected"+": line: "+str(line))
        sys.exit()

def switchstat():
    global tk
    if( tk == "switchtk"):
        tk = lex()
        expression()
        if(tk == "casetk"):
            while(tk == "casetk"):
                tk = lex()
                expression()
                if(tk == "colontk"):
                    tk = lex()
                    statements()
                else:
                    print("ERROR : ':' expected"+": line: "+str(line))
                    sys.exit()
        else:
            print("ERROR : keyword 'case' expected"+": line: "+str(line))
            sys.exit()
        if(tk == "endswitchtk"):
            tk = lex()
        else:
            print("ERROR: keyword 'endswitch' or ';' expected "+": line: "+str(line))
            sys.exit()
    else :
        print("ERROR : keyword 'switch' expected"+": line: "+str(line))
        sys.exit()

def forcasestat():
    global tk
    if( tk == "forcasetk"):
        tk = lex()
        if(tk == "whentk"):
            while(tk == "whentk"):
                tk = lex()
                condition()
                if(tk == "colontk"):
                    tk = lex()
                    statements()
                else:
                    print("ERROR : ':' expected after condition "+": line: "+str(line))
                    sys.exit()
        else:
            print("ERROR : keyword 'when' expected"+": line: "+str(line))
            sys.exit()
        if(tk == "endforcasetk"):
            tk = lex()
        else:
            print("ERROR: keyword 'endforcase' or ';' expected "+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : keyword 'forcase' expected"+": line: "+str(line))
        sys.exit()

def callstat():
    global tk
    if(tk == "calltk"):
        tk = lex()
        if(tk == "idtk"):
            tk = lex()
            actualpars()
        else:
            print("ERROR : name of procedure expected "+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : keyword 'call' expected"+": line: "+str(line))
        sys.exit()
               
def returnstat():
    global tk
    if(tk == "returntk"):
        tk = lex()
        expression()
    else:
        print("ERROR : keyword 'return' or ';' expected"+": line: "+str(line))
        sys.exit()

def printstat():
    global tk
    if(tk == "printtk"):
        tk = lex()
        expression()
    else:
        print("ERROR : keyword 'print' expected"+": line: "+str(line))
        sys.exit()

def inputstat():
    global tk
    if(tk == "inputtk"):
        tk = lex()
        if(tk == "idtk"):
            tk = lex()
        else:
            print("ERROR : name of input variable expected"+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR : keyword 'input' expected"+": line: "+str(line))
        sys.exit()

def actualpars():
    global tk
    if(tk == "rightbrackettk"):
        tk = lex()
        actualparlist()
        if(tk == "leftbrackettk"):
            tk = lex()
        else:
            print("ERROR: ')' expected after actual parameters"+": line: "+str(line))
            sys.exit()
    else:
        print("ERROR: '(' expected before actual parameters "+": line: "+str(line))
        sys.exit()

def actualparlist():
    global tk
    actualparitem()
    while(tk == "commatk"):
        tk = lex()
        actualparitem()

def actualparitem():
    global tk
    if(tk == "intk"):
        tk = lex()
        expression()
    elif(tk == "inouttk"):
        tk = lex()
        if(tk == "idtk"):
            tk = lex()
        else:
            print("ERROR: name of actual parameter expected "+": line: "+str(line))
    else:
        print("ERROR: 'in' or 'inout' keyword expected "+": line: "+str(line))

def condition():
    global tk
    boolterm()
    while(tk == "ortk"):
        tk = lex()
        boolterm()

def boolterm():
    global tk
    boolfactor()
    while( tk == "andtk"):
        tk = lex()
        boolfactor()

def boolfactor():
    global tk
    if (tk == "nottk"):
        tk = lex()
        if( tk == "rightsqbrackettk"):
            tk = lex()
            condition()
            if(tk == "leftsqbrackettk"):
                tk = lex()
            else:
                print( "ERROR : ']' expected after condition "+": line: "+str(line))
                sys.exit()
        else:
            print("ERROR : '[' expected after 'not' keyword "+": line: "+str(line))
            sys.exit()
    elif(tk == "rightsqbrackettk"):
        tk = lex()
        condition()
        if( tk == "leftsqbrackettk"):
            tk = lex()
        else:
            print( "ERROR : ']' expected after condition"+": line: "+str(line))
            sys.exit()
    elif(tk == "truetk"):
        tk = lex()
    elif( tk == "falsetk"):
        tk = lex()
    else:
        expression()
        relationaloper()
        expression()

def expression():
	optionalsign()
	term()
	while(tk == "plustk" or tk == "minustk"):
		addoper()
		term()

def term():
	factor()
	while(tk == "multk" or tk == "divtk"):
		muloper()
		factor()

def factor():
    global tk
    if(tk == "constanttk"):
        tk = lex()
    elif(tk == "rightbrackettk"):
        tk = lex()
        expression()
        if(tk == "leftbrackettk"):
            tk =lex()
        else:
            print("ERROR : ')' expected after expression"+": line: "+str(line))
            sys.exit()
    elif(tk == "idtk"):
        tk = lex()
        idtail()
   

def idtail():
	if(tk == "rightbrackettk"):
		actualpars()

def relationaloper():
    global tk
    
    if(tk == "equaltk" or tk == "lessequaltk" or tk == "moreequaltk" or tk == "lesstk" or tk == "moretk" or tk == "morelesstk"):
        tk = lex()
        
    else:
       print("ERROR: relational operator expected "+": line: "+str(line))
       sys.exit()

def addoper():
    global tk
    if(tk == "plustk" or tk == "minustk"):
        tk = lex()
    else:
        print("ERROR: '+' or '-' expected "+": line: "+str(line))
        sys.exit()

def muloper():
    global tk
    if(tk == "multk" or tk == "divtk"):
        tk = lex()
    else:
        print("ERROR: '*' or '/' expected"+": line: "+str(line))
        sys.exit()
               
def optionalsign():
    global tk
    if(tk == "plustk" or tk == "minustk"):
        tk = lex()
        addoper()


tk = lex()
program()

