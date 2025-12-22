class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        numberOfFleets = 0

        def myFunc(e):
            return e[1]

        def calculateArrivalTime(car, target: int) -> float:
            result = (target - car[1]) / car[2]
            return result

        for i in range(len(position)):
            cars.append((i, position[i], speed[i]))
        
        cars.sort(key=myFunc, reverse=True)
        for car in cars:
            arrivalTime = calculateArrivalTime(car, target)
            if not stack:
                stack.append(arrivalTime)
            else:
                if arrivalTime <= stack[-1]:
                    continue
                stack.append(arrivalTime)   
        return len(stack)

