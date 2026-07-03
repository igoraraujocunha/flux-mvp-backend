# FLUX - API de Portfólio de Projetos

API RESTful desenvolvida em Flask para o gerenciamento do portfólio de projetos do FLUX. Este serviço compõe o backend para a entrega do MVP da Pós-Graduação em Engenharia de Software da PUC-Rio.

## Stack
* Python / Flask
* SQLAlchemy (SQLite)
* Flasgger (Swagger UI)
* Flask-CORS

## Setup Local

```bash
git clone [https://github.com/igoraraujocunha/flux-mvp-backend.git](https://github.com/igoraraujocunha/flux-mvp-backend.git)
cd flux-mvp-backend

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

## Documentação 
Com o servidor em execução, a documentação OpenAPI interativa fica disponível em:
http://127.0.0.1:5000/apidocs/