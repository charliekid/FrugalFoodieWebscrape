import requests
from bs4 import BeautifulSoup

produce_url = 'https://frazierfarmsmarket.com/specials/category/produce'
produce_page = requests.get(produce_url)
produce_soup = BeautifulSoup(produce_page.content, 'html.parser')

protein_url = 'https://frazierfarmsmarket.com/specials/category/meat-seafood'
protein_page = requests.get(protein_url)
protein_soup = BeautifulSoup(protein_page.content, 'html.parser')

# writing out files stuff
sale_items_file = open("SaleItems2.txt", "w")

# Look through the HTML file where the div is 'adItemText'
# after that the item name is after the <h3>
# after that the item price is after the <h5>
for ad_item_text in produce_soup.find_all("div", "adItemText"):
    item_name = ad_item_text.find('h3')
    item_price_line = ad_item_text.find('h5')
    print(item_name.text)
    print(item_price_line.text)
    print()
    sale_items_file.write(item_name.text)
    sale_items_file.write(";")
    #sale_items_file.write(item_price_line.text)
    sale_items_file.write(item_price_line.text)
    sale_items_file.write("\n")

# closing to reopen to append
sale_items_file.close()

# Here we will try for the other pages
sale_items_file = open("SaleItems2.txt", "a")

for protein_ad_item_text in protein_soup.find_all("div", "adItemText"):
    protein_item_name = protein_ad_item_text.find('h3')
    protein_item_price_line = protein_ad_item_text.find('h5')
    print(protein_item_name.text)
    print(protein_item_price_line.text)
    print()
    sale_items_file.write(protein_item_name.text)
    sale_items_file.write(";")
    #sale_items_file.write(item_price_line.text)
    sale_items_file.write(protein_item_price_line.text)
    sale_items_file.write("\n")

sale_items_file.close()
