print("Hello, GitHub!")
import requests

# Replace 'your_username' and 'your_repository' with your GitHub details
url = "https://raw.githubusercontent.com/your_username/your_repository/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print("Fetched script content:")
    print(response.text)
else:
    print(f"Failed to fetch script. Status code: {response.status_code}")
