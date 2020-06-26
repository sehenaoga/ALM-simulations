# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
line1 = FindSource('Line1')

# set active source
SetActiveSource(line1)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/AT/AT1.csv', proxy=line1)

# find source
line2 = FindSource('Line2')

# set active source
SetActiveSource(line2)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/AT/AT2.csv', proxy=line2)

# find source
line3 = FindSource('Line3')

# set active source
SetActiveSource(line3)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/AT/AT3.csv', proxy=line3)

# find source
rT11 = FindSource('RT1.1')

# set active source
SetActiveSource(rT11)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT1-1.csv', proxy=rT11)

# find source
rT12 = FindSource('RT1.2')

# set active source
SetActiveSource(rT12)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT1-2.csv', proxy=rT12)

# find source
rT13 = FindSource('RT1.3')

# set active source
SetActiveSource(rT13)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT1-3.csv', proxy=rT13)

# find source
rT21 = FindSource('RT2.1')

# set active source
SetActiveSource(rT21)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT2-1.csv', proxy=rT21)

# find source
rT22 = FindSource('RT2.2')

# set active source
SetActiveSource(rT22)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT2-2.csv', proxy=rT22)

# find source
rT23 = FindSource('RT2.3')

# set active source
SetActiveSource(rT23)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT2-3.csv', proxy=rT23)

# find source
rT31 = FindSource('RT3.1')

# set active source
SetActiveSource(rT31)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT3-1.csv', proxy=rT31)

# find source
rT32 = FindSource('RT3.2')

# set active source
SetActiveSource(rT32)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT3-2.csv', proxy=rT32)

# find source
rT33 = FindSource('RT3.3')

# set active source
SetActiveSource(rT33)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT3-3.csv', proxy=rT33)

# find source
rT41 = FindSource('RT4.1')

# set active source
SetActiveSource(rT41)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT4-1.csv', proxy=rT41)

# find source
rT42 = FindSource('RT4.2')

# set active source
SetActiveSource(rT42)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT4-2.csv', proxy=rT42)

# find source
rT43 = FindSource('RT4.3')

# set active source
SetActiveSource(rT43)

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run11/Postprocessing/RT/RT4-3.csv', proxy=rT43)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).