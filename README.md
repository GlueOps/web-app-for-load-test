# web-app-for-load-test
The goal of this app is to use it on the receiving end of a load testing tool. 

## Setting up .env file

- Clone the [repo](https://github.com/development-captains/test-80-np.pluto.onglueops.rocks) into a codespace.

- Then run, in the root folder
```bash
$ source .env
```

- Clone the repository you want to work on and ```cd``` into that directory.
  
## Running the QR code generator

- Development environment

```python
uvicorn qr-generator:app --reload
```

- Ensure [public](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-visibility-of-forwarded-ports#overview) port forwarding in codespace.

## Running the Dockerfile

```bash
$ docker build -t qr-bot-generator .
$ docker run -p 8000:8000 qr-bot-generator
```

## Access the website

- In your browser, navigate to ```https://127.0.0.1:8000.preview.app.github.dev/v1/qr?url=<your-url>```

A QR code will be generated
<img width="931" alt="image" src="https://github.com/GlueOps/github-actions-build-push-containers/assets/49791498/d66f773c-e05c-43db-b978-0bebbb303bb2">
