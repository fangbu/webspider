# encoding=utf-8

import urllib
from bs4 import BeautifulSoup

debug = True # 设置是否打印log
def log(message):
    if debug:
        print message

def download_image(url, save_path): 
    ''' 根据图片url下载图片到save_path '''
    try:
        urllib.urlretrieve(url, save_path)
        log('Downloaded a image: ' + save_path)
    except Exception, e:
        print 'An error catched when download a image:', e

def load_page_html(url):
    ''' 得到页面的HTML文本 '''
    log('Get a html page : ' + url)
    return urllib.urlopen(url).read()

def down_page_images(page, save_dir):
	''' 下载第page页的图片 '''
	html_context = load_page_html('http://www.miyijia.com/?o=1&page=%d.html' % page)
	soup = BeautifulSoup(html_context)
	cont = soup.findAll('div',{ 'class':'contbox'})
	for cover in cont:
		tiny = cover.find('img')
		if tiny is not None and  tiny.has_attr('src') :
			src = tiny.attrs['src'] 
			height = tiny.attrs['height']
			filename = '%s.jpg' % (height) 
			download_image(src, save_dir + filename)
		else :
			print aaaaaaaaaaaaaaa

def download_myj(frm=1, page_count=1, save_dir='.\home\\fangbu\\'):
	for x in xrange(frm, frm + page_count):
		log('Page : ' + `x`)
		down_page_images(x, save_dir)

def main():
	base_path = '~\home\\fangbu\\'
	download_myj(frm=1, page_count=10, save_dir=base_path)

if __name__ == '__main__':
	main()
