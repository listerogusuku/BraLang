## BraLang

![BraLang](http://insideuniversity.com.br/wp-content/uploads/2023/10/BraLang_background.png)

**BraLang** is a programming language adapted for native Portuguese speakers. It was designed with the aim of providing a more intuitive and culturally relevant approach for programmers and learners who are more comfortable with Portuguese-based keywords and structures. Through BraLang, users can write code using terms like se (if), mostre (print), enquanto (while), and others, making the language especially accessible for beginners or for those seeking a Portuguese alternative to traditional programming languages.


#### EBNF:
``` 
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}" };

STATEMENT = ( λ | ASSIGN | IF | PRINT | WHILE | FOR | DECLARE ), "\n" ;

ASSIGN = IDENTIFIER, "<-", EXPRESSION;

DECLARE = "declare", IDENTIFIER, [TYPE | "<-", EXPRESSION];

PRINT = "mostre", "(", EXPRESSION, ")";

WHILE = "enquanto", EXPRESSION, BLOCK;

FOR = "para", IDENTIFIER, "de", EXPRESSION, "ate", EXPRESSION, [STEP], BLOCK;

STEP = "passo", EXPRESSION;

IF = "se", EXPRESSION, BLOCK, ["senao", BLOCK];

EXPRESSION = TERM, {("ou" | "e"), TERM};

TERM = FACTOR, {("==" | "!=" | ">" | "<" | ">=" | "<="), FACTOR};

FACTOR = ELEMENT, {("+" | "-" | "*" | "/"), ELEMENT};

ELEMENT = (NUMBER | IDENTIFIER | "(" , EXPRESSION , ")" );

TYPE = ("inteiro" | "real" | "texto");

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

NUMBER = DIGIT, { DIGIT }, [".", {DIGIT}];

LETTER = (a | ... | z | A | ... | Z);

DIGIT = (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);
```

#### Example (1) of code in BraLang:
```
declare a inteiro <- 5
declare b inteiro <- 10
declare resultado inteiro

se a > b {
    mostre("a é maior que b")
} senao {
    mostre("b é maior ou igual a a")
}

para i de 1 ate 10 passo 1 {
    mostre(i)
}

enquanto a < 20 {
    a <- a + 1
}

mostre(a)

```

#### Example (2) of code in BraLang:
```
declare base real <- 5.0
declare altura real <- 10.0
declare area real

area <- (base * altura) / 2

mostre("A área do triângulo é: ", area)
```

#### Example (3) of code in BraLang:
```
declare n inteiro <- 5
declare fatorial inteiro <- 1

para i de 1 ate n passo 1 {
    fatorial <- fatorial * i
}

mostre("O fatorial de ", n, " é: ", fatorial)
```
