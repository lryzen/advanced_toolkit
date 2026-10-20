#advanced_toolkit.py
#After downloading and putting into your python folder remove the file extention. 
#Define all variable needed globally in functions
usrout = 'usrin() has not ran'
charout = 'charin() has not ran'

#Take user input and save it to the variable usrin
def usrin(prompt=">>> "):
  global usrout
  usrout = input(prompt)

#Take the user input and save only a selected character
def charin(prompt=">>> ", lower=False):
  global charout
  usrin = input(prompt)
  if lower:
    charout = usrin[0].lower()
  elif lower == False:
    charout = usrin[0]
  else:
    raise runtimeError("Error in logic for paramater lower in charin()")
