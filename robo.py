# -*- coding: utf-8 -*-
"""Toy Robot Simulator"""
other_commands = ["MOVE", "LEFT", "RIGHT", "REPORT"]
Faces = ["NORTH", "SOUTH", "EAST", "WEST"]
xyf_list = [0, 0, "Origin"]
face_mem = []


def slice_x(input_text):
    """Get the value x"""
    x = ""
    if command_valid(input_text) is False:
        slice_xyf = input_text[6:].split(",")
        x = int(slice_xyf[0])
        if (isinstance(x, int)) is False:
            raise ValueError('Expected interger value')
    return x


def slice_y(input_text):
    """Get the value y"""
    y = ""
    if command_valid(input_text) is False:
        slice_xyf = input_text[6:].split(",")
        y = int(slice_xyf[1])
        if (isinstance(y, int)) is False:
            raise ValueError('Expected interger value')
    return y


def slice_f(input_text):
    """Which direction is the robot facing"""
    f = ""
    if command_valid(input_text) is False:
        slice_xyf = input_text[6:].split(",")
        f = slice_xyf[2].upper()
        if f not in Faces:
            raise ValueError('Expected NORTH, SOUTH, EAST or WEST')
    return f


def on_table(x, y):
    """Check if it is within the square"""
    on_square = False
    x_ontable = False
    y_ontable = False
    if(x >= 0 and x <= 5) is True:
        x_ontable = True
    if(y >= 0 and y <= 5) is True:
        y_ontable = True
    if(x_ontable and y_ontable) is True:
        on_square = True
    else:
        on_square = False
    return on_square


def command_valid(input_text):
    """If command not Place, is it valid?"""
    is_valid = False
    if input_text in other_commands:
        is_valid = True
    return is_valid

    
def place_validation(input_text):
    """Is the input place a valid position for the robot?"""   
    place_txt = input_text[:5].upper()
    Faces = ["NORTH", "SOUTH", "EAST", "WEST"]
    f_valid = False
    place_txt_valid = False
    xyf_txt_valid = False 
    if command_valid(input_text) is False:
        x = slice_x(input_text)
        y = slice_y(input_text)
        f = slice_f(input_text)
        xy_int = isinstance(x, int) is True and isinstance(x, int)
    if f in Faces:
        f_valid = True
    if xy_int is True and f_valid is True and on_table(x, y) is True:
        xyf_txt_valid = True   
    if place_txt == "PLACE" and xyf_txt_valid is True:
        place_txt_valid = True
    return place_txt_valid


def place(input_text):
    """Execute command place"""
    x = slice_x(input_text)
    y = slice_y(input_text)
    if place_validation(input_text) is True and on_table(x, y) is True:
        xyf_list[0] = x
        xyf_list[1] = y
        xyf_list[2] = slice_f(input_text)
        face_mem.append(slice_f(input_text))


def facing():
    """Where is the robot facing"""
    if face_mem[-1] == "NORTH":
        return "y_pos"
    if face_mem[-1] == "SOUTH":
        return "y_neg"
    if face_mem[-1] == "WEST":
        return "x_neg"
    if face_mem[-1] == "EAST":
        return "x_pos"
    else:
        return None


def move():
    """Execute command move"""
    x = xyf_list[0]
    y = xyf_list[1]
    if facing() == "y_pos":
        y = y + 1
        if on_table(x, y) is True:
            xyf_list[1] += 1
    elif facing() == "y_neg":
        y = y - 1
        if on_table(x, y) is True:
            xyf_list[1] -= 1
    elif facing() == "x_pos":
        x = x + 1
        if on_table(x, y) is True:
            xyf_list[0] += 1
    elif facing() == "x_neg":
        x = x + 1
        if on_table(x, y) is True:
            xyf_list[0] -= 1


def left():
    """Execute command left"""
    if face_mem[-1] == "NORTH":
        face_mem.append("WEST")
    elif face_mem[-1] == "WEST":
        face_mem.append("SOUTH")
    elif face_mem[-1] == "SOUTH":
        face_mem.append("EAST")
    elif face_mem[-1] == "EAST":
        face_mem.append("NORTH")


def right():
    """Execute command right"""
    if face_mem[-1] == "NORTH":
        face_mem.append("EAST")
    if face_mem[-1] == "WEST":
        face_mem.append("NORTH")
    if face_mem[-1] == "SOUTH":
        face_mem.append("WEST")
    if face_mem[-1] == "EAST":
        face_mem.append("SOUTH")


def report():
    """Print current position"""
    return "{},{},{}".format(xyf_list[0], xyf_list[1], face_mem[-1])


while True:
    command = input("").strip().upper()
    if command[:5].upper() == "PLACE":
        place(command)
    elif command_valid(command) is True:
        if command == "MOVE":
            move()
        if command == "LEFT":
            left()
        if command == "RIGHT":
            right()
        if command == "REPORT":
            print(report())
    elif command == "Q":
        break
