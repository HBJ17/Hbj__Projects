import torch
import soundfile as sf
import numpy as np
import json
import wave
from transformers import (
    Wav2Vec2FeatureExtractor,
    Wav2Vec2ForSequenceClassification,
    AutoTokenizer,
    AutoModelForSequenceClassification
)
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer

# Stable softmax
def softmax(logits):
    exp_logits = np.exp(logits - np.max(logits))  # subtract max for stability
    return exp_logits / np.sum(exp_logits)


#Change

AUDIO_FILE_PATH = r"D:\Studies\Projects\Multi Modal Analyzer\Audio\oooo.wav"   #input audio
AUDIO_FIXED_PATH = r"D:\Studies\Projects\Multi Modal Analyzer\Audio\oooo_fix.wav"
VOSK_MODEL_PATH = r"D:\Studies\Projects\Multi Modal Analyzer\Files\vosk-model-small-en-us-0.15"  # STT


#Convert Audio to 16kHz Mono for Processing

print(f"Converting {AUDIO_FILE_PATH} to 16kHz mono...")
try:
    sound = AudioSegment.from_file(AUDIO_FILE_PATH)
    sound = sound.set_frame_rate(16000).set_channels(1)
    sound.export(AUDIO_FIXED_PATH, format="wav")
    print(f"Saved {AUDIO_FIXED_PATH}")
except Exception as e:
    print(f"Error converting audio file: {e}")
    exit()


#Speech-to-Text (Vosk)

model = Model(VOSK_MODEL_PATH)
wf = wave.open(AUDIO_FIXED_PATH, "rb")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

results = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        results.append(json.loads(rec.Result()))
results.append(json.loads(rec.FinalResult()))
wf.close()

TEXT_TRANSCRIPT = " ".join([res.get("text", "") for res in results]).strip()

print(f"Analyzing audio: {AUDIO_FIXED_PATH}")
print(f"Transcript: \"{TEXT_TRANSCRIPT}\"\n")
print("-" * 30)


#Emotion from Audio

print("Loading Audio Model...")
audio_model_name = "superb/wav2vec2-base-superb-er"
audio_feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(audio_model_name)
audio_model = Wav2Vec2ForSequenceClassification.from_pretrained(audio_model_name)

speech, _ = sf.read(AUDIO_FIXED_PATH)
inputs = audio_feature_extractor(speech, sampling_rate=16000, return_tensors="pt", padding=True)
with torch.no_grad():
    audio_logits = audio_model(**inputs).logits

audio_labels = audio_model.config.id2label
audio_scores = softmax(audio_logits[0].numpy())

print("\n--- Audio-Only Results ---")
for i, label in enumerate(audio_labels.values()):
    print(f"{label}: {audio_scores[i]:.4f}")


#Emotion from Text

print("\n" + "-" * 30)
print("Loading Text Model...")
text_model_name = "j-hartmann/emotion-english-distilroberta-base"
text_tokenizer = AutoTokenizer.from_pretrained(text_model_name)
text_model = AutoModelForSequenceClassification.from_pretrained(text_model_name)

if not TEXT_TRANSCRIPT:
    print("WARNING: Empty transcript. Using neutral emotion.")
    text_logits = torch.tensor([[0, 0, 0, 0, 1, 0, 0]])
else:
    inputs = text_tokenizer(TEXT_TRANSCRIPT, return_tensors="pt")
    with torch.no_grad():
        text_logits = text_model(**inputs).logits

text_labels = text_model.config.id2label
text_scores = softmax(text_logits[0].numpy())

print("\n--- Text-Only Results ---")
for i, label in enumerate(text_labels.values()):
    print(f"{label}: {text_scores[i]:.4f}")


#Fusion (Audio + Text)

COMMON_LABELS = ['angry', 'happy', 'neutral', 'sad']

audio_fused_logits = np.array([
    audio_logits[0][audio_model.config.label2id['ang']].item(),
    audio_logits[0][audio_model.config.label2id['hap']].item(),
    audio_logits[0][audio_model.config.label2id['neu']].item(),
    audio_logits[0][audio_model.config.label2id['sad']].item()
])

text_fused_logits = np.array([
    text_logits[0][text_model.config.label2id['anger']].item(),
    text_logits[0][text_model.config.label2id['joy']].item(),
    text_logits[0][text_model.config.label2id['neutral']].item(),
    text_logits[0][text_model.config.label2id['sadness']].item()
])

audio_probs = softmax(audio_fused_logits)
text_probs = softmax(text_fused_logits)
fused_scores = 0.5 * audio_probs + 0.5 * text_probs
fused_scores /= np.sum(fused_scores)

print("\n" + "=" * 30)
print("--- FINAL MULTIMODAL Results ---")
for i, label in enumerate(COMMON_LABELS):
    print(f"{label}: {fused_scores[i]:.4f}")


#Distress Mapping

def get_distress_level(emotion, score):
    mapping = {
        'happy': 'low distress',
        'neutral': 'low distress',
        'sad': 'medium distress',
        'angry': 'high distress'
    }
    level = mapping.get(emotion, 'undefined')
    if emotion == 'angry' and score > 0.90:
        level = 'peak emergency distress'
    elif emotion == 'sad' and score > 0.95:
        level = 'high distress'
    return level

final_emotion_index = np.argmax(fused_scores)
final_emotion = COMMON_LABELS[final_emotion_index]
final_score = fused_scores[final_emotion_index]
distress_token = get_distress_level(final_emotion, final_score)

print("---  FINAL MULTIMODAL ANALYSIS  ---")

print(f"Predicted Emotion: {final_emotion.upper()} (Score: {final_score:.4f})")
print(f"Distress Token:    {distress_token.upper()}")
