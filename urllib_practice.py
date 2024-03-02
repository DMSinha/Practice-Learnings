""""urllib.request module provides functions for making HTTP requests, including GET and POST 
requests, and handling responses."""

"""
import urllib.request
# Example: Sending a GET request 
response = urllib.request.urlopen("https://www.flipkart.com/search?q=tv")
html=response.read()
print(html)

urllib.parse module is used for parsing URLs, breaking them down into their 
components such as scheme, netloc, path, query, and fragment.
import urllib.parse
url = "https://www.flipkart.com/search?q=tv"
parsed_url = urllib.parse.urlparse(url)
print(parsed_url)
"""


#The urllib.error module handles exceptions and errors that may occur during HTTP requests.
"""import urllib.error
import urllib.request
try:
    response = urllib.request.urlopen('https://nonexistent-url.com')
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code}')
except urllib.error.URLError as e:
    print(f'URL Error: {e.reason}')

import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://example.com/robots.txt')
rp.read()
allowed = rp.can_fetch('MyCrawler', 'https://example.com/page')
print(allowed)
"""

#Sending Get request
#Sending GET requests to retrieve web content is a fundamental operation in urllib.

"""import urllib.request

response = urllib.request.urlopen('https://example.com')
html = response.read()
print(html)
"""

#POST requests are used to send data to a server, often used in web forms.

"""import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'param1': 'value1', 'param2': 'value2'}).encode('utf-8')
response = urllib.request.urlopen('https://example.com/post', data=data)
html = response.read()
print(html)"""

#various properties of an HTTP response, such as status code, headers, and content.
"""import urllib.request

response = urllib.request.urlopen('https://www.flipkart.com/search?q=tv')
status_code = response.getcode()
headers = response.info()
html = response.read()

print(f'Status Code: {status_code}')
print(f'Headers: {headers}')
print(html)"""

#error handling for HTTP-related issues, such as 404 Not Found or connection errors.
"""import urllib.error
import urllib.request
try:
    response = urllib.request.urlopen('https://nonexistent-url.com')
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code}')
except urllib.error.URLError as e:
    print(f'URL Error: {e.reason}')
"""

#Parsing URL
"""import urllib.parse

url = 'https://www.example.com/path?param=value'
parsed_url = urllib.parse.urlparse(url)

print(f'Scheme: {parsed_url.scheme}')
print(f'Netloc: {parsed_url.netloc}')
print(f'Path: {parsed_url.path}')
print(f'Query: {parsed_url.query}')"""

#Constructing URLs:can construct URLs by combining their components using urllib.parse.urlunparse() or by appending query parameters to an existing URL.
"""import urllib.parse

components = ('https', 'example.com', 'path', '', 'param=value', '')
constructed_url = urllib.parse.urlunparse(components)
print(constructed_url)
"""
#Working with Headers
"""import urllib.request

url = 'https://example.com'
headers = {'User-Agent': 'My User Agent'}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
print(response)
"""

#Handling Timeouts:set timeouts for HTTP requests to prevent them from hanging indefinitely.
import urllib.request
import urllib.error

url = 'https://example.com'
try:
    response = urllib.request.urlopen(url, timeout=10)  # Set a timeout of 10 seconds
    html = response.read()
    print(html)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("Request timed out.")
    else:
        print(f"URL Error: {e.reason}")