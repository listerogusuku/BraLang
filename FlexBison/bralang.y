%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}


%token INT REAL STRING ATRIB PARENDIR CHAVEDIR CHAVEESQ VIRGULA PARENESQ
%token SE SENAO PARA MOSTRE VARIAVEL PONTOVIRGULA NAO SUB MULT DIV
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
      VARIAVEL IDENTIFICADOR tipo ';'
    | VARIAVEL IDENTIFICADOR tipo ATRIB expressao ';'
    ;

tipo: 
      INT 
    | REAL 
    | STRING 
    ;

instrucao:
      instrucao_se
    | instrucao_para
    | instrucao_mostre
    ;

instrucao_se:
      SE expressao '{' lista_instrucoes '}' 
    | SE expressao '{' lista_instrucoes '}' SENAO '{' lista_instrucoes '}'
    ;

instrucao_para:
      PARA '(' declaracao_variavel expressao ';' expressao ')' '{' lista_instrucoes '}'
    ;

instrucao_mostre:
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

