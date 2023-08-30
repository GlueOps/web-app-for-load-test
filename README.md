# web-app-simulate-workload
The goal of this app is to use it on the receiving end of a load testing tool. It supports:
- Slow response times with /v1/sleep
- Uploading files with the GUI at: /uploadfile or via API at: /v1/uploadfile

## Running the app

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
