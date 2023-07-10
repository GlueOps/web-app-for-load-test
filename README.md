# web-app-to-simulate-load
The goal of this app is to use it on the receiving end of a load testing tool. 

## Setting up .env file

- Clone the repository you want to work on and ```cd``` into that directory.
  
## Running the QR code generator

- Development environment

```python
uvicorn main:app --reload
```

## Running the Dockerfile

```bash
$ docker build -t simulate-workload .
$ docker run -p 8000:8000 simulate-workload
```

## Access the website

- In your browser, navigate to ```https://127.0.0.1:8000/v1/sleep?ms=1000```
