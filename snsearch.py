# -*- coding: utf-8 -*-

__author__ = 'Sagacity'

import urllib
import xml.dom.minidom

theQuery = u"{query}"
# theQuery = u"io"
theQuery = theQuery.strip().lower()
rssurl = 'http://news.dbanotes.net/rss'
urldoc = xml.dom.minidom.parse( urllib.urlopen( rssurl ) )

print "<?xml version=\"1.0\"?>\n<items>"
for item in urldoc.getElementsByTagName('item'):
    title = item.getElementsByTagName('title')[0].firstChild.data.replace( "&", "##" )
    link = item.getElementsByTagName('link')[0].firstChild.data.replace( "&", "%26" )
    comments = item.getElementsByTagName('comments')[0].firstChild.data.replace( "&", "%26" )

    if (theQuery in title.lower()) or theQuery == "all":
        print "    <item uid=\"SN\" arg=\""+ link + "|" + comments + "\">"
        print "        <title>" + title.encode('utf-8') + "</title>"
        print "        <subtitle>" + comments + "</subtitle>"
        print '''        <icon type="fileicon">/Applications/Safari.app/</icon>
    </item>'''
print "</items>\n"