from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware

from project.software.software import Software


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        name_of_the_hardware = [h for h in System._hardware if h.name == hardware_name]
        name_of_the_software = [s for s in System._software if s.name == software_name]

        if name_of_the_hardware and name_of_the_software:
            name_of_the_hardware[0].uninstall(name_of_the_software[0])
            System._software.remove(name_of_the_software[0])
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis" \
               f"\nHardware Components: {len(System._hardware)}" \
               f"\nSoftware Components: {len(System._software)}" \
               f"\nTotal Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum([h.memory for h in System._hardware])}" \
               f"\nTotal Capacity Taken: {sum([s.used_capacity for s in System._hardware])} / {sum([h.capacity for h in System._hardware])}"

    @staticmethod
    def system_split():
        pass



