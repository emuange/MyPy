import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.saruk.co.ke/item/hp-omen-obelisk-desktop-875-amd-ryzen-7-3700x-16gb-ram-256gb-pcie-nvme-m2-ssd-plus-2tb-7200-rpm-sata-8gb-nvidia-geforce-rtx-3070-9068.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price"})
string_price = element.text.strip()
budget = 180000

price_without_symbol = string_price[:]

price = float(price_without_symbol.replace(',',''))

if price < budget:
    print("You can buy this computer it is below your budget!")
else:
    print("You cannot afford this computer! Forget about it!")
