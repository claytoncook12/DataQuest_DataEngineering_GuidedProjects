import concurrent.futures
from bs4 import BeautifulSoup
import time
import json
from collections import Counter

def tag_count(content):
    found = BeautifulSoup(content, 'html.parser').find_all()
    c = Counter([tag.name for tag in found])
    return c

def main():
    
    # Read in data file
    with open('wiki_content_extracted.txt', 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    process_pool = [6,5,4,3,2,1]
    
    for num in process_pool:
        c = None
        start = time.time()
        pool = concurrent.futures.ProcessPoolExecutor(max_workers=num)
        content_count = pool.map(tag_count,content)
        content_count = list(content_count)
        end = time.time() - start
        print("Time of {} processes: {:0.2f} secs".format(num,end))
        
    # Write out content_count file
    with open('wiki_content_count.txt', 'w', encoding='utf-8') as f:
        json.dump(content_count, f)
        
if __name__=='__main__':
    main()
