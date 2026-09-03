class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type: str, length: int) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        self.type = figure_type
        self.length = length

    @property
    def get_angles(self) -> int:
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3
        return 0