# compiladores
Este projeto implementa uma análise léxica e sintática para a linguagem Elgol, com base na biblioteca sly em Python. A linguagem Elgol apresenta palavras-chave, identificadores, operadores aritméticos e estruturas de controle. O projeto inclui uma análise léxica que reconhece tokens específicos da linguagem e gera uma tabela de símbolos com base nos identificadores encontrados no código-fonte.


# Estrutura do Projeto
O projeto é composto por duas classes principais:

- SymbolTable: gerencia a tabela de símbolos, onde cada identificador é armazenado com seu tipo e valor.

- ElgolLexer: Realiza a análise léxica do código-fonte de Elgol, identificando tokens e classificando elementos como identificadores, nomes de função, números e palavras-chave.

# Dependências
- Python 3.8+
- Biblioteca sly: Instale usando pip install sly

# Instalação

1. Nó diretório do código, execute o comando <br>
``` pip install -r requirements.txt ```<br>


2. Caso ocorra algum problema, instale a biblioteca através do seguinte comando <br>  ```pip install sly```

3. Execute o arquivo lex.py <br> ```py lex.py```

4. Para que o analisador léxico avalie um novo código, basta alterar o conteúdo da variável "data", presente no método __main__


#### Nomes: Douglas, Deividi e Yan