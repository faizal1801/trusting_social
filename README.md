# trusting_social
Trusting Social Prescreening Test Repo

Notes:
- Using Python 3 Environment

Start service with this command:
- $ python3 trusting_server.py <br>
waiting for connection...


Open other terminal, input data with this command:
- $ curl -s -d '{"id": "1", "name": "John Doe", "age": "25"}' -H "Content-Type: application/json" -X POST 127.0.0.1:5555

On the server side will shown like this:
- $ python3 trusting_server.py <br>
waiting for connection... <br>
...connected from:  ('127.0.0.1', 42760)
