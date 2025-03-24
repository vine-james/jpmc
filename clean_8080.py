import subprocess


def main():


    """Step 1 - find the task id for the port number"""
    port_number = 8080  # Replace with your desired port number

    command = f'netstat -ano | findstr :{port_number}'

    # Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture output and errors
    output, error = process.communicate()


    # Print the results
    if not output:
        print("No matching connections found.")
        return 0


    if error:
        print("Error:", error)
        return 0
    

    # Proccess the output
    taskid = output.split(" ")[-1]

    print("Matching connections found.")
    print(f"Taskid: {taskid}")

    
    """Step 2 - Kill the task on the port using the task id"""
    command = f'taskkill /PID {taskid} /F'

    # Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture output and errors
    output, error = process.communicate()


    # Print the results
    if not output:
        print(f"Could not kill task: {taskid} on port: {port_number}.")
        return 0


    if error:
        print("Error:", error)
        return 0
    
    
    print(f"Killed task: {taskid} on port: {port_number}.")


    return 1

if __name__ == "__main__":
    main()