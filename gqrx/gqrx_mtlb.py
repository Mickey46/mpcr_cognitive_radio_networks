import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# Define the Gqrx parameters
sample_rate = 48000
chunk_size = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the Gqrx audio stream
stream = audio.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=sample_rate,
    input=True,
    frames_per_buffer=chunk_size
)

# Initialize the plot
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [])

# Set plot parameters
ax.set_ylim(-1, 1)
ax.set_xlim(0, chunk_size)

try:
    while True:
        # Read audio stream data
        data = stream.read(chunk_size)

        # Convert audio data to NumPy array
        audio_array = np.frombuffer(data, dtype=np.float32)

        # Update the plot
        line.set_data(np.arange(len(audio_array)), audio_array)
        plt.draw()
        plt.pause(0.001)

except KeyboardInterrupt:
    # Close the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()
