from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd
import time

options = Options()
options.add_argument("--incognito")
options.add_argument("--window-size=1920x1080")

# Driver path
driver = webdriver.Chrome(options=options, executable_path="./chromedriver_win32/chromedriver.exe")


def layer_three(layer_two_file):

    '''

    This layer will retrieve layer_two.csv.
    Layer one contains author name and its profile url
    Layer two contains paper name and its url.

    The objective of layer three is retrieve paper title, description, paperlink, authors and date.
    This is the final layer to obtain the data.

    '''

    base_url = "https://scholar.google.co.uk"

    # Define dataframe for third layer
    layer_three_data = pd.DataFrame(
        columns=["df_paper_title", "df_paper_url", "df_paper_description", "df_paper_author", "df_paper_date"])
    data = {}

    df_layer_two_file = pd.read_csv(layer_two_file)
    print("Loading dataframe")
    print(df_layer_two_file)
    print("dataframe loaded")

    for i in range(len(df_layer_two_file["df_paper_url"])):
        time.sleep(2)
        print("Moving to " + (base_url + df_layer_two_file["df_paper_url"][i]))
        driver.get(base_url + df_layer_two_file["df_paper_url"][i])  # Moves to unique paper page
        print("No of paper accessed", i)

        # Obtain title
        paperTitle = driver.find_elements_by_css_selector(".gsc_vcd_title_link")
        paperTitles = [el.text for el in paperTitle]
        print("Pasting paper title")
        data['df_paper_title'] = paperTitles

        # Obtain link
        paper_title_links = driver.find_elements_by_css_selector(".gsc_vcd_title_link")
        paperlink = [el.get_attribute("href") for el in paper_title_links]
        print("Pasting paper url")
        data['df_paper_url'] = paperlink

        # Obtain Description
        paper_descriptions = driver.find_elements_by_xpath("//*[@id='gsc_vcd_descr']/div")
        paper_description = [el.text for el in paper_descriptions]
        print("Pasting paper description")
        data['df_paper_description'] = paper_description

        # Obtain authors
        paper_authors = driver.find_elements_by_xpath("//*[@id='gsc_vcd_table']/div[1]/div[2]")
        paper_author = [el.text for el in paper_authors]
        print("Pasting paper authors")
        data['df_paper_author'] = paper_author

        # Obtain publication date
        paper_publication_dates = driver.find_elements_by_xpath("//*[@id='gsc_vcd_table']/div[2]/div[2]")
        paper_publication_date = [el.text for el in paper_publication_dates]
        print("Pasting paper publication date")
        data['df_paper_date'] = paper_publication_date

        layer_three_data = layer_three_data.append(data, ignore_index=True)
        print(layer_three_data)

        layer_three_data.to_csv("./layer_three_data.csv", index=False)
        print("CSV saved, number of i", i)

        time.sleep(2)

    print("End of layer three")
    print("File crawling completed with" + "Papers")

    # Inner function for crawler

    # layer_one()
    # layer_two("layer_one_bak.csv")
    # layer_three("layer_two_data.csv")