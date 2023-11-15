from Crawler import get_medical_departments, download_youtube_video


if __name__ == '__main__':
    url = 'https://www.nhimc.or.kr/dept/profList.do?deptNo=29'
    departments = get_medical_departments(url)
    print(departments)
