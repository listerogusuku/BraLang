/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_BRALANG_TAB_H_INCLUDED
# define YY_YY_BRALANG_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    INTEIRO = 258,                 /* INTEIRO  */
    REAL = 259,                    /* REAL  */
    TEXTO = 260,                   /* TEXTO  */
    ATRIB = 261,                   /* ATRIB  */
    PARENDIR = 262,                /* PARENDIR  */
    CHAVEDIR = 263,                /* CHAVEDIR  */
    CHAVEESQ = 264,                /* CHAVEESQ  */
    VIRGULA = 265,                 /* VIRGULA  */
    PARENESQ = 266,                /* PARENESQ  */
    SE = 267,                      /* SE  */
    SENAO = 268,                   /* SENAO  */
    PARA = 269,                    /* PARA  */
    ENQUANTO = 270,                /* ENQUANTO  */
    MOSTRE = 271,                  /* MOSTRE  */
    DECLARE = 272,                 /* DECLARE  */
    PONTOVIRGULA = 273,            /* PONTOVIRGULA  */
    NAO = 274,                     /* NAO  */
    SUB = 275,                     /* SUB  */
    MULT = 276,                    /* MULT  */
    DIV = 277,                     /* DIV  */
    IDENTIFICADOR = 278,           /* IDENTIFICADOR  */
    NUMERO = 279,                  /* NUMERO  */
    OU = 280,                      /* OU  */
    E = 281,                       /* E  */
    IGUAL = 282,                   /* IGUAL  */
    DIFERENTE = 283,               /* DIFERENTE  */
    MENOR = 284,                   /* MENOR  */
    MAIOR = 285,                   /* MAIOR  */
    MENOR_IGUAL = 286,             /* MENOR_IGUAL  */
    MAIOR_IGUAL = 287,             /* MAIOR_IGUAL  */
    SOMA = 288,                    /* SOMA  */
    SUBTRACAO = 289,               /* SUBTRACAO  */
    MULTIPLICACAO = 290,           /* MULTIPLICACAO  */
    DIVISAO = 291,                 /* DIVISAO  */
    NEGACAO = 292                  /* NEGACAO  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_BRALANG_TAB_H_INCLUDED  */
