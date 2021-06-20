class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        hour1, minute1 = startTime.split(":")
        hour1, minute1 = int(hour1), int(minute1)
        hour2, minute2 = finishTime.split(":")
        hour2, minute2 = int(hour2), int(minute2)
        if hour2 < hour1 or (hour2 == hour1 and minute2 < minute1):
            hour2 += 24
        num = (hour2 - hour1 - 1) * 4
        num += (60 - minute1) // 15
        num += minute2 // 15

        return num
