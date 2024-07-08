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

