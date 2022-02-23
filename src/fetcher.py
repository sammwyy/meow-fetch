import platform
import psutil
from screeninfo import get_monitors
import os, platform
import cpuinfo
import distro

class Fetcher:
    def __init__(self, char):
        self.char = char

    # System
    def get_architecture(self):
        return platform.processor()
    def get_kernel(self):
        return platform.release()
    def get_hostname(self):
        return platform.node()
    def get_user(self):
        return os.getlogin()
    def get_shell(self):
        return os.readlink('/proc/%d/exe' % os.getppid())
    def get_de(self):
        de = os.environ.get('DESKTOP_SESSION')

        if de is not None:
            de = de.lower()
            if de.startswith("ubuntu"):
                return "unity"
            elif de.startswith("lubuntu"):
                return "lxde"
            elif de.startswith("kubuntu"):
                return "kde"
            elif de.startswith("razon"):
                return "razor-qt"
            elif de.startswith("wmaker"):
                return "window-maker"
            else:
                return de
        elif os.environ.get('KDE_FULL_SESSION') == 'true':
            return "kde"
        elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                if not "deprecated" in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                    return "gnome2"
        return "unknown"

    def get_os(self):
        os = platform.system()
        if os == "Linux":
            distro_info = distro.linux_distribution(full_distribution_name=False)
            return distro_info[0].capitalize() + " " + str(distro_info[1])
        return os
    # Screen
    def get_screen_size(self):
        for m in get_monitors():
            return str(m.width) + "x" + str(m.height)
        return "unknown"
    # Disk
    def get_hdd_used(self):
        return int(psutil.disk_usage("/").used / 1024 / 1024 / 1024)
    def get_hdd_total(self):
        return int(psutil.disk_usage("/").total / 1024 / 1024 / 1024)
    def get_hdd_free(self):
        return int(psutil.disk_usage("/").free / 1024 / 1024 / 1024)
    def get_hdd_usage(self):
        return psutil.disk_usage("/").percent
    # CPU
    def get_cpu_brand(self):
        return cpuinfo.get_cpu_info()['brand_raw']
    def get_cpu_usage(self):
        return psutil.cpu_percent()
    def get_cpu_count(self):
        return psutil.cpu_count()
    def get_cpu_max_freq(self):
        return psutil.cpu_freq().max / 1000
    def get_cpu_min_freq(self):
        return psutil.cpu_freq().min / 1000
    def get_cpu_freq(self):
        return psutil.cpu_freq().current / 1000
    # RAM
    def get_ram_usage(self):
        return psutil.virtual_memory().percent
    def get_ram_used(self):
        return int(psutil.virtual_memory().used / 1024 / 1024)
    def get_ram_free(self):
        return int(psutil.virtual_memory().free / 1024 / 1024)
    def get_ram_total(self):
        return int(psutil.virtual_memory().total / 1024 / 1024)

    def format(self, text):
        return (text
            # RAM
            .replace("{ram_total}", str(self.get_ram_total()) + "MiB")
            .replace("{ram_free}", str(self.get_ram_free()) + "MiB")
            .replace("{ram_used}", str(self.get_ram_used()) + "MiB")
            .replace("{ram_usage}", str(self.get_ram_usage()) + "%")

            # CPU
            .replace("{cpu_freq}", str(self.get_cpu_freq()) + "GHz")
            .replace("{cpu_min_freq}", str(self.get_cpu_min_freq()) + "GHz")
            .replace("{cpu_max_freq}", str(self.get_cpu_max_freq()) + "GHz")
            .replace("{cpu_count}", str(self.get_cpu_count()))
            .replace("{cpu_usage}", str(self.get_cpu_usage()) + "%")
            .replace("{cpu_brand}", str(self.get_cpu_brand()))

            # Disk
            .replace("{hdd_usage}", str(self.get_hdd_usage()) + "%")
            .replace("{hdd_free}", str(self.get_hdd_free()) + "GiB")
            .replace("{hdd_total}", str(self.get_hdd_total()) + "GiB")
            .replace("{hdd_used}", str(self.get_hdd_used()) + "GiB")

            # Screen
            .replace("{screen_size}", str(self.get_screen_size()))

            # System
            .replace("{de}", str(self.get_de()))
            .replace("{shell}", str(self.get_shell()))
            .replace("{os}", str(self.get_os()))
            .replace("{user}", str(self.get_user()))
            .replace("{hostname}", str(self.get_hostname()))
            .replace("{kernel}", str(self.get_kernel()))
            .replace("{arch}", str(self.get_architecture()))

            # Colors
            .replace("{colors_light}", "{light_black}{char} {light_red}{char} {light_green}{char} {light_yellow}{char} {light_blue}{char} {light_magenta}{char} {light_cyan}{char} {light_white}{char}")
            .replace("{colors}", "{black}{char} {red}{char} {green}{char} {yellow}{char} {blue}{char} {magenta}{char} {cyan}{char} {white}{char}")

            # Extra
            .replace("{char}", self.char)
        )
