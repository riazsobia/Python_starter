# README #

This is the README file for Flask Boiler Plate App which helps to get you up and running very quickly.

# flask_boilerplate directory #

It contains all the application source:

 - app
 - core
 - exceptions

# App Directory #

It contains all the webservice app requisites including:

 - authentication - It'll handle the authentication of the paths.
 - conf - It contains the configuration of app.
 - controllers - It contains the fucntions which handle the requests.
 - helpers - It contains the helper functions.
 - routes - It contains the paths of app.

# Core Directory #

It contains the core source code of the application.

# Exceptions Directory #

It contains the modules to handle errors and Exceptions.

# How to run the app #

Please run below command from root directory.

```bash
docker-compose up
```

# Usage

```bash
curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" http://127.0.0.1:5001/addition -d '{"value_1": 10, "value_2":10}' | python -mjson.tool
```

Response is below:
```bash
{
    "sum": 20
}
```