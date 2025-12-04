
# Author:Yi Sun(Tim) 2025-1-20

'''Disconnect wifi'''

import subprocess

def disconnect_wifi():
    try:
        # 断开所有无线网络连接
        subprocess.run(["netsh", "wlan", "disconnect"], check=True)
        print("WiFi 已断开连接。")
    except subprocess.CalledProcessError as e:
        print(f"断开 WiFi 时出现错误: {e}")

if __name__ == "__main__":
    disconnect_wifi()