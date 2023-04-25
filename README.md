# REST_Keypair_python

This is a HTTP_Server request , which used REST Api

This code is a server side that is running on  local machine (host='localhost', port=3000)

HTTP endpoints:

# PUT /<key> — Set the value of a key

# GET /<key> — Fetch the value of a key

# DELETE /<key> — Delete a key

* The server's database is a persisted to the file system (using file access locking, and error handling).

* Restarting the server should not lose writes that have already been acknowledged with a 2XX response status code.

* Keys must be between 1 and 255 bytes long and will use the ASCII characters a-z,A-Z,0-9.

* Values are byte strings  utf-8 with a maximum length of 1024 bytes.

* This code try to follow try-except blocks to handle file I/O errors and respond with appropriate error codes

* This code also used file locking to prevent conflict when multiple clients try to access the same key-value pair at the same time

* The logging is also in the code to report the errors in a seperate file "error.log" in a serverside storage


--The requirments (having knowledge of Error handling on Flask Abort() ),

1- install python , curl on your OS

2- install pip

3- install Flask latest version by the help of pip
```
  $ pip install Flask
  
```
  
4- run this command in main directory of python code where you copy/pate main.py file
```
  $ flask --app main.py run
```

5-leave the terminal open, the output should be like below, means server is listening on port 5000 on your localhost

  output:
  
         Serving Flask app 'main.py'
         
         Debug mode: off
         
         WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
         
         Running on http://localhost:3000
         
         Press CTRL+C to quit

6- Please open another new Terminal

7- Run these commands

# Write a value "hello world!" to the key "foo" by Client:

```
curl -i -X PUT 'http://localhost:3000/foo' -H 'Content-Type: application/octet-stream' --data-binary 'hello world!'

```

# Fetch the value of "foo" from client
```
curl -i 'http://localhost:3000/foo'

```


# Fetch the value of "qux" (which does not exist) from Client
```

curl -i 'http://localhost:3000/qux'

```


# Delete the key "foo"
```

curl -i -X DELETE 'http://localhost:3000/foo'

```


8- try this scenario , First add key and value, make server stop, again make server start, and try to Fetch the value of key

9- # Write a value "hello world!" to the key "foo" by Client

```
curl -i -X PUT 'http://localhost:3000/foo' -H 'Content-Type: application/octet-stream' --data-binary 'hello world!'

```


10- make server down , ctrl + c in the first Terminal

11- make server up , in the first Terminal
```
$ flask --app main.py run  

```
12- jump to second Terminal or open a new terminal

13- # Fetch the value of "foo" from client

        $curl -i 'http://localhost:3000/foo'
        
        output:
              HTTP/1.1 200 OK
              Server: Werkzeug/2.2.3 Python/3.11.3
              Date: Tue, 25 Apr 2023 12:01:07 GMT
              Content-Type: application/octet-stream
              Content-Length: 12
              Connection: close

              hello world!%     




