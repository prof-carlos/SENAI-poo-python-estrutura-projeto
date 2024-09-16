import os

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa
from models.endereco import Endereco


os.system("cls || clear")

# Instanciando classe.
pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO, 
                  Endereco("Rua A.", 35, UnidadeFederativa.BAHIA))

print(pessoa_1)