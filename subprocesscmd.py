import subprocess

#This part properly executes ta_runner file by eleminating space between the parameters and variables
mode = "test_windows"
config = "$SAMPLE"
payload = "tests.zip,bootstrap_windows.py"

subprocess.call(['python', 'safezone/ta_runner.py', '--mode=' + mode, '--config=' + config, '--payload=' + payload])



#This part for testing 

#mode = "--mode=test_windows"
#config = "--config=$SAMPLE"
#payload = "--payload=tests.zip,bootstrap_windows.py"
#subprocess.call(['python', 'green/ta_runner.py', mode, config, payload])
