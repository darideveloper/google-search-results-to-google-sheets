<div><a href='https://github.com/github.com/darideveloper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/github.com/darideveloper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/google-search-results-to-google-sheets/blob/master/logo.png?raw=true' alt='Google Search Results To Google Sheets' height='80px'/>

# Google Search Results To Google Sheets

Search specific keywords in google, and for specific number of the firsts pages, get metadata (title and description) and page structure (headings).

Start date: **2022-03-10**

Last update: **2023-04-13**

Project type: **client's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a><a href='https://sheets.google.com/' target='_blank'> <img src='https://www.gstatic.com/images/branding/product/1x/sheets_2020q4_48dp.png' alt='Google Sheets' title='Google Sheets' height='50px'/> </a></div>

# Details

Save all data in a google sheet.

This project works automating a google chrome window.

*Note: the project automatically excludes PDF files, videos and Google questions.*

# Install

## Third party modules

Open Terminal in project folder and install all modules from pip:
(here a tutorial about [how to open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)) 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following programs must be installed:

* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Settings

There are some few steps before run the project:

## Generate a google sheets api key

For use this project, you need to generate a *google sheets api key*, from google console, sand save it in the folder "spreadsheet_manager", width the name "credentials.json". 
Here a tutorial about [how to generate a google sheets api key, step by step](https://github.com/DariHernandez/tutorials/tree/master/generate%20google%20sheets%20api%20key)

**WARNING:** Without the api key, the program will raise and error.

## Google sheets template

For use the program, you need a google spreadsheet with the next sheets: 
* Keywords
* Results meta
* Results structure

You can copy this sample sheet: https://docs.google.com/spreadsheets/d/1mR_WqM2cHQw5OsIyH7jev8s2DCrcz32Zg79_UzS0l1A/edit?usp=sharing 

Create or copy the spreadsheet, and generate a share link with edit permissions (you will need it in the next step)

*Note: Each time that you run the program, the data for each sheet is cleaned. If you want to sae the data, backupo before run the program*


## Config.json

In the *config.json* file, there are the project options (you can create it manually in the project folder)

```json
{
 "show_browser": false,
 "max_results": 10,
 "gs_link": "https://docs.google.com/spreadsheets/d/.../edit?usp=sharing"
}
```

### show_browser

Show (true) or hide (false) the google chrome window.

### max_results

Max number of results for save in the google sheet

### gs_link

Shared link with edit permissions of your google sheet

# Run

Run the **__main __.py** or the **project folder** with your python 3.9 interpreter.

You can do it from terminal or by **double clicking the file**


