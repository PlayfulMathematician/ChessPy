import copy
class MoveError(Exception):
    pass
DiagonalError = lambda:MoveError("bishop must move diagonally")
PieceBlockingMovementError = lambda piece_name,loc: MoveError(f"there is a piece blocking the {piece_name} from moving to {loc}")
def coords_to_pos(coords):
    convert_dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'h':7}
    for i in convert_dict.keys():
        if convert_dict[i] == coords[0]:
            return i + str(coords[1]) 
class Piece():
    def __init__(self,color,pos,brd,typ):
        self.color=color
        self.typ = typ
        self.pos=pos
        self.brd= brd
    def convert_to_coords(self):
        conversion_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'h':7}
        return (conversion_dict[self.pos[0]],int(self.pos[1]))
    
    def get_info(self):
        return {'color':self.color,'typ':self.typ,'pos':self.pos}
class Bishop(Piece):
    def __init__(self,*args):
        super().__init__(*args,'B')
    def move(self,coords):
        coords=Piece.convert_to_coords(Piece(0,coords,self.brd,self.typ))
        coords2= self.convert_to_coords()
        for piece in brd:
            crds = Piece.convert_to_coords(Piece(0,piece["pos"],[],[]))
            if (crds == coords2) && (piece["color"] == self.color):
                raise PieceBlockingMovementError("bishop",coords)
                
            if abs(coords[0]-crds[0])==abs(coords[1]-crds[1]):
                pass
                    
        if abs(coords[0]-coords2[0])==abs(coords[1]-coords2[1]):
            self.pos= coords_to_pos(coords)
        else:
            raise DiagonalError()
#b=Bishop('b','f6',[])
#
