import ai2thor.controller
import keyboard
import time 
import random
import cv2
from stranscription import sync_record, transcribe
player_size = 500
controller = ai2thor.controller.Controller()
controller.start(player_screen_width=player_size * 1.5, player_screen_height=player_size)
event = controller.step(dict(action='Initialize', gridSize=0.25, renderObjectImage = False))

def detectPicture(event):
    img = event.cv2img
    cv2.imshow("image", img)
def pickUp(event):
        for o in event.metadata['objects']:
            if o['visible'] and o['pickupable']:
                event = controller.step(dict(action='PickupObject', objectId=o['objectId']), raise_for_failure=True)
                object_id = o['objectId']
                break
rotate = 0

event = controller.step(dict(action='Rotate',rotation=rotate))
while 1:
	sw = 0 
	#event = controller.step(dict(action='Rotate',rotation=45))
	sync_record('test.wav',3,16000,1)
	time.sleep(0.5)
	voice = transcribe('test.wav')
	for i in range(len(voice)):
		try:
			if voice[i] == 'RIGHT' and voice[i-1] =='SPIN':
				rotate +=45
				event = controller.step(dict(action='Rotate',rotation=rotate))
			if voice[i] == 'LEFT' and voice[i-1] =='SPIN':
				rotate -=45
				event = controller.step(dict(action='Rotate',rotation=rotate))

			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'ONE':
				event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'TWO':
				for j in range(2):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'THREE':
				for j in range(3):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'FOUR':
				for j in range(4):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'FIVE':
				for j in range(5):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'SIX':
				for j in range(6):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'SEVEN':
				for j in range(7):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'EIGHT':
				for j in range(8):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i+2] == 'GRID' and voice[i] == 'MOVE' and voice[i+1] == 'NINE':
				for j in range(9):
					event = controller.step(dict(action='MoveAhead'))
			if voice[i] == 'MOVE' and voice[i+1] == 'BACK':
				event = controller.step(dict(action='MoveBack'))
				#controller.reset('FloorPlan'+ str(random.randint(1, 30)))
				#controller.step(dict(action='Initialize', gridSize=0.25))
				#controller.step(dict(action = 'InitialRandomSpawn', randomSeed = 0, forceVisible = False, maxNumRepeats = 5))
				
		except:
			pass
		if keyboard.is_pressed('esc'):
			event.stop()
			break
	try:
		if voice[0] == 'TURN' and voice[1] == 'OFF':
			break
	except:
		pass
	if keyboard.is_pressed('right'):
		rotate +=15
		event = controller.step(dict(action='Rotate',rotation=rotate))
		#time.sleep(0.1)
	elif keyboard.is_pressed('left'):
		rotate -=15
		event = controller.step(dict(action='Rotate',rotation=rotate))
		#time.sleep(0.1)
	elif keyboard.is_pressed('up'):
		event = controller.step(dict(action='LookUp'))
		time.sleep(0.1)
	elif keyboard.is_pressed('down'):
		event = controller.step(dict(action='LookDown'))
		time.sleep(0.1)
	elif keyboard.is_pressed('w'):		
		event = controller.step(dict(action='MoveAhead'))
		time.sleep(0.05)
	elif keyboard.is_pressed('s'):
		event = controller.step(dict(action='MoveBack'))		
		time.sleep(0.05)
	elif keyboard.is_pressed('d'):
		time.sleep(0.05)
		event = controller.step(dict(action='MoveRight'))
	elif keyboard.is_pressed('a'):
		time.sleep(0.05)
		event = controller.step(dict(action='MoveLeft'))
	elif keyboard.is_pressed('f'):
		takePicture(event)
	elif keyboard.is_pressed('c'):
		time.sleep(0.1)
		pickUp(event)
	elif keyboard.is_pressed('v'):
		event = controller.step(dict(action='DropHandObject'))
	try:
		if voice[0] == 'TURN':
			time.sleep(0.05)
			controller.reset('FloorPlan'+ str(random.randint(1, 30)))
			controller.step(dict(action='Initialize', gridSize=0.25))
			controller.step(dict(action = 'InitialRandomSpawn', randomSeed = 0, forceVisible = False, maxNumRepeats = 5))
	except:
		pass









