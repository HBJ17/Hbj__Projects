from pydub import AudioSegment
import wave
import json
from vosk import Model, KaldiRecognizer

# Convert to 16kHz WAV
input_file = r"D:\Studies\PycharmProjects\PythonProject\Audio\WhatsApp Audio 2025-09-21 at 14.24.45_38d0db8a.wav"
output_file = r"D:\Studies\PycharmProjects\PythonProject\Audio\WhatsApp Audio 2025-09-21 at 14.24.45_38d0db8a_fixed.wav"

sound = AudioSegment.from_file(input_file)
sound = sound.set_frame_rate(16000).set_channels(1)
sound.export(output_file, format="wav")

# Load model
model = Model(r"D:\Studies\PycharmProjects\PythonProject\files\vosk-model-small-en-us-0.15")

# Open fixed WAV file
wf = wave.open(output_file, "rb")
rec = KaldiRecognizer(model, wf.getframerate())

results = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        results.append(json.loads(rec.Result()))

results.append(json.loads(rec.FinalResult()))

transcription = " ".join([res.get("text", "") for res in results])
print("Transcription:", transcription)

