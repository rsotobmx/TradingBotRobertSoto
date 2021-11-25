import pytest
import csv
from mint import CSVLogger 

class TestCSVLogger:
    def test_run(self):
        # initializing component
        logs = CSVLogger()
        
        #writing a message
        message = "test"
        logs.run(data=message)
        
        
        #assertions
        with open(logs.file_name,'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    assert row[-1]== message 
                