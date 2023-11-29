"""Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja )

além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

- exibir a mensagem: "o {tipo} atacou usando {ataque}")
- aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
se guerreiro -> no ataque exibir (usou espada)
se monge -> no ataque exibir (usou artes marciais)
se ninja -> no ataque exibir (usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada"""

class Heroi():
    def __init__(self):
        self.nome = self.definir_nome()
        self.idade = self.definir_idade()
        self.tipo_heroi = self.definir_tipo()
        self.ataque()

    def definir_nome(self):
        return str(input("Qual o nome do heroi? "))

    def definir_idade(self):
        return int(input("Qual a idade do heroi? "))

    def definir_tipo(self):
        tipos = {
            1: "MAGO",
            2: "Guerreiro",
            3: "Monge",
            4: "Ninja"
        }

        print("[1] MAGO\n[2] Guerreiro\n[3] Monge\n[4] Ninja")
        while True:
            try:
                tipo = int(input("Qual a classe do heroi? "))
                if tipo not in tipos:
                    print("VALOR INVÁLIDO, por favor digite um valor válido")
                    continue
                break
            except (ValueError, TypeError):
                print("VALOR INVÁLIDO, por favor digite um valor válido")
        return tipos[tipo]

    def ataque(self):
        ataques = {
            "MAGO": "magia",
            "Guerreiro": "espada",
            "Monge": "artes marciais",
            "Ninja": "shuriken"
        }

        tipo_heroi = self.tipo_heroi
        ataque_heroi = ataques.get(tipo_heroi, "ataque desconhecido")

        print(f"O {tipo_heroi} atacou usando {ataque_heroi}")

heroi_instancia = Heroi()
