from scrapy import Spider, Request
from steam.items import SteamGameItem, SteamReviewItem
from scrapy.http import FormRequest

class SteamSpider(Spider):
    ''' Class statement for the steam spider that is crawls the steam website.
    '''

    name = 'steam_spider'
    allowed_urls = ['https://store.steampowered.com']
    start_urls = ['https://store.steampowered.com/app/10/CounterStrike/']
    #              '&supportedlang=english']
    timeout_urls = 'timeout_urls.list'
    cur_tag_index_pair = 0

    def parse(self, response):
        '''Calls the ids from our csv and their 
        '''

        import re
        import pandas as pd

        game_list = pd.read_csv("steam_ids.csv", usecols = ['steam_appid']).squeeze("columns")
        for index, game in game_list.items():
            game_id = game
            # meta variable that will be passed forward to detail page
            meta = {}
            detail_url = "https://store.steampowered.com/app/" + str(game_id)
            if detail_url.find('/sub/') > 0:
                # Skip entries that point to bundles since not tracking them.
                continue
            meta = {'game_id': game_id}
            yield Request(url=detail_url, callback=self.parse_game_detail,
                          meta=meta, cookies = {
    'wants_mature_content':'1',
    'birthtime':'189302401',
    'lastagecheckage': '1-January-1976',
})

    def parse_game_detail(self, response):
        '''Scrap the entries for an individual game.  '''
        import re
        tag_list = list(map(lambda x: x.strip(), response.xpath(
            '//div[@class="glance_tags popular_tags"]/a/text()').extract()))

        title = response.xpath('.//div[@class="apphub_AppName"]/text()')\
                    .extract_first()
        try:
            deck =  response.css('div#application_config').attrib['data-deckcompatibility']
        except:
            deck = ""

        print(deck)
        # Set booleans
        early_access = response.xpath('//div[@class="early_access_header"' +
                                      ']') != []
        vr_only =  response.xpath('.//span[@class="vr_required"' + 
                                    ']') != []
        vr_supported =  response.xpath('.//span[@class="vr_supported"' + 
                                    ']') != []
        vr_pcinput = list(map(lambda x: x.strip(), response.xpath(
            '//div[@class="VR_warning"]/text()').extract()))

        # Create a new game item and store the scraped data from current game.
        game_item = SteamGameItem()
        game_item['title'] = title
        game_item['deck'] = deck
        game_item['vr_only'] = vr_only
        game_item['vr_supported'] = vr_supported
        game_item['vr_pcinput'] = vr_pcinput
        game_item['game_id'] = response.meta['game_id']
        game_item['tag_list'] = tag_list
        game_item['early_access'] = early_access
        print(game_item)
        return game_item