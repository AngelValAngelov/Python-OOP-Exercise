from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        all_memory = sum([m.memory_consumption for m in self.software_components])
        all_capacity = sum([c.capacity_consumption for c in self.software_components])
        if self.memory - all_memory < software.memory_consumption or self.capacity - all_capacity < software.capacity_consumption:
            raise Exception("Software cannot be installed")
        else:
            self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)


    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

