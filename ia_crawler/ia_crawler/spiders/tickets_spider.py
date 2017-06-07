import scrapy


class TicketsSpider(scrapy.Spider):
	name = "tickets"

	def __init__(self, departLocation=None, arriveLocation=None, month=None, day=None, *args, **kwargs):
		super(TicketsSpider, self).__init__(*args, **kwargs)
		self.start_urls = [
			'https://book.latam.com/TAM/dyn/air/booking/upslDispatcher?B_LOCATION_1=%s&E_LOCATION_1=%s&TRIP_TYPE=O&B_DATE_1=2017%s%s0000&adults=1&children=0&infants=0&LANGUAGE=BR&SITE=JJBKJJBK&WDS_MARKET=BR&MARKETING_CABIN=E' % (departLocation, arriveLocation, month, day),
			'https://www.decolar.com/shop/flights/results/oneway/%s/%s/2017-07-21/1/0/0?from=SB' %(departLocation, arriveLocation),
		]
	#start_urls = [
		#'https://book.latam.com/TAM/dyn/air/booking/upslDispatcher?B_LOCATION_1=SAO&E_LOCATION_1=RIO&TRIP_TYPE=O&B_DATE_1=201706210000&adults=1&children=0&infants=0&LANGUAGE=BR&SITE=JJBKJJBK&WDS_MARKET=BR&MARKETING_CABIN=E',
		#]
	def parse(self, response):
		data = response.css('tr.flight')	#Latam
		# data2 = response.css('div.flights-cluster')	#Decolar
		
		data_day = response.css('aside.stick')
		day = data_day.css('aside.fl p.boxw strong.block::text').extract_first()

		if data:
			for flight in data:
				yield {
					'code' : flight.css('a.linkFlif::text').extract_first(),
					'price' : flight.css('span.price::text').extract_first().strip(),
					'day' : day,
					'departure_location' : flight.css('td.fromTh span.bLocation::text').extract_first(),
					'departure_time' : flight.css('td.fromTh strong::text').extract_first(),
					'arrive_location' : flight.css('td.toTh span.eLocation::text').extract_first(),
					'arrive_time' : flight.css('td.toTh strong::text').extract_first(),	
					'airline' : 'LATAM',
				}
		# elif data2:	
		# 	for flight in data2:
		# 		yield {
		# 			'travel_code' : flight.css('a.linkFlif::text').extract_first(),
		# 			'price' : flight.css('span.price-amount::text').extract_first(),
		# 			'departure_location' : flight.css('a.picasso-link::text').extract_first(),
		# 			# 'departure_time' : flight.css('route-info-item.departure span.hour::text').extract_first(),
		# 			'arrive_location' : flight.css('a.picasso-link::text').extract_first(),
		# 			# 'arrive_time' : flight.css('td.toTh strong::text').extract_first(),	
		# 			'airline' : 'LATAM',
		# 		}