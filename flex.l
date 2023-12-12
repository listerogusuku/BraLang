%{
#include "braLang.tab.h"

%}

%option yylineno
%option noyywrap


SE              se
SENAO           senao
PARA            para
MOSTRE          mostre
VARIAVEL        variavel
INT             int
REAL            real
STRING          string
PARENESQ        \(
PARENDIR        \)
CHAVEESQ        \{
CHAVEDIR        \}
VIRGULA         ,
PONTOVIRGULA    ;
IGUAL           ==
MAIOR           >
MENOR           <
NAO             !
E               e
OU              ou
SOMA            \+
SUB             \-
MULT            \*
DIV             \/
ATRIB           <-
IDENTIFICADOR   [a-zA-Z_][a-zA-Z0-9_]*
NUMERO          [0-9]+(\.[0-9]+)?

%%

[ \t]                   ; // Ignorar espaços em branco e tabulações

SE                    { return SE; }
SENAO                 { return SENAO; }
PARA                  { return PARA; }
MOSTRE                { return MOSTRE; }
VARIAVEL              { return VARIAVEL; }
INT                   { return INT; }
REAL                  { return REAL; }
STRING                { return STRING; }
PARENESQ              { return PARENESQ; }
PARENDIR              { return PARENDIR; }
CHAVEESQ              { return CHAVEESQ; }
CHAVEDIR              { return CHAVEDIR; }
VIRGULA               { return VIRGULA; }
PONTOVIRGULA          { return PONTOVIRGULA; }
IGUAL                 { return IGUAL; }
MAIOR                 { return MAIOR; }
MENOR                 { return MENOR; }
NAO                   { return NAO; }
E                     { return E; }
OU                    { return OU; }
SOMA                  { return SOMA; }
SUB                   { return SUB; }
MULT                  { return MULT; }
DIV                   { return DIV; }
ATRIB                 { return ATRIB; }
IDENTIFICADOR         { return IDENTIFICADOR; }
NUMERO                { return NUMERO; }

.                       { /* Código para caracteres não reconhecidos */ }
%%