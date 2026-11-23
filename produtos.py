"""
Semana 1 — Modelando produtos (Orientação a Objetos)

Complete os trechos marcados com TODO.
Não altere os nomes das classes, métodos e constantes: a correção é automática.
"""

ALIQUOTA_PADRAO = 0.25  # alíquota padrão hipotética (IBS + CBS)


class Produto:
    """Classe base de todos os produtos do supermercado."""

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        # DONE: atribua o preço usando a property (self.preco = preco),
        #       para que a validação do setter também valha na criação.

    @property
    def preco(self) -> float:
        """Preço do produto SEM imposto."""
        return self._preco
        # DONE: retorne o atributo protegido (ex.: self._preco)

    @preco.setter
    def preco(self, valor: float) -> None:
        if (valor < 0.0):
            raise ValueError('valor inadequado')
        else:
            self._preco = valor
        # DONE: lance ValueError se o valor for negativo;
        #       caso contrário, guarde em self._preco

    def aliquota(self) -> float:
        """Cada subclasse define sua própria alíquota."""
        raise NotImplementedError
        # DONE: lance NotImplementedError (a classe base não tem alíquota)

    def imposto(self) -> float:
        """Imposto de UMA unidade: round(preco * aliquota, 2)."""
        return round(self.preco * self.aliquota(), 2)
        # DONE
        

    def preco_final(self) -> float:
        """Preço + imposto, arredondado em 2 casas."""
        return round(self.preco + self.imposto(), 2)
        # DONE

    def __str__(self) -> str:
        """Formato: 'Arroz 5kg - R$ 25.90 (imposto: R$ 0.00)'"""
        return (f"{self.nome} - R$ {self.preco:.2f} (imposto: R$ {self.imposto():.2f})")
        # DONE: use f-string com :.2f



class ProdutoCestaBasica(Produto):
    """Item da Cesta Básica Nacional: alíquota zero."""
    def aliquota(self):
        return 0.0
    # DONE: sobrescreva aliquota() retornando 0.0


class ProdutoReduzido(Produto):
    """Alimento com redução de 60%: paga 40% da alíquota padrão."""
    def aliquota(self):
        return ALIQUOTA_PADRAO * 0.4
    # DONE: sobrescreva aliquota() usando ALIQUOTA_PADRAO


class ProdutoPadrao(Produto):
    """Produto sem benefício: paga a alíquota padrão."""
    def aliquota(self):
        return ALIQUOTA_PADRAO
    # DONE: sobrescreva aliquota() retornando ALIQUOTA_PADRAO


if __name__ == "__main__":
    # Área livre para testes manuais
    arroz = ProdutoCestaBasica("Arroz 5kg", 25.9)
    refri = ProdutoPadrao("Refrigerante 2L", 9.00)
    print(arroz)
    print(refri)
