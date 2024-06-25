import random


def generateScramble(length=20):
  faces = ['U', 'D', 'L', 'R', 'F', 'B']
  modifiers = ['',"'", '2']
  scramble = []

  opposite_faces = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L',
    'F': 'B',
    'B': 'F'
  }

  last_face = None

  for _ in range(length):
    face = random.choice(faces)

    # Ensure the face is not the same as the last face or its opposite
    while face == last_face or (last_face and face == opposite_faces[last_face]):
        face = random.choice(faces)
    
    modifier = random.choice(modifiers)
    scramble.append(face + modifier)
    last_face = face
  
  return ' '.join(scramble)