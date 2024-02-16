# voice_control

# **DISCLAIMER: THIS PROJECT ONLY SUPPORTS LINUX**

## Description
Voice control script controlling robot panda over bluetooth. Using whisper.

## Installation
Clone, Github repo
```bash
git clone https://github.com/youshitsune/voice_control
```

Install required modules
```bash
cd voice_control/
pip install -r requirements.txt --break-system-packages
```

Run script for installing STT model
```bash
python3 get_model.py
```

## Usage
You first need to bind bluetooth device
```bash
sudo rfcomm bind 0 <ble_address>
```

After that, just run the script
```bash
python3 main.py
```

## Credits
[Whisper](https://github.com/openai/whisper)

## License
This project is licensed with MIT License.

