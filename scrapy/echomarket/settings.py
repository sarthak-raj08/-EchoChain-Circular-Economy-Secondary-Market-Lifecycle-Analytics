BOT_NAME = "echomarket"

SPIDER_MODULES = ["echomarket.spiders"]
NEWSPIDER_MODULE = "echomarket.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "echomarket.pipelines.EchomarketPipeline": 300,
}