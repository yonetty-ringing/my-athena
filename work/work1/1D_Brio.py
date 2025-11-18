import pandas as pd
import matplotlib.pyplot as plt

filename = "Brio-Wu.block0.out1.00040.tab"

# delim_whitespace が将来非推奨なので sep='\s+' を使用
data = pd.read_csv(filename, sep='\\s+', comment='#', header=None)

# 列名を 7 列に合わせる
data.columns = ['i', 'x1v', 'rho', 'press', 'vel1', 'vel2', 'vel3', 'Bcc1', 'Bcc2', 'Bcc3']

# γの設定
gamma = 2

# 疑似温度 Te = p / ρ^γ
data['Te'] = data['press'] / data['rho']

# グラフ作成
plt.figure(figsize=(12,7))
#plt.plot(data['x1v'], data['rho'], label='density', color='blue')
#plt.plot(data['x1v'], data['press'], label='press', color='red')
#plt.plot(data['x1v'], data['vel1'], label='v_x', color='green')
#plt.plot(data['x1v'], data['vel2'], label='v_y', color='darkgreen')
#plt.plot(data['x1v'], data['Bcc1'], label='B_x', color='orange')
#plt.plot(data['x1v'], data['Bcc2'], label='B_y', color='purple')

plt.plot(data['x1v'], data['Te'], label=r'$P/\rho$', color='purple')


plt.xlabel('x')
plt.ylabel(r'$P/\rho$')
plt.title('Brio-Wu MHD Shock Tube')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('1D_Brio_p_rho.png')
import os
os.system('explorer.exe 1D_Brio_p_rho.png')  # Windows 上で開く