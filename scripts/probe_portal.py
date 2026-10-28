import requests
from bs4 import BeautifulSoup

# Page qui liste les appels d'offres (triés par date de mise à jour)
URL = "https://mr.gov.il/ilgstorefront/he/search/?s=TENDER"
HEADERS = {"User-Agent": "Mozilla/5.0 (tender-agent portfolio project)"}

# 1. Récupérer la page
response = requests.get(URL, headers=HEADERS, timeout=30)
print("Status:", response.status_code)
print("HTML size:", len(response.text))

# 2. Lire le HTML
soup = BeautifulSoup(response.text, "html.parser")
print("Page title:", soup.title.string)

# 3. Séparer les liens d'appels d'offres des autres
tender_links = []
other_links = []

for link in soup.find_all("a", href=True):
    href = link["href"]
    if "/ilgstorefront/he/p/" in href:
        tender_links.append(href)
    else:
        other_links.append(href)

# 4. Résumé
print("Tender links:", len(tender_links))
print("Unique tender links:", len(set(tender_links)))
print("Other links:", len(other_links))
print("First 3:", tender_links[:3])