import os
import urllib.parse
from config import Config
from logs import logger
from scraping_manager.automate import Web_scraping
from config import Config

keywords = "hola mundo programación"
def main (): 

    # Generate URL
    keywords_text = urllib.parse.quote(keywords.replace(" ", "+"))
    url = f"https://www.google.com/search?q={keywords_text}"

    # Get credentials from config
    credentials = Config()
    headless = not credentials.get ("show_browser")
    max_results = credentials.get ("max_results")

    # Start browser
    scraper = Web_scraping (headless=headless, web_page=url)

    # Get first results
    selector_results_elems = "#search > div .yuRUbf > a"
    results_elems = scraper.get_elems (selector_results_elems)
    for result_elem in results_elems:
        link = result_elem.get_attribute("href")
        title = result_elem.find_element_by_css_selector ("h3").text
        if not title:
            continue

        print (title, link)


    print ()


if __name__ == "__main__":
    main()