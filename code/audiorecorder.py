import pyaudio
import wave
import os
from scipy.io import wavfile
import noisereduce as nr
def aram():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 16000  # Record at 16000 samples per second
    seconds = 10
    filename = "output2.wav"
    progpath2=os.path.dirname(os.path.realpath(__file__))
    audpath2 = os.path.join(progpath2, 'voice')
    os.chdir(audpath2)
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    #rate, data  = wavfile.read("output2.wav")
    #reduced_noise = nr.reduce_noise(y=data, sr=rate)
    #wavfile.write("output2.wav",rate, reduced_noise)
#aram()
def arotp():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 16000  # Record at 16000 samples per second
    seconds = 10
    filename = "output1.wav"
    progpath2=os.path.dirname(os.path.realpath(__file__))
    audpath2 = os.path.join(progpath2, 'voice')
    os.chdir(audpath2)
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    #rate, data  = wavfile.read("output1.wav")
    #reduced_noise = nr.reduce_noise(y=data, sr=rate)
    #wavfile.write("output1.wav",rate, reduced_noise)
#aram()