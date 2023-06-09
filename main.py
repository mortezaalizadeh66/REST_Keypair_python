from flask import Flask, request, abort
import os
import fcntl
import logging
from logging.handlers import RotatingFileHandler
import datetime

app = Flask(__name__)

# Set up logging %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
log_handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
log_handler.setLevel(logging.ERROR)
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)

#Begin of PUT function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@app.route('/<string:key>', methods=['PUT'])
def put_value(key):
    # Get the value from the request data
    value = request.data
    #request must be a string containing ASCII characters from a-z, A-Z, and 0-9 (1-255 bytes): .
    #length of value must be below 1024 Bytes
    if not all(c.isalnum() or c.isspace() for c in key) and 1 <= len(key) <= 255 and len(value.encode('utf-8')) > 1024:
        abort(400)
    # Write the key-value pair to a txt file and locking the access to file
    try:
        with open(f'{key}.txt', 'wb') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write(value)
    except OSError as e:
        app.logger.error(f'{e.__class__.__name__}: {str(e)} at {datetime.datetime.now()}')
        abort(500)
    # Return a 204 No Content response
    return '', 204
#End of PUT function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#this is GET function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@app.route('/<string:key>', methods=['GET'])
def get_value(key):
    # Check if the key exists
        if not os.path.isfile(f'{key}.txt'):
            abort(404)
        try:
        # Read the value from the file after locking the file access
         with open(f'{key}.txt', 'rb') as f:
             fcntl.flock(f, fcntl.LOCK_SH)
             value = f.read()
        except OSError as e:
             app.logger.error(f'{e.__class__.__name__}: {str(e)} at {datetime.datetime.now()}')
             abort(500)

        # Return a 200 OK response with the value in the response body
        return value, 200, {'Content-Type': 'application/octet-stream'}
#end of GET function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#this is Remove function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@app.route('/<string:key>', methods=['DELETE'])
def delete_value(key):
    # Check if the key exists
    if not os.path.isfile(f'{key}.txt'):
        abort(404)

    # Delete the file
    try:
        os.remove(f'{key}.txt')
    except OSError as e:
        app.logger.error(f'{e.__class__.__name__}: {str(e)} at {datetime.datetime.now()}')
        abort(500)

    # Return a 204 No Content response
    return '', 204
#End of Remove function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#Fix the Host name and related port%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if __name__ == '__main__':
    app.run(host='localhost', port=3000)
