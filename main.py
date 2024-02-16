import serial
import whisper
import os
import time

model = whisper.load_model("small")
options = whisper.DecodingOptions(fp16=False)
#port = serial.Serial("/dev/rfcomm0")

def sim(a, b):
    l = max(len(a), len(b))
    a+=(" "*(l-len(a)))
    b+=(" "*(l-len(b)))
    r = 0
    for i in range(l):
        if a[i] == b[i]:
            r+=1

    return round(r/l, 2)


def record():
    os.system("arecord audio.mp3 -d 3")
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
    while True:
        r = stt()
        print(r)
        if r == "napred":
            port.write(b"%4#4")
        elif r == "nazad":
            port.write(b"%7#7")

if __name__ == "__main__":
    run()


