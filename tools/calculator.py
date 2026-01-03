from utils.Calculator import Calculator
from typing import List
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""

        @tool
        def estimate_total_hotel_cost(price_per_night: str | float | int, total_days: float) -> float:
            """Calculate total hotel cost"""
            try:
                price = float(price_per_night)
            except (ValueError, TypeError):
                raise ValueError(f"Invalid price_per_night: {price_per_night}")
            return self.calculator.multiply(price, total_days)
        
        @tool
        def calculate_total_expense(costs: list[float]) -> float:
            """Calculate total expense of the trip"""
            numbers = []
            for c in costs:
                try:
                    numbers.append(float(c))
                except (ValueError, TypeError):
                    raise ValueError(f"Invalid cost value: {c}")
            return self.calculator.calculate_total(*numbers)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]
