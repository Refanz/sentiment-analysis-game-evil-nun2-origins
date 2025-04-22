from google_play_scraper import app, reviews, Sort, reviews_all
import csv

scraper_view = reviews_all(
    'com.keplerians.evilnun',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=10000
)

with open('evil_nun_reviews.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scraper_view[:10000]:
        writer.writerow([review['content']])

