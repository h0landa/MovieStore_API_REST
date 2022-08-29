# MovieStore_API_REST

# Preparando o ambiente

Para conseguir rodar a API REST MovieStore no seu computador, você deve ter
as seguintes técnologias:
* Python3
* Flask
* Postman(Esse Software é essencial para o desenvolvimento de APIs. Com ele você pode usar todos os métodos.)
* virtualenv(Biblioteca do Python para criação de ambientes virtuais) 

Siga os passos para para configurar seu ambiente.

# Windows

## Tecnologias necessárias.

1. Baixe e instale o Python3: https://www.python.org/downloads/.
2. Baixe e instale o Postman: https://www.postman.com/downloads/.

## Configurações

1. No terminal do seu editor de texto, instale a biblioteca virtualenv para criar
seu ambiente virtual, usando o comando `pip install virtualenv`.
2. Depois de instalar o virtualenv, digite `virtualenv venv`, e seu ambiente será criado.
3. Agora basta ativar seu ambiente com o comando `venv/Scripts/Activate`.
PS:Geralmente a execução desse comando pode retornar um erro relacionado a execução de scripts no windows, que você resolve assim: https://pt.stackoverflow.com/questions/220078/o-que-significa-o-erro-execu%C3%A7%C3%A3o-de-scripts-foi-desabilitada-neste-sistema#:~:text=7%20Respostas&text=Isto%20%C3%A9%20uma%20pol%C3%ADtica%20de,(que%20%C3%A9%20o%20padr%C3%A3o).
3. Agora que você já criou seu ambiente, instale todas as dependencias para rodar o projeto com o comando `pip install -r requiriments.txt`.
4. Para iniciar o servidor, digite: `python app.py`.

Devera retornar:
``` 
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 791-915-549
```
# Observações:

O projeto já possui um banco que já vem preenchido com 50 filmes e 10 atores. Cada filme está relacionado a um ator por meio de relacionamento entre tabelas SQL. Claro que você também pode cadastrar mais filmes.
