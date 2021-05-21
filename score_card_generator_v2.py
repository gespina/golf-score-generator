import csv
from PIL import Image, ImageFont, ImageDraw
import numpy
from dataclasses import dataclass
from dataclass_csv import DataclassReader
from data import dimensions


@dataclass
class GolfScoreCard:
    hole: int
    par: int
    distance: int
    score: int
    score_name: str


img = Image.open('images/scoreboard_v1.png')

dance_font = ImageFont.truetype('Dance.ttf', dimensions.score_font_size)
with open('data/WhittierNarrows_5_14_21_scores.csv', 'r') as csvFile:
    rows = DataclassReader(csvFile, GolfScoreCard)
    front_nine_scores = []
    back_nine_scores = []
    [front_nine_scores.append((r.score, r.score_name)) if r.hole < 10 else back_nine_scores.append(
        (r.score, r.score_name)) for r in rows]
    front_scores_only = [f[0] for f in front_nine_scores]
    back_scores_only = [f[0] for f in back_nine_scores]
    front_nine_total = numpy.sum(front_scores_only)
    back_nine_total = numpy.sum(back_scores_only)
    total_score = front_nine_total + back_nine_total
    all_scores = []
    all_scores.extend(front_nine_scores)
    all_scores.append((front_nine_total, 'par'))
    all_scores.extend(back_nine_scores)
    all_scores.append((total_score, 'par'))
    front_nine_box_x, front_nine_box_y = (dimensions.scorecard_x, dimensions.scorecard_y)

    for idx, (score, score_name) in enumerate(all_scores):
        idx_copy = idx
        # print(front_nine_scores[idx][0])
        clear = img.copy()
        draw = ImageDraw.Draw(clear)
        front_nine_box_x_copy = front_nine_box_x
        while idx_copy >= 0:
            draw.text((front_nine_box_x_copy - 1, front_nine_box_y + 1), str(all_scores[idx - idx_copy][0]), (255, 255, 255),
                      anchor="mm", font=dance_font)
            score_txt = all_scores[idx - idx_copy][1]
            if score_txt == 'birdie':
                draw.ellipse([front_nine_box_x_copy - 17, front_nine_box_y - 17, front_nine_box_x_copy + 14, front_nine_box_y + 14], outline='white')
            if score_txt == 'bogey' or score_txt == 'double' or score_txt == 'other':
                draw.rectangle([front_nine_box_x_copy - 14, front_nine_box_y - 17, front_nine_box_x_copy + 12, front_nine_box_y + 12], outline='white')
            if score_txt == 'double' or score_txt == 'other':
                draw.rectangle([front_nine_box_x_copy - 18, front_nine_box_y - 21, front_nine_box_x_copy + 16, front_nine_box_y + 16], outline='white')
            idx_copy -= 1
            front_nine_box_x_copy += dimensions.score_space_distance

        if idx == 9:
            scorecard = 'score_front'
        elif idx == 19:
            scorecard = 'score_total'
        elif 9 < idx < 19:
            scorecard = f'score{idx}'
        else:
            scorecard = f'score{idx + 1}'

        clear.save(f"/Users/gespina/sample3/{scorecard}.png")
