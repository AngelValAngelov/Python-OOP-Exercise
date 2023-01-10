import unittest

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware
from project.software.software import Software


class testHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("Intel", "Heavy", 100, 100)

    def test_hardware_initialized(self):
        self.assertEqual(self.hardware.name, "Intel")
        self.assertEqual(self.hardware.type, "Heavy")
        self.assertEqual(self.hardware.memory, 100)
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.software_components, [])

    def test_install_method_should_raise_exception(self):
        software = LightSoftware("Yes", 100, 200)
        with self.assertRaises(Exception) as cm:
            self.hardware.install(software)
        self.assertEqual(str(cm.exception), "Software cannot be installed")

    def test_install_method_should_add_components(self):
        software = LightSoftware("Yes", 10, 10)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_uninstall_method_delete_successfully(self):
        software = LightSoftware("Yes", 10, 20)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)

    def test_uninstall_method(self):
        software = LightSoftware("Yes", 1000000, 200000)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)


if __name__ == '__main__':
    unittest.main()
