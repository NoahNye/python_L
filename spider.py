## -*-coding:utf-8-*-
import re
import requests

class spider():
	def __init__(self):
		self.url="http://qingbuyaohaixiu.com/archives/"
		self.header="User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

	def spiderget(self,i):
		html = requests.get(self.url+str(i),self.header).text
		self.items = re.findall('<.*?article.*?src="(.*?)" class="attachment.*?/a>.*?/div>', html, re.S)
		return self.items

	def filew(self,i):
		self.sqidergo(i)
		j=0
		for item in self.items:
				pic = requests.get(item, timeout=10)  # 获取图片
				sring = 'pic\\' + str(i) +str(j)+ '.jpg'  # 定义写入地址及格式
				fq = open(sring, 'wb')  # 打开文件连接
				fq.write(pic.content)  # 写入文件
				fq.close()  # 关闭连接
				j+=1

if __name__ == "__main__":
	a = spider()
	try:
		for i in range(1000000):
			a.filew(i)
	except:
		raise
