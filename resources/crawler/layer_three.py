import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--incognito")
options.add_argument("--window-size=1920x1080")

# Driver path
driver = webdriver.Chrome(options=options, executable_path="../chromedriver_win32/chromedriver.exe")


def layer_three(layer_two_file):
    '''

    This layer will retrieve layer_two.csv.
    Layer one contains author name and its profile url
    Layer two contains paper name and its url.

    The objective of layer three is retrieve paper title, description, paperlink, authors and date.
    This is the final layer to obtain the data.

    '''

    # Define dataframe for third layer
    layer_three_data = pd.DataFrame(
        columns=["df_paper_title", "df_paper_url", "df_paper_abstract", "df_paper_author", "df_paper_date"])
    data = {}

    df_layer_two_file = pd.read_csv(layer_two_file)
    print("Loading dataframe")
    print(df_layer_two_file)
    print("dataframe loaded")

    for i in range(len(df_layer_two_file["df_title_url"])):
        time.sleep(2)
        print("Moving to " + (df_layer_two_file["df_title_url"][i]))
        driver.get(df_layer_two_file["df_title_url"][i])  # Moves to unique paper page
        print("No of paper accessed", i)

        # columns = ["df_paper_title", "df_paper_doi", "df_paper_abstract", "df_paper_author", "df_paper_date"])

        # Obtain title
        paperTitle = driver.find_elements_by_css_selector(".container > div > div > div:nth-child(1) > h1")
        paperTitles = [el.text for el in paperTitle]
        print("Pasting paper title")
        data['df_paper_title'] = paperTitles

        # Obtain link
        paper_title_links = driver.find_elements_by_css_selector(
            ".rendering_contributiontojournal_publicationaccessrenderer > ul.dois > li > div > a")
        paperlink = [el.get_attribute("href") for el in paper_title_links]
        print("Pasting paper url")
        data['df_paper_url'] = paperlink

        # Obtain Abstract
        paper_abstract = driver.find_elements_by_css_selector(
            ".rendering_abstractportal.rendering_contributiontojournal_abstractportal > div")
        paper_abstracts = [el.text for el in paper_abstract]
        print("Pasting paper abstract")
        data['df_paper_abstract'] = paper_abstracts

        # Obtain authors
        paper_authors = driver.find_elements_by_css_selector(
            ".rendering_contributiontojournal_associatespersonsclassifiedportal > p > a:nth-child(1) > span")
        paper_author = [el.text for el in paper_authors]
        print("Pasting paper authors")
        data['df_paper_author'] = paper_author

        # Obtain publication date
        paper_publication_dates = driver.find_elements_by_css_selector(
            ".rendering_contributiontojournal_detailsportal > div > table > tbody > tr.status > td > span.date")
        paper_publication_date = [el.text for el in paper_publication_dates]
        print("Pasting paper publication date")
        data['df_paper_date'] = paper_publication_date

        layer_three_data = layer_three_data.append(data, ignore_index=True)

        layer_three_data.to_csv("./layer_three_data.csv", index=False)
        print("CSV saved, number of paper", i)

    df_layer_three_file = pd.read_csv(layer_three_data)

    df_layer_three_file['df_paper_title'] = df_layer_three_file['df_paper_title'].str.strip('[]')
    df_layer_three_file['df_paper_title'] = df_layer_three_file['df_paper_title'].str.strip("''")

    df_layer_three_file['df_paper_url'] = df_layer_three_file['df_paper_url'].str.strip('[]')
    df_layer_three_file['df_paper_url'] = df_layer_three_file['df_paper_url'].str.strip("''")

    df_layer_three_file['df_paper_abstract'] = df_layer_three_file['df_paper_abstract'].str.strip('[]')
    df_layer_three_file['df_paper_abstract'] = df_layer_three_file['df_paper_abstract'].str.strip("''")

    df_layer_three_file['df_paper_author'] = df_layer_three_file['df_paper_author'].str.strip('[]')
    df_layer_three_file['df_paper_author'] = df_layer_three_file['df_paper_author'].str.strip("''")

    df_layer_three_file['df_paper_date'] = df_layer_three_file['df_paper_date'].str.strip('[]')
    df_layer_three_file['df_paper_date'] = df_layer_three_file['df_paper_date'].str.strip("''")

    df_layer_three_file.to_csv("./layer_three_data.csv", index=False)
    print("CSV saved")

    print("End of layer three")
    driver.close()
    return True


layer_three("layer_two_data.csv")
