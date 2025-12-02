# 🏛️ Sistema de Gerenciamento Universitário

Este é um sistema simples desenvolvido em **Python** para gerenciar uma estrutura universitária. O projeto utiliza conceitos de **Orientação a Objetos (POO)** para cadastrar cursos, criar campus e vincular cursos a unidades específicas.

## 🚀 Como Executar

Certifique-se de ter o **Python 3** instalado.

1.  Abra o terminal (ou prompt de comando) nessa pasta.
2.  Execute o comando:

<!-- end list -->

```bash
python main.py
```

## ✨ Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

### 1\. Gerenciar Cursos (Catálogo Geral)

  * **Criar**: Adiciona um novo curso ao catálogo geral da universidade.
  * **Atualizar**: Permite editar os dados de um curso existente.
      * *Dica:* Ao editar, pressione `ENTER` em um campo vazio para manter o valor atual.
  * **Listar**: Exibe todos os cursos cadastrados.

### 2\. Gerenciar Campus

  * **Criar**: Adiciona um novo campus com código único.
  * **Atualizar**: Edita dados do campus (Nome, Coordenador, CEP).
  * **Listar**: Mostra os campus cadastrados.
  * **Vincular Curso**: Adiciona um curso do catálogo geral para dentro de um campus específico (Relação de Composição/Agregação).
  * **Ver Cursos do Campus**: Lista apenas os cursos ofertados naquela unidade.