import time
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
    result_links = []
    more_pages = True
    while more_pages:

        results_elems = scraper.get_elems (selector_results_elems)
        for result_elem in results_elems:

            # Get valid links
            link = result_elem.get_attribute("href")
            title = result_elem.find_element_by_css_selector ("h3").text
            if not title:
                continue

            # Save valid links
            result_links.append (link)
            if len (result_links) == max_results:
                more_pages = False
                break      

    # Go to next results page
    selector_next = "#pnnext"
    scraper.click (selector_next)

    # Extract data from links pages
    result_position = 0
    for link in result_links:

        # Open next page
        result_position += 1
        scraper.set_page (link)
        time.sleep (1)

        # Get meta data (title)
        selector_title = "head > title"
        title = scraper.get_elem (selector_title).get_attribute('innerHTML')
        title_lenght = len(title)

        # Get meta data (description)
        selector_description = 'head > meta[name="description"]'
        try:
            description = scraper.get_elem (selector_description).get_attribute('innerHTML')
        except: 
            pass
        else:
            description = ""
        description_lenght = len(description)

        print (description_lenght, description)


if __name__ == "__main__":
    main()