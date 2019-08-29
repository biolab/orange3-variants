""" Single Cell add-on for Orange3 """

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution('orange3-singlecell').version
except DistributionNotFound:
    # package is not installed
    pass
