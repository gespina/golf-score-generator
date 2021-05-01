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
c_x, c_y = 1806, 95
top_x, top_y = 1472, 63
bottom_x, bottom_y = 1472, 135

img = Image.open('images/GolfOverlay1.png')
# draw.ellipse((e_1, e_2, e_3, e_4), fill=128)
score_font = ImageFont.truetype('fonts/Exo/Exo-VariableFont_wght.ttf', 60)
top_font = ImageFont.truetype('fonts/Exo/static/Exo-Bold.ttf', 16)

with open('data/RiverviewGC_04_30_21.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader)
    rows = [GolfItem(*item) for item in csvReader]
    # print(rows)
    for row in rows:
        clear = img.copy()
        draw = ImageDraw.Draw(clear)
        score = row.total_score
        hole, shot = row.hole_shot.split('-')
        top_line = f"Hole {hole}   {row.distance}    Par {row.par}"
        bottom_line = f"Shot {shot}    {row.club}"
        draw.text((c_x, c_y), score, (255, 255, 255), anchor="mm", font=score_font)
        draw.text((top_x, top_y), top_line, (94, 0, 0), anchor="lb", font=top_font)
        draw.text((bottom_x, bottom_y), bottom_line, (94, 0, 0), anchor="lb", font=top_font)
        clear.save(f"/Users/gespina/sample/img-hole-{hole}-{shot}.png")

