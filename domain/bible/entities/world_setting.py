from domain.shared.base_entity import BaseEntity


class WorldSetting(BaseEntity):
    """世界设定实体"""

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        setting_type: str  # "location", "item", "rule"
    ):
        super().__init__(id)
        self.name = name
        self.description = description
        self.setting_type = setting_type

    def update_description(self, description: str) -> None:
        """更新描述"""
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")
        self.description = description
