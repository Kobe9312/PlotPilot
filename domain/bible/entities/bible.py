from typing import List, Optional
from domain.shared.base_entity import BaseEntity
from domain.novel.value_objects.novel_id import NovelId
from domain.bible.entities.character import Character
from domain.bible.entities.world_setting import WorldSetting
from domain.bible.value_objects.character_id import CharacterId
from domain.shared.exceptions import InvalidOperationError


class Bible(BaseEntity):
    """Bible 聚合根 - 管理人物和世界设定"""

    def __init__(self, id: str, novel_id: NovelId):
        super().__init__(id)
        self.novel_id = novel_id
        self.characters: List[Character] = []
        self.world_settings: List[WorldSetting] = []

    def add_character(self, character: Character) -> None:
        """添加人物"""
        # 检查重复
        if any(c.character_id == character.character_id for c in self.characters):
            raise InvalidOperationError(
                f"Character with id '{character.character_id.value}' already exists"
            )
        self.characters.append(character)

    def remove_character(self, character_id: CharacterId) -> None:
        """删除人物"""
        character = self.get_character(character_id)
        if character is None:
            raise InvalidOperationError(
                f"Character with id '{character_id.value}' not found"
            )
        self.characters.remove(character)

    def get_character(self, character_id: CharacterId) -> Optional[Character]:
        """获取人物"""
        for character in self.characters:
            if character.character_id == character_id:
                return character
        return None

    def add_world_setting(self, setting: WorldSetting) -> None:
        """添加世界设定"""
        # 检查重复
        if any(s.id == setting.id for s in self.world_settings):
            raise InvalidOperationError(
                f"World setting with id '{setting.id}' already exists"
            )
        self.world_settings.append(setting)

    def remove_world_setting(self, setting_id: str) -> None:
        """删除世界设定"""
        setting = next((s for s in self.world_settings if s.id == setting_id), None)
        if setting is None:
            raise InvalidOperationError(
                f"World setting with id '{setting_id}' not found"
            )
        self.world_settings.remove(setting)
