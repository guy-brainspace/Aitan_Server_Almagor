# “Aitan”Packing House's management tool
This project was developed to assist the packinghouse to be more efficient by capturing it entire activities.


[![](https://mermaid.ink/img/pako:eNptkctOAzEMRX8l8oqKzg9E3SBKJRasukMjIU_iTq3JA_JQBaX_TmZgQmnJyj7Ota7tIyivCSQogzGuGfuAtnWivDvHFo1YfTaNWGc1XNMNx_01faYu4B8sxS27JLCnS7xNgV0venKawnlxlMQntCW8WVwULCaa4WR7snf8BqI27QiHe298qIV4YDsLS_qWUQ1zfjrvNw5W-zWj98gf9Og2RKlihe4B07_6aQW_hjrvjeD4cmCjKwzZVS0swVKwyLpcYtK1kPZkqQVZQk07zCa10LrxK-bkt-9OgUwh0xLyqy4b-bkdyB2aSKcvtHKQnw?type=png)](https://mermaid.live/edit#pako:eNptkctOAzEMRX8l8oqKzg9E3SBKJRasukMjIU_iTq3JA_JQBaX_TmZgQmnJyj7Ota7tIyivCSQogzGuGfuAtnWivDvHFo1YfTaNWGc1XNMNx_01faYu4B8sxS27JLCnS7xNgV0venKawnlxlMQntCW8WVwULCaa4WR7snf8BqI27QiHe298qIV4YDsLS_qWUQ1zfjrvNw5W-zWj98gf9Og2RKlihe4B07_6aQW_hjrvjeD4cmCjKwzZVS0swVKwyLpcYtK1kPZkqQVZQk07zCa10LrxK-bkt-9OgUwh0xLyqy4b-bkdyB2aSKcvtHKQnw)


# Technological tools:
 ![image](https://user-images.githubusercontent.com/58429034/198946311-32c66cd0-5eed-421a-8c4b-35bfc9e88718.png)
 
# DataBase architecture:
 ![image](https://user-images.githubusercontent.com/58429034/198946356-1bf1122b-99c5-481f-b1d5-975c72801595.png)

# Server architecture – example:
 ![image](https://user-images.githubusercontent.com/58429034/198946377-daca0a82-c42b-40d2-9b22-fc45c9886b7b.png)


# Client structure:
 * Components:
      * General comp – Popups, Generic components (table, updatesection , add, edit, table
      * Login –contain username & password (JWT)
      * Main page – contains how all the pages will be designed (main table and infrastructure, actions & reports)
      * Rec_fruit_comp / local market– for each DB table, we can do CRUD
      
 * Redux:
      * For each of the folders above we have the store data updates abilities:
      * Set action types, actions, reducer 
      * Root reducer – combines all the reducer
      * Set of store

 * UTLs:
      * Connections to API
