import requests
from DrissionPage import ChromiumPage, ChromiumOptions # 自动化模块
import re  # 正则表达式模块
import os  # 操作系统模块

url = ""
cookie = ""
user_agent = ""

os.makedirs('media', exist_ok=True)  # 创建文件夹 
os.makedirs('media/videos', exist_ok=True)
os.makedirs('media/images', exist_ok=True)

# 创建无头浏览器实例
co = ChromiumOptions()
co.set_argument('--headless')  # 设置为无头模式
co.set_argument('--disable-gpu')  # 可选，防止部分渲染问题
Google = ChromiumPage(co)  

Google.listen.start("aweme/post")  # 启动监听
Google.get(url)

sjb = Google.listen.wait()  # 等待页面加载
JSON = sjb.response.body  # 获取页面JSON数据
# print(JSON)  # 打印JSON数据

headers = {
    'cookie' : cookie,
    'referer' : url,
    'user-agent' : user_agent
}

data = JSON['aweme_list']
for i in data:
    title = i['desc'].strip().split('\n')[0] # 获取标题
    title_ulti = re.sub('[\\/:*?"<>|]~`+=', '', title)# 替换非法字符
    
    # 视频
    if i['images'] is None: #纯视频的值为none，确保不下载动图视频的音乐
        try:
            video_url = i['video']['play_addr']['url_list'][0]  # 获取视频地址
            res_video = requests.get(video_url, headers=headers).content  # 发送请求获取视频内容
            with open(f"media/videos/{title_ulti}.mp4", 'wb') as f:
                f.write(res_video)  
                print(f"视频: {title_ulti} 下载完成")  # 打印下载完成信息
        except Exception as e:
            print(f"{title_ulti} 视频下载出错: {e}")
    
    # 动图
    try:
        for idx, j in enumerate(i['images']):
            gif_url = j['video']['play_addr']['url_list'][0]
            res_gif = requests.get(gif_url, headers=headers).content
            filename = f"{title_ulti}_{idx}.mp4"
            with open(f"media/videos/{filename}", 'wb') as f:
                f.write(res_gif)
                print(f"动图：{filename} 下载完成")
    except:
        print(f"{title_ulti} 不是图片视频。")
    
    # 图片
    try:
        for idx, j in enumerate(i['images']):
            image_url = j['url_list'][0]
            res_image = requests.get(image_url, headers=headers).content
            filename = f"{title_ulti}_{idx}.webp"
            with open(f"media/images/{filename}", 'wb') as f:
                f.write(res_image)
                print(f"图片：{filename} 下载完成")
    except:
        print(f"{title_ulti} 不是图片视频。")
    
print("所有文件下载完成")
Google.quit()  # 关闭浏览器
