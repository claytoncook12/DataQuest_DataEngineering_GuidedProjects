import concurrent.futures
from bs4 import BeautifulSoup
import time
import json

def extract_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find("div", id="content")
    return str(div)
    
def main():
    
    #Read in data file
    with open('wiki_content.txt', 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    process_pool = [6,5,4,3,2,1]
    
    for num in process_pool:
        content_extracted = None
        start = time.time()
        pool = concurrent.futures.ProcessPoolExecutor(max_workers=num)
        content_extracted = pool.map(extract_content,content)
        content_extracted = list(content_extracted)
        end = time.time() - start
        print("Time of {} processes: {:0.2f} secs".format(num,end))
    
    # Write out content_extracted file
    with open('wiki_content_extracted.txt', 'w', encoding='utf-8') as f:
        json.dump(content_extracted, f)
        
if __name__=='__main__':
    main()
