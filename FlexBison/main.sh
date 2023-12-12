flex flex.l
bison -d bralang.y
gcc lex.yy.c bralang.tab.c -o bralang
./bralang < teste.bl
rm -rf lex.yy.c bralang.tab.c bralang.tab.h