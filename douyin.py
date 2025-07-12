import requests
from DrissionPage import ChromiumPage, ChromiumOptions # 自动化模块
import re  # 正则表达式模块
import os  # 操作系统模块

url = ""
cookie = "UIFID_TEMP=3af258ad659545d9553f15cf32bb8a88df248991ebb865c20b5fa6f7dab6eb54779588e82ce7117d7aea4e6dfdcf799363dc7540ad3bf7ab783ff8d0c4ec009dff4601945350bca795802b002aee369ae9f9a8772cd6db10a86540894d6cc470ef8135eac3e4e6e1781a9931762ae8ca; hevc_supported=true; fpk2=9258db5fffd4f17a8703a19e760af505; fpk1=U2FsdGVkX1+cHjDUyV85caNaW+zH5eRGDuMJNhwzaaysXslcVwiln/4bWUqeqGZhzu5J48hTOYShvDYVb36iow==; bd_ticket_guard_client_web_domain=2; UIFID=3af258ad659545d9553f15cf32bb8a88df248991ebb865c20b5fa6f7dab6eb54779588e82ce7117d7aea4e6dfdcf799363dc7540ad3bf7ab783ff8d0c4ec009da71e4ec16c21aac757bf34f79e0b260a4a87643250ca8e38ceefdfe186b3ebcab67e60391e73817978e0fa1ce8361b3d6379906d3104f3c6d28105eeac56cf916d8a5ef910f1300861bf0221a59142192539698fdb5e42765cec53072bafed304dd214d3a10cd685d1171e4ae7fec36e166c1a995cc7743334d4071fd51102d5; passport_assist_user=CjzIlRfxPmrH3vqiFG4FcM_7UkMhGZBbL0dr6UCbBX6jzTqLwxemQrBFnShkFUAS5oEbO26M0pfsABn-VSsaSgo8XYBRn39XNdXc_-jNTlkd2hBSpjR-HfzvjrBXnf0vydmNIzhLJaGE6cYGYzI6eppps-oiHxAJRIzMaQhmELKm6w0Yia_WVCABIgEDwT0hIg%3D%3D; uid_tt=13b171539f8e5003a458b3f3d4058714; uid_tt_ss=13b171539f8e5003a458b3f3d4058714; sid_tt=7eec55b17629546a887363fad047d22a; sessionid=7eec55b17629546a887363fad047d22a; sessionid_ss=7eec55b17629546a887363fad047d22a; is_staff_user=false; store-region=cn-ln; store-region-src=uid; login_time=1741270315337; SelfTabRedDotControl=%5B%5D; SEARCH_RESULT_LIST_TYPE=%22multi%22; __druidClientInfo=JTdCJTIyY2xpZW50V2lkdGglMjIlM0EyOTglMkMlMjJjbGllbnRIZWlnaHQlMjIlM0E2NTIlMkMlMjJ3aWR0aCUyMiUzQTI5OCUyQyUyMmhlaWdodCUyMiUzQTY1MiUyQyUyMmRldmljZVBpeGVsUmF0aW8lMjIlM0ExJTJDJTIydXNlckFnZW50JTIyJTNBJTIyTW96aWxsYSUyRjUuMCUyMChXaW5kb3dzJTIwTlQlMjAxMC4wJTNCJTIwV2luNjQlM0IlMjB4NjQpJTIwQXBwbGVXZWJLaXQlMkY1MzcuMzYlMjAoS0hUTUwlMkMlMjBsaWtlJTIwR2Vja28pJTIwQ2hyb21lJTJGMTM1LjAuMC4wJTIwU2FmYXJpJTJGNTM3LjM2JTIwRWRnJTJGMTM1LjAuMC4wJTIyJTdE; live_use_vvc=%22false%22; SearchMultiColumnLandingAbVer=2; xgplayer_device_id=54229073359; xgplayer_user_id=707475105873; my_rd=2; _bd_ticket_crypt_cookie=b1b7f2768cd8a08995c0be40200f8200; __live_version__=%221.1.3.2991%22; enter_pc_once=1; dy_swidth=1920; dy_sheight=1080; s_v_web_id=verify_mcwxe0yt_ZzPCGNh7_OdX7_4L37_8AVW_wMdCX92OHf0L; __security_mc_1_s_sdk_crypt_sdk=61672834-40a2-8843; __security_mc_1_s_sdk_cert_key=017d41bf-4baf-8571; __security_mc_1_s_sdk_sign_data_key_web_protect=7ce8c018-4ee3-81e7; passport_csrf_token=a578991a1519a59fcf5f35d62c43fc9a; passport_csrf_token_default=a578991a1519a59fcf5f35d62c43fc9a; session_tlb_tag=sttt%7C7%7CfuxVsXYpVGqIc2P60EfSKv_________859ja5LkSARDWEonjw7ZkPgCZj5jrjo0OiFs8QRYjowo%3D; publish_badge_show_info=%220%2C0%2C0%2C1752123999233%22; sid_guard=7eec55b17629546a887363fad047d22a%7C1752124004%7C5184000%7CMon%2C+08-Sep-2025+05%3A06%3A44+GMT; sid_ucp_v1=1.0.0-KGZjNDdlNDlmMzI3ZjNmZTQ1MDMxOTI2NjY5MTVkODIxYzdkYjQwMmQKHwj16e6DxgEQ5JS9wwYY7zEgDDCshPXCBTgHQPQHSAQaAmhsIiA3ZWVjNTViMTc2Mjk1NDZhODg3MzYzZmFkMDQ3ZDIyYQ; ssid_ucp_v1=1.0.0-KGZjNDdlNDlmMzI3ZjNmZTQ1MDMxOTI2NjY5MTVkODIxYzdkYjQwMmQKHwj16e6DxgEQ5JS9wwYY7zEgDDCshPXCBTgHQPQHSAQaAmhsIiA3ZWVjNTViMTc2Mjk1NDZhODg3MzYzZmFkMDQ3ZDIyYQ; EnhanceDownloadGuide=%220_0_1_1752124019_0_0%22; FOLLOW_RED_POINT_INFO=%221%22; strategyABtestKey=%221752188574.941%22; WallpaperGuide=%7B%22showTime%22%3A1752148507078%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A16%2C%22cursor2%22%3A4%2C%22hoverTime%22%3A1752151299807%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA7JBfrhrjfzhyi8epczROmKVlmKVdJvoPi4NLMthrT3M%2F1752249600000%2F0%2F1752188591658%2F0%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.153%7D; download_guide=%223%2F20250711%2F0%22; __ac_nonce=06870d5ae00a0ad84523; __ac_signature=_02B4Z6wo00f01RnSYOAAAIDB8voqKzmmwCUZ8mRAAC4H2d; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA7JBfrhrjfzhyi8epczROmKVlmKVdJvoPi4NLMthrT3M%2F1752249600000%2F0%2F1752225201487%2F0%22; xg_device_score=7.747010392962505; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT3BCR1VNS2U5VWxSaERNM1p5bmV2ZlQza3ZPYVNQZlRURFpIQys3S2tGY1dtZUdUYzBkT21KWWw3SFRhOXg2Mm52MHBvektMQkJBemNBYXRRZ1hiM289IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=1351297cd57a9eac0f48abc91ef3fb2f21c67edf57c5e1a8638f5c63a6e81fc1716c5b443bf56a3717045e34f3f5b3e3a47e03324a3a2c9b8748ab557f2beb3a; ttwid=1%7CiQxd1Jtue_B1XbhdZMWRRJgmrA8KUDGgzHcN4W6iMek%7C1752225232%7Cb81ed512f751c760deb5a3b1110b6ce6f6c50c470c72188dba6223408b142ab4; biz_trace_id=a0259b00; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2733313c34363133373737303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=hQbYaziNSZh842RUJL-yZ4D6jAc9xprJy37Z8sMvWVyL9rgK5CIN4WaXZpkT1QRVYMLjVKZrlRIV_9fTLBo_EW8rtFBJTfmoak9YJ_2Ek_WHg1ruoAodFMdhbjcve9jAy4v1gXr5T2yslx8LZMMr3wl-mDSzu41EA18dY6EfGcyuwk1gWqxuSEs-RH9SGMzluw-ea5t4lrCvzxUupa4SWX07qfZuWs1oU4IhcDSdw0-W0h3xTV3nzZua8maUGfqTdur85XuliAWH3Oq_Wa9ECAvb-G7Hkd_PhMPCEyrMNrTClPLea_rfcHBvnEW0GmOUhkaw7sxKek01m_eXGrSFF3IECfDWOxYQRX68ivHDNZkU5wvB2pGGGmxIiLSELWI7mqiiWekJBQqyo5dMzgV0qZgG1v3Ae9-4siG9SX6w1VmE6aAsU6Luvk4gQVg4dpEbWFKb4fSlZsennCLPiPnwliw6VWF-ZKsYD9E1FCy-g9UvshaJIuw0KEKYZYwSA0b5BrDzAu4tzTR5lFYFX3xZk28PTcMN3YNHDg3CF8HF9cQ%3D; gulu_source_res=eyJwX2luIjoiNzU0M2ZjOGQ1M2I0ODllM2QzNDA1NDBmYmViY2VhOTQ5YjdkNmE0NmQyY2RiODQzN2RiNDY4OTdiNDkzN2RlZiJ9; passport_auth_mix_state=0198hizvnv8o8v0v5qyla3t4gy8uzts9; passport_fe_beating_status=false; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"

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
    if i['images'] == 'none': #纯视频的值为none，确保不下载动图视频的音乐
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