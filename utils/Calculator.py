class Calculator:
    @staticmethod
    def multiply(a, b) -> float:
        """
        Multiply two numbers (int or float)
        """
        return float(a) * float(b)

    
    @staticmethod
    def calculate_total(*x) -> float:
        # Flatten in case someone passes a list
        flat = []
        for item in x:
            if isinstance(item, (list, tuple)):
                flat.extend(item)
            else:
                flat.append(item)
        return sum(flat)


    
    @staticmethod
    def calculate_daily_budget(total, days) -> float:
        """
        Calculate daily budget safely
        """
        return float(total) / float(days) if days > 0 else 0.0
    
    