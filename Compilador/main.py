# BraLang | Lógica da Computação 2023.2
# Engenharia de Computação - Insper
# Aluno: Lister Ogusuku Ribeiro
# Professor: Raul Ikeda

import sys
from abc import ABC, abstractmethod
tipo_var = ["int", "string"]

# Classe que representa os elementos individuais encontrados no meu código-fonte:
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Classe que transforma meu código-fonte em uma sequência de tokens, que serão consumidos pelo Parser:
class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None
        self.selectNext()
    
    # Verificador se chegamos ao final do código-fonte:
    def selectNext(self):
        if self.position >= len(self.source):
            self.next = Token("EOF", None)
            return
        
        while self.position < len(self.source) and (self.source[self.position]==" " or self.source[self.position]=='\t'):
            self.position += 1
        
        if self.position >= len(self.source):
            self.next = Token("EOF", None)
            return
        # Verifica se o caractere é um dígito; se for constrói uma sequência de caracteres representando um inteiro;
        # Se for + ou - irá definir como PLUS ou MINUS (como orientado no slide de aula), senão irá indicar uma exceção;
        
        if self.source[self.position].isdigit():
            num_str = ""
            while self.position < len(self.source) and self.source[self.position].isdigit():
                num_str += self.source[self.position]
                self.position += 1

            if (self.position < len(self.source) and 
                self.source[self.position].isspace() and 
                '+' not in self.source and 
                '-' not in self.source and 
                '*' not in self.source and 
                '/' not in self.source
            ):
                raise SyntaxError("Entrada inválida!!!")

            
            cont_rparen = 0
            cont_lparen = 0
            for i in self.source:
                if i == "(":
                    cont_rparen += 1
                if i == ")":
                    cont_lparen += 1


            if cont_rparen != cont_lparen:
                raise SyntaxError("Conjunto de pareteses inválido!!!")
        
            self.next = Token("NUMBER", int(num_str))

        elif self.source[self.position] == '"':
            string = ""
            self.position+=1
            while self.position<len(self.source) and (self.source[self.position] != '"'):
                string+=self.source[self.position]
                self.position+=1
            self.position+=1
            if self.source[self.position-1] != '"':
                raise ValueError('Erro: faltou fechar as aspas')
            self.next = Token("STRING", string)

        elif self.source[self.position].isalpha():
            ident_str = ""
            while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                ident_str += self.source[self.position]
                self.position += 1
            
            if ident_str == "mostre":
                self.next = Token("PRINT", "Println")
            elif ident_str == 'para':
                self.next = Token('FOR', "for")
            elif ident_str == 'se':
                self.next = Token('IF', "if")
            elif ident_str == 'senao':
                self.next = Token('ELSE', "else")
            elif ident_str == 'guarde':
                self.next = Token('INPUT', "Scanln")
            elif ident_str == 'variavel':
                self.next = Token('VARIABLE', "var")
            elif ident_str == 'int' or ident_str == 'string':
                self.next = Token('TIPO', ident_str)
            else:
                self.next = Token("IDENTIFIER", ident_str)

        # elif self.source[self.position].isalpha():
        #     ident_str = ""
        #     while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
        #         ident_str += self.source[self.position]
        #         self.position += 1

        #     if ident_str == "Println":
        #         self.next = Token("PRINT", None)
        #     else:
        #         self.next = Token("IDENTIFIER", ident_str)
        elif self.source[self.position] == "+":
            self.next = Token("PLUS", None)
            self.position += 1
        elif self.source[self.position] == "-":
            self.next = Token("MINUS", None)
            self.position += 1
        elif self.source[self.position] == "/":
            self.next = Token("DIV", None)
            self.position += 1
        elif self.source[self.position] == "*":
            self.next = Token("MULT", None)
            self.position += 1
        elif self.source[self.position] == ")":
            self.next = Token("RPAREN", None)
            self.position += 1
        elif self.source[self.position] == "(":
            self.next = Token("LPAREN", None)
            self.position += 1
        elif self.source[self.position] == "\n":
            self.next = Token("LINEBREAK", None)
            self.position += 1
        elif self.source[self.position] == '=':
            if self.source[self.position+1] == '=':
                self.next = Token("EQUALCOMPARE", "==")
                self.position+=2
            else:
                self.next = Token("EQUAL", "=")
                self.position+=1
        elif self.source[self.position] == '!':
            self.next = Token("NOT", "!")
            self.position+=1
        elif self.source[self.position] == '>':
            self.next = Token("MAIOR", ">")
            self.position+=1
        elif self.source[self.position] == '<':
            self.next = Token("MENOR", "<")
            self.position+=1
        elif self.source[self.position] == ';':
            self.next = Token("FINAL", ";")
            self.position+=1
        elif self.source[self.position] == '{':
            self.next = Token("LKEY", "{")
            self.position+=1
        elif self.source[self.position] == '}':
            self.next = Token("RKEY", "}")
            self.position+=1
        elif self.source[self.position] == '|':
            self.next = Token("OR", "||")
            self.position+=2
        elif self.source[self.position] == '&':
            self.next = Token("AND", "&&")
            self.position+=2
        elif self.source[self.position] == '.':
            self.next = Token("CONCATENATION", '.')
            self.position+=1
        else:
            raise SyntaxError("Caracter inválido!!!")


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def get(self, name):
        return self.symbols.get(name, None)

    def set(self, name, value, type_value=None):
        self.symbols[name] = (value, type_value)
    
    def create(self, name, value, type_value=None):
        if name in self.symbols:
            raise ValueError(f"Variável '{name}' já existe.")
        else:
            self.symbols[name] = (value, type_value)


