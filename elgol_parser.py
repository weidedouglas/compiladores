from sly import Lexer, Parser

# ------------------------- LEXER -------------------------
class ElgolLexer(Lexer):
    tokens = {
        IDENT, FUNC_NAME, RESERV, NUMBER, ZERO, COMP, 
        ELGIO, INTEIRO, ENQUANTO, SE, ENTAO, SENAO, 
        INICIO, FIM, MAIOR, MENOR, IGUAL, DIFERENTE,
        PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, DOT, COMMA, EQUAL
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
        'diferente': 'DIFERENTE',
    }

    literals = { '=', '+', '-', 'x', '/', '(', ')', '.' }

    ignore = ' \t'
    ignore_newline = r'\n+'

    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    IDENT = r'[A-Z][a-zA-Z]{2,}'
    FUNC_NAME = r'_([A-Z][a-zA-Z]{2,})'
    NUMBER = r'[1-9][0-9]*'
    ZERO = r'zero'
    COMMA = r','
    EQUAL = r'='

    @_(r'[a-zA-Z]+')
    def RESERV(self, t):
        t.type = self.keywords.get(t.value, 'RESERV')
        return t

    def error(self, t):
        print(f"Erro léxico: Caractere inválido '{t.value[0]}' na linha {self.lineno}")
        self.index += 1

# ------------------------- PARSER -------------------------
class ElgolParser(Parser):
    tokens = ElgolLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    @_('function program')
    def program(self, p):
        pass

    @_('INICIO DOT statements FIM DOT')
    def program(self, p):
        pass

    @_('INTEIRO FUNC_NAME LPAREN param_list RPAREN DOT INICIO DOT statements FIM DOT')
    def function(self, p):
        pass

    @_('INTEIRO IDENT')
    def param_list(self, p):
        pass

    @_('param_list COMMA INTEIRO IDENT')
    def param_list(self, p):
        pass

    @_('INTEIRO IDENT DOT')
    def statement(self, p):
        pass

    @_('IDENT EQUAL expr DOT')
    def statement(self, p):
        pass

    @_('ELGIO EQUAL expr DOT')
    def statement(self, p):
        pass

    @_('SE condition DOT ENTAO DOT block SENAO DOT block')
    def statement(self, p):
        pass

    @_('ENQUANTO condition DOT INICIO DOT statements FIM DOT')
    def statement(self, p):
        pass

    @_('statements statement')
    def statements(self, p):
        pass

    @_('statement')
    def statements(self, p):
        pass

    @_('expr PLUS term', 'expr MINUS term')
    def expr(self, p):
        pass

    @_('term')
    def expr(self, p):
        pass

    @_('term TIMES factor', 'term DIVIDE factor')
    def term(self, p):
        pass

    @_('factor')
    def term(self, p):
        pass

    @_('NUMBER', 'ZERO', 'IDENT')
    def factor(self, p):
        pass

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        pass

    @_('expr COMP expr')
    def condition(self, p):
        pass

    @_('INICIO DOT statements FIM DOT')
    def block(self, p):
        pass

    def error(self, token):
        if token:
            print(f"Erro sintático: Token inesperado '{token.value}' na linha {token.lineno}")
        else:
            print("Erro sintático: EOF inesperado")
        self.errok()

# ------------------------- TESTE -------------------------
if _name_ == '_main_':
    lexer = ElgolLexer()
    parser = ElgolParser()

    test_code = """
        inteiro _Soma (inteiro Num, inteiro Dois) .
        inicio .
            elgio = Num + Dois .
        fim .

        inicio .
            inteiro Variavel .
            Variavel = 10 .
        fim .
    """

    try:
        tokens = lexer.tokenize(test_code)
        parser.parse(tokens)
        print("Análise completa: Código válido.")
    except Exception as e:
        print(f"Erro durante a análise: {e}")