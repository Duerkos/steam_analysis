# steam_analysis
Conclusions here: https://duerkos.github.io/steam_analysis/
As a pet project, I wanted to explore Steam data.

The acquisition and cleaning are more documented here in github. In this dataset you can find the cleaned data, as well as some minor files that I extracted to support the analysis. I mainly extracted data from Steam API, Steam Spy (which at the end was not much useful), Steam Reviews API and the Steam web with a web-scraping tool ( https://scrapy.org/ )

A preliminary version (unclean, raw data and a bit more outdated) can be found here: https://www.kaggle.com/datasets/vicentearce/steam-and-steam-spy-raw-datasets

Although the process has diverged much from my original version, I could not have began to do it without following the work from Nik Davis, with minor diferences in the gathering code.
See https://www.kaggle.com/nikdavis/steam-store-raw

Also thanks to Sean Justice, I used his scrapy bot and modified what I wanted to obtain https://github.com/scjustice/steam_webscraper.
Changes:
Added method to bypass age check, with cookies (the method Sean uses is not valid anymore)
Instead of looking for IDs in the steam search pages, I provide them manually from the records from the API.
The data I get is different (but that part is very easy to modify)

If I had to do it again, I think I would use only scrapy and forget about the Steam API. Why? Well, the Steam API seems a bit outdated and there is data that is not being stored, such as Tags,Early Access, VR compatibility and now Steam Deck compatibility. It also allows a faster pulling rate than the Steam API which only allows 200 entries every 5 minutes (or something similar). However, it is true that it might contain some information which is not visible in the store.

The notebooks with the exploratory data which contains extra plots, and of course the data itself after cleaning can be found in kaggle, here: https://www.kaggle.com/datasets/vicentearce/steamdata

The results are in the conclusions html.
