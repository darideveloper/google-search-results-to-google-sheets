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

    # Set spreadsheet 
    ss_manager = SS_manager(gs_link, gs_credentials)

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
        # scraper.go_bottom ()
        scraper.refresh_selenium()

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
        selector_structure = "h1, h2, h3, h4, h5, h6"
        headers_elem = scraper.get_elems (selector_structure)
        headers_formated = []
        for header in headers_elem:

            header_text = header.text
            header_tag = header.tag_name

            # Skip empty or hide tags
            if not header_text:
                continue

            header_formated = f"<{header_tag}> {header_text}"
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
    

    # KEYWORDS SHEET
    # Set sheet and clean
    ss_manager.change_sheet ("Keywords")
    ss_manager.worksheet.clear ()

    # Create header
    data_formated = []
    data_formated.append (["Google Main Keyword"])

    # Format data
    data_formated.append ([keywords])

    # Save
    ss_manager.worksheet.update ("A1", data_formated)


    # META SHEET
    # Set sheet and clean
    ss_manager.change_sheet ("Results meta")
    ss_manager.worksheet.clear ()

    # Create header
    data_formated = []
    data_formated.append (["Position", "Meta Title", "Length", "Meta Description", "Length", "URL"])

    # Format data
    for page in data:
        row_formated = [
            page["position"],
            page["title"],
            page["title_lenght"],
            page["description"],
            page["description_lenght"],
            page["url"],
        ]
        data_formated.append (row_formated)
    
    # Save
    ss_manager.worksheet.update ("A1", data_formated)


    # STRUCTURE SHEET
    # Set sheet and clean
    ss_manager.change_sheet ("Results structure")
    ss_manager.worksheet.clear ()
    data_formated = []
    data_name = ["Name"]
    data_url = ["URL"]
    data_title = ["Meta Title"]
    data_description = ["Meta Description"]
    data_structure_header = ["Page Structure"]
    data_structure = []
    structure_max_rows = 0

    # Format general data
    for page in data:

        # Get page domain
        domain = urllib.parse.urlparse(page["url"]).netloc

        # Order data in correct list
        data_name.append (domain)
        data_url.append (page["url"])
        data_title.append (page["title"])
        data_description.append (page["description"])

        structure_rows = len (page["structure"])
        if structure_rows > structure_max_rows:
             structure_max_rows = structure_rows
    
    # Format structure data
    for structure_column in range (structure_max_rows):

        # add new column
        data_structure.append ([])

        # Save row data
        for page in data:
            if len(page["structure"]) >= structure_column + 1:
                data_structure[structure_column].append (page["structure"][structure_column])
            else:
                data_structure[structure_column].append ("")

    # Save sublists in main list
    data_formated.append (data_name)
    data_formated.append (data_url)
    data_formated.append (data_title)
    data_formated.append (data_description)
    data_formated.append (data_structure_header)

    # Save general data
    ss_manager.worksheet.update ("A1", data_formated)

    # Save data structure
    ss_manager.worksheet.update ("B5", data_structure)


if __name__ == "__main__":
    main()