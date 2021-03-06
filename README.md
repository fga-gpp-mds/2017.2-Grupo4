
# Classificação de risco na pediatria
  [![Issue Count](https://codeclimate.com/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico/badges/issue_count.svg)](https://codeclimate.com/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico)
  [![Code Climate](https://codeclimate.com/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico/badges/gpa.svg)](https://codeclimate.com/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico)
  [![Coverage Status](https://coveralls.io/repos/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico/badge.svg?branch=master)](https://coveralls.io/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico?branch=master)
  [![Build Status](https://travis-ci.org/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico.svg?branch=master)](https://travis-ci.org/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico)
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

O projeto busca melhorar a eficiência da atual classificação de risco do Hospital Materno-Infantil de Brasília, por meio de sua automatização.

O software terá como função classificar os pacientes em estados imediato,  hospitalar e ambulatorial, recomendando o local mais apropriado para o atendimento, de acordo com os sintomas verificados pelos responsáveis pela triagem.

**CRP** foi desenvolvido inicialmente por estudantes das disciplinas Métodos de Desenvolvimento de Software e Gestão de Portifólio e Projeto de Software, do curso de engenharia de software da Universidade de Brasília Faculdade do Gama.


**Se você deseja contribuir com CRP, leia a nossa [licença](https://github.com/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico/blob/master/LICENSE). Esse projeto está sob a [licença MIT](https://mit-license.org/). Ao contribuir com esse projeto, você estará de acordo com essa licença.**


## Instalação

Para contribuir com o projeto você deve possuir o docker, docker-compose e uma conta no github, após isso clone o projeto.
  - [Download docker](https://docs.docker.com/engine/installation/)
  - [Download docker-compose](https://docs.docker.com/compose/install/)
  - Para instalar o git nos sistemas linux que utilizam o apt-get, utilize o comando:

  ``` sudo apt-get install git ```

  - Para clonar o projeto, utilize o comando

  `git clone      https://github.com/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico.git`

  - Após clonar o projeto entre no diretório pelo comando

  `cd 2017.2-Classificacao-de-Risco-Pediatrico`

  - Construa as imagens do docker pelo comando

  `sudo docker-compose build`

  - Faça as migrações pelo comando

  `sudo docker-compose run web python manage.py makemigrations`

  - Aplique as migrações pelo comando

  `sudo docker-compose run web python manage.py migrate`

  ## Rodando Aplicação

  - Após a realização de todos os passos suba a aplicação pelo comando

  `sudo docker-compose up`

## Como Contribuir

Para contribuir com o projeto basta clonar o repositório através do comando
```shell
git clone https://github.com/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico.git
```
Com isso você poderá contribuir resolvendo issues que estiverem abertas na nossa board do ZenHub. Para finalizar sua contribuição nos envie um Pull Requeste que será avaliado pela nossa equipe.
