import pytest
from main import execute_batch_jobs, compare_csvs_pandas, compare_csvs_manual

def test_execute_batch_jobs():
    sample_jobs = ["test_job1", "test_job2"]
    servers = ["server1:8080", "server2:8080"]
    # Test shouldn't raise any exceptions
    execute_batch_jobs(sample_jobs, servers)

def test_csv_comparisons(tmp_path):
    # Create test CSV files
    file1 = tmp_path / "test1.csv"
    file2 = tmp_path / "test2.csv"
    file1.write_text("col1,col2\n1,2\n3,4")
    file2.write_text("col1,col2\n1,2\n5,6")
    
    output_pandas = tmp_path / "diff_pandas.csv"
    output_manual = tmp_path / "diff_manual.csv"
    
    compare_csvs_pandas([str(file1), str(file2)], str(output_pandas))
    compare_csvs_manual([str(file1), str(file2)], str(output_manual))
    
    assert output_pandas.exists()
    assert output_manual.exists()