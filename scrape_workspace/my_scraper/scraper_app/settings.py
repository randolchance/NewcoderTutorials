BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'abcdefgh',
    'database': 'scrape'
}

ITEM_PIPELINES = ['scraper_app.pipelines.LivingSocialPipeline']
