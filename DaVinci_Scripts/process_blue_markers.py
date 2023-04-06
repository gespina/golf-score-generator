import time
from python_get_resolve import GetResolve
import sys


resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
clip = project.GetCurrentTimeline().GetCurrentVideoItem()
currentTimeline = project.GetCurrentTimeline()
offset = currentTimeline.GetStartFrame()
markersList = currentTimeline.GetMarkers()

mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()
clips = rootFolder.GetClipList()

if not markersList:
    print('No Markers found!')
    sys.exit(0)

# print(markers)

curr_score_track = currentTimeline.GetTrackName("video", 2)
sorted_marker_keys = sorted(markersList.keys())

blue_markers = [
    m for m in sorted_marker_keys if markersList[m]['color'] == 'Blue']
blue_names = [markersList[m]['name']
              for m in blue_markers]
blue_notes = [tuple(markersList[m]['note'].strip().upper().split(','))
              for m in blue_markers]
zipped_markers = dict(zip(blue_names, blue_notes))
print(zipped_markers)

sys.exit(0)
