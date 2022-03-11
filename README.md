# Google search result to google sheet
**python version: 3.9**

Search specific keywords in google, and for specific number of the firsts pages, get metadata (title and description) and page structure (headings).

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

# Run

Run the **__main __.py** or the **project folder** with your python 3.9 interpreter.

You can do it from terminal or by **double clicking the file**

## Run sample from terminal:

Before, [open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)

After, type: 

``` bash
$ py __main__.py
```

or

``` bash
$ py.
```

# Settings

Rhere are some few steps before run the project:

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

* ### show_browser

Show (true) or hide (false) the google chrome window.

* ### max_results

Max number of results for save in the google sheet

* ### gs_link

Shared link with edit permissions of your google sheet