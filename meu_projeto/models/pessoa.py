from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa


class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return (
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.texto}"
                f"\nSexo: {self.sexo.caracter}"
                f"\nEndereço: {self.endereco}"
                )
