#!/usr/bin/env python3
"""以 Python 標準函式庫檢查所有正式 HTML 頁面的結構與本機連結。"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import sys
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / 'index.html', *sorted((ROOT / 'pages').glob('*.html'))]
REQUIRED_FILES = [
    ROOT / 'AGENTS.md', ROOT / 'README.md', ROOT / 'index.html',
    ROOT / 'assets' / 'style.css', ROOT / 'assets' / 'site.js',
    ROOT / 'templates' / 'page-template.html'
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()
        self.tags = []
        self.title_count = 0
        self.h1_count = 0
        self.has_lang = False
        self.has_description = False
        self.has_viewport = False
        self.bad_images = 0
        self.titles = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attr = dict(attrs)
        if tag == 'html':
            self.has_lang = attr.get('lang') == 'zh-Hant'
        if tag == 'meta' and attr.get('name') == 'description':
            self.has_description = bool(attr.get('content'))
        if tag == 'meta' and attr.get('name') == 'viewport':
            self.has_viewport = True
        if tag in ('a', 'link', 'script', 'img'):
            url = attr.get('href') if tag in ('a','link') else attr.get('src')
            if url:
                self.refs.append((tag,url))
        if tag == 'img' and 'alt' not in attr:
            self.bad_images += 1
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'title':
            self.title_count += 1
            self.in_title = True
        if 'id' in attr:
            self.ids.add(attr['id'])

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.titles.append(data)


def main():
    errors = []
    for file in REQUIRED_FILES:
        if not file.is_file():
            errors.append(f'缺少必要檔案：{file.relative_to(ROOT)}')
    for file in PAGES:
        html = file.read_text(encoding='utf-8')
        parser = PageParser()
        parser.feed(html)
        rel = file.relative_to(ROOT)
        if parser.h1_count != 1:
            errors.append(f'{rel}: h1 數量應為 1，實際 {parser.h1_count}')
        if parser.title_count != 1 or not ''.join(parser.titles).strip():
            errors.append(f'{rel}: 缺少有效 title')
        if not parser.has_lang or not parser.has_description or not parser.has_viewport:
            errors.append(f'{rel}: 缺少 lang=zh-Hant / description / viewport')
        if not all(tag in parser.tags for tag in ('header', 'nav', 'main', 'footer')):
            errors.append(f'{rel}: 缺少 header / nav / main / footer')
        if parser.bad_images:
            errors.append(f'{rel}: {parser.bad_images} 張圖片缺少 alt')
        if '【' in html or '】' in html:
            errors.append(f'{rel}: 有未填寫的版型占位符【...】')
        for tag, url in parser.refs:
            parsed = urlparse(url)
            if parsed.scheme in ('http','https','mailto','tel') or url.startswith('//'):
                continue
            if parsed.scheme or url.startswith('/'):
                errors.append(f'{rel}: 不支援的站內網址 {url}')
                continue
            target = unquote(parsed.path)
            if target:
                target_file = (file.parent / target).resolve()
                if not target_file.is_relative_to(ROOT.resolve()) or not target_file.is_file():
                    errors.append(f'{rel}: 連結不存在 {url}')
            elif parsed.fragment and parsed.fragment not in parser.ids:
                errors.append(f'{rel}: 頁面錨點不存在 {url}')
        print(f'檢查：{rel}')
    if errors:
        print('\n❌ 網站驗證失敗：')
        for e in errors: print(' -',e)
        return 1
    print(f'\n✅ 檢查通過：{len(PAGES)} 個正式 HTML 頁面、必要檔案、語意結構與站內連結。')
    return 0

if __name__ == '__main__':
    sys.exit(main())
