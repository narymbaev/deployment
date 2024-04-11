import enum


@enum.unique
class Sex(enum.Enum):
    UNDEFINED = -1
    MALE = 0
    FEMALE = 1

    @staticmethod
    def is_valid_sex(value) -> bool:
        if value and isinstance(value, int):
            return any(value == i.value for i in [Sex.MALE, Sex.FEMALE])
        return False
