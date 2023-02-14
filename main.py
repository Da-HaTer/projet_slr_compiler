input="""algorithme maximum 
entier a, b, c; 
debut 
lire a ; 
lire b ;
si a < b alors 
afficher "a est plus petit b" ;
sinon
afficher "a est plus grand b" ; 
finsi 
c <- b * b + 4 * a *c ;
afficher c;
fin """


from htmlparser import table, headers,get_productions
from grammar_config import grammar
from slrstack import slr_parserearn
from analex import analysis
import os
productions=get_productions(grammar)
input_str=analysis(input)
input=" ".join(input.split("\n"))
os.system("cls")
print(f"input:\n{input}\nlexical analysis:\n{'-'*100}\n{input_str}\n")
# print (input_str)
# exit()
result=slr_parser(productions,headers,table, input_str)
from prettytable import PrettyTable
mytable=PrettyTable(result[0])
for row in result[1:]:
    mytable.add_row(row)

print(mytable)