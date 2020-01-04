# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
resultsOpenFOAM = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1546, 547]

# show data in view
resultsOpenFOAMDisplay = Show(resultsOpenFOAM, renderView1)

# trace defaults for the display properties.
resultsOpenFOAMDisplay.Representation = 'Surface'
resultsOpenFOAMDisplay.AmbientColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.ColorArrayName = [None, '']
resultsOpenFOAMDisplay.DiffuseColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.LookupTable = None
resultsOpenFOAMDisplay.MapScalars = 1
resultsOpenFOAMDisplay.MultiComponentsMapping = 0
resultsOpenFOAMDisplay.InterpolateScalarsBeforeMapping = 1
resultsOpenFOAMDisplay.Opacity = 1.0
resultsOpenFOAMDisplay.PointSize = 2.0
resultsOpenFOAMDisplay.LineWidth = 1.0
resultsOpenFOAMDisplay.RenderLinesAsTubes = 0
resultsOpenFOAMDisplay.RenderPointsAsSpheres = 0
resultsOpenFOAMDisplay.Interpolation = 'Gouraud'
resultsOpenFOAMDisplay.Specular = 0.0
resultsOpenFOAMDisplay.SpecularColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.SpecularPower = 100.0
resultsOpenFOAMDisplay.Luminosity = 0.0
resultsOpenFOAMDisplay.Ambient = 0.0
resultsOpenFOAMDisplay.Diffuse = 1.0
resultsOpenFOAMDisplay.EdgeColor = [0.0, 0.0, 0.5]
resultsOpenFOAMDisplay.BackfaceRepresentation = 'Follow Frontface'
resultsOpenFOAMDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.BackfaceOpacity = 1.0
resultsOpenFOAMDisplay.Position = [0.0, 0.0, 0.0]
resultsOpenFOAMDisplay.Scale = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.Orientation = [0.0, 0.0, 0.0]
resultsOpenFOAMDisplay.Origin = [0.0, 0.0, 0.0]
resultsOpenFOAMDisplay.Pickable = 1
resultsOpenFOAMDisplay.Texture = None
resultsOpenFOAMDisplay.Triangulate = 0
resultsOpenFOAMDisplay.UseShaderReplacements = 0
resultsOpenFOAMDisplay.ShaderReplacements = ''
resultsOpenFOAMDisplay.NonlinearSubdivisionLevel = 1
resultsOpenFOAMDisplay.UseDataPartitions = 0
resultsOpenFOAMDisplay.OSPRayUseScaleArray = 0
resultsOpenFOAMDisplay.OSPRayScaleArray = 'U'
resultsOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
resultsOpenFOAMDisplay.OSPRayMaterial = 'None'
resultsOpenFOAMDisplay.Orient = 0
resultsOpenFOAMDisplay.OrientationMode = 'Direction'
resultsOpenFOAMDisplay.SelectOrientationVectors = 'None'
resultsOpenFOAMDisplay.Scaling = 0
resultsOpenFOAMDisplay.ScaleMode = 'No Data Scaling Off'
resultsOpenFOAMDisplay.ScaleFactor = 4.5
resultsOpenFOAMDisplay.SelectScaleArray = 'None'
resultsOpenFOAMDisplay.GlyphType = 'Arrow'
resultsOpenFOAMDisplay.UseGlyphTable = 0
resultsOpenFOAMDisplay.GlyphTableIndexArray = 'None'
resultsOpenFOAMDisplay.UseCompositeGlyphTable = 0
resultsOpenFOAMDisplay.UseGlyphCullingAndLOD = 0
resultsOpenFOAMDisplay.LODValues = []
resultsOpenFOAMDisplay.ColorByLODIndex = 0
resultsOpenFOAMDisplay.GaussianRadius = 0.225
resultsOpenFOAMDisplay.ShaderPreset = 'Sphere'
resultsOpenFOAMDisplay.CustomTriangleScale = 3
resultsOpenFOAMDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
resultsOpenFOAMDisplay.Emissive = 0
resultsOpenFOAMDisplay.ScaleByArray = 0
resultsOpenFOAMDisplay.SetScaleArray = ['POINTS', 'U']
resultsOpenFOAMDisplay.ScaleArrayComponent = 'X'
resultsOpenFOAMDisplay.UseScaleFunction = 1
resultsOpenFOAMDisplay.ScaleTransferFunction = 'PiecewiseFunction'
resultsOpenFOAMDisplay.OpacityByArray = 0
resultsOpenFOAMDisplay.OpacityArray = ['POINTS', 'U']
resultsOpenFOAMDisplay.OpacityArrayComponent = 'X'
resultsOpenFOAMDisplay.OpacityTransferFunction = 'PiecewiseFunction'
resultsOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
resultsOpenFOAMDisplay.SelectionCellLabelBold = 0
resultsOpenFOAMDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
resultsOpenFOAMDisplay.SelectionCellLabelFontFamily = 'Arial'
resultsOpenFOAMDisplay.SelectionCellLabelFontFile = ''
resultsOpenFOAMDisplay.SelectionCellLabelFontSize = 18
resultsOpenFOAMDisplay.SelectionCellLabelItalic = 0
resultsOpenFOAMDisplay.SelectionCellLabelJustification = 'Left'
resultsOpenFOAMDisplay.SelectionCellLabelOpacity = 1.0
resultsOpenFOAMDisplay.SelectionCellLabelShadow = 0
resultsOpenFOAMDisplay.SelectionPointLabelBold = 0
resultsOpenFOAMDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
resultsOpenFOAMDisplay.SelectionPointLabelFontFamily = 'Arial'
resultsOpenFOAMDisplay.SelectionPointLabelFontFile = ''
resultsOpenFOAMDisplay.SelectionPointLabelFontSize = 18
resultsOpenFOAMDisplay.SelectionPointLabelItalic = 0
resultsOpenFOAMDisplay.SelectionPointLabelJustification = 'Left'
resultsOpenFOAMDisplay.SelectionPointLabelOpacity = 1.0
resultsOpenFOAMDisplay.SelectionPointLabelShadow = 0
resultsOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
resultsOpenFOAMDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
resultsOpenFOAMDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
resultsOpenFOAMDisplay.GlyphType.TipResolution = 6
resultsOpenFOAMDisplay.GlyphType.TipRadius = 0.1
resultsOpenFOAMDisplay.GlyphType.TipLength = 0.35
resultsOpenFOAMDisplay.GlyphType.ShaftResolution = 6
resultsOpenFOAMDisplay.GlyphType.ShaftRadius = 0.03
resultsOpenFOAMDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
resultsOpenFOAMDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
resultsOpenFOAMDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
resultsOpenFOAMDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
resultsOpenFOAMDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
resultsOpenFOAMDisplay.DataAxesGrid.XTitle = 'X Axis'
resultsOpenFOAMDisplay.DataAxesGrid.YTitle = 'Y Axis'
resultsOpenFOAMDisplay.DataAxesGrid.ZTitle = 'Z Axis'
resultsOpenFOAMDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
resultsOpenFOAMDisplay.DataAxesGrid.XTitleFontFile = ''
resultsOpenFOAMDisplay.DataAxesGrid.XTitleBold = 0
resultsOpenFOAMDisplay.DataAxesGrid.XTitleItalic = 0
resultsOpenFOAMDisplay.DataAxesGrid.XTitleFontSize = 12
resultsOpenFOAMDisplay.DataAxesGrid.XTitleShadow = 0
resultsOpenFOAMDisplay.DataAxesGrid.XTitleOpacity = 1.0
resultsOpenFOAMDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
resultsOpenFOAMDisplay.DataAxesGrid.YTitleFontFile = ''
resultsOpenFOAMDisplay.DataAxesGrid.YTitleBold = 0
resultsOpenFOAMDisplay.DataAxesGrid.YTitleItalic = 0
resultsOpenFOAMDisplay.DataAxesGrid.YTitleFontSize = 12
resultsOpenFOAMDisplay.DataAxesGrid.YTitleShadow = 0
resultsOpenFOAMDisplay.DataAxesGrid.YTitleOpacity = 1.0
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleFontFile = ''
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleBold = 0
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleItalic = 0
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleFontSize = 12
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleShadow = 0
resultsOpenFOAMDisplay.DataAxesGrid.ZTitleOpacity = 1.0
resultsOpenFOAMDisplay.DataAxesGrid.FacesToRender = 63
resultsOpenFOAMDisplay.DataAxesGrid.CullBackface = 0
resultsOpenFOAMDisplay.DataAxesGrid.CullFrontface = 1
resultsOpenFOAMDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.DataAxesGrid.ShowGrid = 0
resultsOpenFOAMDisplay.DataAxesGrid.ShowEdges = 1
resultsOpenFOAMDisplay.DataAxesGrid.ShowTicks = 1
resultsOpenFOAMDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
resultsOpenFOAMDisplay.DataAxesGrid.AxesToLabel = 63
resultsOpenFOAMDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
resultsOpenFOAMDisplay.DataAxesGrid.XLabelFontFile = ''
resultsOpenFOAMDisplay.DataAxesGrid.XLabelBold = 0
resultsOpenFOAMDisplay.DataAxesGrid.XLabelItalic = 0
resultsOpenFOAMDisplay.DataAxesGrid.XLabelFontSize = 12
resultsOpenFOAMDisplay.DataAxesGrid.XLabelShadow = 0
resultsOpenFOAMDisplay.DataAxesGrid.XLabelOpacity = 1.0
resultsOpenFOAMDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
resultsOpenFOAMDisplay.DataAxesGrid.YLabelFontFile = ''
resultsOpenFOAMDisplay.DataAxesGrid.YLabelBold = 0
resultsOpenFOAMDisplay.DataAxesGrid.YLabelItalic = 0
resultsOpenFOAMDisplay.DataAxesGrid.YLabelFontSize = 12
resultsOpenFOAMDisplay.DataAxesGrid.YLabelShadow = 0
resultsOpenFOAMDisplay.DataAxesGrid.YLabelOpacity = 1.0
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelFontFile = ''
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelBold = 0
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelItalic = 0
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelFontSize = 12
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelShadow = 0
resultsOpenFOAMDisplay.DataAxesGrid.ZLabelOpacity = 1.0
resultsOpenFOAMDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
resultsOpenFOAMDisplay.DataAxesGrid.XAxisPrecision = 2
resultsOpenFOAMDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
resultsOpenFOAMDisplay.DataAxesGrid.XAxisLabels = []
resultsOpenFOAMDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
resultsOpenFOAMDisplay.DataAxesGrid.YAxisPrecision = 2
resultsOpenFOAMDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
resultsOpenFOAMDisplay.DataAxesGrid.YAxisLabels = []
resultsOpenFOAMDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
resultsOpenFOAMDisplay.DataAxesGrid.ZAxisPrecision = 2
resultsOpenFOAMDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
resultsOpenFOAMDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
resultsOpenFOAMDisplay.PolarAxes.Visibility = 0
resultsOpenFOAMDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
resultsOpenFOAMDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
resultsOpenFOAMDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
resultsOpenFOAMDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.EnableCustomRange = 0
resultsOpenFOAMDisplay.PolarAxes.CustomRange = [0.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.PolarAxisVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.RadialAxesVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.DrawRadialGridlines = 1
resultsOpenFOAMDisplay.PolarAxes.PolarArcsVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.DrawPolarArcsGridlines = 1
resultsOpenFOAMDisplay.PolarAxes.NumberOfRadialAxes = 0
resultsOpenFOAMDisplay.PolarAxes.AutoSubdividePolarAxis = 1
resultsOpenFOAMDisplay.PolarAxes.NumberOfPolarAxis = 0
resultsOpenFOAMDisplay.PolarAxes.MinimumRadius = 0.0
resultsOpenFOAMDisplay.PolarAxes.MinimumAngle = 0.0
resultsOpenFOAMDisplay.PolarAxes.MaximumAngle = 90.0
resultsOpenFOAMDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
resultsOpenFOAMDisplay.PolarAxes.Ratio = 1.0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
resultsOpenFOAMDisplay.PolarAxes.PolarLabelVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
resultsOpenFOAMDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
resultsOpenFOAMDisplay.PolarAxes.RadialLabelVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
resultsOpenFOAMDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
resultsOpenFOAMDisplay.PolarAxes.RadialUnitsVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.ScreenSize = 10.0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleFontFile = ''
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleBold = 0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleItalic = 0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleShadow = 0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTitleFontSize = 12
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelFontFile = ''
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelBold = 0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelItalic = 0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelShadow = 0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisLabelFontSize = 12
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextBold = 0
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextItalic = 0
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextShadow = 0
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
resultsOpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
resultsOpenFOAMDisplay.PolarAxes.EnableDistanceLOD = 1
resultsOpenFOAMDisplay.PolarAxes.DistanceLODThreshold = 0.7
resultsOpenFOAMDisplay.PolarAxes.EnableViewAngleLOD = 1
resultsOpenFOAMDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
resultsOpenFOAMDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
resultsOpenFOAMDisplay.PolarAxes.PolarTicksVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
resultsOpenFOAMDisplay.PolarAxes.TickLocation = 'Both'
resultsOpenFOAMDisplay.PolarAxes.AxisTickVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.AxisMinorTickVisibility = 0
resultsOpenFOAMDisplay.PolarAxes.ArcTickVisibility = 1
resultsOpenFOAMDisplay.PolarAxes.ArcMinorTickVisibility = 0
resultsOpenFOAMDisplay.PolarAxes.DeltaAngleMajor = 10.0
resultsOpenFOAMDisplay.PolarAxes.DeltaAngleMinor = 5.0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
resultsOpenFOAMDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
resultsOpenFOAMDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
resultsOpenFOAMDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
resultsOpenFOAMDisplay.PolarAxes.ArcMajorTickSize = 0.0
resultsOpenFOAMDisplay.PolarAxes.ArcTickRatioSize = 0.3
resultsOpenFOAMDisplay.PolarAxes.ArcMajorTickThickness = 1.0
resultsOpenFOAMDisplay.PolarAxes.ArcTickRatioThickness = 0.5
resultsOpenFOAMDisplay.PolarAxes.Use2DMode = 0
resultsOpenFOAMDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(resultsOpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
resultsOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]
vtkBlockColorsLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# create a new 'Slice'
slice1 = Slice(Input=resultsOpenFOAM)
slice1.SliceType = 'Plane'
slice1.Crinkleslice = 0
slice1.Triangulatetheslice = 1
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [22.5, 11.25, 11.25]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]
slice1.SliceType.Offset = 0.0

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [22.5, 11.25, 6.845]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [22.5, 11.25, 6.845]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.AmbientColor = [1.0, 1.0, 1.0]
slice1Display.ColorArrayName = [None, '']
slice1Display.DiffuseColor = [1.0, 1.0, 1.0]
slice1Display.LookupTable = None
slice1Display.MapScalars = 1
slice1Display.MultiComponentsMapping = 0
slice1Display.InterpolateScalarsBeforeMapping = 1
slice1Display.Opacity = 1.0
slice1Display.PointSize = 2.0
slice1Display.LineWidth = 1.0
slice1Display.RenderLinesAsTubes = 0
slice1Display.RenderPointsAsSpheres = 0
slice1Display.Interpolation = 'Gouraud'
slice1Display.Specular = 0.0
slice1Display.SpecularColor = [1.0, 1.0, 1.0]
slice1Display.SpecularPower = 100.0
slice1Display.Luminosity = 0.0
slice1Display.Ambient = 0.0
slice1Display.Diffuse = 1.0
slice1Display.EdgeColor = [0.0, 0.0, 0.5]
slice1Display.BackfaceRepresentation = 'Follow Frontface'
slice1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
slice1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
slice1Display.BackfaceOpacity = 1.0
slice1Display.Position = [0.0, 0.0, 0.0]
slice1Display.Scale = [1.0, 1.0, 1.0]
slice1Display.Orientation = [0.0, 0.0, 0.0]
slice1Display.Origin = [0.0, 0.0, 0.0]
slice1Display.Pickable = 1
slice1Display.Texture = None
slice1Display.Triangulate = 0
slice1Display.UseShaderReplacements = 0
slice1Display.ShaderReplacements = ''
slice1Display.NonlinearSubdivisionLevel = 1
slice1Display.UseDataPartitions = 0
slice1Display.OSPRayUseScaleArray = 0
slice1Display.OSPRayScaleArray = 'U'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.OSPRayMaterial = 'None'
slice1Display.Orient = 0
slice1Display.OrientationMode = 'Direction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.Scaling = 0
slice1Display.ScaleMode = 'No Data Scaling Off'
slice1Display.ScaleFactor = 4.5
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.UseGlyphTable = 0
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.UseCompositeGlyphTable = 0
slice1Display.UseGlyphCullingAndLOD = 0
slice1Display.LODValues = []
slice1Display.ColorByLODIndex = 0
slice1Display.GaussianRadius = 0.225
slice1Display.ShaderPreset = 'Sphere'
slice1Display.CustomTriangleScale = 3
slice1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
slice1Display.Emissive = 0
slice1Display.ScaleByArray = 0
slice1Display.SetScaleArray = ['POINTS', 'U']
slice1Display.ScaleArrayComponent = 'X'
slice1Display.UseScaleFunction = 1
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityByArray = 0
slice1Display.OpacityArray = ['POINTS', 'U']
slice1Display.OpacityArrayComponent = 'X'
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelBold = 0
slice1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
slice1Display.SelectionCellLabelFontFamily = 'Arial'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionCellLabelFontSize = 18
slice1Display.SelectionCellLabelItalic = 0
slice1Display.SelectionCellLabelJustification = 'Left'
slice1Display.SelectionCellLabelOpacity = 1.0
slice1Display.SelectionCellLabelShadow = 0
slice1Display.SelectionPointLabelBold = 0
slice1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
slice1Display.SelectionPointLabelFontFamily = 'Arial'
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.SelectionPointLabelFontSize = 18
slice1Display.SelectionPointLabelItalic = 0
slice1Display.SelectionPointLabelJustification = 'Left'
slice1Display.SelectionPointLabelOpacity = 1.0
slice1Display.SelectionPointLabelShadow = 0
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
slice1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
slice1Display.GlyphType.TipResolution = 6
slice1Display.GlyphType.TipRadius = 0.1
slice1Display.GlyphType.TipLength = 0.35
slice1Display.GlyphType.ShaftResolution = 6
slice1Display.GlyphType.ShaftRadius = 0.03
slice1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
slice1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
slice1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitle = 'X Axis'
slice1Display.DataAxesGrid.YTitle = 'Y Axis'
slice1Display.DataAxesGrid.ZTitle = 'Z Axis'
slice1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.XTitleBold = 0
slice1Display.DataAxesGrid.XTitleItalic = 0
slice1Display.DataAxesGrid.XTitleFontSize = 12
slice1Display.DataAxesGrid.XTitleShadow = 0
slice1Display.DataAxesGrid.XTitleOpacity = 1.0
slice1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleBold = 0
slice1Display.DataAxesGrid.YTitleItalic = 0
slice1Display.DataAxesGrid.YTitleFontSize = 12
slice1Display.DataAxesGrid.YTitleShadow = 0
slice1Display.DataAxesGrid.YTitleOpacity = 1.0
slice1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleBold = 0
slice1Display.DataAxesGrid.ZTitleItalic = 0
slice1Display.DataAxesGrid.ZTitleFontSize = 12
slice1Display.DataAxesGrid.ZTitleShadow = 0
slice1Display.DataAxesGrid.ZTitleOpacity = 1.0
slice1Display.DataAxesGrid.FacesToRender = 63
slice1Display.DataAxesGrid.CullBackface = 0
slice1Display.DataAxesGrid.CullFrontface = 1
slice1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.ShowGrid = 0
slice1Display.DataAxesGrid.ShowEdges = 1
slice1Display.DataAxesGrid.ShowTicks = 1
slice1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
slice1Display.DataAxesGrid.AxesToLabel = 63
slice1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.XLabelBold = 0
slice1Display.DataAxesGrid.XLabelItalic = 0
slice1Display.DataAxesGrid.XLabelFontSize = 12
slice1Display.DataAxesGrid.XLabelShadow = 0
slice1Display.DataAxesGrid.XLabelOpacity = 1.0
slice1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelBold = 0
slice1Display.DataAxesGrid.YLabelItalic = 0
slice1Display.DataAxesGrid.YLabelFontSize = 12
slice1Display.DataAxesGrid.YLabelShadow = 0
slice1Display.DataAxesGrid.YLabelOpacity = 1.0
slice1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelBold = 0
slice1Display.DataAxesGrid.ZLabelItalic = 0
slice1Display.DataAxesGrid.ZLabelFontSize = 12
slice1Display.DataAxesGrid.ZLabelShadow = 0
slice1Display.DataAxesGrid.ZLabelOpacity = 1.0
slice1Display.DataAxesGrid.XAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.XAxisPrecision = 2
slice1Display.DataAxesGrid.XAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.XAxisLabels = []
slice1Display.DataAxesGrid.YAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.YAxisPrecision = 2
slice1Display.DataAxesGrid.YAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.YAxisLabels = []
slice1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.ZAxisPrecision = 2
slice1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.Visibility = 0
slice1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
slice1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
slice1Display.PolarAxes.EnableCustomRange = 0
slice1Display.PolarAxes.CustomRange = [0.0, 1.0]
slice1Display.PolarAxes.PolarAxisVisibility = 1
slice1Display.PolarAxes.RadialAxesVisibility = 1
slice1Display.PolarAxes.DrawRadialGridlines = 1
slice1Display.PolarAxes.PolarArcsVisibility = 1
slice1Display.PolarAxes.DrawPolarArcsGridlines = 1
slice1Display.PolarAxes.NumberOfRadialAxes = 0
slice1Display.PolarAxes.AutoSubdividePolarAxis = 1
slice1Display.PolarAxes.NumberOfPolarAxis = 0
slice1Display.PolarAxes.MinimumRadius = 0.0
slice1Display.PolarAxes.MinimumAngle = 0.0
slice1Display.PolarAxes.MaximumAngle = 90.0
slice1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
slice1Display.PolarAxes.Ratio = 1.0
slice1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisTitleVisibility = 1
slice1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
slice1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
slice1Display.PolarAxes.PolarLabelVisibility = 1
slice1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
slice1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
slice1Display.PolarAxes.RadialLabelVisibility = 1
slice1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
slice1Display.PolarAxes.RadialLabelLocation = 'Bottom'
slice1Display.PolarAxes.RadialUnitsVisibility = 1
slice1Display.PolarAxes.ScreenSize = 10.0
slice1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
slice1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisTitleBold = 0
slice1Display.PolarAxes.PolarAxisTitleItalic = 0
slice1Display.PolarAxes.PolarAxisTitleShadow = 0
slice1Display.PolarAxes.PolarAxisTitleFontSize = 12
slice1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
slice1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelBold = 0
slice1Display.PolarAxes.PolarAxisLabelItalic = 0
slice1Display.PolarAxes.PolarAxisLabelShadow = 0
slice1Display.PolarAxes.PolarAxisLabelFontSize = 12
slice1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
slice1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextBold = 0
slice1Display.PolarAxes.LastRadialAxisTextItalic = 0
slice1Display.PolarAxes.LastRadialAxisTextShadow = 0
slice1Display.PolarAxes.LastRadialAxisTextFontSize = 12
slice1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
slice1Display.PolarAxes.EnableDistanceLOD = 1
slice1Display.PolarAxes.DistanceLODThreshold = 0.7
slice1Display.PolarAxes.EnableViewAngleLOD = 1
slice1Display.PolarAxes.ViewAngleLODThreshold = 0.7
slice1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
slice1Display.PolarAxes.PolarTicksVisibility = 1
slice1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
slice1Display.PolarAxes.TickLocation = 'Both'
slice1Display.PolarAxes.AxisTickVisibility = 1
slice1Display.PolarAxes.AxisMinorTickVisibility = 0
slice1Display.PolarAxes.ArcTickVisibility = 1
slice1Display.PolarAxes.ArcMinorTickVisibility = 0
slice1Display.PolarAxes.DeltaAngleMajor = 10.0
slice1Display.PolarAxes.DeltaAngleMinor = 5.0
slice1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
slice1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
slice1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
slice1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
slice1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.ArcMajorTickSize = 0.0
slice1Display.PolarAxes.ArcTickRatioSize = 0.3
slice1Display.PolarAxes.ArcMajorTickThickness = 1.0
slice1Display.PolarAxes.ArcTickRatioThickness = 0.5
slice1Display.PolarAxes.Use2DMode = 0
slice1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(resultsOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=slice1,
    Source='High Resolution Line Source')
