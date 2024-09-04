# COMO INICIAR ESTE PROJETO EM AMBIENTE DE DESENVOLVIMENTO

1. Clonar este repositório

2. Acessar o diretório com o prompt de comando, powershell ou terminal

3. Criar o ambiente virtual:
~~~
python -m venv venv
~~~

4. Ativar o ambiente virtual:
~~~
venv\Scripts\activate.bat
~~~

5. Baixar as dependências do projeto:
~~~
pip install -f requirements.txt
~~~

6. Executar o comando de migração de dados:
~~~
python manage.py makemigrations
python manage.py migrate
~~~   

7. Setar o admin:
~~~
python manage.py createsuperuser
~~~

8. Iniciar o servidor:
~~~
python manage.py runserver
~~~

9. Verificar se o endpoint está funcional pelo navegador de internet através do endereço:
   http://localhost:8000/
