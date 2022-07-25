# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamGameItem(scrapy.Item):
    ''' Class for holding the data scraped from each individual game. '''

    tag_list = scrapy.Field()
    title = scrapy.Field()
    game_id = scrapy.Field()
    early_access = scrapy.Field()
    deck = scrapy.Field()
    vr_only = scrapy.Field()
    vr_supported = scrapy.Field()
    vr_pcinput = scrapy.Field()
    def __str__(self):
        ''' Function to generate a string for printing contents of game item.
        '''

        ret_val = '''Title = {} : game_id = {} : tags = {} : deck = {}
        '''.format(self['title'], self['game_id'], str(self['tag_list']), str(self['deck']))
        ret_val += '''
        Early Access = {}
        '''.format(str(self['early_access']))
        ret_val += '''
        VR Only = {}
        '''.format(str(self['vr_only']))
        ret_val += '''
        VR Supported = {}
        '''.format(str(self['vr_supported']))
        ret_val += '''
        VR with PC Input = {}
        '''.format(str(self['vr_pcinput']))
        return ret_val


class SteamReviewItem(scrapy.Item):
    ''' Class for storing the data scraped from game reviews.
        Currently not used by scraper
    '''

    title = scrapy.Field()
    recommend = scrapy.Field()
    hours_played = scrapy.Field()
    date_posted = scrapy.Field()
    review_text = scrapy.Field()
    username = scrapy.Field()
    products_owned = scrapy.Field()
    num_helpful = scrapy.Field()
    num_funny = scrapy.Field()

    def __str__(self):
        ''' Function to generate a string for printing contents of review item.
        '''
        review_sum = ' '.join(self['review_text'].split()[0:10])
        ret_val = '''
        Title = {}
        Recommend = {}, Hours played = {}, Date posted = {}
        Review = {}
        Username = {}, Products owned = {}
        Number found helpful = {}, Number found funny = {}'''\
        .format(self['title'], str(self['recommennd']),
                self['hours_played'], self['date_posted'], review_sum,
                self['username'], self['products_owned'], self['num_helpful'],
                self['num_funny'])

        return ret_val