class Node(ABC):
    def __init__(self):
        self.value = None
        self.children = []

    @abstractmethod
    def Evaluate(self):
        pass
    
class Print(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table):
        print(self.children[0].Evaluate(symbol_table)[0])
    
class Block(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table):
        for node in self.children:
            node.Evaluate(symbol_table)

class InputOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table):
        return (int(input()), tipo_var[0])

class AssigmentOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table):
        result = self.children[1].Evaluate(symbol_table)
        if type(self.children[1]) is InputOp and symbol_table.get(self.children[0].value)[1] == tipo_var[1]:
            raise ValueError("Erro: Scanln() nao pode ser string")
        return symbol_table.set(self.children[0].value, result[0], result[1])

class VarOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table):
        return symbol_table.get(self.value)
    
class ForOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table):
        self.children[0].Evaluate(symbol_table)
        while(self.children[1].Evaluate(symbol_table)[0]):
            self.children[3].Evaluate(symbol_table)
            self.children[2].Evaluate(symbol_table)

class IfOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table):
        if self.children[0].Evaluate(symbol_table):
            self.children[1].Evaluate(symbol_table)
        else:
            if(len(self.children)>2):
                self.children[2].Evaluate(symbol_table)

class BinOp(Node):
    def __init__(self, left, operator, right):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right

    def Evaluate(self, symbol_table):

        if self.operator in ['+', '-', '*', '/']:
            if self.left.Evaluate(symbol_table)[1] != tipo_var[0] or self.right.Evaluate(symbol_table)[1] !=  tipo_var[0]:
                raise ValueError(f"Erro: {self.value}")
            if self.operator == '+':
                return (self.left.Evaluate(symbol_table)[0] + self.right.Evaluate(symbol_table)[0], tipo_var[0])
            elif self.operator == '-':
                return (self.left.Evaluate(symbol_table)[0] - self.right.Evaluate(symbol_table)[0], tipo_var[0])
            elif self.operator == '*':
                return (self.left.Evaluate(symbol_table)[0] * self.right.Evaluate(symbol_table)[0], tipo_var[0])
            elif self.operator == '/':
                return (self.left.Evaluate(symbol_table)[0] // self.right.Evaluate(symbol_table)[0], tipo_var[0])
        elif self.operator in ['>', '<', '=']:
            if self.left.Evaluate(symbol_table)[1] != self.right.Evaluate(symbol_table)[1]:
                raise ValueError("Erro: tipos diferentes")
            if self.left.Evaluate(symbol_table)[1] not in tipo_var:
                raise ValueError(f"Erro: {self.left.Evaluate(symbol_table)[1]}")
            if self.operator == '=':
                return (int(self.left.Evaluate(symbol_table)[0] == self.right.Evaluate(symbol_table)[0]), tipo_var[0])
            elif self.operator == '<':
                return (int(self.left.Evaluate(symbol_table)[0] < self.right.Evaluate(symbol_table)[0]), tipo_var[0])
            elif self.operator == '>':
                return (int(self.left.Evaluate(symbol_table)[0] > self.right.Evaluate(symbol_table)[0]), tipo_var[0])
        elif self.operator in ['|', '&']:
            if self.left.Evaluate(symbol_table)[1] != tipo_var[0] or self.right.Evaluate(symbol_table)[1] != tipo_var[0]:
                raise ValueError(f"Erro: {self.value}")
            if self.operator == '&':
                return (self.left.Evaluate(symbol_table)[0] and self.right.Evaluate(symbol_table)[0], tipo_var[0])
            elif self.operator == '|':
                return (self.left.Evaluate(symbol_table)[0] or self.right.Evaluate(symbol_table)[0], tipo_var[0])
        elif self.operator in ['.']:
            return (f'{str(self.left.Evaluate(symbol_table)[0])}{str(self.right.Evaluate(symbol_table)[0])}', tipo_var[1])
        else:
            raise ValueError("Operador inválido")

class UnOp(Node):
    def __init__(self, operator, operand):
        super().__init__()
        self.operator = operator
        self.operand = operand

    def Evaluate(self, symbol_table):
        valor_operand = self.operand.Evaluate(symbol_table)[0]
        if self.operator == '-':
            return (-valor_operand, tipo_var[0])
        elif self.operator=='+':
            return (valor_operand, tipo_var[0])
        elif self.operator=='!':
            return (not valor_operand, tipo_var[0])
        else:
            raise ValueError("Operador unário inválido")

class IntVal(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def Evaluate(self, symbol_table):
        return (self.value, tipo_var[0])

class StrVal(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def Evaluate(self, symbol_table):
        return (self.value, tipo_var[0])
    
class NoOp(Node):
    def Evaluate(self, symbol_table):
        return None  
    
class VarDec(Node):
    def __init__(self, value, children):
        super().__init__()    
        self.value = value
        self.children = children 
    
    def Evaluate(self, symbol_table):
        if len(self.children) > 1:
            symbol_table.set(self.children[0].value,  self.children[1].Evaluate(symbol_table)[0],  self.children[1].Evaluate(symbol_table)[1])
        else:
            symbol_table.create(self.children[0].value,  None,  self.value)

# Classe que interpreta os tokens gerados pelo Tokenizer e realiza as operações:
class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    @staticmethod
    def parseTerm(tokenizer):
        result = Parser.parseFactor(tokenizer)  # Começa analisando o primeiro termo

        while tokenizer.next.type in ["DIV", "MULT"]:
            op = tokenizer.next
            tokenizer.selectNext()

            if op.type == "DIV":
                result = BinOp(result, "/",Parser.parseFactor(tokenizer))
            else:  # op.type == "MINUS"
                result = BinOp(result, "*",Parser.parseFactor(tokenizer))
        return result
    
    @staticmethod
    def parseExpression(tokenizer):
        result = Parser.parseTerm(tokenizer)  # Começa analisando o primeiro termo

        while tokenizer.next.type in ["PLUS", "MINUS", "CONCATENATION"]:
            op = tokenizer.next
            tokenizer.selectNext()

            if op.type == "PLUS":
                result = BinOp(result, "+",Parser.parseTerm(tokenizer))
            elif op.type == 'CONCATENATION':
                result = BinOp(result, '.', Parser.parseTerm(tokenizer))
            else:  # op.type == "MINUS"
                result = BinOp(result, "-",Parser.parseTerm(tokenizer))

        return result
    
    @staticmethod
    def parseAssign(tokenizer):
        if tokenizer.next.type == "IDENTIFIER":
            name = VarOp(tokenizer.next.value, [])
            tokenizer.selectNext()
            
            if tokenizer.next.type != "EQUAL":
                raise SyntaxError("Expected '=' after identifier")
                
            tokenizer.selectNext()
            expr = Parser.boolExpression(tokenizer)
            return AssigmentOp("=", [name, expr])
        
    @staticmethod
    def parseStatement(tokenizer):
        if tokenizer.next.type == "IDENTIFIER":
            name = VarOp(tokenizer.next.value,[])
            tokenizer.selectNext()
            
            if tokenizer.next.type != "EQUAL":
                raise SyntaxError("Expected '=' after identifier")
                
            tokenizer.selectNext()
            expr = Parser.parseExpression(tokenizer)
            return AssigmentOp("=", [name, expr])
        elif tokenizer.next.type == "PRINT":
            tokenizer.selectNext()
            if tokenizer.next.type != "LPAREN":
                raise SyntaxError("Expected '(' after 'println'")
            tokenizer.selectNext()
            expr = Parser.boolExpression(tokenizer)
            if tokenizer.next.type != "RPAREN":
                raise SyntaxError("Expected ')' after expression")
            tokenizer.selectNext()
            return Print("Println", [expr])
        elif tokenizer.next.type == 'IF':
            tokenizer.selectNext()  
            condicao = Parser.boolExpression(tokenizer)
            block = Parser.parseBlock(tokenizer)
            if tokenizer.next.type == 'ELSE':
                tokenizer.selectNext()  
                return IfOp("senao", [condicao, block, Parser.parseBlock(tokenizer)])
            else:
                tokenizer.selectNext()  
                return IfOp("se", [condicao, block])
        elif tokenizer.next.type == 'FOR':
            tokenizer.selectNext()
            assign = Parser.parseAssign(tokenizer)
            if tokenizer.next.type == 'FINAL':
                tokenizer.selectNext()
                expression = Parser.boolExpression(tokenizer)
                if tokenizer.next.type != 'FINAL':
                    raise ValueError(f"erro {tokenizer.next.type}")
                tokenizer.selectNext()
                return ForOp("for", [assign, expression, Parser.parseAssign(tokenizer), Parser.parseBlock(tokenizer)])
            else:
                raise ValueError(f"erro {tokenizer.next.type}")
        elif tokenizer.next.type=='VARIABLE':
            tokenizer.selectNext()
            if tokenizer.next.type!="IDENTIFIER":
                raise ValueError(f"Erro: tipo {tokenizer.next.type}")
            ident=VarOp(tokenizer.next.value,[])
            tokenizer.selectNext()
            if tokenizer.next.type !="TIPO":
                raise ValueError(f"Erro: tipo {tokenizer.next.type}")
            type_value=tokenizer.next.value
            tokenizer.selectNext()
            if tokenizer.next.type=="EQUAL":
                tokenizer.selectNext()
                return VarDec(type_value,[ident,Parser.boolExpression(tokenizer)])
            else:
                return VarDec(type_value,[ident])
        if tokenizer.next.type in ("LINEBREAK", "EOF"):
            tokenizer.selectNext()
            return NoOp()
        else:
            return Parser.parseExpression(tokenizer)

    @staticmethod
    def parseFactor(tokenizer):
        if tokenizer.next.type == "NUMBER":
            result = IntVal(tokenizer.next.value)
            tokenizer.selectNext()
        elif tokenizer.next.type == "STRING": 
            result = StrVal(tokenizer.next.value)
            tokenizer.selectNext()
        elif tokenizer.next.type == "IDENTIFIER":
            name = VarOp(tokenizer.next.value,[])
            tokenizer.selectNext()
            return name
        elif tokenizer.next.type == "PLUS":
            tokenizer.selectNext()
            result = Parser.parseFactor(tokenizer)
        elif tokenizer.next.type == "MINUS":
            tokenizer.selectNext()
            result = UnOp('-',Parser.parseFactor(tokenizer))
        elif tokenizer.next.type == "NOT":
            tokenizer.selectNext()
            result = UnOp('!',Parser.parseFactor(tokenizer))
        elif tokenizer.next.type == "LPAREN":
            tokenizer.selectNext()
            expr = Parser.boolExpression(tokenizer)
            if tokenizer.next.type != "RPAREN":
                raise SyntaxError(f"Expected ')' but got '{tokenizer.next.value}' of type '{tokenizer.next.type}'")
            tokenizer.selectNext()
            return expr
        elif tokenizer.next.type == 'INPUT':
            tokenizer.selectNext()
            if tokenizer.next.type == 'LPAREN':
                tokenizer.selectNext()
                if tokenizer.next.type != 'RPAREN':
                    raise ValueError("Fechar parenteses do Scanf")
                tokenizer.selectNext()
                return InputOp("Scanln",[])                    
        else:
            raise SyntaxError(f"Invalid factor: got '{tokenizer.next.value}' of type '{tokenizer.next.type}'")

        return result
    
    @staticmethod
    def relExpression(tokenizer):
        result = Parser.parseExpression(tokenizer)

        while tokenizer.next.type in ('EQUALCOMPARE', 'MAIOR','MENOR'):
            operator = tokenizer.next.type
            tokenizer.selectNext()
            rel_expression = Parser.parseExpression(tokenizer)
            if operator == 'EQUALCOMPARE':
                result = BinOp(result, '=', rel_expression)
            elif operator=='MAIOR':
                result = BinOp(result, '>', rel_expression)
            elif operator=='MENOR':
                result=BinOp(result, '<', rel_expression)
        return result
    
    @staticmethod
    def boolTerm(tokenizer):
        result=Parser.relExpression(tokenizer)
        while tokenizer.next.type in ('AND'):
            operator=tokenizer.next.type
            tokenizer.selectNext()
            bool_Term=Parser.relExpression(tokenizer)
            if operator =='AND':
                result=BinOp(result, '&', bool_Term)
        return result

    @staticmethod
    def boolExpression(tokenizer):
        result=Parser.boolTerm(tokenizer)
        while tokenizer.next.type in ('OR'):
            operator=tokenizer.next.type
            tokenizer.selectNext()
            bool_Expression=Parser.boolTerm(tokenizer)
            if operator =='OR':
                result=BinOp(result, '|', bool_Expression)
        return result

    @staticmethod
    def parseBlock(tokenizer):
        statements = []
        if tokenizer.next.type != 'LKEY':
            raise ValueError(f"Erro de sintaxe: {tokenizer.next.type}")
        tokenizer.selectNext()
        if tokenizer.next.type != 'LINEBREAK':
            raise ValueError(f"Erro de sintaxe: {tokenizer.next.type}")
        tokenizer.selectNext()
        while tokenizer.next.type != 'RKEY':
            statement = Parser.parseStatement(tokenizer)
            statements.append(statement)
        tokenizer.selectNext()
        return Block(None, statements)
        
    @staticmethod
    def parseProgram(string):
        tokenizer = Tokenizer(string)
        statements = []
        while tokenizer.next.type != "EOF":
            statements.append(Parser.parseStatement(tokenizer))
        return Block("Block", statements)
    
    @staticmethod
    def run(code):
        result = Parser.parseProgram(code)
        return result


class PrePro:
    @staticmethod
    def filter(code):
        result = ""
        i = 0
        while i < len(code):
            # Se encontrarmos "//", ignore tudo até a próxima linha
            if code[i:i+2] == "//":
                while i < len(code) and code[i] != '\n':
                    i += 1
                continue

            # Se encontrarmos "/*", ignore tudo até "*/"
            elif code[i:i+2] == "/*":
                while i < len(code) - 1 and (code[i] != '*' or code[i+1] != '/'):
                    i += 1
                i += 2
                continue

            # Caso contrário, adicione o caractere atual ao resultado
            result += code[i]
            i += 1

        return result



if __name__ == "__main__":
    symbol_table = SymbolTable()
    recebo = sys.argv[1]
    with open(recebo, "r") as file:
        recebo = file.read()
    recebo = PrePro.filter(recebo)
    asts = Parser.run(recebo)
    result = asts.Evaluate(symbol_table)