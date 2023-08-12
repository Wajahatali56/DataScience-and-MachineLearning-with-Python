# Markers- You can use arguments marker to emphasize each point with specified marker

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 , 7 , 10 , 15 , 1])
plt.plot(ypoints , marker = 'o')
plt.show()

# format string "fmt" - marker |line|color

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 , 7 , 10 , 15 , 1])
plt.plot(ypoints , 'o:r')
plt.show()


'''
# Line reference

- solid line
: dotted line
-- dashed line
-. dashedline/dottedline

# Color reference
r - red
g - green
b - blue
c - cyan
m - magenta
y - yellow
k - black
w - white

'''

# Marker size - ms

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 , 7 , 10 , 15 , 1])
plt.plot(ypoints , marker = 'o', ms =20)
plt.show()

# Marker Edge Color - mec

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 , 7 , 10 , 15 , 1])
plt.plot(ypoints , marker = 'o', ms =20 , mec = 'y')
plt.show()

# Marker face Color - mfc

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 , 7 , 10 , 15 , 1])
plt.plot(ypoints , marker = 'o', ms =20 , mec = 'y' , mfc = 'k')
plt.show()


# Using # values

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 , 7 , 10 , 15 , 1])
plt.plot(ypoints , marker = 'o', ms =20 , mec = 'y' , mfc = '#FF3333')
plt.show()


#__________________BEST OF LUCK ____________________#
