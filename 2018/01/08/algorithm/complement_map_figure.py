import matplotlib.pyplot as plt
import numpy as np

plt.axis([-150,150,0,270])
plt.xlabel("x")
plt.ylabel("y")

#先把右边和上边的边界设置为不可见
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#然后把下边界和左边界移动到0点
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.plot([-128,0],[128,255])
plt.plot([0,127],[0,127])

plt.plot([-128,-128],[128,0],'b--')
plt.plot([127,127],[127,0],'b--')
plt.text(-128, 0,'-128')
plt.text(127, 0,'127')


plt.show()
