
# Python WebApp Username Brute Forcer


The following tool can be used to brute force for valid usernames
where a web application gives some indication if a user is valid
regardless if the password was wrong.

## Configuration

The script uses a YAML script for input paramters.

The input params should be:

* url - the target URL
* user_field - The name of the user input field the API accepts
* methods - a list of request methods to use
* data - a list of other parameters that may be required by the API/App
* proxies - a list of proxies to be used
* response - used for recording the response field parameters that indiciate a valid user
* response_key - nested under response and used for the key to check for a valid/invalid message
* valid_response - nested under response, the value returned that confirm the a successful guess of a username.
* users - a list of users

The following YAML demonstrates the above:

```
url: "http://some.website/api/v1/login"
user_field: "userName"

data: null

methods:
- POST
- GET
- PUT

proxies:
  http: "http://127.0.0.1:5000"
  https: "https://127.0.0.1:5000"
  ftp: "ftp://127.0.0.1:5000"

response:
    response_key: message
    valid_response: "Username correct but password not supplied"

users:
- bsmith@blah.com
- jbloggs@blah.com

```


## Operation

Clone the source code from git and install via pip.

```
pip install -e python-webapp-username-bruteforcer
```

Run the script with:

```
python -m username_bruteforcer my_conf.yaml
```


Once complete two YAML output files will be generated.

valid_users.yaml - a list of valid usernames

invalid_users - a list of usernames where no match was found
