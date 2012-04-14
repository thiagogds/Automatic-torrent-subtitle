import sys

full_name = sys.argv[1]
short_name = ''
found = False

if full_name.find('.720p') != -1:
    short_name = full_name[:full_name.find('.720p')]
    found = True

if full_name.find('.HDTV') != -1 and not found:
    short_name = full_name[:full_name.find('.HDTV')]


print short_name
