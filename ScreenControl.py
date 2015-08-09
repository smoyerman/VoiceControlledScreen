import speech_recognition as sr
import ILI9341

# Construct screen and speech recognizer
disp = ILI9341.ILI9341()
disp.begin()
r = sr.Recognizer()

# Hard-coded colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
puple = (100,0,100)

# Loop and listen 10 times
for i in range(10):

    # Listen for audio each time
    print "Start Listening..."
    with sr.Microphone() as source:
        # Only check for ambient noise the first time
        if i == 0:
            r.adjust_for_ambient_noise(source)      
        audio = r.listen(source)                   
    print "Done Listening..."

    try:
        # Parse text
        speechString = r.recognize(audio)
        print("You said " + speechString)   
        speechArray = speechString.split()
        # Check for colors
        if "red" in speechArray: color = red 
        elif "blue" in speechArray: color = blue 
        elif "green" in speechArray: color = green
        elif "purple" in speechArray: color = purple
        elif "white" in speechArray: color = white 
        elif "black" in speechArray: color = black
        # Display to screen	
        disp.clear(color)
        disp.display()

    # Check for error
    except LookupError:  
        print("Could not understand audio")
