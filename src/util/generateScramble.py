import random


def generateScramble(length=20):
  faces = ['U', 'D', 'L', 'R', 'F', 'B']
  modifiers = ['',"'", '2']
  scramble = []

  last_face = None

  for _ in range(length):
    face = random.choice(faces)

    while face == last_face:
      face = random.choice(faces)
    
    modifier = random.choice(modifiers)
    scramble.append(face + modifier)
    last_face = face
  
  return ' '.join(scramble)

