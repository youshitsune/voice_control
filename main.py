import serial
import whisper
import os
import time
import json

model = whisper.load_model("small")
options = whisper.DecodingOptions(fp16=False)
port = serial.Serial("/dev/rfcomm0")

def sim(a, b):
    l = len(a)
    b+=(" "*(l-len(b)))
    r = 0
    for i in range(l):
        if a[i] == b[i]:
            r+=1

    return round(r/l, 2)

def record():
    os.system("arecord audio.mp3 -d 2")
    audio = whisper.load_audio("audio.mp3")
    audio = whisper.pad_or_trim(audio)
    os.system("rm audio.mp3")
    return audio

def stt():
    global model, options
    audio = record()
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    result = whisper.decode(model, mel, options)
    return result.text.lower()

    
def run():
    with open("config.json", "r") as f:
        cmd = json.loads(f.read())["commands"]
    while True:
        r = stt()
        for i in list(cmd.keys()):
            if sim(i, r) >= 0.6:
                port.write(cmd[i].encode())
                break

if __name__ == "__main__":
    run()


