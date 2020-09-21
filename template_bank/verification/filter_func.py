def filter_injections(mass1, mass2, spin1z, spin2z):
    """Filter injections according to O2 requirements.

    Taking mass1, mass2, spin1z, spin2z return a boolean array which is True
    if point is within the O2 template region and False if it is outside the
    O2 template region. Currently using the PyCBC definition, but this can
    always be updated.
    """
    import numpy
    from scipy.interpolate import UnivariateSpline
    from lalinspiral.sbank.waveforms import SEOBNRv4ROMTemplate
    psd_data = numpy.loadtxt('/home/koustav.chandra/projects/pycbc/pycbc-config/O3C00/focusedIMBHBpipeline/psds/txt/H1L1V1-AVERAGE_PSD-1258642818-28800.txt')
    f_orig, psddata = psd_data[:,0], psd_data[:,1]
    interpolator = UnivariateSpline(f_orig, numpy.log(psddata), s=0)
    noise_m = lambda g: numpy.where(g < 1024, numpy.exp(interpolator(g)),
                                    numpy.inf)

    class Dummy(object):
        pass

    bank = Dummy()
    bank.flow = 15.
    bank.fhigh_max = 1024
    bank.noise_model = noise_m
    bank.optimize_flow = 0.995

    outs = []
    for i in xrange(len(mass1)):
        t = SEOBNRv4ROMTemplate(mass1[i], mass2[i], spin1z[i], spin2z[i],
                                bank=bank)
        try:
            tdur = t.dur
        except:
            tdur = -1

        if (tdur > 0.07) and (100. <= (mass1[i] + mass2[i]) <= 600.) and (1.*mass1[i]/mass2[i] <= 10.):
            outs.append(True)
        else:
            outs.append(False)
    return outs
    
