# FLUX - API de Portfólio de Projetos

API RESTful desenvolvida em Flask para o gerenciamento do portfólio de projetos do FLUX. Este serviço compõe o backend para a entrega do MVP da Pós-Graduação em Engenharia de Software da PUC-Rio.

## Stack
* Python / Flask
* SQLAlchemy (SQLite)
* Flasgger (Swagger UI)
* Flask-CORS

## Instruções de Instalação e Inicialização

Siga os passos abaixo para configurar o ambiente local e rodar a API:

1. Clone o repositório e acesse a pasta:
```bash
git clone [https://github.com/igoraraujocunha/flux-mvp-backend.git](https://github.com/igoraraujocunha/flux-mvp-backend.git)
cd flux-mvp-backend
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv

# No Windows:
venv\Scripts\activate

# No Mac/Linux:
source venv/bin/activate
```

3. Instale as dependências do projeto e execute o servidor:
```bash
pip install -r requirements.txt

python app.py
```
## Acesso a Documentação
Após iniciar o servidor, a documentação Swagger (OpenAPI) ficará disponível no seu navegador através do endereço:
http://127.0.0.1:5000/apidocs/
