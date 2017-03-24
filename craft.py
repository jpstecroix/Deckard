import requests
from bs4 import BeautifulSoup

def get_craft(mc_item):
    #print(mc_item)
    r = requests.get('https://www.minecraftcraftingguide.net/search/?s=%s' % mc_item)
    #print(r.status_code)
    soup = BeautifulSoup(r.content, "html.parser")
    craft_recipes = soup.find_all("div", attrs={"class": "craftingContainer"})
    if craft_recipes == None:
        return "Cannot find craft recipe"
    #Sprint(craft_recipe)
    for craft in craft_recipes:
        craft_images = craft.find_all("img")
        return craft_images
        bob = dict()
        for craft_image in craft_images:

            print(craft_image.get('alt'))
            print(craft_image.get('src'))
            print(craft_image.get('title'))
        #    return craft_image

    #return craft_recipe


#print(get_craft('glass'))
for craft in get_craft('glass'):
    print(craft)
