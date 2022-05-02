# By hefei
import time

start=time.time()# 获取当前时间
print(len(str(2**pow(2,15))))
print("计算耗时：",time.time()-start)# 计算时间

import decimal
num1=3.141582623341213123312
print("正常打印：",num1,"超过15位精度丢失")
num2=decimal.Decimal('3.141582623341213123312')
print("使用decimal后：",num2)
