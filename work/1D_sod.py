import pandas as pd
import matplotlib.pyplot as plt

filename = "Sod.block0.out1.00025.tab"

# delim_whitespace が将来非推奨なので sep='\s+' を使用
data = pd.read_csv(filename, sep='\\s+', comment='#', header=None)

# 列名を 7 列に合わせる
data.columns = ['x', 'rho', 'vx', 'vy', 'vz', 'P', 'E']

# グラフ作成
plt.figure(figsize=(12,7))
plt.plot(data['x'], data['rho'], label='Density', color='blue')
plt.plot(data['x'], data['vx'], label='Velocity x', color='red')
plt.plot(data['x'], data['P'], label='Pressure', color='green')

plt.xlabel('x')
plt.ylabel('Value')
plt.title('Sod Shock Tube')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('1D_sod.png')
import os
os.system('explorer.exe 1D_sod.png')  # Windows 上で開く