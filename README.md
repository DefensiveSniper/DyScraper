# 📥 Douyin Scraper - 抖音内容下载器

这是一个基于 Python + DrissionPage + Requests 的抖音爬虫工具，可批量下载某个用户主页发布的**视频、动图、图片**内容，适用于个人学习与数据分析用途。

## ✨ 功能特点

- 支持下载抖音视频，用户主页视频、分享链接视频以及个人关注列表视频
- 支持下载图片及动图（GIF 实际为 MP4）
- 自动分类保存至 `media/videos` 与 `media/images` 文件夹
- 使用 Chromium 无头浏览器监听网页数据包抓取接口 JSON，无需逆向 API
- 扫码登录获取 cookies

## 🧰 使用依赖

- Python 3.10.11
- [DrissionPage](https://github.com/g1879/DrissionPage) - 强大的浏览器控制工具，结合 Requests 和 Selenium 特性

## 🚀 使用方法

1. 克隆本仓库：
    ```bash
    git clone https://github.com/DefensiveSniper/DyScraper
    cd DyScraper
    ```

2. 修改 `douyin.py` 文件中的以下变量：
    - `url`：目标用户主页地址（必须是完整链接，且你已登录能访问）
    - `cookie`：你的登录 Cookie（建议使用浏览器插件复制）
    - `user_agent`：你的浏览器 UA
    **新增扫码登陆后无需手动配置**
    **仅需修改`config.yaml`中的`sec_user_id`以及`share_link`**

3. 运行爬虫脚本：
    ```bash
    python main.py
    ```
    **主函数`main.py`中包含三种爬取方式，自行选择**

4. 下载完成的媒体文件会保存在：
    - 视频与动图：`media/videos/`
    - 图片：`media/images/`

## ⚠️ 注意事项

- 抖音接口有一定频率限制，请勿频繁执行。
- 请确保你拥有对应内容的合法使用权，**本项目仅供学习和研究使用**。
- Cookie 具有时效性，失效后需重新抓取。


## 📁 项目结构

```
douyin-scraper/
├── douyin.py             # 主爬虫脚本
├── media/
│   ├── videos/           # 保存视频和动图
│   └── images/           # 保存图片
```