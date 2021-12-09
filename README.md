# Cesar Labs test
Flask application, with Celery, Redis running inside Docker microservices.

To run the application, follow the steps below:

## 1. Clone the GitHub repository:

```sh
$ git clone https://github.com/demetriushenry/cesarlabs.git
$ cd cesarlabs/
```

## 2. Build and run Docker services.

```sh
$ sudo docker-compose up -d
```

## 3. Access the Morse Code Decoding page.

* Open Browser and insert the following URL bellow:
> http://localhost:5000/
* Place the morse code in the text area.
* Click the Decode button.
* Check the output.

## Send requests via command line (Optional)

```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"code":".. .- -- .... .. .-. . -.."}' http://localhost:5000/api/morse_decode
```

#### You can use the Postman app to test the endpoint: *http://localhost:5000/api/morse_decode*

## Run unit tests

```sh
$ sudo docker-compose run app python -m unittest tests/test_decode_code.py
```

## Stop all services

```sh
$ sudo docker-compose stop
or
$ sudo docker-compose down -v
```