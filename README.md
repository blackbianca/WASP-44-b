# WASP-44-b
Astrophysics Laboratory 2: project for WASP-44 b

## Mass and Radius
We used PARAM software web interface to infer mass and radius of the star. For PARAM input, we considered NASA Exoplanet Archive suggested papers, ruling out any atmospheric parameter of non-spectroscopic origin. This leaves us just with the discovery paper (Anderson et al, 2011). Also, PARAM did not work out so we made use of another code (Morton 2015)

## Limb darkening
We make use of Antonio Claret's tables to calibrate a relationship between atmospheric parameters and limb darkening coefficients. We're going to use these results as priors later in the analysis.

## TASTE analysis and aperture selection
We correct Copernico images, provided by TASTE project, by using bias and flat field, exploiting "huggy". Then we focuse on the target and found a suitable reference star within the FoV. Then we use "sentinel" to work out the apertures in units pixels. We read and study TASTE data comparing two apertures at a time. This data is already ready for further elaboration (PyORBIT).

## TESS analysis
We now download another set of data from ExoFOP (TESS, Transiting Exoplanet Survey Satellite). We have a look at data and rule out outliers. Then we properly flatten the lightcurve and apply a linear fit. Finally, we detect transits. We end up with a flattened lightcurve that we save for later.

## PyORBIT
We usually the lightcurve files from both TESS and TASTE to run the code "PyORBIT" and get estimates for period and central transit time, as well as limb darkening coefficients to be compared with the ones we already have.
