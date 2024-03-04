#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    """fetches https://intranet.hbtn.io/status"""
    import urllib.request
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
