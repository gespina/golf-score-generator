import csv
from typing import NamedTuple
from PIL import Image, ImageFont, ImageDraw
import numpy


class GolfScoreCard(NamedTuple):
    hole: int
    par: int
    distance: int
    score: int


# Where the texts would go
front_nine_box = (440, 928)
back_nine_box = (985, 928)

scorecard_fn_size = 20
fnt_rgb = (106, 94, 94)


img = Image.open('images/Dad_Miller.001.png')

anime_font = ImageFont.truetype('fonts/anime-ace-20-bb-font/AnimeAce20BbBold-2Av.ttf', scorecard_fn_size)
with open('data/Dad_Miller_Score_Card.csv', 'r') as csvFile:
    # with open('data/test.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader)
    rows = [GolfScoreCard(*item) for item in csvReader]
    front_nine_score = ''
    back_nine_score = ''
    front_nine_all_scores = [int(x.score) for x in rows if int(x.hole) < 10]
    front_nine_total = numpy.sum(front_nine_all_scores)
    back_nine_all_scores = [int(x.score) for x in rows if int(x.hole) > 9]
    back_nine_total = numpy.sum(back_nine_all_scores)
    total_score = front_nine_total + back_nine_total

    for row in rows:
        if int(row.hole) == 1:
            front_nine_score = '' + row.score
        elif int(row.hole) <= 9:
            front_nine_score = front_nine_score + '    %s' % row.score
        if int(row.hole) == 5:
            front_nine_score = front_nine_score + ' '
        if int(row.hole) == 9:
            front_nine_score = front_nine_score + '    %d' % front_nine_total
        # print('Front 9: ', front_nine_score)
        if int(row.hole) > 9:
            if int(row.hole) == 10:
                back_nine_score = row.score
            else:
                back_nine_score = back_nine_score + '    %s' % row.score
        if int(row.hole) == 14:
            back_nine_score = back_nine_score + ' '
        if int(row.hole) == 18:
            back_nine_score = back_nine_score + '   %d   %d' % (back_nine_total, total_score)

        # print('Back 9', back_nine_score)

        clear = img.copy()
        draw = ImageDraw.Draw(clear)
        draw.text(front_nine_box, front_nine_score, (0, 0, 0), anchor="lm", font=anime_font)
        draw.text(back_nine_box, back_nine_score, (0, 0, 0), anchor="lm", font=anime_font)
        clear.save(f"/Users/gespina/sample/scorecard_hole_{row.hole}.png")

