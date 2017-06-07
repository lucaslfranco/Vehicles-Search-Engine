import scrapy


class CarsSpider(scrapy.Spider):
	name = "cars"

	def __init__(self, car=None, *args, **kwargs):
		self.start_urls = [
			'http://www.buscaacelerada.com.br/carro/%s' % car,
		]
		
	def parse(self, response):
		self.allowed_domains = ['http://www.buscaacelerada.com.br']

		data = response.css('li.item-offer')	#Latam
		if data:
			for car in data:
				yield {
					'model' : car.css('h2.title::text').extract_first().strip(),
					'price' : car.css('span.price::text').extract_first().strip().split(' ')[1],
					'year' : car.css('span.date::text').extract_first().strip(),
					'location' : car.css('span.location::text').extract_first().strip().split('/')[1],
					'tags' : car.css('h2.title::text').extract_first().strip().split(' '),
					'url' : self.allowed_domains[0] + car.css('a::attr(href)').extract_first()
				}

			next_page = response.css('div.pagination a[id=btnMaisResultados]::attr(href)').extract_first()
	        if next_page is not None:
				next_page = response.urljoin(next_page)
				yield scrapy.Request(next_page, callback=self.parse)