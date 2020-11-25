import sys
import math

def define_rotation_cyle(rotation):
    """We return a cycle of rotation depending on the movement of the cube"""
    if "x" in rotation:
        return ["U", "B", "D", "F"]
    elif "y" in rotation:
        return ["L", "B", "R", "F"]
    else:
        return ["U", "R", "D", "L"]

def apply_rotation(face, rotation):
    """We apply the rotation to the face given in parameter"""
    clockwise = False if "'" in rotation else True
    rotation_cycle = define_rotation_cyle(rotation)
    
    #If the applied rotation will change the position of the face
    if face in rotation_cycle:
        index_face = rotation_cycle.index(face)
        if index_face < len(rotation_cycle) - 1 and clockwise:
            return rotation_cycle[index_face+1]
        elif index_face == len(rotation_cycle)-1 and clockwise:
            return rotation_cycle[0]
        elif index_face > 0 and not clockwise:
            return rotation_cycle[index_face-1]
        elif index_face == 0 and not clockwise:
            return rotation_cycle[len(rotation_cycle)-1]
    else:
        return face

rotations = input().split(" ")
face_1 = input()
face_2 = input()

#We apply the rotations
for rotation in rotations:
    face_1 = apply_rotation(face_1, rotation)
    face_2 = apply_rotation(face_2, rotation)

#Answer
print(face_1)
print(face_2)