from web_app import app
import unittest

class TestFlask(unittest.TestCase):
    
    def test_getItems(self):
        test = app.test_client(self)
        response = test.get("/getItems")
        status_code = response.status_code
        self.assertEqual(200, status_code, msg="Error occurred retrieving resource")

    def test_add(self):
        test = app.test_client(self)
        n1 = 10
        n2 = 20 
        result = n1 + n2
        response = test.get(f"/add?n1={n1}&n2={n2}")
        data = response.get_data().decode('utf-8') # Need to decode the string, it is returned as b'' (Bytes)
        self.assertEqual(f"The sum of {n1} and {n2} is: {str(result)}.", data, msg=f"Incorrect Sum, Expected: {str(result)}")

    def test_mult(self):
        test = app.test_client(self)
        n1 = 10
        n2 = 20 
        result = n1 * n2
        response = test.get(f"/mult?n1={n1}&n2={n2}")
        data = response.get_data().decode('utf-8') # Need to decode the string, it is returned as b'' (Bytes)
        self.assertEqual(f"The multiplication of {n1} and {n2} is: {str(result)}.", data, msg=f"Incorrect Multiplication, Expected: {str(result)}")
    
    def test_diff(self):
        test = app.test_client(self)
        n1 = 10
        n2 = 20 
        result = n1 - n2
        response = test.get(f"/diff?n1={n1}&n2={n2}")
        data = response.get_data().decode('utf-8') # Need to decode the string, it is returned as b'' (Bytes)
        self.assertEqual(f"The difference between {n1} and {n2} is: {str(result)}.", data, msg=f"Incorrect Difference, Expected: {str(result)}")
    
    def test_addMissingParams(self):
        test = app.test_client(self)
        n1 = 10
        response = test.get(f"/add?n1={n1}")
        data = response.status_code
        self.assertEqual(400, data, msg="Expected: 400 Bad Request")

    def test_power(self):
        test = app.test_client(self)
        n1 = 2
        n2 = 4
        power = 16
        response = test.get(f"/power?n1={n1}&n2={n2}")
        data = response.get_data().decode('utf-8') # Need to decode the string, it is returned as b'' (Bytes)
        self.assertEqual(f"{n1} to the power of {n2} is: {str(power)}.", data, msg=f"Incorrect Power, Expected: {str(power)}")

    def test_getCustomers(self):
        test = app.test_client(self)
        response = test.get("/getCustomers")
        status_code = response.status_code
        self.assertEqual(200, status_code, msg="Error occurred retrieving resource")
    
    def test_getCustomerAge(self):
        test = app.test_client(self)
        response = test.get("/getCustomerAge")
        status_code = response.status_code
        self.assertEqual(200, status_code, msg="Error occurred retrieving resource")

if __name__ == "__main__":
    unittest.main()