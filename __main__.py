import os
import time
import urllib.parse
from config import Config
from logs import logger
from scraping_manager.automate import Web_scraping
from config import Config
from spreadsheet_manager.google_ss import SS_manager

keywords = "hola mundo programación"
def main (): 

    # Generate URL
    keywords_text = urllib.parse.quote(keywords.replace(" ", "+"))
    url = f"https://www.google.com/search?q={keywords_text}"

    # Get credentials from config
    credentials = Config()
    headless = not credentials.get ("show_browser")
    max_results = credentials.get ("max_results")
    gs_link = credentials.get ("gs_link")
    gs_credentials = os.path.join (os.path.dirname(__file__), "spreadsheet_manager", "credentials.json")

    print (gs_credentials)
    ss_keyword = SS_manager(gs_link, gs_credentials, "Keyword")
    ss_results = SS_manager(gs_link, gs_credentials, "Results")
    ss_results_structure = SS_manager(gs_link, gs_credentials, "Results structure")

    ss_keyword.worksheet.clear ()

    return None

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

            # Skip pdf files
            if ".pdf" in link:
                continue

            # Save valid links
            result_links.append (link)
            if len (result_links) == max_results:
                more_pages = False
                break      

    # Go to next results page
    if more_pages:
        selector_next = "#pnnext"
        scraper.click (selector_next)

    # Extract data from links pages
    result_position = 0
    data = []
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

        # Get page structure
        selector_structure = "h1, h2, h3, h4, h5, h3"
        headers_elem = scraper.get_elems (selector_structure)
        headers_formated = []
        for header in headers_elem:

            header_text = header.text
            header_tag = header.tag_name
            header_formated = f"<{header_tag}>{header_text}<{header_tag}/>"
            headers_formated.append (header_formated)
        
        # Save data
        data_row = {
            "url": link,
            "position": result_position,
            "title": title, 
            "title_lenght": title_lenght,
            "description": description, 
            "description_lenght": description_lenght,
            "structure": headers_formated
        }
        data.append (data_row)
    
    # Format data for google sheets
    print ("")

if __name__ == "__main__":
    main()