# -*- coding: utf-8 -*-

from weicav import WeiCav
import json
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import time
import sys


OMEGA = VALUE_OMEGA
DISORDER = VALUE_DISORDER
UP = VALUE_UP
SEED = VALUE_S

# 创建一个包含数据的 Python 字典"
data = {
    "light_size": 1,
    "total_size": 1000001,
    "molecule_start": 2,
    
    
    "hbar": 1,
    "dt": 0.001, #0.001
    "tf": 2000,
    
    "floquet_level": 3,

    "e_molecule": 0,
    "e_molecule_distribution": True,
    "disorder":DISORDER, # 2,1,0.5  \Delta E = 12  if 0; same number
    "seed":True,

    "e_light": None,
    "e_light_distribution":False,
    "V_coupling_strength":0.01, #1, 1.5, 2
    "DeltaE": 13,
    "scale": 20,

    "gamma":0.1, #gaussian width

    "omega": OMEGA, # w: cos(wt+phase)  0 0.1 0.5
    "phase":np.pi, # phase: cos(wt+phase)
    "phase_up":UP,
    "phase_dw":32,
    "phase_random": SEED,
    "left_lim": -20, # x_axis = np.linspace(left_lim,right_lim,length_lim)
    "right_lim": 20,
    "length_lim":1000,
}

# 指定要保存 JSON 数据的文件路径
json_file_path = f"data_{UP}.json"

# 使用 json.dump() 将数据写入 JSON 文件
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=2)

print(f"数据已成功写入 {json_file_path}")

### 记录开始时间
start_time = time.time()

SOD = WeiSOD(json_file_path)

w,p = SOD.get_DOS(k=30)

SOD.plot_spectrum(w,p,SAVE=True,PLOT=True)

# 记录结束时间
end_time = time.time()

# 计算经过的时间
elapsed_time = end_time - start_time

print(f"光谱经过的时间：{elapsed_time}秒")

# ### 记录开始时间
# start_time = time.time()

# TIME, observable = SOD.run_dynamics()

# SOD.plot_corr(TIME, observable,SAVE=True,PLOT=True)

# # SOD.plot_both(TIME, observable,w,p,SAVE=True)

# # 记录结束时间
# end_time = time.time()

# # 计算经过的时间
# elapsed_time = end_time - start_time

# print(f"动力学经过的时间：{elapsed_time}秒")

