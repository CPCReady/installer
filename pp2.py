import requests


def get_latest_release ():
    url = f"https://api.github.com/repos/cpcready/installer/releases/latest"
    headers = {}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("name")
    else:
        return "0"
