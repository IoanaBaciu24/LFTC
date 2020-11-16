from typing import List
from pif import PIF
from symbol_table import SymbolTable, GLOBAL_ID
import re 
from finite_automata import FiniteAutomata


class Scanner:
    def __init__(self, file_path: str, in_lang_separators, tokens_path: str):
        self.file_path = file_path
        self.in_lang_separators = in_lang_separators
        self.tokens = tokens_path
        

    def scan(self, pif: PIF, sym_table_identifiers: SymbolTable, sym_table_constants):
        global GLOBAL_ID
        f = open(self.file_path)
        number = 0
        while True:
            line = f.readline()
            if not line:
                break
            line = line[:-1]
            tokens = self.detect_tokens(line)
            print(tokens)
            for tok in tokens:
                if self.is_reserved_word_or_operator(tok):
                    pif = self.genPif(tok, 0, pif)
                elif self.is_identifier(tok):
                    id = sym_table_identifiers.add_value(tok).id
                    pif = self.genPif(tok, id, pif)
                elif self.is_numerical_constant(tok) or self.is_string_constant(tok) or self.is_boolean_constant(tok):
                    id = sym_table_constants.add_value(tok).id
                    pif = self.genPif(tok, id, pif)                    
                else:
                  
                    raise ValueError('lexical error at line: ' + str(number) + ' from token: ' + tok)
            number+=1
        # if the function returns without any error, it means that the program is lexically correct
        return pif, sym_table_identifiers, sym_table_constants
                    
    def __is_operator(self, tok: str) -> bool:
        f = open(self.in_lang_separators)
        lines = f.read().splitlines()
        if tok  in lines:
            b=True
        else:
            b=False
        f.close()
        return b

    def is_numerical_constant(self, tok):
        # return re.match(r'^(-?\d+\.\d+)$|^(-?\d+)$', tok) is not None
        fa = FiniteAutomata.read_from_file("FAINTS.in")
        return fa.check_sequence(tok)
    
    def is_boolean_constant(self, tok):
        return tok=='TRU' or tok == 'FALS'
    
    def is_string_constant(self,tok):
        return tok[0] == "'" and tok[-1] == "'"
    
    def is_identifier(self, tok):
        # return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', tok) is not None
        fa = FiniteAutomata.read_from_file("FAIDS.in")
        return fa.check_sequence(tok)


    def detect_tokens(self, line: str) -> List[str]:

        toks = []
        word = ''
        i=0
        while i < len(line):
            if line[i] == "'":
                if word!='':
                    toks.append(word)
                word = "'"
                i+=1
                while i<len(line) and line[i]!="'":
                    word+=line[i]
                    i+=1
                if i<len(line):     # this line should complete the string, if possible 
                    word+=line[i]
                    i+=1
            elif line[i] == ' ':
                if word!='':
                    toks.append(word)
                    word = ''
            elif self.__is_operator(line[i]):
                if word != '':
                    toks.append(word)

                if line[i] == "-" and toks[-1] == "<-":
                    word = "-"
                else:
                    if i< len(line)-1 and self.__is_operator(line[i] + line[i+1]):
                        toks.append(line[i] + line[i+1])
                        i=i+1

                    else:
                        toks.append(line[i])
                    word = ''
            else:
                word+=line[i]
            i+=1
        if word!='':
            toks.append(word)
        return toks  

                

                
    def is_operator_separator(self, tok: str) -> bool:
        f = open(self.in_lang_separators)
        lines = f.read().splitlines()
        if tok in lines:
            b=True
        else:
            b=False
        f.close()
        return b


    def is_reserved_word_or_operator(self, tok: str) -> bool:
        f = open(self.tokens)
        lines = f.read().splitlines()
        if tok in lines:
            b=True
        else:
            b=False
        f.close()
        return b        
    

    def genPif(self, tok: str, index: int, pif: PIF):
        
        pif.add(tok,index)
        return pif


def test_scanner():
    #TODO: handle the -number case    

    scanner = Scanner('p1.txt', 'seps.txt', 'tokens.in')
    pif = PIF()
    sym_table_identifiers = SymbolTable('identifiers')
    sym_table_constants = SymbolTable('constants')
    pif, symi, symc = scanner.scan(pif, sym_table_identifiers, sym_table_constants)
    # print(pif)
    print('-------------------PIF START-----------------------------------')
    for elem in pif.data:
        print(elem)

    print('-------------------PIF END-----------------------------------')

    print("Identifiers symbol table")
    print(symi)
    print("Constants symbol table")
    print(symc)


test_scanner()