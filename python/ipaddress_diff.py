from ipaddress import ip_address
import unittest


def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


class TestIpsBetween(unittest.TestCase):

    def test_ips_between(self):
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)

if __name__ == "__main__":
    unittest.main()