import requests
from bs4 import BeautifulSoup
from pytube import YouTube

def get_medical_departments(url):    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    department_list = []
    for department in soup.select('.x_dept_info'):
        department_list.append(department.text.strip())
    return department_list



def download_youtube_video(url, path):
    """
    YouTube 동영상을 MP4 형식으로 다운로드하는 함수.

    :param url: YouTube 동영상의 URL
    :param path: 저장할 파일 경로 (예: 'downloads/video.mp4')
    """
    yt = YouTube(url)
    video = yt.streams.filter(file_extension='mp4').get_lowest_resolution()
    video.download(output_path=path)
