# A little something... For you, From Shubh
from aqt import mw
from aqt.utils import qconnect
from aqt.qt import *
from aqt.gui_hooks import browser_menus_did_init
import os
import subprocess
import sys

# Function to open the media folder
def open_media_folder():
    media_folder_path = os.path.join(mw.pm.profileFolder(), "collection.media")
    subprocess.Popen(f'explorer "{media_folder_path}"')

# Function to open the add-on folder
def open_addon_folder():
    pfad = os.path.dirname(os.path.realpath(__file__))
    if os.name == 'nt':  # Check if the OS is Windows
        plugin_folder = pfad[:pfad.rindex("\\")]
    else:  # For macOS and Linux
        plugin_folder = pfad[:pfad.rindex("/")]
    subprocess.Popen(f'explorer "{plugin_folder}"' if os.name == 'nt' else f'open "{plugin_folder}"')

# Function to open the update log folder
def open_update_log_folder():
    update_log_path = mw.pm.profileFolder()
    subprocess.Popen(f'explorer "{update_log_path}"' if os.name == 'nt' else f'open "{update_log_path}"')

# Function to open the backup folder
def open_backup_folder():
    backup_path = mw.pm.backupFolder()
    subprocess.Popen(f'explorer "{backup_path}"' if os.name == 'nt' else f'open "{backup_path}"')

# Function to create the GoTo menu in the Tools menu
def setup_goto_menu():
    goto_menu = mw.form.menuTools.addMenu("GoTo...")

    # Add actions to the GoTo menu
    media_action = QAction("Open Media Folder", mw)
    qconnect(media_action.triggered, open_media_folder)
    goto_menu.addAction(media_action)

    addon_action = QAction("Open Add-on Folder", mw)
    qconnect(addon_action.triggered, open_addon_folder)
    goto_menu.addAction(addon_action)

    update_log_action = QAction("Open Update Log Folder", mw)
    qconnect(update_log_action.triggered, open_update_log_folder)
    goto_menu.addAction(update_log_action)

    backup_action = QAction("Open Backup Folder", mw)
    qconnect(backup_action.triggered, open_backup_folder)
    goto_menu.addAction(backup_action)

# Function to add actions to the Browse menu
def setup_browser_menu(browser):
    menu = browser.form.menuEdit  # Add under the "Edit" menu in the browser
    action = QAction("Open Media Folder", browser)
    qconnect(action.triggered, open_media_folder)
    menu.addSeparator()
    menu.addAction(action)

    # Set up a shortcut for opening the media folder in the Browse window
    browse_shortcut = QShortcut(QKeySequence("Ctrl+Alt+M"), browser)
    qconnect(browse_shortcut.activated, open_media_folder)

# Register the setup_browser_menu function to the browser menu initialization hook
browser_menus_did_init.append(setup_browser_menu)

# Set up a shortcut for opening the media folder in the main window
def setup_main_shortcut():
    main_shortcut = QShortcut(QKeySequence("Ctrl+Alt+M"), mw)
    qconnect(main_shortcut.activated, open_media_folder)

# Call the setup functions to add the GoTo menu to the Tools menu
setup_goto_menu()
setup_main_shortcut()
