

![Badge](https://img.shields.io/static/v1?label=DjangoRestFramework&message=v3.1.1.1&color=blue&style=<STYLE>&logo=ghost) 


# Desafio Hourth

## Pré-Requisitos📃
   * Python3
## Instalação💻
   
   * Primeiramente baixe o arquivo ou clone com o comando git clone
   
~~~
 git clone https://github.com/lowliet64/DesafioHourth.git
~~~

  * Em seguida entre no diretório da aplicação
  
  ~~~
    cd DesafioHourth
  ~~~

   * Crie um ambiente virtual para instalacao das dependencias:
 ~~~
    pip -m venv .venv
 ~~~~
   
  * Em seguida ative o ambiente virtual com :

 ~~~
    source .venv/bin/activate
 ~~~~
   * Dentro da pasta instale as dependencias executando :
   
  ~~~
    pip install -r requirements.txt
  ~~~~
 * rode as migrations com 
   
  ~~~
    python manage.py migrate
  ~~~~
  
  * popule o banco utilizando:
  ~~~
   python manage.py seed
  ~~~


  * Por último inicie o serviço com o comando :
  ~~~
   python3 manage.py runserver
  ~~~

O Serviço estará disponivel em http://127.0.0.1:8080

