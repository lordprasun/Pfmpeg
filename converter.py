import ffmpy
import ffmpeg

# Converts one format to the other
inp='F:\MObtv\HEVC_Subtitle\V500_W.mp4'
out1 = 'F:\MObtv\HEVC_Subtitle\V502_W.avi'
out2 = 'F:\MObtv\HEVC_Subtitle\\9\%02d.jpg'
fileconvert = ffmpy.FFmpeg(inputs={inp: None},outputs={out1: None})
frameextract = ffmpy.FFmpeg(global_options=['-r 24/1'],inputs={inp: None},outputs={out2: None})

frameextract.run()