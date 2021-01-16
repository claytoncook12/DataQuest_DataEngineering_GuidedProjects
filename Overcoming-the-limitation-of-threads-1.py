import threading
import time
import statistics

times = []
threaded_times = []

def open_csv():
    with open('Emails.csv', encoding='utf-8') as file:
        for line in file:
            pass
    

for _ in range(100):
    start = time.time()
    open_csv()
    times.append(time.time() - start)

    
for _ in range(100):
    start = time.time()
    
    # Create and run threads
    t1 = threading.Thread(target=open_csv)
    t2 = threading.Thread(target=open_csv)
    t1.start()
    t2.start()
    
    # Join threads
    for thread in [t1,t2]:
        thread.join()
    
    threaded_times.append(time.time() - start)
    
       
print("Median time of unthreaded read (runs {}): {:.2f}".
      format(len(times),statistics.median(times)))
print("Median time of threaded read (runs {}): {:.2f}".
      format(len(threaded_times),statistics.median(threaded_times))) 
