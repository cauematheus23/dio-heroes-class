class Heroi {
    constructor() {
        this.nome = this.definirNome();
        this.idade = this.definirIdade();
        this.tipoHeroi = this.definirTipo();
        this.ataque();
    }

    definirNome() {
        return prompt("Qual o nome do heroi?");
    }

    definirIdade() {
        return parseInt(prompt("Qual a idade do heroi?"));
    }

    definirTipo() {
        const tipos = {
            1: "MAGO",
            2: "Guerreiro",
            3: "Monge",
            4: "Ninja"
        };

        alert("[1] MAGO\n[2] Guerreiro\n[3] Monge\n[4] Ninja");

        while (true) {
            try {
                const tipo = parseInt(prompt("Qual a classe do heroi?"));
                if (!(tipo in tipos)) {
                    alert("VALOR INVÁLIDO, por favor digite um valor válido");
                    continue;
                }
                return tipos[tipo];
            } catch (error) {
                alert("VALOR INVÁLIDO, por favor digite um valor válido");
            }
        }
    }

    ataque() {
        const ataques = {
            "MAGO": "magia",
            "Guerreiro": "espada",
            "Monge": "artes marciais",
            "Ninja": "shuriken"
        };

        const tipoHeroi = this.tipoHeroi;
        const ataqueHeroi = ataques[tipoHeroi] || "ataque desconhecido";

        alert(`O ${tipoHeroi} atacou usando ${ataqueHeroi}`);
    }
}

// Criando uma instância da classe Heroi
const heroiInstancia = new Heroi();
