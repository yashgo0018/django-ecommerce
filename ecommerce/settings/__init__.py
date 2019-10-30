import os
if False:  # os.environ.get('PRODUCTION') == '1':
    from .prod import *
else:
    from .local import *
