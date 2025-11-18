# 📘 Sistema Universitário – Gerenciamento de Cursos e Campus

Este projeto é um sistema simples em Python para gerenciar **Campus** e **Cursos** de uma instituição.
Ele utiliza menus interativos no terminal e classes orientadas a objetos.

---

## 🧱 Estrutura do Projeto

* **Curso.py** → define a classe Curso
* **Campus.py** → define a classe Campus
* **main.py** → contém o menu principal e os submenus CRUD

---

## 🎯 Objetivo do Sistema

O sistema permite:

### ✔ Gerenciar Cursos

* Criar curso
* Atualizar curso
* Remover curso
* Listar cursos

### ✔ Gerenciar Campus

* Criar campus
* Atualizar campus
* Remover campus
* Listar campus
* Adicionar cursos a um campus
* Remover cursos do campus
* Listar cursos do campus

---

## 🧠 Conceitos Utilizados

O projeto demonstra:

* Programação **Orientada a Objetos (POO)**
* Criação de **classes** e **métodos**
* Associações entre objetos (um campus pode ter vários cursos)
* Estruturas de repetição para menus interativos
* Manipulação de listas em Python

---

## 📚 Classes do Sistema

### 🔹 Classe **Curso**

Representa um curso da instituição.

Atributos:

* nome
* duração
* tipo (tecnólogo, bacharelado, etc.)
* modalidade (presencial, EAD)

### 🔹 Classe **Campus**

Representa um campus físico.

Atributos:

* nome
* código
* coordenador
* CEP
* lista de cursos associados

Métodos permitem adicionar, remover ou atualizar cursos dentro do campus.

---
