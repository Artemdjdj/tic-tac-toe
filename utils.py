class button:
    def __init__(self):
        self.clicked = False
        self.type = None


dictionary = {
    'button11' : [0,0],
    'button12' : [0,1],
    'button13' : [0,2],
    'button21' : [1,0],
    'button22' : [1,1],
    'button23' : [1,2],
    'button31' : [2,0],
    'button32' : [2,1],
    'button33' : [2,2],
}

win_combinations_dict = [
   [[0,0],[0,1],[0,2]],
   [[1,0],[1,1],[1,2]],
   [[2,0],[2,1],[2,2]],
   [[0,0],[1,0],[2,0]],
   [[0,1],[1,1],[2,1]],
   [[0,2],[1,2],[2,2]],
   [[0,0],[1,1],[2,2]],
   [[0,2],[1,1],[2,0]],
]
def get_position(string):
    for key, values in dictionary.items():
        if key == string:
            return values
    return []
        
def get_key(value):
    for key, values in dictionary.items():
        if value == values:
            return key
    return "nothing"

