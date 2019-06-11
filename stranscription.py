import os, sys
from pocketsphinx.pocketsphinx import * 
from pocketsphinx import LiveSpeech, get_model_path
from sphinxbase.sphinxbase import * 
import sounddevice as sd
import soundfile as sf
import numpy as np

def sync_record(filename, duration, fs, channels):
	sd.play(5.0*np.sin(2*np.pi*940*np.arange(fs)/fs), samplerate=fs, blocking=True)
	print('recording')
	myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
	sd.wait()
	sf.write(filename, myrecording, fs)
	print('done recording')

def transcribe(sample):
	modeldir=get_model_path()
	#print(modeldir)
	# Create a decoder with certain model
	config = Decoder.default_config()
	config.set_string('-hmm', modeldir+'/en-us')
	config.set_string('-lm', modeldir+'/TAR1745/1745.lm')
	config.set_string('-dict', modeldir+'/TAR1745/1745.dic')
	decoder = Decoder(config) 

	# Decode streaming data.
	decoder = Decoder(config)
	decoder.start_utt()
	stream = open(sample, 'rb')
	while True:
		buf = stream.read(1024)
		if buf:
			decoder.process_raw(buf, False, False)
		else:
			break
	decoder.end_utt()

	#print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
	output=[seg.word for seg in decoder.seg()]
	transcript = list()
	try:
		output.remove('<s>')
		output.remove('</s>')

		for i in range(len(output)):
			if output[i] == '<sil>' or output[i] == '[SPEECH]':
				pass
			else:
				transcript.append(output[i])

		print(transcript)
	except:
		print(transcript)

	return transcript
#t=1 
#i=0
#while t>0:
#	sync_record('test.wav',2,16000,1)
#	transcribe('test.wav')





