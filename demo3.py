import requests        #导入requests包
url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)