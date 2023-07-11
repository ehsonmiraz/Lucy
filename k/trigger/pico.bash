read buffer < /home/pi/Desktop/jarvis2/text.txt
pico2wave -w=file1.wav "${buffer}"
aplay --rate=100 file1.wav
