import time
import requests
from DrissionPage import ChromiumPage, ChromiumOptions # 自动化模块
import re  # 正则表达式模块
import os  # 操作系统模块
from func.download_aweme_list import download_aweme_list

# 设置
max_download_num = 40 # 最大视频获取数量
creator = { # 作者sec_id
    "MS4wLjABAAAA0IZKpfYuk8glL5SEWXAGnc13GDz4ITas4Z1DM9vSbbI",
    } 

def main(creator):
    global max_download_num
    already_download_nums = 0  # 已经下载的视频数量
    
    url = f"https://www.douyin.com/user/{creator}" # 作者主页链接
    cookie = "douyin.com; __ac_nonce=068722f000031658e6f13; __ac_signature=_02B4Z6wo00f01MHL4pgAAIDDX69CCF0UOpDB6-YAAFgG22; enter_pc_once=1; UIFID_TEMP=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee647407b11caad055db1101605067df5d71c1a751074e808e64cc33f1415f69e7e388d11ecbddaa6d17a707ee0fc37d25a9fd2; x-web-secsdk-uid=40d27b04-ff9b-4607-8400-5701d92ec76a; douyin.com; s_v_web_id=verify_md029wd2_3kS1wqVh_n9fd_4Nm1_9t6m_UYfSfFJ3CEyZ; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; hevc_supported=true; dy_swidth=1920; dy_sheight=1080; fpk1=U2FsdGVkX1/R5U1zWfknuMsW/Ujvk//srQRLjOlQSIN2UFfXTHZTICdVuAtPdTmqpZaTcZud/bBtG8roPB83vw==; fpk2=7ddeda88d0c599cc494da0dece6554d5; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22volume%22%3A0.6%2C%22isMute%22%3Atrue%7D; xgplayer_user_id=91112859564; xg_device_score=7.733653425650942; UIFID=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee647407b11caad055db1101605067df5d71c1a962911ed6ec8b6ccbf1f312aa53ebfef0b1b08a0a379c2967276081e6eb2e887dd1edefc03b5c507eafc9acca21d21f0c0ccfee80641703082ca7fbde935977c0ab08cb4add9c8ccb23b96ab45dc05da4d75f7dcd72110cca17f9b06cfcf87abf7f134a21a857cfcac83b5c96934ac01; is_dash_user=1; strategyABtestKey=%221752313614.616%22; passport_csrf_token=7f13e98bbfdad1c85947956a687dfc1f; passport_csrf_token_default=7f13e98bbfdad1c85947956a687dfc1f; __security_mc_1_s_sdk_crypt_sdk=e11fa6f7-430d-b214; bd_ticket_guard_client_web_domain=2; download_guide=%221%2F20250712%2F0%22; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273c36373d373d31343637303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=8IRWe397y5abctkMsCrVHfyB9kkVyBRpE9dA31ODoxjMR-DMxrvyrl2BlU9zmst7HE8AMqTma3KUcqEs0DNvWSEvBSYA6XfW5NAkn3Uhxp34byeWc2r6ZcRgLkPLg3eV3TSgy3GqgIC_C3-QGXqkxGwalZQjensKGN8zMkpO8XLc35woQjG9jbTOJrnFZJnUBzmIas2d_SYCzG3EhOy9en2BTGHWsZaFftPmRaLQHSMutITf-s9EVeufVoK9aaiofiNjcQLclk3iDzW1njP0-XRq3m_y9lgKEPJ11vc9se7mJA9q87pnHLamgLKrLo7E5laOakXa_2_bEXP_9_0bH2j8EfEilDf9lw9ER3ubfYCODA2qMMZkV4OMUkGoD120U9BRGotJy8yPtI-gxVffyq80sp8ih8dHLqm--r9MXf0GgSh4rWytfJDXAoLYawY02plE3ZfjyVYvD4z96Gm6Fj-YGH6tH3U_WKPjW1SsEU6XFltiz6g8JzcynsPE4rXX; gulu_source_res=eyJwX2luIjoiYTlmMjU3NzAxMWQ2OTIyYjc5NWQ5Zjk3NjY1OWVkOTNkMGQ2NjBjMWZhMmNkYzdjMGI4NmI5YTU2YjlhYmU1OCJ9; passport_auth_mix_state=3fs27rdt1cbp6i50c4tdbbmx0x73pgot9upxmttkvg04p24o; passport_assist_user=CkCcxlx7RSrUFa06FXcvX-8ed4dtMwhr3VhTxU0WQVccj7u7Ajd_18sOWP-yOLqPnZLv9y-2pEXKc7ubKYopq7RpGkoKPAAAAAAAAAAAAABPOYTDzlrrl8vmKq-yxFB1KIN1ayig9SIAIO1HGzfCyC7EslTwwDtYXv69nK8O34HjjBDNxfYNGImv1lQgASIBA_WiwLI%3D; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=ab6c29c608fd6d5a7a11741ee23238bd%7C1752314838%7C5184000%7CWed%2C+10-Sep-2025+10%3A07%3A18+GMT; uid_tt=ebaa753d610eb47b5539332b1f6aa836; uid_tt_ss=ebaa753d610eb47b5539332b1f6aa836; sid_tt=ab6c29c608fd6d5a7a11741ee23238bd; sessionid=ab6c29c608fd6d5a7a11741ee23238bd; sessionid_ss=ab6c29c608fd6d5a7a11741ee23238bd; session_tlb_tag=sttt%7C12%7Cq2wpxgj9bVp6EXQe4jI4vf_________6Gn_erjXRUCkWlYzsvRGp7HsQmQVeKSesYVUxqdwpKk0%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KGQ2YjE5NzYzOTQ3NTFhOTlmYTVkYzA4NDNhMzQyMjY4Y2UzZmVmYTYKIAj39-CUwvU7ENbnyMMGGO8xIAww5tOI_gU4B0D0B0gEGgJobCIgYWI2YzI5YzYwOGZkNmQ1YTdhMTE3NDFlZTIzMjM4YmQ; ssid_ucp_v1=1.0.0-KGQ2YjE5NzYzOTQ3NTFhOTlmYTVkYzA4NDNhMzQyMjY4Y2UzZmVmYTYKIAj39-CUwvU7ENbnyMMGGO8xIAww5tOI_gU4B0D0B0gEGgJobCIgYWI2YzI5YzYwOGZkNmQ1YTdhMTE3NDFlZTIzMjM4YmQ; login_time=1752314838159; publish_badge_show_info=%220%2C0%2C0%2C1752314838513%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; SelfTabRedDotControl=%5B%5D; home_can_add_dy_2_desktop=%221%22; _bd_ticket_crypt_cookie=dac10c3a8bfad2afc65361728264e192; __security_mc_1_s_sdk_sign_data_key_web_protect=8108eea2-4e22-9ede; __security_mc_1_s_sdk_cert_key=8d0ba45c-40a8-9bf1; __security_server_data_status=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTWFXN2pXeHkyMXp4UWpvbVN5Y2U1SUdyTXE2bFlNbitjMnZMTVBCYWwyajM5N2NyRHRzL2NMZHNoTmtxUDNUcmQ2OVlIS2FyOWFOeEVMRG5CeUNNWDQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; biz_trace_id=20d53e66; ttwid=1%7CzNbWjmfstt_OUd-PVPVSxSYmpF4_FFvqDCPQlPNsttM%7C1752314845%7C98f61127a88cff4948827ec65eac442c359869674916c59e11bb8ead15f47c28; odin_tt=f7e5da0e15f4438fdf592d57250a1c67311e816cfe837b34e7c6353db2293275e84211732c9024db17e96fa90502ef4818e10097bb821d2e0a1a8ce485b8eb90; IsDouyinActive=false; passport_fe_beating_status=false"
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