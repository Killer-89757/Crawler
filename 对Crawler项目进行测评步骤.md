# 对Crawler项目进行测评步骤

> 项目地址：https://github.com/ShilongLee/Crawler
>
> 项目技术：flask、数据库(sqlite)、execjs等
>
> 主要功能：
>
> - 对**抖音**、**bilibili**、**快手**根据接口完成添加用户，获取用户列表、详情页信息、评论信息、回复信息和搜索请求，获取数据
> - bilibili：多一个下载功能
>
> 项目**启动**方式：
>
> - 我的python版本 3.10
> - 创建虚拟环境(略)，`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/`
> - 直接运行main.py文件即可
>
> 使用`postman`进行请求模拟操作
>
> - 文件：Crawler测试项目.postman_collection.json
> - 直接使用postman导入，更换cookie即可使用
>
> 以Bilibili为例，进行详细操作解释，抖音和快手同理

## Bilibili

### 添加用户功能

**cookie的查找**

- 登录后，随便找个视频进入详情页，F12打开控制台，选择Network，清空之前的请求，在刷新一次即可，找到第一个请求，直接将cookie复制出来就行了

![1717340654508](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717340654508-d917c2.png)

```python
注意这个部分是存在过期时间：bili_ticket_expires=1717584123; 
当请求不成功，可能是expires出了问题
```

![1717340876513](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717340876513-15440a.png)

**在postman中进行请求**

![1717341409784](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341409784-7f3c08.png)

在这个地方改了下源码

![1717341194433](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341194433-a25f15.png)

添加成功

![1717341245779](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341245779-6040bc.png)

> 经常性出现这个问题：
>
> ![1717342452616](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717342452616-45ea4f.png)
>
> 可能就是cookie失效了

### 获取账号列表

![1717341377935](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341377935-594bf7.png)

### 获取视频详情

![1717341553948](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341553948-f5aced.png)

![1717341626517](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341626517-2b0272.png)

### 获取视频评论

> 翻页参数自行测试
>
> - offset  搜索翻页偏移量, 默认**0**
> - limit   结果数量, 默认10

![1717341780981](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341780981-fb13dc.png)

### 获取评论回复

> 翻页参数自行测试
>
> - offset  搜索翻页偏移量, 默认**0**
> - limit   结果数量, 默认10

![1717341866377](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341866377-f2b10a.png)

### 关键词搜索视频

> 翻页参数自行测试
>
> - offset  搜索翻页偏移量, 默认**0**
> - limit   结果数量, 默认10

![1717341944074](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717341944074-5730b0.png)

### bilibili视频下载

首先服务要开着，因为脚本中调用了**服务**的detail的接口获取信息

```python
python3 script/bilibili/download.py --id=<video_id> --dir=<dir> --retain=<retain> --hostport=<hostport>
```

![1717342116309](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717342116309-ef24bf.png)

![1717342973168](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717342973168-9ca6d8.png)

## 快手

**cookie的查找**

- 登录后，随便找个视频进入详情页，F12打开控制台，选择Network，清空之前的请求，在刷新一次即可，找到第一个请求，直接将cookie复制出来就行了

![1717343195883](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717343195883-ba54a4.png)

**id的查找**

![1717343415714](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717343415714-bc9e2e.png)![1717343562587](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717343562587-ff965d.png)

## 抖音

**cookie的查找**

- 登录后，https://www.douyin.com/discover，F12打开控制台，选择Network，清空之前的请求，在刷新一次即可，找到第一个请求，直接将cookie复制出来就行了

![1717343692782](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717343692782-b7aa5e.png)**id的查找**

![1717343909386](https://cdn.jsdelivr.net/gh/Killer-89757/PicBed/images/2024%2F06%2F1717343909386-447cb6.png)

- 其中有执行js的代码部分，需要使用到**node.js**的环境(网上很多安装教程)