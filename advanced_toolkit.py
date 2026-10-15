#advanced_toolkit.py
#Define all variable needed globally in functions
usrin = ''
charin = ''

#Take user input and save it to the variable usrin
def usrin(prompt=">>> "):
  global usrin
  usrin = input(prompt)

"""#Take the user input and save only a selected character
def charin(prompt=">>> ", index=0, lower=False):
  global charin
  usrin = input(prompt)
  if lower:
    charin = usrin[index].lower()
  elif lower == False:
    charin = usrin[index]
  else:
    raise runtimeError("Error in logic for paramater lower in charin()")
"""
