# Melakukan import library
import pandas as pd
from google_play_scraper import Sort, reviews_all

# Melakukan proses scraping
scraper_view = reviews_all(
    'id.co.bri.brimo',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=100
)

# Menyimpan hasil scraping ke dalam DataFrame
app_reviews_df = pd.DataFrame(scraper_view)

# Melakukan konversi dari Dataframe ke CSV
app_reviews_df.to_csv('review-dataset.csv', index=False)

