# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from steam.items import SteamGameItem, SteamReviewItem
from scrapy.exporters import CsvItemExporter

game_filename = 'game_data.csv'
review_filename = 'review_data.csv'


class SteamPipeline(object):
    ''' Class to handle exporting both game and review items.'''

    def open_spider(self, spider):
        # Dict to save the exporters for both game and review items.
        self.exporters = {}

    def _exporter_for_item(self, item_type):
        ''' Helper function to initialize exporters the first time called,
            and return the correct exporter each time afterwards. Writes
            contents of item to a csv.
        '''
        if item_type not in self.exporters:
            filename = game_filename if item_type == 'game' \
                    else review_filename
            csv = open(filename, 'wb')
            exporter = CsvItemExporter(csv)
            exporter.start_exporting()
            self.exporters[item_type] = exporter
        return self.exporters[item_type]

    def process_item(self, item, spider):
        # print('Processing item: {}'.format(item['title']))
        # Process each item based on the contents of the item
        if isinstance(item, SteamGameItem):
            exporter = self._exporter_for_item('game')
        elif item is SteamReviewItem:
            exporter = self._exporter_for_item('review')
        exporter.export_item(item)
