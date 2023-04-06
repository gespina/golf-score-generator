from python_get_resolve import GetResolve

# =================================================
data = {
    '1st-1st': {
        'par': '4',
        'distance': '335y',
        'club': 'Driver',
        'total_score': 'E'
    },
    '1st-2nd': {
        'par': '4',
        'distance': '160y',
        'club': '6i',
        'total_score': 'E'
    },
    '1st-3rd': {
        'par': '4',
        'distance': '115y',
        'club': 'PW',
        'total_score': 'E'
    },
    '1st-4th': {
        'par': '4',
        'distance': '20ft',
        'club': 'Putter',
        'total_score': 'E'
    },
    '1st-5th': {
        'par': '4',
        'distance': '6ft',
        'club': 'Putter',
        'total_score': 'E'
    },
    '1st-6th': {
        'par': '4',
        'distance': '1ft',
        'club': 'Putter',
        'total_score': '+2'
    },
}
# =================================================

resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
clip = project.GetCurrentTimeline().GetCurrentVideoItem()
currentTimeline = project.GetCurrentTimeline()
offset = currentTimeline.GetStartFrame()
markersList = currentTimeline.GetMarkers()
if not markersList:
    print('No Markers found!')
    sys.exit(0)

# print(markers)

fu = resolve.Fusion()
resolve.OpenPage("Fusion")
comp = fu.GetCurrentComp()
# Get start of comp
if clip.GetName() == 'Adjustment Clip':
    start = 0
else:
    start = int(comp.GetAttrs()['COMPN_RenderStart'])

hole = comp.FindTool("Hole")
hole.StyledText[0] = '1st'

par = comp.FindTool("Par")
par.StyledText[0] = 'Par --'

yards = comp.FindTool("Yards")
yards.StyledText[0] = '--Yds'

shot = comp.FindTool("Shot")
shot.StyledText[0] = '1st Shot'

score = comp.FindTool("Score")
score.StyledText[0] = 'E'

sorted_marker_keys = sorted(markersList.keys())
data_keys = sorted(data.keys())
# print(data_keys)
combined_keys = zip(sorted_marker_keys, data_keys)
# print(combined_keys)
for marker, shot_cnt in combined_keys:
    hole_num, shot_num = shot_cnt.split('-')
    par_num = data[shot_cnt]['par']
    distance = data[shot_cnt]['distance']
    total_score = data[shot_cnt]['total_score']

    frameNumber = int(marker) - int(start)
    hole.StyledText[frameNumber] = '%s Hole' % (hole_num)
    shot.StyledText[frameNumber] = '%s Shot' % (shot_num)
    par.StyledText[frameNumber] = 'Par %s' % (par_num)
    yards.StyledText[frameNumber] = distance
    score.StyledText[frameNumber] = total_score

sys.exit(0)
