# 🛒 Projeto E-commerce com Azure

Este projeto faz parte do desafio da **DIO (Digital Innovation One)** e tem como objetivo demonstrar a criação de uma aplicação simples de e-commerce utilizando **serviços da Microsoft Azure**, integrando **upload de imagens no Azure Blob Storage** e **persistência de dados em banco de dados**.

---

## 📌 Objetivo do Projeto

Criar uma aplicação backend capaz de:

* Cadastrar produtos
* Armazenar imagens no **Azure Blob Storage**
* Salvar informações dos produtos em banco de dados
* Expor endpoints para inserção de dados

---

## 🧰 Tecnologias Utilizadas

* **Python**
* **Flask**
* **Azure Blob Storage**
* **Azure SQL Database**
* **Git & GitHub**
* **dotenv** para gerenciamento de variáveis de ambiente

---

## 🗂 Estrutura do Projeto

```
.
├── main.py
├── requirements.txt
├── .env.example
├── README.md
```

---

## 🧪 Funcionalidades Implementadas

* 📤 Upload de imagens para o Azure Blob Storage
* 📦 Inserção de produtos no banco de dados
* 🔗 Geração de URL pública da imagem
* 🧾 Cadastro de produto com:

  * Nome
  * Descrição
  * Preço
  * URL da imagem

---

## 🛢 Estrutura da Tabela no Banco de Dados

```sql
CREATE TABLE Produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255),
    descricao NVARCHAR(MAX),
    preco DECIMAL(18,2),
    imagem_url NVARCHAR(2083)
);
```

---

## ⚙️ Configuração do Ambiente

1. Clone o repositório:

```bash
git clone https://github.com/augustojoselg/dio-azure-ecommerce.git
```

2. Crie um arquivo `.env` baseado no `.env.example` e configure suas credenciais do Azure.

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python main.py
```

---

## 🚀 Resultado

A aplicação permite o cadastro de produtos com imagens armazenadas na nuvem, demonstrando na prática a integração entre **Python** e **Azure**, seguindo boas práticas de segurança com uso de variáveis de ambiente.

---

## 📸 Evidências

* Prints da aplicação em execução
* Prints do container no Azure Blob Storage
* Prints do banco de dados com registros inseridos

---

## 👨‍💻 Autor

**Augusto José Lazaro Gonçalves**
🔗 [LinkedIn](https://www.linkedin.com/in/augustojoselg/)

---

Projeto desenvolvido para fins educacionais no bootcamp da **DIO**.
