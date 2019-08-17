"""
TODO:
    - Filter fields and create more intelligent names.
"""

import os
import pickle
from typing import Dict, List, Optional

from soulstruct.bnd.core import BND, BaseBND
from soulstruct.params import ParamTable, DrawParamTable, PARAMDEF_BND
from soulstruct.params.fields import GAME_PARAM_INFO


class DarkSoulsGameParameters(object):

    AI: ParamTable
    Armor: ParamTable
    ArmorUpgrades: ParamTable
    Behaviors: ParamTable
    Bosses: ParamTable
    Bullets: ParamTable
    Cameras: ParamTable
    CharacterAttacks: ParamTable
    CharacterBehaviors: ParamTable
    CharacterSheets: ParamTable
    Dialogue: ParamTable
    Faces: ParamTable
    Goods: ParamTable
    Terrains: ParamTable
    ItemLots: ParamTable
    MenuColors: ParamTable
    CreatureAttacks: ParamTable
    CreatureBehaviors: ParamTable
    Movement: ParamTable
    NPCs: ParamTable
    Objects: ParamTable
    ObjectActivations: ParamTable
    Rings: ParamTable
    Shops: ParamTable
    SpecialEffects: ParamTable
    Spells: ParamTable
    Throws: ParamTable
    Weapons: ParamTable
    WeaponUpgrades: ParamTable
    VisualEffects: ParamTable

    def __init__(self, game_param_bnd_source):
        """Unpack DS1 GameParams into a single modifiable structure.

        Args:
            game_param_bnd_source: any valid source for GameParam.parambnd[.dcx] (its file path, the directory
                containing it, the unpacked BND directory, or an existing BND instance). It will default to the
                DEFAULT_GAME package. The appropriate bundled ParamDef will be loaded automatically, detected based on
                the DCX compression of the BND.
        """
        self._reload_warning = True
        self._data = {}

        if os.path.isdir(game_param_bnd_source):
            game_param_bnd_source = os.path.join(game_param_bnd_source, 'GameParam.parambnd')
        if isinstance(game_param_bnd_source, BaseBND):
            self._game_param_bnd = game_param_bnd_source
        else:
            try:
                self._game_param_bnd = BND(game_param_bnd_source)
            except TypeError:
                raise TypeError("Could not load DarkSoulsGameParameters from given source.")
        self.paramdef_bnd = PARAMDEF_BND('dsr' if self._game_param_bnd.dcx else 'ptd')

        for entry in self._game_param_bnd:
            # print(f"Loading PARAMBND entry {entry.id} ({entry.basename}) ...")
            p = self._data[entry.path] = ParamTable(entry.data, self.paramdef_bnd)
            # print(f"  Success. Param attribute name: {p.param_name}")
            try:
                param_nickname, field_nicknames = GAME_PARAM_INFO[entry.basename[:-len('.param')]]
            except KeyError:
                pass
            else:
                setattr(self, param_nickname, p)
                # TODO: field nicknames

    def update_bnd(self):
        """Update the internal BND by packing the current ParamTables. Called automatically by `save()`."""
        for param_table_entry_path, param_table in self._data.items():
            self._game_param_bnd.entries_by_path[param_table_entry_path].data = param_table.pack()

    def save(self, game_param_bnd_path=None, auto_pickle=True):
        """Save the DarkSoulsGameParameters. If no path is given, it will attempt to save to the same BND file."""
        self.update_bnd()
        if auto_pickle:
            self.pickle()
        self._game_param_bnd.write(game_param_bnd_path)
        if not self._reload_warning:
            print('\nDarkSoulsGameParameters saved successfully. (Remember to reload your game.)')
            self._reload_warning = True
        else:
            print('\nDarkSoulsGameParameters saved successfully.')

    def pickle(self, game_param_pickle_path=None):
        """Save the entire DarkSoulsGameParameters to a pickled file, which will be faster to load in future."""
        if game_param_pickle_path is None:
            game_param_pickle_path = self._game_param_bnd.bnd_path
            if game_param_pickle_path is None:
                raise ValueError("Could not automatically determine DarkSoulsGameParameters path for pickling.")
        if game_param_pickle_path.endswith('.dcx'):
            game_param_pickle_path = game_param_pickle_path[:len('.dcx')]
        if game_param_pickle_path.endswith('.parambnd'):
            game_param_pickle_path = game_param_pickle_path[:len('.parambnd')]
        game_param_pickle_path += '.pickle'
        with open(game_param_pickle_path, 'wb') as f:
            pickle.dump(self, f)


DRAW_PARAM_TABLES = ('Dof', 'EnvLightTex', 'Fog', 'LensFlare', 'LensFlareEx', 'AmbientLight', 'ScatteredLight',
                     'PointLight', 'Shadow', 'ToneCorrect', 'ToneMap', 's_AmbientLight')


