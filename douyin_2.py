import requests
import time
from func.download_aweme_list import *
from func.get_a_bogus import *

# ====== 配置区 ======
# sec_user_id = ""
# cookie_str = ""
# max_download_num = 200  # 最大下载数
# ====================

# 将 cookie 字符串转换为结构化列表
def cookie_str_to_dict(cookie):
    result = {}
    for item in cookie.split("; "):
        if "=" in item:
            k, v = item.split("=", 1)
            result[k] = v
    return result

def download_user(sec_user_id: str, cookie_str: str, max_download_num: int):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "accept": "application/json, text/plain, */*",
        "referer": f"https://www.douyin.com/user/{sec_user_id}",
    }

    cookies = cookie_str_to_dict(cookie_str)

    max_cursor = 0 # 初始游标
    has_more = True # 是否有更多数据
    already_download_nums = 0 # 已下载数量

    while has_more and already_download_nums < max_download_num:
        url = (
            f"https://www.douyin.com/aweme/v1/web/aweme/post/"
            f"?device_platform=webapp"
            f"&aid=6383"
            f"&channel=channel_pc_web"
            f"&sec_user_id={sec_user_id}"
            f"&max_cursor={max_cursor}"
            f"&locate_query=false"
            f"&show_live_replay_strategy=1"
            f"&need_time_list=0"
            f"&time_list_query=0"
            f"&whale_cut_token="
            f"&cut_version=1"
            f"&count=18"
            f"&publish_video_strategy_type=2"
            f"&from_user_page=1"
            f"&update_version_code=170400"
            f"&pc_client_type=1"
            f"&pc_libra_divert=Windows"
            f"&support_h265=1"
            f"&support_dash=1"
            f"&cpu_core_num=20"
            f"&version_code=290100"
            f"&version_name=29.1.0"
            f"&cookie_enabled=true"
            f"&screen_width=1920"
            f"&screen_height=1080"
            f"&browser_language=zh-CN"
            f"&browser_platform=Win32"
            f"&browser_name=Chrome"
            f"&browser_version=138.0.0.0"
            f"&browser_online=true"
            f"&engine_name=Blink"
            f"&engine_version=138.0.0.0"
            f"&os_name=Windows"
            f"&os_version=10"
            f"&device_memory=8"
            f"&platform=PC"
            f"&downlink=10"
            f"&effective_type=4g"
            f"&round_trip_time=0"
            f"&webid=7526129557382022696"
            f"&uifid=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee647407b11caad055db1101605067df5d71c1a962911ed6ec8b6ccbf1f312aa53ebfef0b1b08a0a379c2967276081e6eb2e887dd1edefc03b5c507eafc9acca21d21f0c0ccfee80641703082ca7fbde935977c0ab08cb4add9c8ccb23b96ab45dc05da4d75f7dcd72110cca17f9b06cfcf87abf7f134a21a857cfcac83b5c96934ac01"
            f"&verifyFp=verify_md029wd2_3kS1wqVh_n9fd_4Nm1_9t6m_UYfSfFJ3CEyZ"
            f"&fp=verify_md029wd2_3kS1wqVh_n9fd_4Nm1_9t6m_UYfSfFJ3CEyZ"
            f"&msToken={msToken}"
            f"&a_bogus={a_bogus}"
        )
        
        try:
            r = requests.get(url, headers=headers, cookies=cookies, timeout=10)
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            print("请求失败：", e)
            break

        aweme_list = data.get("aweme_list", [])
        if not aweme_list:
            print("无更多作品")
            break

        # 下载当前页数据
        nums = download_aweme_list(
            aweme_list, headers, already_download_nums, max_download_num
        )
        already_download_nums += nums
        if already_download_nums >= max_download_num:
            print(f"已达到最大下载数量 {max_download_num}，停止下载。")
            break

        # 翻页判断
        has_more = data.get("has_more", 0) == 1 and already_download_nums < max_download_num
        max_cursor = data.get("max_cursor", 0)
        time.sleep(1.5)  # 防ban

    print("全部下载完成，总计：", already_download_nums, "个")
