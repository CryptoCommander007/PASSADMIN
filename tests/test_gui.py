import unittest
from gui.main_window import MainWindow
class TestGUI(unittest.TestCase):
    def test_main_window(self):
        app = MainWindow()
        self.assertEqual(app.title(), "Mi Proyecto")
if __name__ == "__main__":
    unittest.main()
