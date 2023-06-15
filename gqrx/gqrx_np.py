import pyaudio
import numpy as np

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

try:
    while True:
        # Read audio stream data
        data = stream.read(chunk_size)

        # Convert audio data to NumPy array
        audio_array = np.frombuffer(data, dtype=np.float32)

        # Print the audio array
        print(audio_array)

except KeyboardInterrupt:
    # Close the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()
