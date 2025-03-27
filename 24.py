import time
import subprocess

def keep_dashwave_active():
    while True:  # Infinite loop to run 24×7
        try:
            start_time = time.time()
            
            while True:
                # Prevent inactivity in Dashwave
                subprocess.run(["echo", "Keeping workspace active"], check=True)

                # Heartbeat message to keep session alive
                elapsed = int(time.time() - start_time)
                print(f"✅ Dashwave active. Uptime: {elapsed} sec", flush=True)

                # Wait 5 minutes before next keep-alive signal
                time.sleep(300)

        except Exception as e:
            print(f"⚠️ Error: {e}. Restarting keep-alive script...", flush=True)
            time.sleep(5)  # Short delay before auto-restart

# 🔄 Start 24×7 execution
keep_dashwave_active()