import requests
import time
import urllib.parse
from func.download_aweme_list import *
from func.get_aweme_id import *
from func.get_a_bogus import *
from func.logger import logger

# 将 cookie 字符串转换为结构化列表
def cookie_str_to_dict(cookie_str):
    result = {}
    for item in cookie_str.split("; "):
        if "=" in item:
            k, v = item.split("=", 1)
            result[k] = v
    return result

async def download_user(sec_user_id: str, cookie_str: str, max_download_num: int, msToken: str):
    max_cursor = 0 # 初始游标
    has_more = True # 是否有更多数据
    already_download_nums = 0 # 已下载数量
    
    url = 'https://www.douyin.com/aweme/v1/web/aweme/post/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "accept": "application/json, text/plain, */*",
        "referer": f"https://www.douyin.com/user/{sec_user_id}",
        "cookie": cookie_str
    }

    author = ""
    while has_more and already_download_nums < max_download_num:
        
        commom_params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'sec_user_id': sec_user_id,
            'max_cursor': f'max_cursor',
            'locate_item_id': '7528528308951158068',
            'locate_query': 'false',
            'show_live_replay_strategy': '1',
            'need_time_list': '1',
            'time_list_query': '0',
            'whale_cut_token': '',
            'cut_version': '1',
            'count': '18',
            'publish_video_strategy_type': '2',
            'from_user_page': '1',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '0',
            'cpu_core_num': '20',
            'version_code': '290100',
            'version_name': '29.1.0',
            'cookie_enabled': 'true',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '138.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '138.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '0',
            'webid': get_web_id(),
            'uifid': '3af258ad659545d9553f15cf32bb8a88df248991ebb865c20b5fa6f7dab6eb54779588e82ce7117d7aea4e6dfdcf799363dc7540ad3bf7ab783ff8d0c4ec009da71e4ec16c21aac757bf34f79e0b260a4a87643250ca8e38ceefdfe186b3ebcab67e60391e73817978e0fa1ce8361b3d6379906d3104f3c6d28105eeac56cf916d8a5ef910f1300861bf0221a59142192539698fdb5e42765cec53072bafed304dd214d3a10cd685d1171e4ae7fec36e166c1a995cc7743334d4071fd51102d5',
            'verifyFp': 'verify_mcwxe0yt_ZzPCGNh7_OdX7_4L37_8AVW_wMdCX92OHf0L',
            'fp': 'verify_mcwxe0yt_ZzPCGNh7_OdX7_4L37_8AVW_wMdCX92OHf0L',
            'msToken': msToken,
        }
        params = commom_params
        params_string = urllib.parse.urlencode(params)
        params['a_bogus'] = await get_a_bogus(url, params_string, headers['user-agent'])
        
        try:
            # response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            logger.info(f"请求失败：{e}")
            break

        aweme_list = data.get("aweme_list", [])
        if not aweme_list:
            logger.info("无更多作品")
            break

        # 下载当前页数据
        nums, author = download_aweme_list(
            aweme_list, headers, already_download_nums, max_download_num
        )
        already_download_nums += nums
        if already_download_nums >= max_download_num:
            logger.info(f"已达到最大下载数量 {max_download_num}，停止下载。")
            break

        # 翻页判断
        has_more = data.get("has_more", 0) == 1 and already_download_nums < max_download_num
        max_cursor = data.get("max_cursor", 0)
        time.sleep(1.5)  # 防ban

    logger.info(f"用户 <{author}> 的作品下载完成，总计：{already_download_nums} 个")