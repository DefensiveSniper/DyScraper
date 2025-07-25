import requests
import os
import random
import string
import re
import urllib.parse
import asyncio
import time
import json
from func.logger import logger
from func.get_a_bogus import get_web_id, get_a_bogus, get_a_bogus_from_js


msToken = 'iB1J6MpL6xp6fRAYwLSa5R08uG6oIkqibP-Zes5pChkdvj24ak4z3fDSQo8WsPyaJA0vD-I-6H90g-0oWRPpkOUGMzSMe_2QpmUQEH59xRsv4gf_cwt3e7z47_wqzULxFkRjTvO2QLoJ4BV8TuKeZnGhDYVj58K7GMdBCuybjEcDwA=='
cookie_str = 'enter_pc_once=1; UIFID_TEMP=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee647407b11caad055db1101605067df5d71c1a751074e808e64cc33f1415f69e7e388d11ecbddaa6d17a707ee0fc37d25a9fd2; s_v_web_id=verify_md029wd2_3kS1wqVh_n9fd_4Nm1_9t6m_UYfSfFJ3CEyZ; hevc_supported=true; dy_swidth=1920; dy_sheight=1080; fpk1=U2FsdGVkX1/R5U1zWfknuMsW/Ujvk//srQRLjOlQSIN2UFfXTHZTICdVuAtPdTmqpZaTcZud/bBtG8roPB83vw==; fpk2=7ddeda88d0c599cc494da0dece6554d5; xgplayer_user_id=91112859564; UIFID=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee647407b11caad055db1101605067df5d71c1a962911ed6ec8b6ccbf1f312aa53ebfef0b1b08a0a379c2967276081e6eb2e887dd1edefc03b5c507eafc9acca21d21f0c0ccfee80641703082ca7fbde935977c0ab08cb4add9c8ccb23b96ab45dc05da4d75f7dcd72110cca17f9b06cfcf87abf7f134a21a857cfcac83b5c96934ac01; is_dash_user=1; passport_csrf_token=7f13e98bbfdad1c85947956a687dfc1f; passport_csrf_token_default=7f13e98bbfdad1c85947956a687dfc1f; __security_mc_1_s_sdk_crypt_sdk=e11fa6f7-430d-b214; bd_ticket_guard_client_web_domain=2; passport_assist_user=CkCcxlx7RSrUFa06FXcvX-8ed4dtMwhr3VhTxU0WQVccj7u7Ajd_18sOWP-yOLqPnZLv9y-2pEXKc7ubKYopq7RpGkoKPAAAAAAAAAAAAABPOYTDzlrrl8vmKq-yxFB1KIN1ayig9SIAIO1HGzfCyC7EslTwwDtYXv69nK8O34HjjBDNxfYNGImv1lQgASIBA_WiwLI%3D; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=ab6c29c608fd6d5a7a11741ee23238bd%7C1752314838%7C5184000%7CWed%2C+10-Sep-2025+10%3A07%3A18+GMT; uid_tt=ebaa753d610eb47b5539332b1f6aa836; uid_tt_ss=ebaa753d610eb47b5539332b1f6aa836; sid_tt=ab6c29c608fd6d5a7a11741ee23238bd; sessionid=ab6c29c608fd6d5a7a11741ee23238bd; sessionid_ss=ab6c29c608fd6d5a7a11741ee23238bd; session_tlb_tag=sttt%7C12%7Cq2wpxgj9bVp6EXQe4jI4vf_________6Gn_erjXRUCkWlYzsvRGp7HsQmQVeKSesYVUxqdwpKk0%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KGQ2YjE5NzYzOTQ3NTFhOTlmYTVkYzA4NDNhMzQyMjY4Y2UzZmVmYTYKIAj39-CUwvU7ENbnyMMGGO8xIAww5tOI_gU4B0D0B0gEGgJobCIgYWI2YzI5YzYwOGZkNmQ1YTdhMTE3NDFlZTIzMjM4YmQ; ssid_ucp_v1=1.0.0-KGQ2YjE5NzYzOTQ3NTFhOTlmYTVkYzA4NDNhMzQyMjY4Y2UzZmVmYTYKIAj39-CUwvU7ENbnyMMGGO8xIAww5tOI_gU4B0D0B0gEGgJobCIgYWI2YzI5YzYwOGZkNmQ1YTdhMTE3NDFlZTIzMjM4YmQ; login_time=1752314838159; publish_badge_show_info=%220%2C0%2C0%2C1752314838513%22; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_cookie=dac10c3a8bfad2afc65361728264e192; __security_mc_1_s_sdk_sign_data_key_web_protect=8108eea2-4e22-9ede; __security_mc_1_s_sdk_cert_key=8d0ba45c-40a8-9bf1; __security_server_data_status=1; my_rd=2; download_guide=%223%2F20250712%2F0%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA0PBqJ_oQIsL749omlrStGZazhopNLgs3cjHq84trFao%2F1752336000000%2F0%2F0%2F1752317600613%22; EnhanceDownloadGuide=%220_0_1_1752336628_0_0%22; xgplayer_device_id=39612927190; WallpaperGuide=%7B%22showTime%22%3A1752337505303%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A22%2C%22cursor2%22%3A6%2C%22hoverTime%22%3A1752374572212%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_signature=_02B4Z6wo00f01qDwjpwAAIDBPpQuD4V5Rq6g0IoAAMBQe3; douyin.com; xg_device_score=7.76978613458075; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; strategyABtestKey=%221752733947.928%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA0PBqJ_oQIsL749omlrStGZazhopNLgs3cjHq84trFao%2F1752768000000%2F1752733955867%2F1752733947418%2F0%22; volume_info=%7B%22volume%22%3A0.189%2C%22isMute%22%3Afalse%2C%22isUserMute%22%3Afalse%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTWFXN2pXeHkyMXp4UWpvbVN5Y2U1SUdyTXE2bFlNbitjMnZMTVBCYWwyajM5N2NyRHRzL2NMZHNoTmtxUDNUcmQ2OVlIS2FyOWFOeEVMRG5CeUNNWDQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=c28b3b179d34c9f585b546cc31a718bab49ff0d0dc6a03cd9fdcf3c1300c6299790a499fa664059950903d66b3ffff2c778a8dc72e4012188fb461354c6dd899; biz_trace_id=82fc32a9; ttwid=1%7CzNbWjmfstt_OUd-PVPVSxSYmpF4_FFvqDCPQlPNsttM%7C1752734113%7Ccecb66583981ed897ab48d02f8e8f3ad0530b6e476fb634d3bdcc6fa2299d55f; __druidClientInfo=JTdCJTIyY2xpZW50V2lkdGglMjIlM0ExNzYwJTJDJTIyY2xpZW50SGVpZ2h0JTIyJTNBODg5JTJDJTIyd2lkdGglMjIlM0ExNzYwJTJDJTIyaGVpZ2h0JTIyJTNBODg5JTJDJTIyZGV2aWNlUGl4ZWxSYXRpbyUyMiUzQTElMkMlMjJ1c2VyQWdlbnQlMjIlM0ElMjJNb3ppbGxhJTJGNS4wJTIwKFdpbmRvd3MlMjBOVCUyMDEwLjAlM0IlMjBXaW42NCUzQiUyMHg2NCklMjBBcHBsZVdlYktpdCUyRjUzNy4zNiUyMChLSFRNTCUyQyUyMGxpa2UlMjBHZWNrbyklMjBDaHJvbWUlMkYxMzguMC4wLjAlMjBTYWZhcmklMkY1MzcuMzYlMjIlN0Q=; passport_fe_beating_status=false; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22'


