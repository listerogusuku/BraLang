## BraLang

![BraLang](./Brand/BraLang_background.png)

**BraLang** é uma linguagem de programação adaptada para falantes nativos do português, sobretudo **estudantes de escolas públicas, os quais historicamente possuem acesso precário ou ineficiente à língua inglesa e encontram nisso um obstáculo no aprendizado de programação.** A **BraLang** ataca justamente essa dor e foi projetada com o objetivo de quebrar a barreira linguística, visando fornecer uma abordagem mais intuitiva e culturalmente relevante para estudantes e educadores que se sentem mais confortáveis com palavras-chave e estruturas baseadas no português.

A apresentação completa da BraLang no formato .pdf está disponível na raiz deste repositório, no arquivo ["Apresentacao_BraLang.pdf"](https://github.com/listerogusuku/BraLang/blob/main/Apresentacao_BraLang.pdf)

#### EBNF:

```
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}" };

STATEMENT = ( λ | ASSIGNMENT  | IF_STATEMENT | PRINT | FOR | COMMENT ), "\n" ;

ASSIGN = IDENTIFIER, "=", EXPRESSION;

PRINT = "mostre", "(", EXPRESSION, ")";

FOR = "para", IDENTIFIER, EXPRESSION, EXPRESSION, BLOCK;

IF = "se", EXPRESSION, BLOCK, ["senao", BLOCK];

EXPRESSION = TERM, {("+" | "-" ), TERM};

TERM = FACTOR, {("==" | "!=" | ">" | "<" | ">=" | "<="), FACTOR};

FACTOR = (("+" | "-" | "!" | "*" | "/"), FACTOR | DIGIT | "(", EXPRESSION, ")" | IDENTIFIER);

TYPE = ("int" | "string");

COMMENT = "//", { Any valid character }, "\n";

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

NUMBER = DIGIT, { DIGIT }, [".", {DIGIT}];

LETTER = ( "a" | ... | "z" | "A" | ... | "Z" );

DIGIT = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );

```

#### Exemplo (1) de código escrito em BraLang:

```
variavel y int = 2
variavel z int
z = (y == 2)   // comparação booleana
mostre(y+z)    // 3
mostre(y-z)    // 1
mostre(y*z)    // 2
mostre(y/z)    // 2
mostre(y == z) // 0
mostre(y < z)  // 0
mostre(y > z)  // 1
```

#### Exemplo (2) de código escrito em BraLang:

```
mostre("- - - BraLang - - -")
mostre("Olá, tudo bem?")
mostre("Para mostrar algo na tela, utilize o mostre()")
mostre("- - - BraLang - - -")

```

#### Exemplo (3) de código escrito em BraLang:

```
variavel x int = 0
variavel y int = 2
para x = 0; x < 5 && y == 2; x = x + 1 {
    mostre("Ola!")
}
mostre("Você chegou ao fim do seu programa BraLang!!")
```

#### Exemplo (4) de código escrito em BraLang:

```
variavel x_1 int = 3

se (x_1 > 1 && !!!(x_1 < 1)) || x_1 == 3 {
    x_1 = 2
    mostre(x_1)
} senao {
    mostre(x_1+1)
}

mostre("Fim!")
```

#### Exemplo (5) de código escrito em BraLang:

```
variavel a string
variavel b string
variavel x_1 int = 1

x_1 = 1
y = 1
z = 2
a = "abc"
b = "defg"
mostre(a.b) //concatenacao
mostre(a.x_1)
mostre(x_1.a)
mostre(y.z)
mostre(a.(x_1==1))
mostre(a == a)
mostre(a < b)
mostre(a > b)
```

## Testando a linguagem:

### Flex & Bison:
```
sudo apt install flex
sudo apt install bison
git clone https://github.com/listerogusuku/BraLang
cd BraLang/
./main.sh
```

### Compilador:
cd Compilador
python main.py main.bl