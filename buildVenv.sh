#!/bin/bash

# Script que cria um ambiente virtual para o python, e já instala
# o conteúdo do requirements.txt caso exista.

# Executar este script com o comando:
# source buildVenv.sh
read -p "Voce está executando este script com o comando source? (y/n)" choice

if [[ "$choice" = "y" ]];
then
	python3 -m venv .venv;
	source .venv/bin/activate;
	pip install --upgrade pip;
	if [ -f requirements.txt ]; then
	    pip install -r requirements.txt;
	fi
fi
