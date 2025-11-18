import pandas as pd
import matplotlib.pyplot as plt

filename = "Sod.block0.out1.00025.tab"

# delim_whitespace が将来非推奨なので sep='\s+' を使用
data = pd.read_csv(filename, sep='\\s+', comment='#', header=None)

# 列名を 7 列に合わせる
data.columns = ['i', 'x1v', 'rho', 'press', 'vel1', 'vel2', 'vel3']

# グラフ作成
plt.figure(figsize=(12,7))
plt.plot(data['x1v'], data['rho'], label='density', color='blue')
plt.plot(data['x1v'], data['press'], label='press', color='red')
plt.plot(data['x1v'], data['vel1'], label='velocity', color='green')

plt.xlabel('x')
plt.ylabel('value')
plt.title('Sod Shock Tube')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('1D_sod_3value.png')
import os
os.system('explorer.exe 1D_sod_3value.png')  # Windows 上で開く