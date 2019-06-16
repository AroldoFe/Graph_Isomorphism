# Graph_Isomorphism

Este repositório contém os arquivos correspondentes ao trabalho da terceira unidade da disciplina DIM0549 - Grafos, ofertada para o Bacheralado em Tecnlogia de Informação(BTI) na Universidade Federal do Rio Grande do Norte(UFRN).

## Objetivo

O presente trabalho possui o objetivo de comparar estruturas químicas, representadas através de grafos, de modo a avaliar se elas possivelmente são isomorfas ou não.

## Instruções para o algoritmo da pasta codes

O projeto foi desenvolvido considerando-se que será executado em ambiente Linux.

1. Para executar o projeto é necessário que o python 3 esteja instalado em sua máquina. Você pode checar a versão do python3 de sua máquina abrindo o terminal e digitando:
```bash
$ python3 --version
```
2. Caso não possua o python3, a instalação pode ser feita facilmente através de linha do comando de acordo com a versão do seu sistema operacional.

- Ubuntu 17.10 e 18.04: Possuem o Python 3.6 por padrão.

- Ubuntu 16.10 e 17.04: O Python 3.6 pode ser instalado através das seguintes linhas de comando
```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```

- Ubuntu 14.04 ou 16.04: O Python 3.6 pode ser instalado através das seguintes linhas de comando
```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
```

Obs: Devido as atualizações nos sistemas operacionais, as instruções para instalação do python 3 podem ter mudado. Caso enfrente algum problema para executar o programa ou instalar o python 3, por favor entrar em contato através do e-mail gabriel.igorq@gmail.com.

3. Agora com o python 3 devidamente instalado, entre no repositório do projeto através do terminal e insira os seguintes comandos:
```bash
$ cd codes/
```
4. Dentro da pasta dos códigos, basta executar o programa. Entretanto, dependendo da sua versão do sistema operacional, a execução pode ser feita de duas formas. Logo, basta testar e ver qual das formas funciona.
```bash
$ python3 main.py
```
Ou:
```bash
$ python3.6 main.py
```

## Instruções para o algoritmo da pasta adjacency

O algoritmo da pasta adjacency além de exigir o python 3 (seguindo os mesmo passos da seção anterior), ele também necessita da instalação do numpy

1. Para instalar o numpy, digite primeiramente no terminal:
```bash
$ sudo apt install python3-pip
$ pip3 install numpy
```

2. Com o numpy instalado, basta entrar na pasta adjacency com o comando:
```bash
$ cd adjacency/
```

3. Dentro da pasta 'adjacency' basta executar o programa. Entretanto, dependendo da sua versão do sistema operacional, a execução pode ser feita de duas formas. Logo, basta testar e ver qual das formas funciona.
```bash
$ python3 main.py
```
Ou:
```bash
$ python3.6 main.py
```

## Observações

1. Medidas para impedir ou corrigir o usuário caso informações erradas sejam inseridas pelo usuário, não foram implementadas. Logo, é natural que caso erre a escrita de um arquivo, erros sejam apresentados no terminal. Basta digitar nomes de arquivos existentes na pasta "compostos" que o programa irá executar normalmente.

2. Como caso de teste inicial, para a pasta codes, é sugerido utilizar os arquivo dos compostos "metano.txt" e "silano.txt", que são mais simples, para facilitar o entendimento do funcionamento do programa. Em seguida, testar os arquivos "etano.txt" e "metilsilano.txt".


## Autores

Projeto desenvolvido pelos alunos:

- Aroldo Felix (junioraroldo37@gmail.com)
- Gabriel Igor (gabriel.igorq@gmail.com)
