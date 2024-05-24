import unittest
import sys

sys.path.append("../")
from mqttsimdatagenerator import *


class TestMqttSimDataGenerator(unittest.TestCase):
    def test_randi_min_max(self):
        generator = MqttSimDataGenerator("<%randi min=0 max=10%>")
        values = []
        for _ in range(1000):
            values.append(int(generator.next_message()))

        self.assertTrue(all(map(lambda val: 0 <= val <= 10, values)))

    def test_randf_min_max(self):
        generator = MqttSimDataGenerator("<%randf min=-0.5 max=0.5%>")
        values = []
        for _ in range(1000):
            values.append(float(generator.next_message()))

        self.assertTrue(all(map(lambda val: -0.5 <= val <= 0.5, values)))

    def test_randu_min_max(self):
        generator = MqttSimDataGenerator("<%randu min=20 max=50%>")
        values = []
        for _ in range(1000):
            values.append(int(generator.next_message()))

        self.assertTrue(all(map(lambda val: 20 <= val <= 50, values)))

    def test_rands_collection(self):
        collection = ["a", "ab", "abc"]
        generator = MqttSimDataGenerator('<%rands collection=["a","ab","abc"]%>')
        values = []
        for _ in range(10):
            values.append(generator.next_message().strip('"'))
        self.assertTrue(all(map(lambda val: val in collection, values)))

    def test_rands_length(self):
        generator = MqttSimDataGenerator("<%rands length=10%>")
        values = []
        for _ in range(10):
            values.append(generator.next_message().strip('"'))
        self.assertTrue(all(map(lambda val: len(val) == 10, values)))

    def test_time(self):
        generator = MqttSimDataGenerator("<%time%>")
        now_gen = generator.next_message().strip('"').split(".")[0]
        now_dt_now = str(datetime.now().time()).split(".")[0]
        # no msecs
        self.assertEqual(now_gen, now_dt_now)

    def test_file_separator(self):
        # test.csv: a,b,c,d
        generator = MqttSimDataGenerator('<%file src="test.csv" separator=","%>')
        self.assertEqual(generator.next_message(), '"a"')
        self.assertEqual(generator.next_message(), '"b"')
        self.assertEqual(generator.next_message(), '"c"')
        self.assertEqual(generator.next_message(), '"d"')
        self.assertEqual(generator.next_message(), '"a"')

    def test_file_full_content(self):
        # test2.csv:
        # {
        #   message: "hello world"
        # }
        #
        generator = MqttSimDataGenerator('<%file src="test2.csv" separator="None"%>')
        self.assertEqual(generator.next_message(), '"{\n    message: "hello world"\n}"')
        self.assertEqual(generator.next_message(), '"{\n    message: "hello world"\n}"')

    def test_inc_start_int(self):
        generator = MqttSimDataGenerator('<%inc start=1%>')
        self.assertEqual(generator.next_message(), '1')
        self.assertEqual(generator.next_message(), '2')
        self.assertEqual(generator.next_message(), '3')

    def test_inc_inc_int(self):
        generator = MqttSimDataGenerator('<%inc inc=2%>')
        self.assertEqual(generator.next_message(), '0')
        self.assertEqual(generator.next_message(), '2')
        self.assertEqual(generator.next_message(), '4')
    
    def test_inc_reset_int(self):
        generator = MqttSimDataGenerator('<%inc reset=2%>')
        self.assertEqual(generator.next_message(), '0')
        self.assertEqual(generator.next_message(), '1')
        self.assertEqual(generator.next_message(), '2')
        self.assertEqual(generator.next_message(), '0')

    def test_inc_start_float(self):
        generator = MqttSimDataGenerator('<%inc start=1.5%>')
        self.assertEqual(generator.next_message(), '1.5')
        self.assertEqual(generator.next_message(), '2.5')
        self.assertEqual(generator.next_message(), '3.5')

    def test_inc_inc_float(self):
        generator = MqttSimDataGenerator('<%inc inc=0.5%>')
        self.assertEqual(generator.next_message(), '0')
        self.assertEqual(generator.next_message(), '0.5')
        self.assertEqual(generator.next_message(), '1.0')
    
    def test_inc_reset_float(self):
        generator = MqttSimDataGenerator('<%inc inc=0.5 reset=1.5%>')
        self.assertEqual(generator.next_message(), '0')
        self.assertEqual(generator.next_message(), '0.5')
        self.assertEqual(generator.next_message(), '1.0')
        self.assertEqual(generator.next_message(), '1.5')
        self.assertEqual(generator.next_message(), '0')

if __name__ == "__main__":
    unittest.main()