def download_following_list(data, headers, already_download_nums, max_download_num):
    if not data:
        logger.info("无内容，跳过。")
        return
    
    nums = 0  # 初始化下载计数
    
    for i in data:
        print
        author = i['aweme']['author']['nickname']# 获取作者ID
        os.makedirs(f"./media/关注/{author}/images", exist_ok=True)  # 创建作者视频文件夹
        os.makedirs(f"./media/关注/{author}/videos", exist_ok=True)  # 创建作者图片文件夹

        item_title = i['aweme']['item_title'].strip().split('\n')[0] # 获取标题
        caption = i['aweme']['caption'].strip().split('\n')[0]
        title = "" + item_title + caption 
        if not title:
            title = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # 如果标题为空，生成随机标题
        title_ulti = re.sub('[\/:*?"<>|]', '', title)# 替换非法字符

        # 视频
        if i['aweme']['images'] is None: #纯视频的值为none，确保不下载动图视频的音乐
            try:
                video_url = i['aweme']['video']['play_addr']['url_list'][0]  # 获取视频地址
                res_video = requests.get(video_url, headers=headers).content  # 发送请求获取视频内容
                
                nums += 1 # 增加下载计数
                if nums + already_download_nums >= max_download_num:
                    # 达到指定下载数，停止下载
                    break
                
                with open(f"media/关注/{author}/videos/{title_ulti}.mp4", 'wb') as f:
                    f.write(res_video)  
                    logger.info(f"视频: {title_ulti} 下载完成")
                    continue
            except Exception as e:
                logger.error(f"{title_ulti} 视频下载出错: {e}")
        
        # 动图、图片
        else:
            # 动图
            for idx, j in enumerate(i['aweme']['images']):
                try:
                    gif_url = j['video']['play_addr']['url_list'][0]
                    res_gif = requests.get(gif_url, headers=headers).content
                    filename = f"{title_ulti}_{idx}"
                    with open(f"media/关注/{author}/videos/{filename}.mp4", 'wb') as f:
                        f.write(res_gif)
                        logger.info(f"动图：{filename} 下载完成")
                except:
                    logger.error(f"{title_ulti} 不是动图，开始下载图片")
                
                try:
                    image_url = j['url_list'][0]
                    res_image = requests.get(image_url, headers=headers).content
                    filename = f"{title_ulti}_{idx}"
                    with open(f"media/关注/{author}/images/{filename}.webp", 'wb') as f:
                        f.write(res_image)
                        logger.info(f"图片：{filename} 下载完成")
                except:
                    logger.error(f"{title_ulti} 也不是图片。报错信息：{e}")
        
        nums += 1 # 增加下载计数
        if nums + already_download_nums >= max_download_num:
            break
    return nums  # 返回下载的视频数量

