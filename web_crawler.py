import requests
from bs4 import BeautifulSoup

def get_medical_departments(url):    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    department_list = []
    for department in soup.select('.x_dept_info'):
        department_list.append(department.text.strip())
    return department_list


if __name__ == '__main__':
    url = 'https://www.nhimc.or.kr/dept/profList.do?deptNo=29'
    departments = get_medical_departments(url)
    print(departments)
