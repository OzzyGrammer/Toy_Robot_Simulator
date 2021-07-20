import unittest
import robo


class TestRobot(unittest.TestCase):

    def test_slice_x(self):

        self.assertEqual(robo.slice_x("PLACE 0,0,NORTH"), 0)
        self.assertEqual(robo.slice_x("PLACE 0,0,NORTH"), 0)
        self.assertEqual(robo.slice_x("PLACE 1,2,EAST"), 1)
        with self.assertRaises(ValueError):
            robo.slice_x("PLACE x,0,NORTH")

    def test_slice_y(self):

        self.assertEqual(robo.slice_y("PLACE 0,0,NORTH"), 0)
        self.assertEqual(robo.slice_y("PLACE 0,0,NORTH"), 0)
        self.assertEqual(robo.slice_y("PLACE 1,2,EAST"), 2)
        with self.assertRaises(ValueError):
            robo.slice_y("PLACE 0,y,NORTH")

    def test_slice_f(self):

        self.assertEqual(robo.slice_f("PLACE 0,0,NORTH"), "NORTH")
        self.assertEqual(robo.slice_f("PLACE 0,0,NORTH"), "NORTH")
        self.assertEqual(robo.slice_f("PLACE 1,2,EAST"), "EAST")
        with self.assertRaises(ValueError):
            robo.slice_f("PLACE 0,0,CENTER")

    def test_on_table(self):

        self.assertEqual(robo.on_table(1, 3), True)
        self.assertEqual(robo.on_table(2, 4), True)
        self.assertEqual(robo.on_table(7, 3), False)

    def test_command_valid(self):

        self.assertEqual(robo.command_valid("MOVE"), True)
        self.assertEqual(robo.command_valid("LEFT"), True)
        self.assertEqual(robo.command_valid("MIDDLE"), False)
        self.assertEqual(robo.command_valid("RIGHT"), True)
        self.assertEqual(robo.command_valid("REPORT"), True)

    def test_place_validation(self):

        self.assertEqual(robo.place_validation("PLACE 0,0,NORTH"), True)
        self.assertEqual(robo.place_validation("PLACE 1,2,EAST"), True)
        self.assertEqual(robo.place_validation("PLACES 1,2,EAST"), False)
        self.assertEqual(robo.place_validation("PLACE 1,2,NORTH"), True)

    def test_place(self):

        self.assertEqual(robo.place_validation("PLACE 0,0,NORTH"), True)
        self.assertEqual(robo.place_validation("PLACE 1,2,EAST"), True)
        self.assertEqual(robo.place_validation("PLACE 1,2,EAST"), True)
        self.assertEqual(robo.place_validation("PLACE 1,2,NORTH"), True)

    def test_place_validation(self):

        self.assertEqual(robo.place_validation("PLACE 0,0,NORTH"), True)
        self.assertEqual(robo.place_validation("PLACE 1,2,EAST"), True)
        self.assertEqual(robo.place_validation("PLACE 1,2,EAST"), True)
        self.assertEqual(robo.place_validation("PLACE 1,2,NORTH"), True)

if __name__ == '__main__':
    unittest.main()
