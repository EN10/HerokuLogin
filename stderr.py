# print to pythonanywhere error log

import sys
print("fatal error", file=sys.stderr)

# might be faster to run function() and click Run rather the Reload
