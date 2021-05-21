import os, sys
import csv
from typing import NamedTuple
from PIL import Image, ImageFont, ImageDraw


class GolfItem(NamedTuple):
    hole_shot: str
    par: str
    distance: str
    club: str
    total_score: str


# Where the texts would go
circle_xy = (1770, 143)
top_xy = (1165, 89)
bottom_xy = (1165, 219)
player_pos = (1165, 176)

small_fn_size = 24
score_fn_size = 112
player_fn_size = 90

fnt_rgb = (106, 94, 94)

player_name = "GLENN ESPINA"

img = Image.open('images/GolfScoreInfo.png')

score_font = ImageFont.truetype('fonts/Exo/static/Exo-Bold.ttf', score_fn_size)
top_font = ImageFont.truetype('fonts/Exo/static/Exo-Bold.ttf', small_fn_size)
player_font = ImageFont.truetype('fonts/Bebas_Neue/BebasNeue-Regular.ttf', player_fn_size)

with open('data/DadMillerMay62021.csv', 'r') as csvFile:
    # with open('data/test.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader)
    rows = [GolfItem(*item) for item in csvReader]
    # print(rows)
    for row in rows:
        clear = img.copy()
        draw = ImageDraw.Draw(clear)
        score = row.total_score
        hole, shot = row.hole_shot.split('-')
        top_line = f"{hole} HOLE          {row.distance.upper()}           PAR {row.par}"
        bottom_line = f"{shot} SHOT            {row.club.upper()}"

        draw.text(player_pos, player_name, fnt_rgb, anchor="ls", font=player_font)
        draw.text(circle_xy, score, (255, 255, 255), anchor="mm", font=score_font)
        draw.text(top_xy, top_line, fnt_rgb, anchor="ls", font=top_font)
        draw.text(bottom_xy, bottom_line, fnt_rgb, anchor="ls", font=top_font)
        clear.save(f"/Users/gespina/dad_miller_05_06_2021/img-{hole}-{shot}.png")
