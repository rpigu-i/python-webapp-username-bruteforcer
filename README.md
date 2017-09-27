
# Python WebApp Username Sniffer


The following tool can be used to sniff for valid usernames
where a web application gives some indication if a user is valid
regardless if the password was wrong.

## Configuration

The script uses a YAML script for input paramters. This should be called user.yaml
and be located in the same folder as the script

Note: This will be made an input param in future releases. 

The input params should be:

* url - the target URL
* user_field - The name of the user input field the API accepts
* data - a list of other parameters that may be required by the API/App
* response - used for recording the response field parameters that indiciate a valid user
* response_key - nested under response and used for the key to check for a valid/invalid message
* valid_response - nested under response, the value returned that confirm the a successful guess of a username.
* users - a list of users

The following YAML demonstrates the above:

```
url: "http://some.website/api/v1/login"
user_field: "userName"

data: null

response:
    response_key: message
    valid_response: "Username correct but password not supplied"

users:
- bsmith@blah.com
- jbloggs@blah.com

```


## Operation

Run the script with:

```
python user_sniffer.py 

```


Once complete two YAML output files will be generated.

valid_users.yaml - a list of valid usernames

invalid_users - a list of usernames where no match was found








