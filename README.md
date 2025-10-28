# 🧩 User Manager

Sistema simples de **gerenciamento de usuários** desenvolvido com **Flask (Python)**.  
> Aplicação web que permite o cadastro e visualização de usuários em uma interface amigável, desenvolvida para fins de estudo de **desenvolvimento full stack com Python e Flask**.


---

## 🚀 Funcionalidades

- 📝 **Cadastro de usuários** (nome e e-mail)  
- 👥 **Listagem de usuários cadastrados**  
- ⚡ Mensagens de confirmação usando `flash`  
- 🌐 Integração entre **frontend (HTML, CSS)** e **backend (Flask)**  

---

## 🧠 Tecnologias utilizadas

- **Python 3**
- **Flask** — framework backend
- **HTML5 / CSS3** — frontend
- **Jinja2** — engine de templates
- **Render.com** — hospedagem e deploy automático (CI/CD)

---

## 🗂️ Estrutura de pastas

```
user-manager/
│
├── static/                 # Arquivos estáticos (CSS, imagens, JS)
│    ├── style.css          # Estilos principais do site
│    └── img/               # Pasta com imagens do projeto
│         ├── pinUser.svg
│         └── pinUsers.svg
│
├── templates/              # Páginas HTML renderizadas pelo Flask (com Jinja2)
│    ├── index.html         # Tela inicial (cadastro)
│    └── clientes.html      # Tela de usuários cadastrados
│
├── Procfile                # Diz ao Render como rodar o app (ex: "web: python app.py")
├── app.py                  # Código principal do Flask (rotas e lógica)
├── requirements.txt        # Dependências do projeto (ex: Flask)
├── .gitignore              # Define arquivos que não serão enviados ao GitHub
└── README.md               # Descrição e instruções do projeto
```
---

## 🧑‍💻 Autor

**José Satiro de Lima**

💼 Projeto para estudo de desenvolvimento **Full Stack**, utilizando:
- **Python** e **Flask** no back-end  
- **HTML** e **CSS** no front-end
