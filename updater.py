import subprocess
import os

def check_for_updates():
    try:
        # Change to the project directory
        os.chdir('/home/admin/ShowMonLidarCounter')
        
        # Fetch the latest metadata from GitHub
        subprocess.run(['git', 'fetch'], check=True)
        
        # Compare local HEAD with the remote main branch
        local_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
        remote_hash = subprocess.check_output(['git', 'rev-parse', 'origin/main']).decode().strip()
        
        if local_hash != remote_hash:
            print("Changes detected on GitHub. Updating...")
            # Reset hard to ensure local files match GitHub exactly
            subprocess.run(['git', 'reset', '--hard', 'origin/main'], check=True)
            
            # Restart BOTH services
            print("Restarting services...")
            
            # Restart ShowMonLidarCounter
            subprocess.run(['sudo', 'systemctl', 'restart', 'ShowMonLidarCounter.service'], check=False)
            
            # Restart LidarCounter
            subprocess.run(['sudo', 'systemctl', 'restart', 'LidarCounter.service'], check=False)
            
            print("Update complete and services restarted.")
        else:
            print("Already up to date.")
            
    except Exception as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    check_for_updates()
