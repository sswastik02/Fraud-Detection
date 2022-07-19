# Voice-Authentication-CNN
A simple Voice Authentication system using pre-trained Convolutional Neural Network.

___

## How to Run :

**Create a virtual environment**
```python3 -m venv venv```
then
```source venv/bin/activate```

   
**Install dependencies by running**  ```pip3 install -r requirments.txt```

**To install pyaudio on Python versions 3.6.9 and above, run this on terminal:
 ```sudo apt install portaudio19-dev python3-pyaudio```
 then run
 ```pip3 install pyaudio```

 Once the setup is ready, it is time to enrol users.

___


## Enrollment:
Enroll a new user using an audio file of his/her voice

``C:\Users\Desktop\Voice-Recognition-CNN>python voice_auth.py -t enroll -n "name of person" -f C:\path\to\audio\audio.wav``

## Enrollment using csv:
Enroll mutiple users using a .csv file containing list of names and file paths respectively

``C:\Users\Desktop\Voice-Recognition-CNN>python voice_auth.py -t enroll -f C:\path\to\csv\list.csv``

 
## Recognition:
Authenticate a user if it matches voice prints saved on the disk

``C:\Users\Desktop\Voice-Recognition-CNN>python voice_auth.py -t recognize -f C:\path\to\audio\audio.flac``


___

## Precautions:

Make sure to upload 2 sample audios of same user. Make sure that the speaker speaks loud and clear. To train the model better, familiarize and introduces various accented speakers with longer clips(~20s) of audio.

