# import scrapy

# class AllMyTechFullSpider(scrapy.Spider):
#     name = "allmytech_full"
#     allowed_domains = ["allmytech.pk"]
#     start_urls = ["https://allmytech.pk/"]

#     def parse(self, response):
#         # Top-level categories
#         top_categories = response.css('li.menu-item.item-level-0')
#         for category in top_categories:
#             top_cat_name = category.css('a > span.nav-link-text::text').get()
            
#             # Sub-categories
#             sub_categories = category.css('ul.wd-sub-menu li.item-level-1')
#             for sub in sub_categories:
#                 sub_cat_name = sub.css('a::text').get()
#                 sub_cat_url = sub.css('a::attr(href)').get()
#                 if sub_cat_url:
#                     yield scrapy.Request(
#                         url=sub_cat_url,
#                         callback=self.parse_subcategory,
#                         meta={'top_category': top_cat_name, 'sub_category': sub_cat_name}
#                     )

#     def parse_subcategory(self, response):
#         top_category = response.meta.get('top_category')
#         sub_category = response.meta.get('sub_category')

#         # Products in this sub-category
#         products = response.css('li.product.type-product')
#         for product in products:
#             product_url = product.css('a.woocommerce-LoopProduct-link::attr(href)').get()
#             if product_url:
#                 # Go to product detail page
#                 yield scrapy.Request(
#                     url=product_url,
#                     callback=self.parse_product,
#                     meta={'top_category': top_category, 'sub_category': sub_category}
#                 )

#         # Pagination: next page
#         next_page = response.css('a.next.page-numbers::attr(href)').get()
#         if next_page:
#             yield scrapy.Request(
#                 url=next_page,
#                 callback=self.parse_subcategory,
#                 meta={'top_category': top_category, 'sub_category': sub_category}
#             )

#     def parse_product(self, response):
#         top_category = response.meta.get('top_category')
#         sub_category = response.meta.get('sub_category')

#         # Product name
#         product_name = response.css('h1.product_title::text').get()
#         if product_name:
#             product_name = product_name.strip()

#         # Price
#         price = response.css('p.price span.woocommerce-Price-amount bdi::text').get()
#         if price:
#             price = price.strip()

#         # SKU
#         sku = response.css('span.sku::text').get()
#         if sku:
#             sku = sku.strip()

#         # Categories
#         categories = response.css('span.posted_in a::text').getall()

#         # Brand
#         brand = response.css('div.wd-product-brands img::attr(alt)').get()

#         # Rating
#         rating = response.css('div.star-rating span.rating::text').get()

#         # Review count
#         review_count = response.css('a.woocommerce-review-link span.count::text').get()

#         # Images
#         images = response.css('figure.woocommerce-product-gallery__image a::attr(href)').getall()

#         yield {
#             'top_category': top_category,
#             'sub_category': sub_category,
#             'product_name': product_name,
#             'price': price,
#             'sku': sku,
#             'categories': categories,
#             'brand': brand,
#             'rating': rating,
#             'review_count': review_count,
#             'images': images,
#             'url': response.url
#         }