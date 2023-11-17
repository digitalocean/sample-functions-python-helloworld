# Sample Function: Python "Hello World"

## Introduction

This repository contains a sample "Hello World" function written in Python. You can deploy it on DigitalOcean's App Platform as a Serverless Function component or as a standalone Function. Documentation is available at https://docs.digitalocean.com/products/functions.

### Requirements

* You need a DigitalOcean account. If you don't already have one, you can sign up at [https://cloud.digitalocean.com/registrations/new](https://cloud.digitalocean.com/registrations/new).
* To deploy from the command line, you will need the [DigitalOcean `doctl` CLI](https://github.com/digitalocean/doctl/releases).

## Deploying the Function

```
# clone this repo
git clone git@github.com:digitalocean/sample-functions-python-helloworld.git
```

```
# deploy the project, using a remote build so that compiled executable matched runtime environment
doctl serverless deploy sample-functions-python-helloworld --remote-build
```

The output from the deploy command will resemble the following.
```
Deploying 'sample-functions-python-helloworld'
  to namespace 'fn-...'
  on host '...'
Deployment status recorded in 'sample-functions-python-helloworld/.deployed'

Deployed functions ('doctl sls fn get <funcName> --url' for URL):
  - sample/hello
```

## Using the Function

```
doctl serverless functions invoke sample/hello
```

This will return the default response from the function.
```
{
  "body": "Hello stranger!"
}
```

You can pass a parameter to your function using the `-p` command line argument.
```
doctl serverless functions invoke sample/hello -p name:functions
{
  "body": "Hello functions!"
}
```

Use this command to retrieve the URL for your function and use it as an API.
```
doctl sls fn get sample/hello --url
```

You can use that API directly in your browser, with `curl` or with an API platform such as Postman.
Parameters may be passed as query parameters, or as JSON body. Here are some examples using `curl`.

```
curl `doctl sls fn get sample/hello --url`?name=query
```

```
curl -H 'Content-Type: application/json' -d '{"name":"body"}' `doctl sls fn get sample/hello --url`
```

### Learn More

You can learn more about Functions by reading the [Functions Documentation](https://docs.digitalocean.com/products/functions).
