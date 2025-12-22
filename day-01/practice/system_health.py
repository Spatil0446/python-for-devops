import psutil  # Import psutil library to fetch system resource usage

def check_cpu_threshold():
    # Ask the user to define the CPU usage threshold
    cpu_user_threshold = int(input("Please define the CPU threshold: "))

    # Get the current CPU usage percentage (measured over 1 second)
    cpu_current = psutil.cpu_percent(interval=1)

    # Display current CPU usage and user-defined threshold
    print("Current CPU usage is:", cpu_current)
    print("CPU threshold is:", cpu_user_threshold)

    # Compare current CPU usage with the threshold
    if cpu_current > cpu_user_threshold:
        # Message shown when CPU usage exceeds the threshold
        print("CPU threshold is breached. Please check the system.")
    else:
        # Message shown when CPU usage is within the acceptable range
        print("CPU usage is normal.")

# Call the function to execute the CPU threshold check
check_cpu_threshold()