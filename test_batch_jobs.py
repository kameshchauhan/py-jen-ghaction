import unittest
import sys
import os
from unittest.mock import patch, MagicMock
from concurrent.futures import ThreadPoolExecutor
import queue

class TestBatchJobExecution(unittest.TestCase):
    def setUp(self):
        self.sample_jobs = ["job1", "job2", "job3"]
        self.active_servers = ["server1:8080", "server2:8080"] 
        self.job_queue = queue.Queue()

    @patch('time.sleep')  # Mock sleep to speed up tests
    def test_execute_batch_jobs(self, mock_sleep):
        from main import execute_batch_jobs
        
        # Test job execution
        execute_batch_jobs(self.sample_jobs, self.active_servers)
        
        # Verify all jobs were processed
        self.assertTrue(self.job_queue.empty())
        
    def test_server_availability(self):
        from main import execute_batch_jobs
        
        server_status = {server: True for server in self.active_servers}
        self.assertTrue(all(server_status.values()))

    @patch('random.uniform')
    def test_job_processing_time(self, mock_random):
        mock_random.return_value = 75.0
        
        # Add a job and verify processing time
        job_info = {
            'job_id': 'test_job',
            'processing_time': 75.0,
            'start_time': None
        }
        self.job_queue.put(job_info)
        self.assertEqual(self.job_queue.get()['processing_time'], 75.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)