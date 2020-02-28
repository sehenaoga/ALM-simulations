# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
aT = FindSource('AT')

# set active source
SetActiveSource(aT)

# find source
line1 = FindSource('Line1')

# set active source
SetActiveSource(line1)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run21/Postprocessing/AT/AT1.csv', proxy=line1)

# find source
line2 = FindSource('Line2')

# set active source
SetActiveSource(line2)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run21/Postprocessing/AT/AT2.csv', proxy=line2)

# find source
line3 = FindSource('Line3')

# set active source
SetActiveSource(line3)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run21/Postprocessing/AT/AT3.csv', proxy=line3)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).