plotOverLine1.PassPartialArrays = 1
plotOverLine1.ComputeTolerance = 1
plotOverLine1.Tolerance = 2.220446049250313e-16

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [0.0, 0.0, 6.84499979019165]
plotOverLine1.Source.Point2 = [45.0, 22.5, 6.84499979019165]
plotOverLine1.Source.Resolution = 1000

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [10.68, 12.25, 6.84499979019165]
plotOverLine1.Source.Point2 = [20.715, 12.25, 6.84499979019165]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.AmbientColor = [1.0, 1.0, 1.0]
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.DiffuseColor = [1.0, 1.0, 1.0]
plotOverLine1Display.LookupTable = None
plotOverLine1Display.MapScalars = 1
plotOverLine1Display.MultiComponentsMapping = 0
plotOverLine1Display.InterpolateScalarsBeforeMapping = 1
plotOverLine1Display.Opacity = 1.0
plotOverLine1Display.PointSize = 2.0
plotOverLine1Display.LineWidth = 1.0
plotOverLine1Display.RenderLinesAsTubes = 0
plotOverLine1Display.RenderPointsAsSpheres = 0
plotOverLine1Display.Interpolation = 'Gouraud'
plotOverLine1Display.Specular = 0.0
plotOverLine1Display.SpecularColor = [1.0, 1.0, 1.0]
plotOverLine1Display.SpecularPower = 100.0
plotOverLine1Display.Luminosity = 0.0
plotOverLine1Display.Ambient = 0.0
plotOverLine1Display.Diffuse = 1.0
plotOverLine1Display.EdgeColor = [0.0, 0.0, 0.5]
plotOverLine1Display.BackfaceRepresentation = 'Follow Frontface'
plotOverLine1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
plotOverLine1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
plotOverLine1Display.BackfaceOpacity = 1.0
plotOverLine1Display.Position = [0.0, 0.0, 0.0]
plotOverLine1Display.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display.Origin = [0.0, 0.0, 0.0]
plotOverLine1Display.Pickable = 1
plotOverLine1Display.Texture = None
plotOverLine1Display.Triangulate = 0
plotOverLine1Display.UseShaderReplacements = 0
plotOverLine1Display.ShaderReplacements = ''
plotOverLine1Display.NonlinearSubdivisionLevel = 1
plotOverLine1Display.UseDataPartitions = 0
plotOverLine1Display.OSPRayUseScaleArray = 0
plotOverLine1Display.OSPRayScaleArray = 'U'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.OSPRayMaterial = 'None'
plotOverLine1Display.Orient = 0
plotOverLine1Display.OrientationMode = 'Direction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.Scaling = 0
plotOverLine1Display.ScaleMode = 'No Data Scaling Off'
plotOverLine1Display.ScaleFactor = 1.003499984741211
plotOverLine1Display.SelectScaleArray = 'None'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.UseGlyphTable = 0
plotOverLine1Display.GlyphTableIndexArray = 'None'
plotOverLine1Display.UseCompositeGlyphTable = 0
plotOverLine1Display.UseGlyphCullingAndLOD = 0
plotOverLine1Display.LODValues = []
plotOverLine1Display.ColorByLODIndex = 0
plotOverLine1Display.GaussianRadius = 0.05017499923706055
plotOverLine1Display.ShaderPreset = 'Sphere'
plotOverLine1Display.CustomTriangleScale = 3
plotOverLine1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
plotOverLine1Display.Emissive = 0
plotOverLine1Display.ScaleByArray = 0
plotOverLine1Display.SetScaleArray = ['POINTS', 'U']
plotOverLine1Display.ScaleArrayComponent = 'X'
plotOverLine1Display.UseScaleFunction = 1
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityByArray = 0
plotOverLine1Display.OpacityArray = ['POINTS', 'U']
plotOverLine1Display.OpacityArrayComponent = 'X'
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.SelectionCellLabelBold = 0
plotOverLine1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
plotOverLine1Display.SelectionCellLabelFontFamily = 'Arial'
plotOverLine1Display.SelectionCellLabelFontFile = ''
plotOverLine1Display.SelectionCellLabelFontSize = 18
plotOverLine1Display.SelectionCellLabelItalic = 0
plotOverLine1Display.SelectionCellLabelJustification = 'Left'
plotOverLine1Display.SelectionCellLabelOpacity = 1.0
plotOverLine1Display.SelectionCellLabelShadow = 0
plotOverLine1Display.SelectionPointLabelBold = 0
plotOverLine1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
plotOverLine1Display.SelectionPointLabelFontFamily = 'Arial'
plotOverLine1Display.SelectionPointLabelFontFile = ''
plotOverLine1Display.SelectionPointLabelFontSize = 18
plotOverLine1Display.SelectionPointLabelItalic = 0
plotOverLine1Display.SelectionPointLabelJustification = 'Left'
plotOverLine1Display.SelectionPointLabelOpacity = 1.0
plotOverLine1Display.SelectionPointLabelShadow = 0
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
plotOverLine1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
plotOverLine1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
plotOverLine1Display.GlyphType.TipResolution = 6
plotOverLine1Display.GlyphType.TipRadius = 0.1
plotOverLine1Display.GlyphType.TipLength = 0.35
plotOverLine1Display.GlyphType.ShaftResolution = 6
plotOverLine1Display.GlyphType.ShaftRadius = 0.03
plotOverLine1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
plotOverLine1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
plotOverLine1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
plotOverLine1Display.DataAxesGrid.XTitle = 'X Axis'
plotOverLine1Display.DataAxesGrid.YTitle = 'Y Axis'
plotOverLine1Display.DataAxesGrid.ZTitle = 'Z Axis'
plotOverLine1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.XTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.XTitleBold = 0
plotOverLine1Display.DataAxesGrid.XTitleItalic = 0
plotOverLine1Display.DataAxesGrid.XTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.XTitleShadow = 0
plotOverLine1Display.DataAxesGrid.XTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.YTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.YTitleBold = 0
plotOverLine1Display.DataAxesGrid.YTitleItalic = 0
plotOverLine1Display.DataAxesGrid.YTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.YTitleShadow = 0
plotOverLine1Display.DataAxesGrid.YTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.ZTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.ZTitleBold = 0
plotOverLine1Display.DataAxesGrid.ZTitleItalic = 0
plotOverLine1Display.DataAxesGrid.ZTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.ZTitleShadow = 0
plotOverLine1Display.DataAxesGrid.ZTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.FacesToRender = 63
plotOverLine1Display.DataAxesGrid.CullBackface = 0
plotOverLine1Display.DataAxesGrid.CullFrontface = 1
plotOverLine1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.ShowGrid = 0
plotOverLine1Display.DataAxesGrid.ShowEdges = 1
plotOverLine1Display.DataAxesGrid.ShowTicks = 1
plotOverLine1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
plotOverLine1Display.DataAxesGrid.AxesToLabel = 63
plotOverLine1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.XLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.XLabelBold = 0
plotOverLine1Display.DataAxesGrid.XLabelItalic = 0
plotOverLine1Display.DataAxesGrid.XLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.XLabelShadow = 0
plotOverLine1Display.DataAxesGrid.XLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.YLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.YLabelBold = 0
plotOverLine1Display.DataAxesGrid.YLabelItalic = 0
plotOverLine1Display.DataAxesGrid.YLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.YLabelShadow = 0
plotOverLine1Display.DataAxesGrid.YLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.ZLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.ZLabelBold = 0
plotOverLine1Display.DataAxesGrid.ZLabelItalic = 0
plotOverLine1Display.DataAxesGrid.ZLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.ZLabelShadow = 0
plotOverLine1Display.DataAxesGrid.ZLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.XAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.XAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.XAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.XAxisLabels = []
plotOverLine1Display.DataAxesGrid.YAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.YAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.YAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.YAxisLabels = []
plotOverLine1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.ZAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plotOverLine1Display.PolarAxes.Visibility = 0
plotOverLine1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
plotOverLine1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
plotOverLine1Display.PolarAxes.EnableCustomRange = 0
plotOverLine1Display.PolarAxes.CustomRange = [0.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisVisibility = 1
plotOverLine1Display.PolarAxes.RadialAxesVisibility = 1
plotOverLine1Display.PolarAxes.DrawRadialGridlines = 1
plotOverLine1Display.PolarAxes.PolarArcsVisibility = 1
plotOverLine1Display.PolarAxes.DrawPolarArcsGridlines = 1
plotOverLine1Display.PolarAxes.NumberOfRadialAxes = 0
plotOverLine1Display.PolarAxes.AutoSubdividePolarAxis = 1
plotOverLine1Display.PolarAxes.NumberOfPolarAxis = 0
plotOverLine1Display.PolarAxes.MinimumRadius = 0.0
plotOverLine1Display.PolarAxes.MinimumAngle = 0.0
plotOverLine1Display.PolarAxes.MaximumAngle = 90.0
plotOverLine1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
plotOverLine1Display.PolarAxes.Ratio = 1.0
plotOverLine1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisTitleVisibility = 1
plotOverLine1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
plotOverLine1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
plotOverLine1Display.PolarAxes.PolarLabelVisibility = 1
plotOverLine1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
plotOverLine1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
plotOverLine1Display.PolarAxes.RadialLabelVisibility = 1
plotOverLine1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
plotOverLine1Display.PolarAxes.RadialLabelLocation = 'Bottom'
plotOverLine1Display.PolarAxes.RadialUnitsVisibility = 1
plotOverLine1Display.PolarAxes.ScreenSize = 10.0
plotOverLine1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
plotOverLine1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.PolarAxisTitleFontFile = ''
plotOverLine1Display.PolarAxes.PolarAxisTitleBold = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleItalic = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleShadow = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleFontSize = 12
plotOverLine1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
plotOverLine1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.PolarAxisLabelFontFile = ''
plotOverLine1Display.PolarAxes.PolarAxisLabelBold = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelItalic = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelShadow = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelFontSize = 12
plotOverLine1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFile = ''
plotOverLine1Display.PolarAxes.LastRadialAxisTextBold = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextItalic = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextShadow = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontSize = 12
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
plotOverLine1Display.PolarAxes.EnableDistanceLOD = 1
plotOverLine1Display.PolarAxes.DistanceLODThreshold = 0.7
plotOverLine1Display.PolarAxes.EnableViewAngleLOD = 1
plotOverLine1Display.PolarAxes.ViewAngleLODThreshold = 0.7
plotOverLine1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
plotOverLine1Display.PolarAxes.PolarTicksVisibility = 1
plotOverLine1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
plotOverLine1Display.PolarAxes.TickLocation = 'Both'
plotOverLine1Display.PolarAxes.AxisTickVisibility = 1
plotOverLine1Display.PolarAxes.AxisMinorTickVisibility = 0
plotOverLine1Display.PolarAxes.ArcTickVisibility = 1
plotOverLine1Display.PolarAxes.ArcMinorTickVisibility = 0
plotOverLine1Display.PolarAxes.DeltaAngleMajor = 10.0
plotOverLine1Display.PolarAxes.DeltaAngleMinor = 5.0
plotOverLine1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.ArcMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.ArcTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.ArcMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.ArcTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.Use2DMode = 0
plotOverLine1Display.PolarAxes.UseLogAxis = 0

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.UseCache = 0
lineChartView1.ViewSize = [768, 547]
lineChartView1.ChartTitle = ''
lineChartView1.ChartTitleAlignment = 'Center'
lineChartView1.ChartTitleFontFamily = 'Arial'
lineChartView1.ChartTitleFontFile = ''
lineChartView1.ChartTitleFontSize = 18
lineChartView1.ChartTitleBold = 0
lineChartView1.ChartTitleItalic = 0
lineChartView1.ChartTitleColor = [0.0, 0.0, 0.0]
lineChartView1.ShowLegend = 1
lineChartView1.LegendLocation = 'TopRight'
lineChartView1.SortByXAxis = 0
lineChartView1.LegendPosition = [0, 0]
lineChartView1.LegendFontFamily = 'Arial'
lineChartView1.LegendFontFile = ''
lineChartView1.LegendFontSize = 12
lineChartView1.LegendBold = 0
lineChartView1.LegendItalic = 0
lineChartView1.TooltipNotation = 'Mixed'
lineChartView1.TooltipPrecision = 6
lineChartView1.HideTimeMarker = 0
lineChartView1.LeftAxisTitle = ''
lineChartView1.ShowLeftAxisGrid = 1
lineChartView1.LeftAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.LeftAxisColor = [0.0, 0.0, 0.0]
lineChartView1.LeftAxisTitleFontFamily = 'Arial'
lineChartView1.LeftAxisTitleFontFile = ''
lineChartView1.LeftAxisTitleFontSize = 18
lineChartView1.LeftAxisTitleBold = 1
lineChartView1.LeftAxisTitleItalic = 0
lineChartView1.LeftAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.LeftAxisLogScale = 0
lineChartView1.LeftAxisUseCustomRange = 0
lineChartView1.LeftAxisRangeMinimum = 0.0
lineChartView1.LeftAxisRangeMaximum = 6.66
lineChartView1.ShowLeftAxisLabels = 1
lineChartView1.LeftAxisLabelNotation = 'Mixed'
lineChartView1.LeftAxisLabelPrecision = 2
lineChartView1.LeftAxisUseCustomLabels = 0
lineChartView1.LeftAxisLabels = []
lineChartView1.LeftAxisLabelFontFamily = 'Arial'
lineChartView1.LeftAxisLabelFontFile = ''
lineChartView1.LeftAxisLabelFontSize = 12
lineChartView1.LeftAxisLabelBold = 0
lineChartView1.LeftAxisLabelItalic = 0
lineChartView1.LeftAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisTitle = ''
lineChartView1.ShowBottomAxisGrid = 1
lineChartView1.BottomAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.BottomAxisColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisTitleFontFamily = 'Arial'
lineChartView1.BottomAxisTitleFontFile = ''
lineChartView1.BottomAxisTitleFontSize = 18
lineChartView1.BottomAxisTitleBold = 1
lineChartView1.BottomAxisTitleItalic = 0
lineChartView1.BottomAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisLogScale = 0
lineChartView1.BottomAxisUseCustomRange = 0
lineChartView1.BottomAxisRangeMinimum = 0.0
lineChartView1.BottomAxisRangeMaximum = 6.66
lineChartView1.ShowBottomAxisLabels = 1
lineChartView1.BottomAxisLabelNotation = 'Mixed'
lineChartView1.BottomAxisLabelPrecision = 2
lineChartView1.BottomAxisUseCustomLabels = 0
lineChartView1.BottomAxisLabels = []
lineChartView1.BottomAxisLabelFontFamily = 'Arial'
lineChartView1.BottomAxisLabelFontFile = ''
lineChartView1.BottomAxisLabelFontSize = 12
lineChartView1.BottomAxisLabelBold = 0
lineChartView1.BottomAxisLabelItalic = 0
lineChartView1.BottomAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisTitle = ''
lineChartView1.ShowRightAxisGrid = 1
lineChartView1.RightAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.RightAxisColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisTitleFontFamily = 'Arial'
lineChartView1.RightAxisTitleFontFile = 'Arial'
lineChartView1.RightAxisTitleFontSize = 18
lineChartView1.RightAxisTitleBold = 1
lineChartView1.RightAxisTitleItalic = 0
lineChartView1.RightAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisLogScale = 0
lineChartView1.RightAxisUseCustomRange = 0
lineChartView1.RightAxisRangeMinimum = 0.0
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.ShowRightAxisLabels = 1
lineChartView1.RightAxisLabelNotation = 'Mixed'
lineChartView1.RightAxisLabelPrecision = 2
lineChartView1.RightAxisUseCustomLabels = 0
lineChartView1.RightAxisLabels = []
lineChartView1.RightAxisLabelFontFamily = 'Arial'
lineChartView1.RightAxisLabelFontFile = ''
lineChartView1.RightAxisLabelFontSize = 12
lineChartView1.RightAxisLabelBold = 0
lineChartView1.RightAxisLabelItalic = 0
lineChartView1.RightAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisTitle = ''
lineChartView1.ShowTopAxisGrid = 1
lineChartView1.TopAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.TopAxisColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisTitleFontFamily = 'Arial'
lineChartView1.TopAxisTitleFontFile = ''
lineChartView1.TopAxisTitleFontSize = 18
lineChartView1.TopAxisTitleBold = 1
lineChartView1.TopAxisTitleItalic = 0
lineChartView1.TopAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisLogScale = 0
lineChartView1.TopAxisUseCustomRange = 0
lineChartView1.TopAxisRangeMinimum = 0.0
lineChartView1.TopAxisRangeMaximum = 6.66
lineChartView1.ShowTopAxisLabels = 1
lineChartView1.TopAxisLabelNotation = 'Mixed'
lineChartView1.TopAxisLabelPrecision = 2
lineChartView1.TopAxisUseCustomLabels = 0
lineChartView1.TopAxisLabels = []
lineChartView1.TopAxisLabelFontFamily = 'Arial'
lineChartView1.TopAxisLabelFontFile = ''
lineChartView1.TopAxisLabelFontSize = 12
lineChartView1.TopAxisLabelBold = 0
lineChartView1.TopAxisLabelItalic = 0
lineChartView1.TopAxisLabelColor = [0.0, 0.0, 0.0]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, lineChartView1)

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.AttributeType = 'Point Data'
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['p', 'U_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'p', '0.89', '0.1', '0.11', 'U_X', '0.22', '0.49', '0.72', 'U_Y', '0.3', '0.69', '0.29', 'U_Z', '0.6', '0.31', '0.64', 'U_Magnitude', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# set active source
SetActiveSource(resultsOpenFOAM)

# Properties modified on resultsOpenFOAM
resultsOpenFOAM.VolumeFields = ['U', 'UMean', 'p']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# set active source
SetActiveSource(plotOverLine1)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'p', '0.889998', '0.100008', '0.110002', 'U_X', '0.220005', '0.489998', '0.719997', 'U_Y', '0.300008', '0.689998', '0.289998', 'U_Z', '0.6', '0.310002', '0.639994', 'U_Magnitude', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998', 'UMean_X', '0.6', '0.310002', '0.639994', 'UMean_Y', '1', '0.500008', '0', 'UMean_Z', '0.650004', '0.340002', '0.160006', 'UMean_Magnitude', '0', '0', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'UMean_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'UMean_Magnitude', '1', 'UMean_X', '1', 'UMean_Y', '1', 'UMean_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'UMean_Magnitude', '2', 'UMean_X', '2', 'UMean_Y', '2', 'UMean_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'UMean_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.XArrayName = 'Points_X'

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['p', 'U_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['p', 'U_Magnitude', 'UMean_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['p', 'UMean_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['UMean_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['UMean_X', 'UMean_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['UMean_X']

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['U_X', 'UMean_X']

animationScene1.Play()

# save data
SaveData('/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/Run6/Postprocessing/AT0.csv', proxy=plotOverLine1, Precision=5,
    UseScientificNotation=0,
    FieldDelimiter=',',
    WriteTimeSteps=0,
    FieldAssociation='Points')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-47.17699503979047, -61.64024627778429, 45.4294190673189]
renderView1.CameraFocalPoint = [22.5, 11.25, 11.25]
renderView1.CameraViewUp = [0.1892317382941505, 0.2627623172355306, 0.9461222510136776]
renderView1.CameraParallelScale = 27.556759606310752

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).