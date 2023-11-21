%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}


%token INTEIRO REAL TEXTO ATRIB PARENDIR CHAVEDIR CHAVEESQ VIRGULA PARENESQ
%token SE SENAO PARA ENQUANTO MOSTRE DECLARE PONTOVIRGULA NAO SUB MULT DIV
%token IDENTIFICADOR NUMERO

%left OU E
%left IGUAL DIFERENTE MENOR MAIOR MENOR_IGUAL MAIOR_IGUAL
%left SOMA SUBTRACAO
%left MULTIPLICACAO DIVISAO
%right NEGACAO

%%
programa: 
    | programa declaracao
    ;

declaracao:
      instrucao
    | declaracao_variavel
    ;

declaracao_variavel:
      DECLARE IDENTIFICADOR tipo ';'
    | DECLARE IDENTIFICADOR tipo ATRIB expressao ';'
    ;

tipo: 
      INTEIRO 
    | REAL 
    | TEXTO 
    ;

instrucao:
      instrucao_se
    | instrucao_enquanto
    | instrucao_para
    | instrucao_mostra
    ;

instrucao_se:
      SE expressao '{' lista_instrucoes '}' 
    | SE expressao '{' lista_instrucoes '}' SENAO '{' lista_instrucoes '}'
    ;

instrucao_enquanto:
      ENQUANTO expressao '{' lista_instrucoes '}'
    ;

instrucao_para:
      PARA '(' declaracao_variavel expressao ';' expressao ')' '{' lista_instrucoes '}'
    ;

instrucao_mostra:
      MOSTRE '(' expressao ')' ';'
    ;

lista_instrucoes:
      | lista_instrucoes instrucao
    ;

expressao:
      expressao OU expressao
    | expressao E expressao
    | expressao IGUAL expressao
    | expressao DIFERENTE expressao
    | expressao MENOR expressao
    | expressao MAIOR expressao
    | expressao MENOR_IGUAL expressao
    | expressao MAIOR_IGUAL expressao
    | expressao SOMA expressao
    | expressao SUBTRACAO expressao
    | expressao MULTIPLICACAO expressao
    | expressao DIVISAO expressao
    | NEGACAO expressao
    | '(' expressao ')'
    | NUMERO
    | IDENTIFICADOR
    ;
%%

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;

    /* mensagem de erro exibe o símbolo que causou erro e o número da linha */
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main(int argc, char **argv) {
  yyparse();
  return 0;
}

