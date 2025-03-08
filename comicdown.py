import execjs
import requests

for page in range(39):
    # comic chapter url
    url = 'https://www.dm5.com/m1609850/'
    chapter_id = url.split('/')[-2]
    cid = chapter_id[1:]

    page = str(page + 1).zfill(2)

    # Looks cookies is no needed here.
    # cookies = {
    #     '7940D296A3BE781': '19ED29CEE96C1DF96DAE42560E4121424BBA080351871F2B9DD25369411D5AAA436258F6B31043CA8A4A129E83F6C32D183EAD22613FCB73E50DDA0A2CE9D840975F7BAE2FFD8B1B94CC724F43455A6BC0BB5354AE42904BF1C51DD45324C360FC3444375A62D8451B82FA2B172DF25147CDA768977B2A8DACC4C2DDBAB147588A6CDB003E9B97F42581A300B0E5E9991DAC88D5F244E6090302046328F20254A687A33D60D5D7080FCFF54A7DE01B2030B5F0E7CFD7E9821772C4C355346D58C25FB7C301EBBE7164BFDEC61F9E91DB29A63653ED9DC1B7EF566CBF6E1379CF5ECD208EA7E678175CB2FE3126774478E25CB540CB31FD48',
    #     'SERVERID': 'node7',
    #     'Hm_lvt_fa0ea664baca46780244c3019bbfa951': '1741259962',
    #     'HMACCOUNT': 'E2070DB2798F6BCC',
    #     'Hm_lvt_6580fa76366dd7bfcf663327c0bcfbe2': '1741259962',
    #     '_ga': 'GA1.1.490091217.1741259962',
    #     # 'DM5_MACHINEKEY': 'e772c0e5-3b53-43b0-934f-55f6169a34e2',
    #     'appwelfare': '1',
    #     'dm5cookieenabletest': '1',
    #     # 'firsturl': 'https%3A%2F%2Fwww.dm5.com%2Fm1609850%2F',
    #     'ComicHistoryitem_zh': 'History=88768,638770247582382207,1609850,1,0,0,0,2&ViewType=0',
    #     'readhistory_time': '1-88768-1609850-1',
    #     'dm5imgcooke': '1606877%7C37%2C1609850%7C2',
    #     # 'image_time_cookie': '1606877|638770223407022093|0,1609850|638770248898008665|1',
    #     # 'dm5imgpage': '1606877|1:1:57:0,1609850|1:1:57:0',
    #     'Hm_lpvt_fa0ea664baca46780244c3019bbfa951': '1741399290',
    #     'Hm_lpvt_6580fa76366dd7bfcf663327c0bcfbe2': '1741399290',
    #     '_ga_MP98J9MJ9J': 'GS1.1.1741399158.6.1.1741399300.43.0.0',
    # }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Referer': url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': '7940D296A3BE781=19ED29CEE96C1DF96DAE42560E4121424BBA080351871F2B9DD25369411D5AAA436258F6B31043CA8A4A129E83F6C32D183EAD22613FCB73E50DDA0A2CE9D840975F7BAE2FFD8B1B94CC724F43455A6BC0BB5354AE42904BF1C51DD45324C360FC3444375A62D8451B82FA2B172DF25147CDA768977B2A8DACC4C2DDBAB147588A6CDB003E9B97F42581A300B0E5E9991DAC88D5F244E6090302046328F20254A687A33D60D5D7080FCFF54A7DE01B2030B5F0E7CFD7E9821772C4C355346D58C25FB7C301EBBE7164BFDEC61F9E91DB29A63653ED9DC1B7EF566CBF6E1379CF5ECD208EA7E678175CB2FE3126774478E25CB540CB31FD48; SERVERID=node7; Hm_lvt_fa0ea664baca46780244c3019bbfa951=1741259962; HMACCOUNT=E2070DB2798F6BCC; Hm_lvt_6580fa76366dd7bfcf663327c0bcfbe2=1741259962; _ga=GA1.1.490091217.1741259962; DM5_MACHINEKEY=e772c0e5-3b53-43b0-934f-55f6169a34e2; appwelfare=1; dm5cookieenabletest=1; firsturl=https%3A%2F%2Fwww.dm5.com%2Fm1609850%2F; ComicHistoryitem_zh=History=88768,638770247582382207,1609850,1,0,0,0,2&ViewType=0; readhistory_time=1-88768-1609850-1; dm5imgcooke=1606877%7C37%2C1609850%7C2; image_time_cookie=1606877|638770223407022093|0,1609850|638770248898008665|1; dm5imgpage=1606877|1:1:57:0,1609850|1:1:57:0; Hm_lpvt_fa0ea664baca46780244c3019bbfa951=1741399290; Hm_lpvt_6580fa76366dd7bfcf663327c0bcfbe2=1741399290; _ga_MP98J9MJ9J=GS1.1.1741399158.6.1.1741399300.43.0.0',
    }

    params = {
        'cid': cid,
        'page': page,
        'key': '',
        'language': '1',
        'gtk': '6',
        '_cid': cid,
        '_mid': '88768',  # a fixed value?
        '_dt': '2025-03-08 10:01:40',
        '_sign': '51edf7cbd0e50ede53fc4c4ad17414bb',
    }

    response = requests.get('https://www.dm5.com/m1609850/chapterfun.ashx', params=params, headers=headers)

    ctx = execjs.compile(response.text)
    result = ctx.call("dm5imagefun")[0]

    print(f"Page {page} URL: {result}")

    # 下载每一页图片

    headers = {
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'priority': 'i',
        'referer': url,
        # 'referer': 'https://www.dm5.com/m1609850-p4/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-storage-access': 'active',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    }

    params = {
        'cid': cid,
        'key': '6b2d032a27aa570f8415d78c71108ae4',
    }

    response = requests.get(
        result,
        params=params,
        headers=headers,
    )

    # filename = str(page).zfill(2) + '.jpg'
    with open(page + '.jpg', 'wb') as f:
        f.write(response.content)

    print(f"Page {page} downloaded.")
