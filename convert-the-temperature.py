class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        if celsius >= 0:
            Kelvin = celsius + 273.15
            Fahrenheit = celsius * 1.80 + 32.00
            ans = [Kelvin, Fahrenheit]
        return ans