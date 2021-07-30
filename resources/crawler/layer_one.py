import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--incognito")
options.add_argument("--window-size=1920x1080")

# Driver path
driver = webdriver.Chrome(options=options, executable_path="../chromedriver_win32/chromedriver.exe")

'''

Layer one should contain Author(Profile) name and its url.
Layer two should have Author's paper link and name
Layer three should have paper description 

'''


def layer_one():
    # Locate an elements contains
    # Initialise variable

    # start url
    print("Layer one is starting")
    url = "https://pureportal.coventry.ac.uk/en/organisations/coventry-university/persons/"
    driver.get(url)
    print("Chrome is open")
    time.sleep(2)  # async function

    layer_one_data = pd.DataFrame(columns=["df_author_name", "df_author_url"])
    data = {}
    while True:
        page = 20
        for no_of_page in range(page):
            print("#########")
            print("Layer one")

            for i in range(49):
                print(str(i) + "th number")
                author_name = driver.find_elements_by_css_selector(
                    "#main-content > div > section > ul > li.grid-result-item.grid-result-item-" + str(
                        i) + " > div > div > h3 > a > span")
                author_names = [el.text for el in author_name]
                print("Obtaining name", author_names)

                authorHyperlinkParser = driver.find_elements_by_css_selector(
                    "#main-content > div > section > ul > li.grid-result-item.grid-result-item-" + str(
                        i) + "> div > div > h3 > a")
                author_url = [el.get_attribute('href') for el in authorHyperlinkParser]
                print("Obtaining hyperlink", author_url)

                print("Current t", i)
                print("Parsing into Dataframe")

                print("Pasting name")
                data['df_author_name'] = author_names

                print("Pasting url")
                data['df_author_url'] = author_url
                layer_one_data = layer_one_data.append(data, ignore_index=True)

            layer_one_data.to_csv("./layer_one.csv", index=False)
            print("CSV saved")
            driver.get("https://pureportal.coventry.ac.uk/en/organisations/coventry-university/persons/?page=" + str(
                no_of_page))

        layer_one_data.to_csv("./layer_one.csv", index=False)
        print("CSV saved")
        print("End of layer one")
        driver.close()
        return True
