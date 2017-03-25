import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


def get_craft(mc_item):
    url = "https://www.minecraftcraftingguide.net/search/?s=%s" % quote_plus(mc_item)
    r = requests.get(url)
    if r.status_code != 200:
        return "Cannot connect to server"
    soup = BeautifulSoup(r.content, "html.parser")
    craft_recipes = soup.find_all("div", attrs={"class": "craftingContainer"})
    if craft_recipes is None:
        return "Cannot find craft recipe"
    for craft in craft_recipes:
        craft_images = craft.find_all("img")
        resultarray = []
        for craft_image in craft_images:
            resultarray.append({'alt': craft_image.get('alt'), 'src': craft_image.get('src'), 'title': craft_image.get('title'), 'url': url})
        return resultarray
