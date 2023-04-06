import time
from python_get_resolve import GetResolve


def timecode_from_frame(frame, fps=24, offset=0):
    return time.strftime("01:%M:%S:00", time.gmtime((frame + offset) / fps))


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

sorted_marker_keys = sorted(markersList.keys())
blue_markers = [
    m for m in sorted_marker_keys if markersList[m]['color'] == 'Blue']
# print(blue_markers)

keys_file_names = [(k, 'img-%s.png' % markersList[k]['name']) for k in blue_markers]
# print(keys_file_names)

for frame_start, filename in keys_file_names:
    for clip in clips:
        if clip.GetName() == filename:
            tc = timecode_from_frame(frame_start)
            clip.SetClipProperty('Start TC', tc)


sys.exit(0)
