import time
import requests
from DrissionPage import ChromiumPage, ChromiumOptions # 自动化模块
import re  # 正则表达式模块
import os  # 操作系统模块
from func.download_aweme_list import download_aweme_list

# 设置
max_download_num = 40 # 最大视频获取数量
creator = { # 作者sec_id
    "",
    } 

def main(creator):
    global max_download_num
    already_download_nums = 0  # 已经下载的视频数量
    
    url = f"https://www.douyin.com/user/{creator}" # 作者主页链接
    cookie = ""
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"

    # 请求标头
    headers = {
        'Cookie' : cookie,
        'referer' : url,
        'user-agent' : user_agent
    }

    # 将 cookie 字符串转换为结构化列表
    cookie_list = []
    for pair in cookie.split("; "):
        if '=' in pair:
            name, value = pair.split("=", 1) # 保证只分一次（有些值中可能含有 =）
            cookie_list.append({
                'name': name,
                'value': value,
                'domain': '.douyin.com'
            })
    # [
    #     {'name': 'uid_tt', 'value': 'abc123', 'domain': '.douyin.com'},
    #     {'name': 'sid_tt', 'value': 'def456', 'domain': '.douyin.com'},
    #     ...
    # ]
    # 这个结构正是 DrissionPage 中 set.cookies() 所需格式。

    # 第一步：模拟滑动收集URL
    co = ChromiumOptions()
    co.set_argument('--disable-gpu') # 禁用 GPU 硬件加速，避免某些系统上可能出现的兼容性问题
    co.set_argument('--disable-blink-features=AutomationControlled') # 禁用自动化检测，“伪装”为真人浏览器
    co.set_argument('--user-agent=' + user_agent) # 设置浏览器的 User-Agent 字符串，使请求更像普通用户
    # co.set_argument('--headless') # 无头模式（可选），如果不需要可视化浏览器界面，可以启用此选项以提高性能

    Google = ChromiumPage(co)
    Google.get("https://www.douyin.com")  # 必须先访问一个域以便注入 cookie
    Google.set.cookies(cookie_list)
    Google.get(url)
    Google.listen.start("aweme/post")

    time.sleep(5.5) # 第一次登录有五秒的“是否记住登录信息”

    collected_urls = set()
    same_position_count = 0
    last_collected_len = 0

    # 滚动页面并收集URL
    url_num = 0
    while same_position_count < 5:
        Google.scroll.down(500) # 向下滚动
        time.sleep(1)
        
        sjb = Google.listen.wait(timeout=3)
        if sjb and "max_cursor" in sjb.request.url:
            if sjb.request.url not in collected_urls:
                url_num += 1
                collected_urls.add(sjb.request.url)
                print(f"已收集{url_num}个URL: {sjb.request.url}")

        if len(collected_urls) == last_collected_len:
            same_position_count += 1
        else:
            same_position_count = 0
            last_collected_len = len(collected_urls)

    Google.quit()

    # 第二步：处理每个URL
    for idx, request_url in enumerate(collected_urls):
        try:
            print(f"\n处理第 {idx+1} 个链接")
            resp = requests.get(request_url, headers=headers)
            data = resp.json().get('aweme_list', [])
            if not data:
                print("无内容，跳过。")
                continue
            
            already_download_nums = download_aweme_list(data, headers, already_download_nums, max_download_num)
            print(f"已下载 {already_download_nums} 个视频/图片。")
            if already_download_nums >= max_download_num:
                print(f"已达到最大下载数量 {max_download_num}，停止下载。")
                break
        
        except Exception as e:
            print(f"请求或解析失败: {e}")

    print("全部视频/图片下载完成。")
    
if __name__ == "__main__":
    for creator_id in creator:
        main(creator_id)
