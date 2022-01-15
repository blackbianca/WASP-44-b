# WASP-44-b
Astrophysics Laboratory 2: project for WASP-44 b

## Mass and Radius
We used PARAM software web interface to infer mass and radius of the star. For PARAM input, we considered NASA Exoplanet Archive suggested papers, ruling out any atmospheric parameter of non-spectroscopic origin. This leaves us just with the discovery paper (Anderson et al, 2011). We also employ GAIA parallax. However, PARAM had server troubles so we made use of another code (Morton 2015).

## Limb darkening
We make use of Antonio Claret's tables to calibrate a relationship between atmospheric parameters and limb darkening coefficients. We do that in different ways. We're going to use these results as priors later in the analysis.

## TASTE analysis and aperture selection
Copernico images, provided by TASTE project, can be corrected by using bias and flat field, exploiting "huggy" codeset. Then we focus on the target and find a suitable reference star within the FoV. Then we use "sentinel" to work out the apertures in units pixels. We read and study TASTE data comparing two apertures at a time. This data is already ready for further elaboration (PyORBIT).

## TESS analysis
We now download another set of data from ExoFOP (TESS, Transiting Exoplanet Survey Satellite). We have a look at data and rule out outliers. Then we properly flatten (detrend) the lightcurve and apply a linear fit (median and biweight method). Finally, we detect transits by fitting the flux valleys (two methods: Box-fitting Least Squares and Transit Least Squares) to estimate period and transit duration. We end up with a flattened lightcurve that we save for later PyORBIT analysis.

## PyORBIT
Lightcurve files from both TESS and TASTE are analysed by the code "PyORBIT", which gets estimates for period and central transit time, as well as limb darkening coefficients, to be compared with the ones we already have.

## Radial velocity analysis
A quick look to radial velocity data from Anderson 2011, to check whether they confirm predicted period.
