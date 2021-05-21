from PIL import Image, ImageFont, ImageDraw, ImageColor
from data.WhittierNarrowsData import data, test
from proj_constants import *
from dataclasses import dataclass
from dataclass_csv import DataclassReader


@dataclass
class GolfScoreCard:
    hole: int
    par: int
    distance: int
    score: int
    score_name: str


img = Image.open(SCORE_TOP_BG)

large_font = ImageFont.truetype(HANSIEF_FONT, HOLE_FONT_SIZE)
two_line_font_1 = ImageFont.truetype(MONTSERRAT_LIGHT, TWO_LINE_FONT_SIZE)
two_line_font_2 = ImageFont.truetype(MONTSERRAT_BOLD, TWO_LINE_FONT_SIZE)
dark_color = ImageColor.getcolor(DARK_FONT, 'RGB')

with open('data/WhittierNarrows_5_14_21_scores.csv', 'r') as csvFile:
    rows = DataclassReader(csvFile, GolfScoreCard)
    distances = dict([(r.hole, (f'PAR {r.par}', f'{r.distance} YARDS')) for r in rows])


for key, score in data.items():
    clear = img.copy()
    draw = ImageDraw.Draw(clear)
    hole, shot = key.split('-')
    hole = int(hole)
    to_hole, club, curr_score = score
    to_hole_str = f'TO HOLE: {to_hole}'

    par_str, distance_str = distances[hole]

    draw.text(HOLE_XY, str(hole), WHITE_FONT, anchor="rm", font=large_font)
    draw.text(PAR_XY, par_str, dark_color, anchor="lb", font=two_line_font_1)
    draw.text(PAR_DISTANCE_XY, distance_str, dark_color, anchor="lb", font=two_line_font_2)
    draw.text(NAME_XY, PLAYER_NAME, WHITE_FONT, anchor="mm", font=large_font)
    draw.text(CURR_SCORE_XY, curr_score, dark_color, anchor="mm", font=large_font)
    draw.text(CURR_SHOT_XY, shot, dark_color, anchor="lb", font=two_line_font_1)
    draw.text(SHOT_XY, 'SHOT', dark_color, anchor="lb", font=two_line_font_2)
    draw.text(TO_HOLE_XY, to_hole_str, WHITE_FONT, anchor="lb", font=two_line_font_1)
    draw.text(CLUB_XY, club, WHITE_FONT, anchor="lb", font=two_line_font_2)
    clear.save(f'/Users/gespina/sample4/img-{key}.png')
#
#         draw.text(player_pos, player_name, fnt_rgb, anchor="ls", font=player_font)
#         draw.text(circle_xy, score, (255, 255, 255), anchor="mm", font=score_font)
#         draw.text(top_xy, top_line, fnt_rgb, anchor="ls", font=top_font)
#         draw.text(bottom_xy, bottom_line, fnt_rgb, anchor="ls", font=top_font)
#         clear.save(f"/Users/gespina/dad_miller_05_06_2021/img-{hole}-{shot}.png")
