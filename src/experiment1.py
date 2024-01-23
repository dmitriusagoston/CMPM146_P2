import subprocess
import time
script_path = '.\\src\\p2_exp.py'
arguments50 = ['mcts_vanilla', 'exp_mcts_vanilla', '50', '2.']
arguments200 = ['mcts_vanilla', 'exp_mcts_vanilla', '200', '2.']
arguments500 = ['mcts_vanilla', 'exp_mcts_vanilla', '500', '2.']
arguments1000 = ['mcts_vanilla', 'exp_mcts_vanilla', '1000', '2.']


# Construct the command to run the script
command50 = ['python', script_path] + arguments50
command200 = ['python', script_path] + arguments200
command500 = ['python', script_path] + arguments500
command1000 = ['python', script_path] + arguments1000

print("Starting 50 nodes test \n")
print("Processing: ", end='', flush=True)
for _ in range(2):
    print("\rProcessing: {}%".format(_), end='', flush=True)
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command50, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output50.csv', 'a', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)
print("Finished 50 nodes test \n")
print("Starting 200 nodes test \n")
print("Processing: ", end='', flush=True)
for _ in range(2):
    print("\rProcessing: {}%".format(_), end='', flush=True)
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command200, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output200.csv', 'a', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)
print("Finished 200 nodes test \n")
print("Starting 500 nodes test \n")
print("Processing: ", end='', flush=True)
for _ in range(2):
    print("\rProcessing: {}%".format(_), end='', flush=True)
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command500, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output500.csv', 'a', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)
print("Finished 500 nodes test \n")
print("Starting 1000 nodes test \n")
print("Processing: ", end='', flush=True)
for _ in range(2):
    print("\rProcessing: {}%".format(_), end='', flush=True)
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command1000, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output1000.csv', 'a', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)
print("Finished 1000 nodes test \n")