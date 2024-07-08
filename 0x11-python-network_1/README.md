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


