BOT_NAME = "echomarket"

SPIDER_MODULES = ["echomarket.spiders"]
NEWSPIDER_MODULE = "echomarket.spiders"

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "echomarket.pipelines.MarketplaceCsvPipeline": 300,
}