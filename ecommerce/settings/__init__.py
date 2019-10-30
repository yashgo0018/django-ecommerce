import os
if True:  # os.environ.get('PRODUCTION') == '1':
    from .prod import *
else:
    from .local import *
