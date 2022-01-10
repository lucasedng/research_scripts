Um **reticulado** em _Rn_ é um subgrupo aditivo discreto de _Rn_.

Um __empacotamento esférico__ no _Rn_ é uma reunião de esferas de mesmo raio no _Rn_ de modo que quaisquer duas esferas ou não se interceptam ou se interceptam apenas no bordo, enquanto um __empacotamento reticulado__ no _Rn_ é um empacotamento esférico cujo o conjunto dos centros das esferas forma um reticulado.


Em 1900 o problema de determinar qual é o empacotamento esférico que cobre a maior parte do espaço foi categorizado como um dos problemas de Hilbert, que viria a obter destaque na área de Telecomunicações.

Este repositório contém alguns scripts nas linguagens **Python** e **Wolfram Mathematica** com o intuito de acelerar os calculos e o processo de pesquisa sobre **Empacotamento de Áreas**, **Métricas não euclidianas** e **Reticulados**.
___

> python_codes:
>> equals_isometrics_lattices.py: verifica se dois reticulados gerados por uma isometria são iguais.

>> quadratic_algebraic_lattices_evaluate.py: gera reticulados algébricos a partir de anéis de inteiros.

>> roots_of_unity_lattices_evaluate.py: gera reticulados complexos a partir de raizes primitivas da unidade.

>> lattice_data_schema.py: faz a requisição e converte em um arquivo .json, de forma estrutura, os dados sobre reticulados famosos na literatura. (database: https://bit.ly/3qiOHXj)

>> request_lattices_data.py: a partir dos requests feitos em lattice_data_schema.py, busca e formata de forma estruturada os dados necessários. 

___

>mathematica_codes:
>> create_balls_on_p_metric.nb: dado um número inteiro p, e diversos reticulados, criamos bolas em métricas não euclidianas para obter o raio de empacotamento.

>> making_poly_to_backtracking.nb: utilizando backtacking, procuramos pela melhor estrutura de poliominós.

>> plot_lattices_2d.nb: a partir de um conjunto gerador, faz o plot dos reticulados em duas dimensões e seus limites de empacotamento. 

___

Para saber mais sobre reticulados: 


[Lattice-based cryptography](https://en.wikipedia.org/wiki/Lattice-based_cryptography)

[Introdução à Teoria dos Reticulados e suas Propriedades](https://repositorio.unifesp.br/bitstream/handle/11600/60730/Lucas_Eduardo_Trabalho_de_Graduacao_Final.pdf?sequence=7&isAllowed=y)
