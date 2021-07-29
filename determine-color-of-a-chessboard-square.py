class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (coordinates[0] in "aceg" and coordinates[1] in "2468") or (coordinates[0] in "bdfh" and coordinates[1] in "1357")
