#change this input and test

input="""algorithme maximum 
entier a, b, c ; 
debut 
lire a ;// this is a single line comment 
lire b ;
/* hello please ignore all of this
c <- b * b + 4 * a *c 
*/
si a < b alors 
afficher "a est plus petit b" ;
sinon
afficher "a est plus grand b" ; 
finsi 
c <- b * b + 4 * a *c ;
si a != b alors
afficher c;
lire d;
finsi
fin """


from htmlparser import table, headers,get_productions
from grammar_config import grammar
from slrstack import slr_parser
from analex import analysis
import os
productions=get_productions(grammar)
input_str=analysis(input)
input=" ".join(input.split("\n"))
os.system("cls")
print(f"input:\n{input}\nlexical analysis:\n{'-'*100}\n{input_str}\n")
print (headers,input_str,sep="\n")
result=slr_parser(productions,headers,table, input_str)
from prettytable import PrettyTable
mytable=PrettyTable(result[0])
for row in result[1:]:
    mytable.add_row(row)

print(mytable)