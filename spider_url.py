## -*-coding:utf-8-*-
import re
import requests
for a in range(4,6,1):
    url='http://qingbuyaohaixiu.com/page/'+str(a) #定义要爬的页数
    html=requests.get(url).text
    pic_url=re.findall('<.*?article.*?src="(.*?)" class="attachment.*?/a>.*?/div>',html,re.S)#筛选图片地址
    # print pci_url
    j=0#图片按序号排列
    for item in pic_url:
        print item
        pic=requests.get(item,timeout=10)#获取图片
        sring='pic\\'+str(j)+'.jpg'#定义写入地址及格式
        fq=open(sring,'wb')#打开文件连接
        fq.write(pic.content)#写入文件
        fq.close()#关闭连接
        j+=1 #图片序号自加
