from math import gamma
from time import sleep

from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []

    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) == 10:
           raise BowlingError("Bowling game already has 10 frames")
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i < 0:
            raise BowlingError("Frame index out of range")
        if i>=len(self.frames):
            print ("VAL:",len(self.frames))
            raise BowlingError("Frame index out of range")
        return self.frames[i]

    def calculate_score(self) -> int:
        score = 0
        for i,frame in enumerate(self.frames):
            score=score+frame.score()
        """
        for i,frame in enumerate(self.frames):
            if frame.is_spare():
                if i== len(self.frames)-1:
                    frame.set_bonus(self.bonus_throw)
                else:
                    frame.set_bonus(self.frames(i+1).get_first_treow())
            if frame.is_strike():
                if i== len(self.frames)-1:
                    frame.set_bonus(self.bonus_throw+self.set_first_bonus_throw())
                else:
                    if self.frames[i+1].is_strike():
                        frame.set_bonus(self.frames[i+1].get_first_treow()+self.frames[i+1].get_second_treow()+self.frames[i+2].get_third_treow())
                    else:
                        frame.set_bonus(self.frames[i+1].get_first_treow()+self.frames[i+1].get_third_treow())
            score=score+frame.get_score()
            """
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self.bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self.bonus_throw = bonus_throw