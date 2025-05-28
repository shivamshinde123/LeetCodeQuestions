class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age_counter = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                age_counter += 1

        return age_counter
