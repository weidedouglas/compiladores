from sly import Lexer

class SymbolTable:
    def __init__(self):
        # Armazena os símbolos em um dicionário com o nome do símbolo como chave
        self.symbols = {}

    def add_symbol(self, name, symbol_type, value=None):
        # Vai adicionar o simbolo apenas se ele ainda não estiver na tabela
        if name not in self.symbols:
            self.symbols[name] = {
                'type': symbol_type,
                'value': value
            }
            """
            prints adicionados pra debug
            print(f"Símbolo adicionado: {name}, Tipo: {symbol_type}, Valor: {value}")
        #else:
            #print(f"Símbolo '{name}' já está na tabela.")
        """
    def get_symbol(self, name):
        # Vai Retornar o símbolo se ele existir na tabela
        return self.symbols.get(name, None)

    def __str__(self):
        # Mostra a tabela de Simbolos
        return '\n'.join(f"{name}: {info}" for name, info in self.symbols.items())

class ElgolLexer(Lexer):
    tokens = {
        IDENT, FUNC_NAME, RESERV, NUMBER, ZERO, COMP,
        ELGIO, INTEIRO, ENQUANTO, SE, ENTAO, SENAO, INICIO, FIM,
        MAIOR, MENOR, IGUAL, DIFERENTE,
        PLUS, MINUS, TIMES, DIVIDE,
        LPAREN, RPAREN, DOT
    }
    
    keywords = {
        'elgio': 'ELGIO',
        'inteiro': 'INTEIRO',
        'zero': 'ZERO',
        'comp': 'COMP',
        'enquanto': 'ENQUANTO',
        'se': 'SE',
        'entao': 'ENTAO',
        'senao': 'SENAO',
        'inicio': 'INICIO',
        'fim': 'FIM',
        'maior': 'MAIOR',
        'menor': 'MENOR',
        'igual': 'IGUAL',
        'diferente': 'DIFERENTE'
    }

    literals = { '=', '+', '-', 'x', '/', '(', ')', '.' }

    # Inicializa a tabela de símbolos
    def __init__(self):
        super().__init__()
        self.symbol_table = SymbolTable()
    
    # Identificador 
    @_(r'[A-Z][a-zA-Z]{2,}')
    def IDENT(self, t):
        t.type = 'IDENT'
        self.symbol_table.add_symbol(t.value, 'IDENT')
        return t
    
    # Palavra Reservada 
    @_(r'[a-zA-Z]+')
    def RESERV(self, t):
        # Verifica se o valor do token é uma palavra reservada
        if t.value in self.keywords:
            t.type = self.keywords[t.value]
            self.symbol_table.add_symbol(t.value, 'RESERV')
        return t
    
    # Nome de função Começa com _ 
    @_(r'_([A-Z][a-zA-Z]{2,})')
    def FUNC_NAME(self, t):
        self.symbol_table.add_symbol(t.value, 'FUNC_NAME')
        return t
    
    # Números inteiros
    @_(r'[1-9][0-9]*')
    def NUMBER(self, t):
        t.value = int(t.value)
        self.symbol_table.add_symbol(t.value, 'NUMBER', t.value)
        return t

    # Ignora linhas que começam com #
    @_(r'#.*')
    def COMMENT(self, t):
        pass   
    
    # Operadores aritméticos
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'x' # Elgol usa x no lugar de *
    DIVIDE  = r'/'
    
    # Parênteses e ponto final 
    LPAREN  = r'\('
    RPAREN  = r'\)'
    DOT     = r'\.'
    
    ignore = ' \t'
    ignore_newline = r'\n+'

    def error(self, t):
        print(f"Erro léxico: Caractere não reconhecido '{t.value[0]}' na linha {self.lineno}")
        self.index += 1

# Exemplo de teste
if __name__ == '__main__':
    lexer = ElgolLexer()
    data = '''
inteiro _Soma (inteiro Num, inteiro Dois) .
inicio .
    elgio = Num + Dois .
fim .

inteiro Lixo . # minha variável
inteiro Teste .
inteiro Vi     
Lixo = 34 .
comp Lixo .
se Lixo maior zero .
entao.
inicio.
        Lixo = zero .
        Teste = 300 
        Resultado = _Soma (Lixo, Teste) .
fim.
    '''
    print("\n---------------------- LISTA DE TOKENS: ----------------------\n")
    for tok in lexer.tokenize(data):
        print(tok)
    print("\n---------------------- FIM DA LISTA DE TOKENS: ---------------\n")

    # Exibe a tabela de símbolos ao final
    print("\n---------------------- TABELA DE SÍMBOLOS: -------------------\n")
    print(lexer.symbol_table)
    print("\n---------------------- FIM DA TABELA DE SÍMBOLOS: ------------\n")