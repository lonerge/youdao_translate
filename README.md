# 爬取有道翻译结果
get translations from YouDao


2022-1-24

一.抓包对比
发现对有道翻译POST请求中data表单里:i是要翻译的内容;还有三个变化的值分别是: salt sign lts
![image](https://user-images.githubusercontent.com/51309672/150790098-aec2d87b-fd91-4fbc-a527-52bc8fbeac6b.png)

二.解析js
发现lts为13位时间戳; salt为lts加一个随机整数(0-9); sign为"fanyideskweb" + 要翻译内容 + salt + "Y2FYu%TNSbMCxc3t2u^XT"


三.发送POST请求,解析响应,获取翻译结果
![image](https://user-images.githubusercontent.com/51309672/150792745-5332dcda-a7f5-41c9-bc2b-408e602d83d3.png)