async def download_following(max_download_num: int, msToken: str, cookie_str: str):
    max_cursor=0 # 初始游标
    level = 1 # 初始阶段
    has_more = True # 是否有更多数据
    already_download_nums = 0 # 已下载数量
    
    url = "https://www.douyin.com/aweme/v1/web/follow/feed"
    headers = {
        'referer': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'cookie': '',
        'cookie': cookie_str,
    }
    
    while has_more and already_download_nums < max_download_num:
        pull_type = 0 if max_cursor == 0 else 2
        commom_params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'cursor': f'{max_cursor}',
            'level': f'{level}',
            'count': '20',
            'pull_type': f'{pull_type}',
            'aweme_ids': '',
            'room_ids': '',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Chrome',
            'browser_version': '138.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '138.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'cpu_core_num': '20',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '150',
            'webid': f"{get_web_id()}",
            'verifyFp': 'verify_md029wd2_3kS1wqVh_n9fd_4Nm1_9t6m_UYfSfFJ3CEyZ',
            'fp': 'verify_md029wd2_3kS1wqVh_n9fd_4Nm1_9t6m_UYfSfFJ3CEyZ',
            'msToken': msToken,
        }
        
        params = commom_params
        params_string = urllib.parse.urlencode(params)
        params['a_bogus'] = await get_a_bogus(url, params_string, headers['user-agent'])

        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            JSON = response.json()
            
            data = JSON.get("data", [])
            if not data:
                logger.info("无更多视频")
                break
            
            already_download_nums += download_following_list(
                data, headers, already_download_nums, max_download_num
            )
            
            # 翻页判断
            has_more = JSON.get("has_more", 0) == 1 and already_download_nums < max_download_num
            max_cursor = JSON["cursor"]
            level = JSON["level"]
            time.sleep(1)
            
        except Exception as e:
            logger.error(f"下载出错：{e}")
            break

    logger.info(f"全部下载完成，总计：{already_download_nums}个")