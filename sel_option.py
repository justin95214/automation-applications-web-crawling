import os
import xpath_data as xpath

profile = {
    "download.default_directory": os.getcwd() + "\\" + xpath.folder,
    "download.prompt_for_download": False,
    # "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_setting_values.automatic_downloads": 1
}