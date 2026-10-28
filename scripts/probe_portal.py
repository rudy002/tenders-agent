import requests

URL = "https://mr.gov.il/ilgstorefront/he/search/?s=TENDER" # ladresse de la page a recuperer

HEADERS = {
    "User-Agent": "Mozilla/5.0 (tender-agent portfolio project)"
}

response = requests.get(URL, headers=HEADERS, timeout=30)


print("Status:", response.status_code)
print("HTML size:", len(response.text))