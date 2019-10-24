import os
if os.environ.get('PRODUCTION') == '1':
    from .prod import *
else:
    from .local import *
