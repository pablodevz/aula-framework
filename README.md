# 📂 Este diretório reúne todos os **exercícios de back-end e front-end** seguindo as atividades propostas em aula.  

---

# 📂 ex-back

## 📅 Conteúdo

Exercício 01
Criação de **telas básicas com Django + Bootstrap**, incluindo:
- Tela de **Login**
- Tela de **Logout**
- Tela de **Recuperar Senha**
- Tela de **Alterar Senha**
- Tela de **Cadastro**
- Tela de **Perfil**
- Tela **Home**
- Páginas de **erro personalizadas** (404, 403, 500):contentReference[oaicite:0]{index=0}

---

Exercício 02
Implementação de **modelos e autenticação**:
- Criação do **modelo Pessoa** com atributos:
  - Nome, CPF, E-mail, Telefone, Data de nascimento, RG, Endereço, Bairro
- Registro do modelo no **Django Admin**
- Criação de **views** para consulta e retorno de dados
- Desenvolvimento de **template HTML** para exibir informações

---

Exercício 03
Trabalhando com **relacionamentos entre classes**:
- Adição do atributo **usuario** no modelo `Pessoa` (ForeignKey para `User`)
- Criação do modelo **Endereco** com:
  - Rua, Número, Bairro, Cidade, Estado, CEP
- Relacionamento entre **Pessoa** e **Endereco**
- View listando **nome**, **usuário vinculado** e **endereço completo** no template `home.html`:contentReference[oaicite:2]{index=2}

---

## 🛠️ Tecnologias
- **Django** – Framework backend em Python
- **Bootstrap** – Estilização responsiva
- **SQLite** (padrão do Django) para persistência de dados

---
