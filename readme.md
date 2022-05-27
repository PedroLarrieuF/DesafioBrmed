*Olá, este é meu desafio.*

Objetivos:

* Criar tabela comparativa entre EUR, JPY e USD.
* Definir limite de data de até 5 dias úteis.
* Implementar Highcharts.

Feito:

* Tabela comparativa entre EUR, JPY e USD.
* Única view e único template que varia entre métodos. 
* Python e django praticamente puro, sem usos de bibliotecas.
* Velocidade do código.
* Limite de dias.

Não feito: 

* Não consegui implementar esquema de dias úteis.
* Não consegui implementar deploy em Heroku.

*Obs:*

* Adição de dias com limite de até 5 dias anteriores a data atual. Isso permite consultar e escrever dados mais antigos. Porém não permite que seja feito a apartir de data atual. 


*Iniciando a aplicação:*

* Clone o repositório.
* Inicie a variavel de ambiente. Está localizada em 'venv'
    * Para iniciar a variavel de ambiente digite os seguintes comandos: 
        * cd venv
        * cd Scripts
        * activate
    * Em linux:
        * cd venv
        * cd Scripts
        * . activate

        *obs:* Em alguns casos será necessário executar '. actiavte' no ultimo comando.
    *obs*: 
        * Caso queira instalar sua própria venv execute os seguintes comandos:
        * python3 -m venv venv.
        * repita os passos acima.

* Execute o pip:

    * pip install -r  requeriments.txt   

* Em sua IDE, vá até '/src' e execute:

    * python3 manage.py makemigrations
    * python3 manage.py migrate
    * python3 manage.py runserver

    *obs*: O projeto possui duas pastas chamadas 'src' verifique que você está na raiz do sistema e não na 'src/src', pois neste caso será necessário voltar a pasta anterior com o comando 'cd ..'    

* Com aplicação aberta você verá a 'homepage.html'

   * Digite  a data de consulta, respeitando a regra de 5 dias a contar da atual.
   * Perceba em seu terminal que ela criou um objeto e no front end ela renderizou o objeto.
   * A medida que novas datas são adicionadas, ela cria novos objetos. Sempre respeitando a regra de 5 dias.
   * Ela não cria objetos repetidos.