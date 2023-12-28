from src import Gmaps

queries = [
   "wyzmindz solutions pvt ltd bengaluru karnataka"
]

Gmaps.places(queries, scrape_reviews=True, max=1, reviews_max=Gmaps.ALL_REVIEWS)