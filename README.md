# allmytech-scraper
Scrapy spiders for allmytech.pk that scrape all categories, sub-categories, product links, and detailed product information, including price, SKU, brand, images, ratings, and reviews.
git clone <your-repo-url>
cd <repo-folder>
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
scrapy crawl allmy_categories -o categories.json
scrapy crawl allmytech_product_details -o products.json
scrapy crawl allmytech_full -o fulldetails.json
Some pages may return 403 due to website restrictions; using user-agent headers or rotating proxies may help.
Output is saved in JSON format by default, but Scrapy supports CSV, XML, etc.
you have to add your own pipelines i am saving it manually by using this scrapy command.
scrapy crawl allmy_categories -o categories.json
