import scrapy

class AllMyTechProductSpider(scrapy.Spider):
    name = "allmytech_product_details"
    allowed_domains = ["allmytech.pk"]
    start_urls = [
        "https://allmytech.pk/product/iphone-17-pro-max-17-pro-benks-glasswarrior-lens-protector-6948005961657-a/"
    ]

    def parse(self, response):
        # Product name
        product_name = response.css('h1.product_title::text').get()
        if product_name:
            product_name = product_name.strip()

        # Price
        price = response.css('p.price span.woocommerce-Price-amount bdi::text').get()
        if price:
            price = price.strip()

        # SKU
        sku = response.css('span.sku::text').get()
        if sku:
            sku = sku.strip()

        # Categories
        categories = response.css('span.posted_in a::text').getall()

        # Brand
        brand = response.css('div.wd-product-brands img::attr(alt)').get()

        # Rating
        rating = response.css('div.star-rating span.rating::text').get()

        # Review count
        review_count = response.css('a.woocommerce-review-link span.count::text').get()

        # Images
        images = response.css('figure.woocommerce-product-gallery__image a::attr(href)').getall()

        yield {
            'product_name': product_name,
            'price': price,
            'sku': sku,
            'categories': categories,
            'brand': brand,
            'rating': rating,
            'review_count': review_count,
            'images': images,
            'url': response.url
        }
