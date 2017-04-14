#coding=utf-8
'''
    python:  python3
    env:     test on windown7 and ubuntu
    detail:  下载喜马拉雅的音频
    sample:  download_url("http://www.ximalaya.com/44033346/sound/35283707")
    sample:  download_url("http://www.ximalaya.com/sound/35134756")
    sample:  download_url("http://www.ximalaya.com/66918784/album/7068935")
    sample:  download_sound("35134756")
    sample:  download_album("66918784", "7068935")
    sample:  download_page("http://www.ximalaya.com/1000202/album/2667276", 1, 10)
'''

import requests
import re
import json
import os
import gc
import random
from time import sleep
from requests.adapters import HTTPAdapter

#文件下载目录
path = 'E:/temp/'
sleep_min = 100
sleep_max = 500
max_retry = 50

request_header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Host":"www.ximalaya.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "+\
    "(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

session = requests.session()
session.mount("http://", HTTPAdapter(max_retries=max_retry))

def download_sound(song_id):
    try:
        song_json_url = 'http://www.ximalaya.com/tracks/' + song_id + '.json'
        song_json_resp = session.get(song_json_url, headers=request_header)
        song_json_str = song_json_resp.content.decode(encoding='utf-8', errors='strict')
        song_json = json.loads(song_json_str, encoding='utf-8')
        #song_json['play_path_32'] : download url
        #song_json['album_title'] : save dir 
        #song_json['title'] : save file name
        album_name, song_name = song_json['album_title'], song_json['title']
        print("正在下载 \"%s\"专辑 的 \"%s\"" % (album_name, song_name))
        path_name = path+'/'+album_name+'/'
        if not os.path.exists(path_name):
            os.makedirs(path_name)
        file_name = path_name + song_name+'.m4a'
        r = session.get(song_json['play_path_32'], stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: 
                    f.write(chunk)
                    f.flush()
        f.close()
        gc.collect()
        sleep(random.randint(sleep_min, sleep_max))
    except:
        print("下载失败，重启中...")
        gc.collect()
        sleep(random.randint(sleep_min, sleep_max))
        download_sound(song_id);
    
def download_album(user_id, album_id, url=None):
    if url == None:
        url = 'http://www.ximalaya.com/'+user_id+'/album/'+album_id
    server_data = session.get(url, headers=request_header).content.decode(\
        encoding='utf-8', errors='strict')
    re_str = 'href="/'+user_id+'/sound/\d*"'
    song_urls = re.findall(re_str, server_data)
    ids_sti, song_ids = len('href="/'+user_id+'/sound/'), []
    for song_url in song_urls:
        ids_eni = len(song_url) - 1
        if ids_sti != ids_eni:
            song_ids.append(song_url[ids_sti:ids_eni]);
    for i in range(1, len(song_ids), 1):
        download_sound(song_ids[i])
        
def download_url(url):
    album_index = url.find('album')
    sound_index = url.find('sound')
    if sound_index != -1:
        #http://www.ximalaya.com/sound/35134756
        download_sound(url[sound_index+6:])
    if album_index != -1:
        #http://www.ximalaya.com/66918784/album/7068935
        slash_index = url[0:album_index-1].rfind('/')
        user_id = url[slash_index+1:album_index-1]
        download_album(user_id, url[album_index+6:])

def download_page(url, page_start, page_end):
    #url: http://www.ximalaya.com/1000202/album/2667276
    album_index = url.find('album')
    slash_index = url[0:album_index-1].rfind('/')
    user_id = url[slash_index+1:album_index-1]
    for page_index in range(page_start, page_end+1):
        download_album(user_id, url[album_index+6:], url=url+'?page='+str(page_index))
    
if __name__ == "__main__":
    download_page("http://www.ximalaya.com/1000202/album/2667276", 1, 10)
