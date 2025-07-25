import requests
import time
import re
import yaml
import asyncio
from typing import Any, Callable, Dict, Optional
from func.get_a_bogus import get_web_id, get_a_bogus, get_a_bogus_from_js
from func.logger import logger
from func.download_user import cookie_str_to_dict, download_user
from func.download_single import download_single
from func.download_following import download_following
from playwright.async_api import async_playwright
from login_douyin import DouYinLogin

'''
须知：
    第一次使用需要扫码登录，扫码后会保存cookie，后续直接使用cookie即可
    保存文件为 config.yaml
    修改参数请到 config.yaml 文件中修改
    登录方式: "qrcode"、"phone" 或 "cookie"
'''

#========测试登录========
async def main():
    
    #========初始化========
    config = yaml.load(open("config.yaml", "r", encoding="utf-8"), Loader=yaml.FullLoader)
    cookie_str = config["douyin"]["cookie_str"]
    sec_user_id = config["douyin"]["sec_user_id"]
    share_link = config["douyin"]["share_link"]
    msToken = config["douyin"]["msToken"]
    max_download_num = config["douyin"]["max_download_num"]
    #======================
    
    if config["douyin"]["login_type"] != "cookie":
        async with async_playwright() as p:
            # 启动浏览器
            browser = await p.chromium.launch(
                headless = config["douyin"]["headless"],
                # executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                args = [
                    "--disable-blink-features=AutomationControlled"
                ]
            )
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto("https://www.douyin.com/")

            # 实例化 DouYinLogin
            login = DouYinLogin(
                login_type = "qrcode",    # 登录方式: "qrcode" 或 "cookie"
                browser_context = context,                      # Playwright 浏览器上下文
                context_page = page,                            # Playwright 页面对象
                login_phone = "",
                cookie_str = config["douyin"]["cookie_str"]     # Cookie 字符串（如用 Cookie 登录则填写）
            )

            # 开始登录流程
            await login.begin()
            # 登录扫码成功后
            if login.LOGIN_TYPE != "cookie":
                await page.goto("https://www.douyin.com/")
                
                # 获取 cookies
                cookies = await context.cookies()
                cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies if c['name']])
                config["douyin"]["cookie_str"] = cookie_str
                # logger.info(f"cookies: {cookie_str}")

                # 获取 params 中的 msToken
                local_storage: Dict = await page.evaluate("() => window.localStorage")
                msToken = local_storage.get("xmst")
                config["douyin"]["msToken"] = msToken
                logger.info(f"msToken: {msToken}")
                
                # 保存配置
                with open('config.yaml', 'w', encoding='utf-8') as f:
                    yaml.safe_dump(config, f, allow_unicode=True)
            
            # 关闭浏览器
            await browser.close()
    # 功能区
    # await download_user(sec_user_id, cookie_str, max_download_num, msToken)
    # await download_single(share_link, cookie_str, msToken)
    # await download_following(max_download_num, msToken, cookie_str)
# 运行主函数
asyncio.run(main())
#====================