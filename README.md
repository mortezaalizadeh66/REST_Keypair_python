# REST_Keypair_python

This code is a server side that is running on  local machine 127.0.0.1:5000


The requirments,

1- install python , curl on your OS

2- install pip

3- install Flask latest version by the help of pip

  $ pip install Flask
  
4- run this command in main directory of python code where you copy/pate main.py file

  $ flask --app main.py run
  
5-leave the terminal open, the output should be like below, means server is listening on port 5000 on your localhost

  output:
         Serving Flask app 'main.py'
         Debug mode: off
         WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
         Running on http://127.0.0.1:5000
         Press CTRL+C to quit

6- Please open another new Terminal

7- Run these commands

# Write a value "hello world!" to the key "foo" by Client
curl -i -X PUT 'http://localhost:5000/foo' -H 'Content-Type: application/octet-stream' --data-binary 'hello world!'

# Fetch the value of "foo" from client
curl -i 'http://localhost:5000/foo'

# Fetch the value of "qux" (which does not exist) from Client
curl -i 'http://localhost:5000/qux'

# Delete the key "foo"
curl -i -X DELETE 'http://localhost:5000/foo'



8- try this scenario , First add key and value, make server stop, again make server start, and try to Fetch the value of key

9- # Write a value "hello world!" to the key "foo" by Client

curl -i -X PUT 'http://localhost:5000/foo' -H 'Content-Type: application/octet-stream' --data-binary 'hello world!'

10- make server down , ctrl + c in the first Terminal

11- make server up , $ flask --app main.py run in the first Terminal 

12- jump to second Terminal or open a new terminal

13- # Fetch the value of "foo" from client

        $curl -i 'http://localhost:5000/foo'
        
        output:
              HTTP/1.1 200 OK
              Server: Werkzeug/2.2.3 Python/3.11.3
              Date: Tue, 25 Apr 2023 12:01:07 GMT
              Content-Type: application/octet-stream
              Content-Length: 12
              Connection: close

              hello world!%     




