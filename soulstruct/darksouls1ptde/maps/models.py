__all__ = ["MSBModel", "MSBModelList"]

import typing as tp
from functools import partial

from soulstruct.base.maps.msb.models import (
    MSBModel as _BaseMSBModel,
    MSBModelList as _BaseMSBModelList,
)
from soulstruct.base.maps.msb.enums import MSBModelSubtype
from soulstruct.utilities.binary import BinaryStruct

from .msb_entry import MSBEntryList


class MSBModel(_BaseMSBModel):
    """MSB model entry in Dark Souls."""

    MODEL_STRUCT = BinaryStruct(
        ("__name_offset", "i"),
        ("__model_type", "i"),
        ("_model_type_index", "i"),
        ("__sib_path_offset", "i"),
        ("_instance_count", "i"),
        "12x",
    )
    NAME_ENCODING = "shift-jis"
    NULL = b"\0"
    EMPTY_SIB_PATH = b"\0" * 6
    SIB_PATH_STEM = "N:\\FRPG\\data\\Model\\"


class MSBModelList(_BaseMSBModelList, MSBEntryList):

    SUBTYPE_CLASSES = {
        MSBModelSubtype.MapPiece: partial(MSBModel, model_subtype="MapPiece"),
        MSBModelSubtype.Object: partial(MSBModel, model_subtype="Object"),
        MSBModelSubtype.Character: partial(MSBModel, model_subtype="Character"),
        MSBModelSubtype.Player: partial(MSBModel, model_subtype="Player"),
        MSBModelSubtype.Collision: partial(MSBModel, model_subtype="Collision"),
        MSBModelSubtype.Navmesh: partial(MSBModel, model_subtype="Navmesh"),
    }
    ENTRY_CLASS = MSBModel

    new_map_piece_model: tp.Callable[..., MSBModel]
    new_object_model: tp.Callable[..., MSBModel]
    new_character_model: tp.Callable[..., MSBModel]
    new_item_model: tp.Callable[..., MSBModel]
    new_player_model: tp.Callable[..., MSBModel]
    new_collision_model: tp.Callable[..., MSBModel]
    new_navmesh_model: tp.Callable[..., MSBModel]
