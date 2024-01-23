import subprocess
script_path = 'experiment1.py'
arguments200 = ['mcts_vanilla', 'exp_mcts_vanilla', 200, 2.]
arguments500 = ['mcts_vanilla', 'exp_mcts_vanilla', 500, 2.]
arguments1000 = ['mcts_vanilla', 'exp_mcts_vanilla', 1000, 2.]
arguments1500 = ['mcts_vanilla', 'exp_mcts_vanilla', 1500, 2.]

# Construct the command to run the script
command200 = ['python', script_path] + arguments200
command500 = ['python', script_path] + arguments500
command1000 = ['python', script_path] + arguments1000
command1500 = ['python', script_path] + arguments1500

for _ in range(100):
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command200, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output200.csv', 'w', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)

for _ in range(100):
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command500, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output500.csv', 'w', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)

for _ in range(100):
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command1000, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output1000.csv', 'w', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)

for _ in range(100):
    # Run the script using subprocess and capture the output
    try:
        result = subprocess.run(command1500, check=True, capture_output=True, text=True)
        
        # Save the output to a file
        with open('output1500.csv', 'w', newline='') as output_file:
            output_file.write(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Optionally, you can also save the error output to a file
        with open('error_output.txt', 'w') as error_output_file:
            error_output_file.write(e.stderr)