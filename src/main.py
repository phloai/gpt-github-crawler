import requests
import base64
import fnmatch
import json

def main():
    print("Starting the crawler...")

    # Load configuration from a JSON file
    with open('../config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)

    # Run the crawler
    crawled_data = crawl_github_repo()

    total = len(crawled_data)
    successful = len([item for item in crawled_data if item['content']])
    failed = total - successful

    # Save the crawled data to a file
    save_to_file(crawled_data, config['output_file_name'])

    print(f"Finished! Total {total} request: {successful} successful, {failed} failed.")
    
def get_file_content(file_url):
    print(f"Crawling {file_url}")
    
    headers = {'Authorization': f'token {config["github_token"]}'}
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        content = response.json().get('content', '')
        decoded_content = base64.b64decode(content).decode('utf-8')
        return decoded_content
    else:
        print(f"Failed to retrieve file content: {response.status_code}")
        return None

def crawl_github_repo():
    api_url = f"{config['base_url']}/{config['repo_owner']}/{config['repo_name']}/git/trees/{config['branch_name']}?recursive=1"
    headers = {'Authorization': f'token {config["github_token"]}'}
    response = requests.get(api_url, headers=headers)
    crawled_files = []

    if response.status_code == 200:
        tree = response.json().get('tree', [])
        count = 0

        for item in tree:
            if item['type'] == 'blob' and fnmatch.fnmatch(item['path'], config['match_pattern']):
                if count >= config['max_files_to_crawl']:
                    break
                file_content = get_file_content(item['url'])
                if file_content:
                    crawled_files.append({'url': item['url'], 'content': file_content})
                else:
                    crawled_files.append({'url': item['url'], 'content': ''})
                count += 1
    else:
        print(f"Failed to retrieve data: {response.status_code}")

    return crawled_files

def save_to_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
