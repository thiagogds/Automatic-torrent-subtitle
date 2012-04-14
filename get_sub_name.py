import sys

full_name = sys.argv[1]
short_name = ''

if full_name.find('.HDTV') != -1:
    short_name = full_name[:full_name.find('.HDTV')]

if full_name.find('.720p') != -1:
    short_name = full_name[:full_name.find('.720p')]

print short_name
