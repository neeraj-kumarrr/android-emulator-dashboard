import os 


class AndroidSimulator:
    def __init__(self ):
        self.system_info = {}

    def start_emulator(self):
        try:
            print("starting your emulator")
            self.system_info ={
                'status': 'running',
                'os_version': 'Android 17',
                'device_model': 's21 fe',
                'memory': '8GB'
            }
            return True
        except Exception as e:
            print(f"error starting emulator: {e}")
            return False
        
    def install_app(self ,apk_path):
        try:
            print(f"installing app {apk_path}")
            return True
        except Exception as e:
            print(f"error on installing {e}")
            return False
        
    def get_info(self ):
        return self.system_info
    


