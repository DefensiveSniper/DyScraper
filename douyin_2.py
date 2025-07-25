import requests
import time
from func.download_aweme_list import *
from func.get_a_bogus import *

# ====== 配置区 ======
# sec_user_id = "MS4wLjABAAAA9EPzyoQ_7g03sM1nEpUcHrdAOenJuYD7mDdpCIrTNo4"
# cookie_str = "douyin.com; xg_device_score=7.844149484000294; enter_pc_once=1; UIFID_TEMP=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee647407b11caad055db1101605067df5d71c1a751074e808e64cc33f1415f69e7e388d11ecbddaa6d17a707ee0fc37d25a9fd2; s_v_web_id=verify_md029wd2_3kS1wqVh_n9fd_4Nm1_9t6m_UYfSfFJ3CEyZ; hevc_supported=true; dy_swidth=1920; dy_sheight=1080; fpk1=U2FsdGVkX1/R5U1zWfknuMsW/Ujvk//srQRLjOlQSIN2UFfXTHZTICdVuAtPdTmqpZaTcZud/bBtG8roPB83vw==; fpk2=7ddeda88d0c599cc494da0dece6554d5; xgplayer_user_id=91112859564; UIFID=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee647407b11caad055db1101605067df5d71c1a962911ed6ec8b6ccbf1f312aa53ebfef0b1b08a0a379c2967276081e6eb2e887dd1edefc03b5c507eafc9acca21d21f0c0ccfee80641703082ca7fbde935977c0ab08cb4add9c8ccb23b96ab45dc05da4d75f7dcd72110cca17f9b06cfcf87abf7f134a21a857cfcac83b5c96934ac01; is_dash_user=1; passport_csrf_token=7f13e98bbfdad1c85947956a687dfc1f; passport_csrf_token_default=7f13e98bbfdad1c85947956a687dfc1f; __security_mc_1_s_sdk_crypt_sdk=e11fa6f7-430d-b214; bd_ticket_guard_client_web_domain=2; passport_assist_user=CkCcxlx7RSrUFa06FXcvX-8ed4dtMwhr3VhTxU0WQVccj7u7Ajd_18sOWP-yOLqPnZLv9y-2pEXKc7ubKYopq7RpGkoKPAAAAAAAAAAAAABPOYTDzlrrl8vmKq-yxFB1KIN1ayig9SIAIO1HGzfCyC7EslTwwDtYXv69nK8O34HjjBDNxfYNGImv1lQgASIBA_WiwLI%3D; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=ab6c29c608fd6d5a7a11741ee23238bd%7C1752314838%7C5184000%7CWed%2C+10-Sep-2025+10%3A07%3A18+GMT; uid_tt=ebaa753d610eb47b5539332b1f6aa836; uid_tt_ss=ebaa753d610eb47b5539332b1f6aa836; sid_tt=ab6c29c608fd6d5a7a11741ee23238bd; sessionid=ab6c29c608fd6d5a7a11741ee23238bd; sessionid_ss=ab6c29c608fd6d5a7a11741ee23238bd; session_tlb_tag=sttt%7C12%7Cq2wpxgj9bVp6EXQe4jI4vf_________6Gn_erjXRUCkWlYzsvRGp7HsQmQVeKSesYVUxqdwpKk0%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KGQ2YjE5NzYzOTQ3NTFhOTlmYTVkYzA4NDNhMzQyMjY4Y2UzZmVmYTYKIAj39-CUwvU7ENbnyMMGGO8xIAww5tOI_gU4B0D0B0gEGgJobCIgYWI2YzI5YzYwOGZkNmQ1YTdhMTE3NDFlZTIzMjM4YmQ; ssid_ucp_v1=1.0.0-KGQ2YjE5NzYzOTQ3NTFhOTlmYTVkYzA4NDNhMzQyMjY4Y2UzZmVmYTYKIAj39-CUwvU7ENbnyMMGGO8xIAww5tOI_gU4B0D0B0gEGgJobCIgYWI2YzI5YzYwOGZkNmQ1YTdhMTE3NDFlZTIzMjM4YmQ; login_time=1752314838159; publish_badge_show_info=%220%2C0%2C0%2C1752314838513%22; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_cookie=dac10c3a8bfad2afc65361728264e192; __security_mc_1_s_sdk_sign_data_key_web_protect=8108eea2-4e22-9ede; __security_mc_1_s_sdk_cert_key=8d0ba45c-40a8-9bf1; __security_server_data_status=1; my_rd=2; download_guide=%223%2F20250712%2F0%22; WallpaperGuide=%7B%22showTime%22%3A0%2C%22closeTime%22%3A0%2C%22showCount%22%3A0%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA0PBqJ_oQIsL749omlrStGZazhopNLgs3cjHq84trFao%2F1752336000000%2F0%2F0%2F1752317600613%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA0PBqJ_oQIsL749omlrStGZazhopNLgs3cjHq84trFao%2F1752336000000%2F1752320194283%2F1752319083064%2F0%22; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; xg_device_score=7.761775835294689; volume_info=%7B%22volume%22%3A0.255%2C%22isMute%22%3Afalse%2C%22isUserMute%22%3Afalse%7D; __ac_signature=_02B4Z6wo00f01w6CUAgAAIDAkObwmyNchyMOolSAAKvddf; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; __ac_nonce=06872875200dbe9dc855e; strategyABtestKey=%221752336233.476%22; passport_fe_beating_status=true; EnhanceDownloadGuide=%220_0_1_1752336628_0_0%22; gulu_source_res=eyJwX2luIjoiYTlmMjU3NzAxMWQ2OTIyYjc5NWQ5Zjk3NjY1OWVkOTNkMGQ2NjBjMWZhMmNkYzdjMGI4NmI5YTU2YjlhYmU1OCJ9; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; biz_trace_id=adf9cc18; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2730343d353d3d33363637303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=gFqrzrd0BIKLZsuWqwNXSn6NXchMSMizDkEsD7rNtqQQvDGZafvDtq1InBB9RUzQN1-GH2qWSqdRNsmADCYAdkp4r3v64kyVFs4QRknM_LexUVxI7Q54aHoO09C33RMBApc1iY-Mp--H4TNVMfJn2DuFRlBnKI86iXhv0H6PvrbRhVIXhCqgHruTH1lCkT_CKGesTXiuXWVHmbVIXNH8mN8Sz7DcKwkzLN9UZIIvf9HTEoW_iGW2bkoo_uRWpc4IPj-iZODKkghG4oFxtxidg7xr2EXw4QqO8YYXvoUb62Eum5tq7ifGK__VrKHsBn888_VKDZZSpKAKe0WHG66-36ZFVv69sDecYprG4Nl64YVm5z4t4SzNSo8k2VLfVHWZq4GSqFw7OVnSfZZvleTqkyf9JMJedq_TJkHceF0ybASrBPpY_DlG5A0Nfp3yIIPWeXdJOXhnNZrrduF9WU_nbRJG-FBaSW5o2Lnpb30GHu9X0ShkqypGH-nwaI7e5Ldi; passport_auth_mix_state=qaokjynw0c7o0m2l8zjq7ynj6fbad0b9cbolhq3srbz683fv; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTWFXN2pXeHkyMXp4UWpvbVN5Y2U1SUdyTXE2bFlNbitjMnZMTVBCYWwyajM5N2NyRHRzL2NMZHNoTmtxUDNUcmQ2OVlIS2FyOWFOeEVMRG5CeUNNWDQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; ttwid=1%7CzNbWjmfstt_OUd-PVPVSxSYmpF4_FFvqDCPQlPNsttM%7C1752337006%7C045fed291afab752b9b8ab5a6132541448811e17e428fb97e4331bea06f6c345; odin_tt=95a82e7c97e32a8c0713392c6359c0020364abdba3147b3007aa3e05917f72e446d72c13a102b5bdafa2589a607e38f8cf63a8221bf73315ffa87d3f34c798cc; IsDouyinActive=false"
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
            f"&msToken=6E6fKhXCwb9q87wwnupNSMh-82Yvi5ReoyzcnMvROzhp7uEKaTfqQdstIuTJE9jq4OlayRWVZOQ0BNj81DbxMvjX975r2_C7V4TgJhXCh2RZPlATJiwrtSddasLTnEvDzpKzHAP0yjXnzBE12MFNG1lpj2qt73_Rg_RGJYXnLe2V"
            f"&a_bogus=O60RhqyLQxRfFdFGmOra93clMyoArBSyBPTxRF%2FPCNY4G1Fa2SN7iPbcnxFaBqPLk8BskCIHfne%2FYdncKGXzZo9kLmkvSmwfZU%2Fcnz8o8qZdb4Jh7r8LebGEqiTY0CGYYQI9iZWRAsMC2dOWnrCwABI7u%2F3xRcEdFH3XV%2FYnY9u4USujin%2FVa3t2O7JqUD%3D%3D"
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