class DrawParamBlock(object):

    Dof: List[Optional[DrawParamTable]]
    EnvLightTex: List[Optional[DrawParamTable]]
    Fog: List[Optional[DrawParamTable]]
    LensFlare: List[Optional[DrawParamTable]]
    LensFlareEx: List[Optional[DrawParamTable]]
    AmbientLight: List[Optional[DrawParamTable]]
    ScatteredLight: List[Optional[DrawParamTable]]
    PointLight: List[Optional[DrawParamTable]]
    Shadow: List[Optional[DrawParamTable]]
    ToneCorrect: List[Optional[DrawParamTable]]
    ToneMap: List[Optional[DrawParamTable]]
    s_AmbientLight: List[Optional[DrawParamTable]]

    def __init__(self, draw_param_bnd):
        """Structure that holds a single DrawParam file for a single map block."""

        self._data = {}  # type: Dict[str, List[Optional[DrawParamTable], Optional[DrawParamTable]]]
        self.paramdef_bnd = PARAMDEF_BND('dsr' if bool(draw_param_bnd.dcx) else 'ptd')

        if not isinstance(draw_param_bnd, BaseBND):
            draw_param_bnd = BND(draw_param_bnd)

        for entry in draw_param_bnd:
            parts = entry.basename[:-len('.param')].split('_')
            if len(parts) == 2:
                slot = 0
                basename = parts[1]
            elif len(parts) == 3:
                if parts[1] != '1':
                    raise ValueError("Only slot 0 and slot 1 can exist in DrawParams.")
                slot = 1
                basename = parts[2]
            else:
                raise ValueError(f"Malformed params name: '{entry.basename}'")
            if parts[0].startswith('s'):
                basename = 's_' + basename

            self._data.setdefault(basename, [None, None])[slot] = DrawParamTable(entry.data, self.paramdef_bnd)
            try:
                param_nickname, field_nicknames = DRAWPARAM_ALIASES[basename]
            except KeyError:
                raise KeyError(f"Invalid DrawParam base name: {basename}")
            else:
                setattr(self, param_nickname, self._data[basename])

    def __getitem__(self, table_name):
        return getattr(self, table_name)

    def __iter__(self):
        return iter({DRAWPARAM_ALIASES[k]: v for k, v in self._data.items()})

    def save(self):
        pass  # TODO


DRAWPARAM_MAPS = ('m10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'default')


class DarkSoulsLightingParameters(object):

    _MAP_IDS = (10, 11, 12, 13, 14, 15, 16, 17, 18, 99, 'default')

    m10: DrawParamBlock
    m11: DrawParamBlock
    m12: DrawParamBlock
    m13: DrawParamBlock
    m14: DrawParamBlock
    m15: DrawParamBlock
    m16: DrawParamBlock
    m17: DrawParamBlock
    m18: DrawParamBlock
    m99: DrawParamBlock
    default: DrawParamBlock

    def __init__(self, draw_param_directory: str):
        """Unpack DS1 DrawParams into a single modifiable structure.

        Opens all DrawParam BNDs simultaneously for editing and repacking. The appropriate bundled ParamDef file will be
        loaded, with the game version determined by the DrawParam DCX compression.

        Args:
            draw_param_directory: Directory where all the 'aXX_DrawParam.parambnd[.dcx]' files are. This will be inside
                'params/DrawParam' in your game directory. If left out, it will default to the DEFAULT_GAME package path
                in your soulstruct/config.py.

        """

        self._reload_warning = True
        self._data = {}

        for area_id in self._MAP_IDS:
            if isinstance(area_id, int):
                file_map_name = f'a{area_id}'
                map_name = f'm{area_id}'
            else:
                file_map_name = map_name = area_id
            try:
                draw_param_bnd = BND(os.path.join(draw_param_directory, f'{file_map_name}_DrawParam.parambnd.dcx'))
            except FileNotFoundError:
                try:
                    draw_param_bnd = BND(os.path.join(draw_param_directory, f'{file_map_name}_DrawParam.parambnd'))
                except FileNotFoundError:
                    raise FileNotFoundError(f"Could not find '{file_map_name}_DrawParam.parambnd[.dcx]' in "
                                            f"given directory '{draw_param_directory}'.")
            self._data[map_name] = DrawParamBlock(draw_param_bnd)
            setattr(self, map_name, self._data[map_name])

    def __getitem__(self, map_name):
        if map_name not in self._data:
            raise KeyError(f"Invalid DrawParam map name: '{map_name}'")
        return self._data[map_name]

    def __iter__(self):
        return iter(self._data.items())

    # TODO: Restore these methods (particularly `dict_to_param` as `.pack()`).
    # def delete_row(self, params, index):
    #     """ Delete a row. You can undo"""
    #     getattr(self, params).pop(index)

    # def save(self):
    #     for param_name, param_file in self._param_paths.items():
    #         dict_to_param(getattr(self, param_name), param_file, paramdef=getattr(self, param_name)['paramdef'])
    #     repack_bnd(os.path.join(self.param_directory, 'GameParam.parambnd'))
    #     if not self._reload_warning:
    #         print('\nParameters saved successfully. (Remember to reload your game.)')
    #         self._reload_warning = True
    #     else:
    #         print('\nParameters saved successfully.')

    def pack(self, gameparam_bnd_path):
        # TODO
        pass


DRAWPARAM_ALIASES = {
    'DofBank': ('Dof', {}),
    'EnvLightTexBank': ('EnvLightTex', {}),
    'FogBank': ('Fog', {}),
    'LensFlareBank': ('LensFlare', {}),
    'LensFlareExBank': ('LensFlareEx', {}),
    'LightBank': ('AmbientLight', {}),
    'LightScatteringBank': ('ScatteredLight', {}),
    'LodBank': ('Lod', {}),  # default_DrawParam only
    'PointLightBank': ('PointLight', {}),
    'ShadowBank': ('Shadow', {}),
    'ToneCorrectBank': ('ToneCorrect', {}),
    'ToneMapBank': ('ToneMap', {}),
    's_LightBank': ('s_AmbientLight', {}),
}
