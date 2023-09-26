from helper_funcs.downloadSCfile import get_chart
from helper_funcs.createImageGrid import createImage

get_chart('AAPL', '1h')
get_chart('AAPL', '4h')
get_chart('AAPL', '1d')
get_chart('AAPL', '1w')

#createImage()