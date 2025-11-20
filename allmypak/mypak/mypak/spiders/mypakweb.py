import scrapy

class AllMyTechCategoriesSpider(scrapy.Spider):
    name = "allmy_categories"
    allowed_domains = ["allmytech.pk"]
    start_urls = ["https://allmytech.pk/"]

    def parse(self, response):
        # Top-level categories
        top_categories = response.css('li.menu-item.item-level-0')
        for category in top_categories:
            # Optional: top category name
            top_cat_name = category.css('a > span.nav-link-text::text').get()
            
            # Sub-categories
            sub_categories = category.css('ul.wd-sub-menu li.item-level-1')
            for sub in sub_categories:
                sub_cat_name = sub.css('a::text').get()
                sub_cat_url = sub.css('a::attr(href)').get()
                if sub_cat_url:
                    yield scrapy.Request(
                        url=sub_cat_url,
                        callback=self.parse_subcategory,
                        meta={'top_category': top_cat_name, 'sub_category': sub_cat_name}
                    )

    def parse_subcategory(self, response):
        top_category = response.meta.get('top_category')
        sub_category = response.meta.get('sub_category')

        # Products in this sub-category
        products = response.css('li.product.type-product')
        for product in products:
            product_name = product.css('h2.woocommerce-loop-product__title::text').get()
            product_url = product.css('a.woocommerce-LoopProduct-link::attr(href)').get()
            if product_name and product_url:
                yield {
                    'top_category': top_category,
                    'sub_category': sub_category,
                    'product_name': product_name.strip(),
                    'product_url': product_url
                }

        # Pagination: next page
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse_subcategory,
                meta={'top_category': top_category, 'sub_category': sub_category}
            )
