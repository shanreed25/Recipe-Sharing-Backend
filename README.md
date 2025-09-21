# Welcome to PlateShare Project
**A Recipe Sharing Application**

### Application Developer Information
- **App Name :** ABC Recipe
- **Developer & Designer Name :** Shannon Reed
- **Web URL :** http://.......


About this file
The purpose of this file is to provide overview, setup instructions and background information of the project. If you have joined this project as a part of the development team, please ensure this file is up to date.

Note : Any dependencies added / modified to this project which affect the running of the code in this git repository must be listed in this file. All developers must ensure that the instructions mentioned in this file are sufficient to enable a new developer to obtain a executable copy of the lastest code in this repository, without invlvement from any other human assistance.

## Tools and Hardware Requirements Declaration

## Project Technical Specifications
**A high level overview of the technologies used in the project and steps involved in generating the final builds for the project**
- Python
- Flask
    - home page: `index.html`
    - category list page: `category_list.html`
        - includes `recipe_category_cards.html`, contains a card for each category
    - a list of recipes for the choosen category: `recipe_category.html`
        - includes `recipe_list.html`, contains a list of recipes for a choosen category
    - `index.html`, `recipe_category.html`, and `category_list.html` all extend base.html
- Boothstrap
- HTML
- CSS
- SQL SERVER



# Version 2: New Features
- use a single dynamic route with a variable for the recipe type
- uses a single file and dynamically passes in the recipe category from the server to get a list for the selected category



