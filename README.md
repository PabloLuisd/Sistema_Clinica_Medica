
# 🏥 Sistema de Gerenciamento de Clínica Médica

Sistema web desenvolvido em Python e Django para auxiliar no gerenciamento de uma clínica médica, permitindo o cadastro de pacientes, médicos, especialidades e o controle de consultas.

## 📋 Funcionalidades

- **Pacientes**
  - Cadastrar pacientes.
  - Listar pacientes cadastrados.
  - Editar informações.
  - Excluir pacientes.

- **Médicos**
  - Cadastrar médicos.
  - Listar médicos cadastrados.
  - Editar informações.
  - Excluir médicos.

- **Especialidades**
  - Cadastrar especialidades médicas.
  - Consultar especialidades cadastradas.

- **Consultas**
  - Agendar consultas selecionando paciente e médico.
  - Definir data e horário.
  - Consultar consultas agendadas.
  - Alterar o status da consulta: Agendada, Realizada ou Cancelada.
  - Visualizar o paciente e o médico associados a cada consulta.

## 🛠️ Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML5
- CSS3

## 📁 Estrutura do projeto

```text
clinica_medica/
│
├── atendimento/
│   ├── migrations/
│   ├── models/
│   │   ├── paciente.py
│   │   ├── medico.py
│   │   ├── especialidade.py
│   │   └── consulta.py
│   │
│   ├── views/
│   │   ├── home_views.py
│   │   ├── paciente_views.py
│   │   ├── medico_views.py
│   │   ├── especialidade_views.py
│   │   └── consulta_views.py
│   │
│   ├── urls_configs/
│   ├── templates/
│   ├── static/
│   ├── forms.py
│   └── admin.py
│
├── clinica_medica/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── db.sqlite3
```

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta do projeto

```bash
cd clinica_medica
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Instalar o Django

```bash
pip install django
```

### 6. Aplicar as migrações

```bash
python manage.py migrate
```

### 7. Executar o servidor

```bash
python manage.py runserver
```

### 8. Acessar o sistema

Abra o navegador e acesse:

```text
http://127.0.0.1:8000/
```

## 🔒 Regra de negócio

O sistema possui uma validação para impedir que um mesmo médico tenha duas consultas ativas na mesma data e horário.

Consultas com status **Cancelada** não bloqueiam o horário, permitindo que ele seja utilizado novamente.

## 🎯 Objetivo do projeto

O objetivo é aplicar conhecimentos de desenvolvimento web utilizando Django, trabalhando com operações CRUD, relacionamento entre tabelas, formulários, organização de código e regras de negócio.

---

Desenvolvido como projeto acadêmico.
