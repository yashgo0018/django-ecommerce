from dotenv import load_dotenv
import os


load_dotenv()

if os.environ.get('PRODUCTION') == '1':
    from .prod import *
else:
    from .local import *
