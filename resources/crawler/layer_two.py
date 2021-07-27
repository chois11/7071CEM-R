import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--incognito")
options.add_argument("--window-size=1920x1080")

# Driver path
driver = webdriver.Chrome(options=options, executable_path="../chromedriver_win32/chromedriver.exe")


def layer_two(layer_one_file):
    """

    The objective of layer two is obtain the list of papers and its urls, in order to start layer three.
    The function will retrieve url from layer one and will obtain the list of paper name and its url for next layer.

    Layer two data has paper title, paper url

    """

    # Define dataframe for second layer
    layer_two_data = pd.DataFrame(columns=["df_paper_title", "df_title_url"])
    data = {}

    df_layer_one_file = pd.read_csv(layer_one_file)
    print("Loading dataframe")
    print(df_layer_one_file)

    df_layer_one_file['df_author_name'] = df_layer_one_file['df_author_name'].str.strip('[]')
    df_layer_one_file['df_author_name'] = df_layer_one_file['df_author_name'].str.strip("''")

    df_layer_one_file['df_author_url'] = df_layer_one_file['df_author_url'].str.strip('[]')
    df_layer_one_file['df_author_url'] = df_layer_one_file['df_author_url'].str.strip("''")

    # print(df_layer_one_file["df_author_url"][0])
    time.sleep(2)

    for i in range(len(df_layer_one_file["df_author_url"])):
        print("Moving to " + (df_layer_one_file["df_author_url"][i] + "/publications/"))
        driver.get((df_layer_one_file["df_author_url"][i] + "/publications/"))  # Moves to unique paper page
        paperTitle = driver.find_elements_by_css_selector(
            ".rendering_short.rendering_contributiontojournal_short > h3 > a > span")
        paperTitles = [el.text for el in paperTitle]

        # del paperTitles[0:2]
        print(paperTitles)

        num_of_titles = len(paperTitles)
        print("num_of_titles " + str(num_of_titles))

        for s in range(num_of_titles):
            print("Current title no. " + str(s))

            print("Pasting title")
            print(paperTitles[s])
            data['df_paper_title'] = paperTitles[s]

            paperlinkParser = driver.find_elements_by_css_selector(
                ".rendering_short.rendering_contributiontojournal_short > h3 > a")
            paperlink = [el.get_attribute('href') for el in paperlinkParser]

            print("Pasting url")
            print(paperlink[s])
            data['df_title_url'] = paperlink[s]

            layer_two_data = layer_two_data.append(data, ignore_index=True)

            layer_two_data.to_csv("./layer_two_data.csv", index=False)
            time.sleep(2)

    layer_two_data.to_csv("./layer_two_data.csv", index=False)
    print("CSV saved")
    print("End of layer two")
    driver.close()
    return True
