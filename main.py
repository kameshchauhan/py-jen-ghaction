import random
import py_lib
import pandas as pd
import csv
from concurrent.futures import ThreadPoolExecutor
import queue
import matplotlib.pyplot as plt
import time
import requests

def main():
    print("Hello from py-app!")
    print(py_lib.hello())

def test():
    compare_csvs_pandas(['file1.csv', 'file2.csv'], 'diff_pandas.csv')
    compare_csvs_manual(['file1.csv', 'file2.csv'], 'diff_manual.csv') 
    


def compare_csvs_pandas(file_list, output_file):
   # Read all CSVs into DataFrames and concatenate
   dfs = [pd.read_csv(f) for f in file_list]
   # Concatenate and drop duplicates that appear in all files
   all_data = pd.concat(dfs, keys=range(len(dfs)))
   # Find rows that are not duplicated across all files
   diff = all_data.drop_duplicates(keep=False)
   # Write the difference to output
   diff.to_csv(output_file, index=False)

def compare_csvs_manual(file_list, output_file):
   # Read all CSVs into sets of tuples (rows)
   csv_rows = []
   headers = None
   for f in file_list:
      with open(f, newline='') as csvfile:
         reader = csv.reader(csvfile)
         file_headers = next(reader)
         if headers is None:
            headers = file_headers
         rows = set(tuple(row) for row in reader)
         csv_rows.append(rows)
   # Find symmetric difference across all sets
   diff_rows = set.union(*csv_rows) - set.intersection(*csv_rows)
   # Write the difference to output
   with open(output_file, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(headers)
      for row in diff_rows:
         writer.writerow(row)

# Example usage:
# compare_csvs_pandas(['file1.csv', 'file2.csv'], 'diff_pandas.csv')
# compare_csvs_manual(['file1.csv', 'file2.csv'], 'diff_manual.csv')

def test1():
    dfs = [pd.read_csv(f) for f in ['file1.csv','file2.csv']]  
    all_data = pd.concat(dfs)
   
def execute_batch_jobs(jobs, servers):
    """
    Execute batch jobs in parallel across available servers
    jobs: list of jobs to execute
    servers: list of active server addresses
    """
    job_queue = queue.Queue()
    server_status = {server: True for server in servers}  # True means server is available
    
    # Initialize job queue with jobs and add processing time
    for job in jobs:
        processing_time = random.uniform(50,100)
        job_info = {
            'job_id': job,
            'processing_time': processing_time,
            'start_time': None
        }
        job_queue.put(job_info)

    def process_job(server):
        while not job_queue.empty():
            if not server_status[server]:
                continue
            try:
                job = job_queue.get_nowait()
                server_status[server] = False  # Mark server as busy
                print(f"Processing job {job['job_id']} on server {server}")
                # Simulate job processing
                time.sleep(job['processing_time']/100)  # Convert to seconds
                server_status[server] = True  # Mark server as available
                job_queue.task_done()
            except queue.Empty:
                break
                break

    with ThreadPoolExecutor(max_workers=len(servers)) as executor:
        executor.map(process_job, servers)



import cowsay
def test2():
    # basic python
    x = input("Type a number: ")
    y = input("Type another number: ")

    sum = int(x) + int(y)

    print("The sum is: ", sum)

if __name__ == "__main__":
    # Example usage
    test2()
    # sample_jobs = ["job1", "job2", "job3", "job4"]
    # active_servers = ["server1:8080", "server2:8080", "server3:8080"]
    # execute_batch_jobs(sample_jobs, active_servers)
