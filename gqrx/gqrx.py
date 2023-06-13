import numpy as np
import matplotlib.pyplot as plt
import socket
import time


# Function to communicate with gqrx via remote control
def gqrx_command(command, host='127.0.0.1', port=7356):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(command.encode())
    response = s.recv(1024).decode()
    s.close()
    return response


# Start frequency in Hz
start_freq = 88e6
# Stop frequency in Hz
stop_freq = 108e6
# Step size in Hz
step_size = 100e3

# Time to wait for gqrx to process each step (in seconds)
wait_time = 0.001

# Collecting the data
frequencies = np.arange(start_freq, stop_freq, step_size)
waterfall_data = []

for freq in frequencies:
    gqrx_command(f'F {freq}\n')  # Set frequency
    time.sleep(wait_time)  # Wait for gqrx to process
    response = gqrx_command('l STRENGTH\n')  # Get signal strength

    signal_strength = float(response)
    print(signal_strength)
    waterfall_data.append(signal_strength)

# Display the waterfall plot
plt.imshow(np.array([waterfall_data]), aspect='auto', cmap='viridis',
           extent=[start_freq, stop_freq, 0, 1])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Signal Strength (dB)')
plt.title('Waterfall Plot')
plt.colorbar(label='Signal Strength (dB)')
plt.show()
