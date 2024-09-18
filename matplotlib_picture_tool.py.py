# 多行注释：cmd+/
# figure等效于画板，而axes/subplot则是画纸。从书包中拿出画板固定两张张画纸的过程，就相当与以下程序：
# fig=plt.figure() # 创建figure（拿出画板）
# ax1=fig.add_subplot(211) #划分2*1区域，在第一个区域固定一张画纸axes
# ax2=fig.add_subplot(212) #第二张固定另一张画纸
# plt.show() # 展示你的成果
# 那么axes和subplot有区别吗？有的，axes是随意固定在画板的位置，而subplot则是按照均分策略指定区域。下面的效果就可以由axes实现：
# 三维画图
import matplotlib.pyplot as plt
import numpy as np

# plt.close("all")
fig=plt.figure(1)
ax=plt.axes(projection='3d')
x=np.linspace(0,2,100)
ax.plot3D(x,x,np.sin(x),color='r',linewidth=1.5)
ax.plot3D(x,x**2,np.cos(x),linestyle='--')
ax.plot3D(x,x**3,-np.cos(x),color='b',linestyle='dotted')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_zlabel('z label')
ax.set_title('Simple plot3D in Python')
lg=ax.legend(['linear','quadratic','cubic'],title='Curve Type',loc='upper left') #默认best位置标记
lg.get_title().set_fontweight('semibold')# 设置字体
plt.show()

#二维画图
# import matplotlib.pyplot as plt
# import numpy as np

# plt.close("all")
# plt.figure(1)
# x=np.linspace(0,2,100)
# plt.plot(x,x,color='r',linewidth=1.5)
# plt.plot(x,x**2,linestyle='--')
# plt.plot(x,x**3,color='b',linestyle='dotted')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title('Simple plot in Python')
# lg=plt.legend(['linear','quadratic','cubic'],title='Curve Type') #默认best位置标记
# lg.get_title().set_fontweight('semibold')
# plt.show()






