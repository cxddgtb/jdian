import requests
import os

github_token = os.getenv('GITHUB_TOKEN')  # 请确保在GitHub仓库的Secrets中设置了GITHUB_TOKEN

def get_all_repos():
    url = 'https://api.github.com/repositories'
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            # 处理每个仓库的信息，可以输出到文件或者其他地方
            print(repo['full_name'])
    else:
        print(f'Failed to fetch repositories. Status code: {response.status_code}')

if __name__ == '__main__':
    get_all_repos()
