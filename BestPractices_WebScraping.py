#Error Handler

"""
import urllib.error
import urllib.request

try:
    response = urllib.request.urlopen('https://www.flipkart.com/search?q=tv')
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code}')
except urllib.error.URLError as e:
    print(f'URL Error: {e.reason}')
else:
    # Code to execute if there are no errors
    html = response.read()
    print(html)

"""
#User Agent Headers:Set a User-Agent header in your requests to identify your script or application when interacting with websites or APIs.
"""import urllib.request

# Define the User-Agent header
user_agent = 'My Custom User Agent'

# Create a request object with the User-Agent header
url = 'https://www.flipkart.com/search?q=tv'
headers = {'User-Agent': user_agent}
req = urllib.request.Request(url, headers=headers)

# Send the request
response = urllib.request.urlopen(req)

# Now you can work with the response as needed
html = response.read()
print(html)
"""

#Respect Robots.txt: check a website's robots.txt file to see if scraping is allowed and follow the rules to avoid legal issues.

"""import urllib.robotparser

# Create a RobotFileParser object and specify the URL of the website's robots.txt file.
rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.flipkart.com/search?q=tv')

# Read and parse the robots.txt file.
rp.read()

# Check if it's allowed to crawl a specific URL.
is_allowed = rp.can_fetch('MyCrawler', 'https://www.flipkart.com/search?q=tv')

if is_allowed:
    print("Crawling is allowed for this URL.")
else:
    print("Crawling is not allowed for this URL according to robots.txt.")

"""
#Downloading Files from the Internet
"""import urllib.request

file_url = 'https://example.com/file.pdf'
urllib.request.urlretrieve(file_url, 'downloaded_file.pdf')
"""