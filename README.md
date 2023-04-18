# Discord-Chat-Bot

<p align='center'>
<img src='https://forthebadge.com/images/badges/built-with-love.svg'> <img src='https://forthebadge.com/images/badges/made-with-python.svg'><br>
<img src='https://img.shields.io/github/license/gamerrio/discord-chat-bot?style=for-the-badge'><br>
<img src='https://img.shields.io/badge/os-windows-green'>
<img src='https://img.shields.io/badge/os-linux-green'>
<img src='https://img.shields.io/badge/os-mac-green'></p>

***
### A Discord Chat Bot Made using discord.py and Gpt4all (pyllamacpp)
<br>

> ## **Usage:**
1. Clone this repository
```
git clone https://github.com/gamerrio/Discord-Chat-Bot.git
cd Discord-Chat-Bot
```
2. Download [gpt4all-lora-quantized-ggml.bin](https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized-ggml.bin) from [GPT4All](https://github.com/nomic-ai/gpt4all#gpt4all-compatibility-ecosystem) into root of repository.
3. Create a python virtual environment.
```
echo "Create Virtual Environment"
python -m venv myenv
echo "Activate Environment"
source myenv/bin/activate
```
4. Install packages.
```
echo "Install packages"
pip install -r requirements.txt
```
5. create a .env file that should look like:
```
TOKEN ="your-actual-discord-token-goes-here"
MODEL = "you-model-name-here.bin"
```
6. run the python file
```
python3 main.py
```
