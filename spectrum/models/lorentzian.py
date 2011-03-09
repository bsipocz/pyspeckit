import numpy
from numpy.ma import median
from numpy import pi
from mpfit import mpfit

def onedlorentzian(x,H,A,dx,w):
    """
    Returns a 1-dimensional gaussian of form
    H+A*numpy.exp(-(x-dx)**2/(2*w**2))
    """
    return H+A/(2*pi)*w/((x-dx)**2 + (w/2.0)**2)

def n_lorentzian(pars=None,a=None,dx=None,width=None):
    """
    Returns a function that sums over N lorentzians, where N is the length of
    a,dx,sigma *OR* N = len(pars) / 3

    The background "height" is assumed to be zero (you must "baseline" your
    spectrum before fitting)

    pars  - a list with len(pars) = 3n, assuming a,dx,sigma repeated
    dx    - offset (velocity center) values
    width - line widths (Lorentzian FWHM)
    a     - amplitudes
    """
    if len(pars) % 3 == 0:
        a = [pars[ii] for ii in xrange(0,len(pars),3)]
        dx = [pars[ii] for ii in xrange(1,len(pars),3)]
        width = [pars[ii] for ii in xrange(2,len(pars),3)]
    elif not(len(dx) == len(width) == len(a)):
        raise ValueError("Wrong array lengths! dx: %i  width %i  a: %i" % (len(dx),len(width),len(a)))

    def L(x):
        v = numpy.zeros(len(x))
        for i in range(len(dx)):
            v += a[i] / (2*pi) * w / ((x-dx)**2 + (w/2.0)**2)
        return v
    return L
