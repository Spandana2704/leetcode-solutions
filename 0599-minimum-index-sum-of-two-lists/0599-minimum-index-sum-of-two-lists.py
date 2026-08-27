class Solution(object):
    def findRestaurant(self, list1, list2):
        indices = {name: i for i, name in enumerate(list1)}
        result = []
        min_sum = float('inf')

        for j, name in enumerate(list2):
            if name in indices:
                total = indices[name] + j

                if total < min_sum:
                    min_sum = total
                    result = [name]
                elif total == min_sum:
                    result.append(name)

        return result