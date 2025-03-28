import time
import subprocess
import os

def keep_dashwave_active():
    restart_counter = 0
    while True:
        try:
            start_time = time.time()

            while time.time() - start_time < 21600:  # 6 hours = 21600 sec
                subprocess.run(["echo", "Keeping Dashwave session active"], check=True)
                elapsed = int(time.time() - start_time)
                print(f"✅ Dashwave active. Uptime: {elapsed} sec (Restart count: {restart_counter})", flush=True)
                time.sleep(300)

            # Restart script after 6 hours
            restart_counter += 1
            print("🔄 Restarting script after 6 hours...")
            time.sleep(5)
            os.execv(file, ["python3"] + sys.argv)  # Restart script

        except Exception as e:
            print(f"⚠️ Error: {e}. Restarting in 5 seconds...", flush=True)
            restart_counter += 1
            time.sleep(5)

# Start the script
keep_dashwave_active()
