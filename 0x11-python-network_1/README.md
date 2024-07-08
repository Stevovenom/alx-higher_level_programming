## 0x11. Python - Network #1

This task mainly focuses on the backend side of development majorly focusing on data retrieval, that is , through the https requests. Since we are using python as the programming language, the requests module comes pre installed while installing python package. Incase the modulel is corrupted, one could use: <br><br>
<code> sudo apt-get update</code>, then run, <code>pip install requests</code>


For further self indused learning about <strong>HOWTO Fetch Internet Resources Using urllib Package</strong>, Kindly check:-
1. <a href="https://intranet.alxswe.com/rltoken/KoRrs5dVWsb-B82e-M1TQQ">urlib</a>
2. <a href="https://intranet.alxswe.com/rltoken/OGcRGPr7TSWtzypDd0ZibQ">quickstart with the reference package</a>
3. <a href="https://intranet.alxswe.com/rltoken/dUNaNQrV2bMSstILitQbXQ">The request package</a>


After this lets proceed to the tasks:

## task 0
We are to write a pythn script that fetches <strong>https://alx-intranet.hbtn.io/status</strong>

Though I tried to run this code in the first place,<br>
<code>
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
    print(f'\t- utf8 content: {body.decode("utf-8")}')

</code> <br></br> And I received issues with the checker, but on debugging, the main issue was due to not creating a Request object <code>urllib.request.Request("https://intranet.hbtn.io/status</code>, though the outputs were the same.

## task 1

For this one, the scripy should be a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

# Explanation
Imports:

<strong>urllib.request</strong> is imported for making the HTTP request.
<strong>sys</strong> is imported to read command-line arguments.<br>

URL Argument:

The URL is taken from the command-line arguments using sys.argv[1].
Request and Response:

<code>urllib.request.urlopen(url)</code> is used to open the URL.
The with statement ensures that the connection is properly closed after the response is processed.
Headers and X-Request-Id:

<code>response.info()</code> retrieves the headers from the response.
<code>headers.get('X-Request-Id')</code> fetches the value of the X-Request-Id header.
The value is then printed.

## Task 2
Explanation
Imports:

<strong>urllib.request<strong> is imported for making the HTTP request.
<strong>urllib.parse</strong> is imported for encoding the email parameter.
<strong>sys</strong> is imported to read command-line arguments.
URL and Email Arguments:

The URL and email are taken from the command-line arguments using <strong>sys.argv[1]</strong> and <strong>sys.argv[2]</strong>.
## Data Encoding:

<strong><code>urllib.parse.urlencode</code></strong> encodes the email parameter as a query string. The result is then encoded to bytes using .encode('utf-8').
POST Request:

<code>urllib.request.Request(url, data=data)</code> creates a POST request with the URL and the encoded email data.
Sending the Request and Reading the Response:<br></br>

<code>urllib.request.urlopen(request)</code> sends the POST request.<br>
The with statement ensures that the connection is properly closed after the response is processed.
<code>response.read()</code> reads the body of the response.<br></br>
<code>body.decode('utf-8')</code> decodes the response body from bytes to a UTF-8 string.<br></br>
The decoded response body is printed.

## Task 3
For this, I had created two server test programs so as to aid me in the debugging, the names to the files are:<br></br>
1. server_test.py 
2. simple_server.py 

Through this, the test files were being executed fully and optimally.

## Task 4
To fetch the status from https://alx-intranet.hbtn.io/status and display the response using the requests package in Python, follow these steps. Remember, you're only allowed to use the requests package and no other external packages.<br></br>

## Task 5
To achieve the task of fetching the value of the X-Request-Id header from a URL using Python, you'll utilize the requests library for making HTTP requests and sys for handling command-line arguments. <br></br>

## Task 6
I tried to run the code above above, that is the 6-post_email.py using teh command <code>./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com</code> but am receiving the output below: <br></br> 

<strong><i><code>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 501</p>
        <p>Message: Unsupported method ('POST').</p>
        <p>Error code explanation: HTTPStatus.NOT_IMPLEMENTED - Server does not support this operation.</p>
    </body>
</html>

</code></i></strong><br><br>

which signifies that the server at http://0.0.0.0:5000/post_email does not support the POST method, as indicated by the HTTP status code 501 and the message "Unsupported method ('POST')." and now the script could be modified like: <br></br>
<code>
#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Read URL from command-line argument
    email = sys.argv[2]  # Read email from command-line argument
    
    try:
        # Send POST request with email as parameter
        payload = {'email': email}
        response = requests.post(url, data=payload)
        
        # Check response status code
        response.raise_for_status()
        
        # Display the body of the response
        print(response.text)
        
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

</code><br> so as to handle the errors gracefully.

## Task 7
This script ensures that you can fetch and display the body of a response from a URL using requests, while also handling HTTP errors appropriately by printing the error code when necessary.

## Task 8
The script in 8-json_api.py produces the output<br></br>
<code>
root@037e79230746:~/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py
Not a valid JSON
root@037e79230746:~/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py a
Not a valid JSON
root@037e79230746:~/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py 2
Not a valid JSON
root@037e79230746:~/alx-higher_level_programming/0x11-python-network_1# vim 8-json_api.py
</code> <br></br>
The issue you're facing where you're receiving "Not a valid JSON" instead of the expected output ("No result" or "[<id>] <name>") is likely due to how the server is responding to your requests. But when you try oo run teh checker the checker confirms.

Also, you can try to adjust the script this way:- <br></br>
<code>
#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    try:
        response = requests.post(url, data={'q': q})
        response.raise_for_status()  # Raise an exception for HTTP errors
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
    except ValueError:
        print("Not a valid JSON")

</code>

## Task 9
For this task, we are to write a  Python script that takes your GitHub credentials (username and password) and uses the <a href="https://intranet.alxswe.com/rltoken/LjPfW9hW_55YwijGVofyTQ">GitHub API</a> to display your id

The requirements are:<br><br>

1. You must use <a href="https://intranet.alxswe.com/rltoken/ECKUmLiAk_k2G0NPzqdykQ">Basic Authentication</a> with a <a href="https://intranet.alxswe.com/rltoken/Kz4UM-V_bcwrcWajaCAVtQ">personal access token</a> as password to access to your information (only read:user permission is needed)
2. The first argument will be your username
3. The second argument will be your password (in your case, a <a href="https://intranet.alxswe.com/rltoken/Kz4UM-V_bcwrcWajaCAVtQ">personal access token</a> as password)
4. You must use the package requests and sys
5. You are not allowed to import packages other than requests and sys
6. You don’t need to check arguments passed to the script (number or type).<br></br>

In place of our code in the script 10-my_github.py, the following solutions can be viable:<br>

1. <code>
#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
</code><br></br>
and <br></br>
2. <code>
#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
</code>
