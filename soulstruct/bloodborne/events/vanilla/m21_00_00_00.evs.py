"""
linked:
164

strings:
0: PC情報_拠点到達時
22: ボス_撃破
34: PC情報_ボス撃破_拠点ボス
64: ボス_戦闘開始
80: ボス_撃破時間
96: PC情報_ボス撃破_拠点ボス2
128: ボス_戦闘開始2
146: ボス_撃破時間2
164: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(12100010)
    SkipLinesIfFlagOff(1, 9400)
    SetRespawnPoint(2102961)
    SkipLinesIfClient(2)
    SkipLinesIfFlagOff(1, 6600)
    EnableFlag(12101999)
    SkipLinesIfFlagOn(1, 12101999)
    DisableObject(2101100)
    SetNetworkUpdateRate(2100700, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(PLAYER, 110, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 111, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 112, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 113, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 114, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 115, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 116, affect_npc_part_hp=False)
    DisableFlag(72100100)
    DisableFlag(72100101)
    DisableFlag(72100102)
    DisableFlag(72102110)
    DisableFlag(72102200)
    DisableFlag(72102201)
    DisableFlag(72102300)
    DisableFlag(72102301)
    DisableFlag(72102302)
    DisableFlag(72102400)
    DisableFlag(72102401)
    DisableFlag(72102410)
    DisableFlag(72102411)
    DisableFlag(72102412)
    DisableFlag(72102413)
    DisableFlag(72102420)
    DisableFlag(72102421)
    DisableFlag(72102422)
    DisableFlag(72102500)
    DisableFlag(72102501)
    DisableFlag(72102502)
    DisableFlag(72102600)
    DisableFlag(72102601)
    DisableFlag(72102602)
    DisableFlag(72102603)
    DisableFlag(72102700)
    DisableFlag(72102701)
    DisableFlag(72102800)
    DisableFlag(72102801)
    DisableFlag(72102802)
    DisableFlag(72102803)
    DisableFlag(72103200)
    DisableFlag(72103201)
    DisableFlag(72103202)
    DisableFlag(72103203)
    DisableFlag(72103300)
    DisableFlag(72103301)
    DisableFlag(72103400)
    DisableFlag(72103401)
    DisableFlag(72103402)
    DisableFlag(72103403)
    DisableFlag(72103500)
    DisableFlag(72103501)
    DisableFlag(72103502)
    DisableFlag(72103600)
    DisableFlag(72103601)
    DisableFlag(72103602)
    RunEvent(12105210)
    RunEvent(12107000, slot=52, args=(72102110, 2100952, 2112950))
    RunEvent(12107000, slot=0, args=(72102200, 2100951, 2202950))
    RunEvent(12107000, slot=1, args=(72102201, 2100951, 2202951))
    RunEvent(12107000, slot=5, args=(72102300, 2100950, 2302950))
    RunEvent(12107000, slot=6, args=(72102301, 2100950, 2302951))
    RunEvent(12107000, slot=7, args=(72102302, 2100950, 2302952))
    RunEvent(12107000, slot=10, args=(72102400, 2100950, 2402950))
    RunEvent(12107000, slot=11, args=(72102401, 2100950, 2402951))
    RunEvent(12107000, slot=15, args=(72102410, 2100950, 2412950))
    RunEvent(12107000, slot=16, args=(72102411, 2100950, 2412951))
    RunEvent(12107000, slot=17, args=(72102412, 2100950, 2412952))
    RunEvent(12107000, slot=18, args=(72102413, 2100950, 2412953))
    RunEvent(12107000, slot=20, args=(72102420, 2100950, 2422950))
    RunEvent(12107000, slot=21, args=(72102421, 2100950, 2422951))
    RunEvent(12107000, slot=22, args=(72102422, 2100950, 2422952))
    RunEvent(12107000, slot=25, args=(72102500, 2100952, 2502950))
    RunEvent(12107000, slot=26, args=(72102501, 2100952, 2502951))
    RunEvent(12107000, slot=27, args=(72102502, 2100952, 2502952))
    RunEvent(12107000, slot=30, args=(72102600, 2100953, 2602950))
    RunEvent(12107000, slot=31, args=(72102601, 2100953, 2602951))
    RunEvent(12107000, slot=32, args=(72102602, 2100953, 2602952))
    RunEvent(12107000, slot=33, args=(72102603, 2100953, 2602953))
    RunEvent(12107000, slot=35, args=(72102700, 2100951, 2702950))
    RunEvent(12107000, slot=36, args=(72102701, 2100951, 2702951))
    RunEvent(12107000, slot=40, args=(72102800, 2100952, 2802950))
    RunEvent(12107000, slot=41, args=(72102801, 2100952, 2802951))
    RunEvent(12107000, slot=42, args=(72102802, 2100952, 2802952))
    RunEvent(12107000, slot=43, args=(72102803, 2100952, 2802953))
    RunEvent(12107000, slot=45, args=(72103200, 2100951, 3202950))
    RunEvent(12107000, slot=46, args=(72103201, 2100953, 3202951))
    RunEvent(12107000, slot=47, args=(72103202, 2100951, 3202952))
    RunEvent(12107000, slot=48, args=(72103203, 2100953, 3202953))
    RunEvent(12107000, slot=50, args=(72103300, 2100953, 3302950))
    RunEvent(12107000, slot=51, args=(72103301, 2100953, 3302951))
    RunEvent(12107000, slot=55, args=(72103400, 2100231, 3402950))
    RunEvent(12107000, slot=56, args=(72103401, 2100231, 3402951))
    RunEvent(12107000, slot=57, args=(72103402, 2100231, 3402952))
    RunEvent(12107000, slot=58, args=(72103403, 2100231, 3402953))
    RunEvent(12107000, slot=60, args=(72103500, 2100231, 3502950))
    RunEvent(12107000, slot=61, args=(72103501, 2100231, 3502951))
    RunEvent(12107000, slot=62, args=(72103502, 2100231, 3502952))
    RunEvent(12107000, slot=65, args=(72103600, 2100231, 3602950))
    RunEvent(12107000, slot=66, args=(72103601, 2100231, 3602951))
    RunEvent(12107000, slot=67, args=(72103602, 2100231, 3602952))
    DisableFlag(72100420)
    DisableFlag(72100421)
    DisableFlag(72100422)
    DisableFlag(72100423)
    DisableFlag(72100424)
    DisableFlag(72100425)
    DisableFlag(72100426)
    RunEvent(12107100, slot=0, args=(72100420, 2100954, 9020))
    RunEvent(12107100, slot=1, args=(72100421, 2100955, 9021))
    RunEvent(12107100, slot=2, args=(72100422, 2100956, 9022))
    RunEvent(12107100, slot=3, args=(72100423, 2100957, 9023))
    RunEvent(12107100, slot=4, args=(72100424, 2100958, 9024))
    RunEvent(12107100, slot=5, args=(72100425, 2100959, 9025))
    RunEvent(12107100, slot=6, args=(72100426, 2100960, 9026))
    DisableFlag(72100300)
    DisableFlag(72100301)
    DisableFlag(72100302)
    DisableFlag(72100303)
    DisableFlag(72100304)
    DisableFlag(72100305)
    DisableFlag(72100306)
    DisableFlag(72100307)
    DisableFlag(72100308)
    DisableFlag(72100309)
    RunEvent(12107200, slot=0, args=(72100300, 2902950, 9001))
    RunEvent(12107200, slot=1, args=(72100301, 2902951, 9002))
    RunEvent(12107200, slot=2, args=(72100302, 2902952, 9003))
    RunEvent(12107200, slot=3, args=(72100303, 2902953, 9004))
    RunEvent(12107200, slot=4, args=(72100304, 2902954, 9005))
    RunEvent(12107200, slot=5, args=(72100305, 2902955, 9006))
    RunEvent(12107200, slot=6, args=(72100306, 2902956, 9007))
    RunEvent(12107200, slot=7, args=(72100307, 2902957, 9008))
    RunEvent(12107200, slot=8, args=(72100308, 2902958, 9009))
    RunEvent(12107200, slot=9, args=(72100309, 2902959, 9010))
    RunEvent(12100300)
    RunEvent(12100310)
    RunEvent(12100800)
    RunEvent(12100180)
    RunEvent(12101800)
    RunEvent(12101801)
    RunEvent(12101802)
    RunEvent(12104810)
    RunEvent(12104811)
    RunEvent(12104802)
    RunEvent(12104803)
    RunEvent(12104804)
    RunEvent(12104805)
    RunEvent(12104807)
    RunEvent(12104808)
    RunEvent(12101803)
    RunEvent(12100000)
    RunEvent(12100002)
    RunEvent(12101850)
    RunEvent(12101851)
    RunEvent(12101852)
    RunEvent(12104880)
    RunEvent(12104881)
    RunEvent(12104852)
    RunEvent(12104853)
    RunEvent(12104854)
    RunEvent(12104855)
    RunEvent(12101853)
    RunEvent(12104860, slot=0, args=(5, 5, 1, 100, 480, 490, 8000), arg_types="hihiiii")
    RunEvent(12104860, slot=1, args=(6, 6, 2, 150, 481, 491, 8010), arg_types="hihiiii")
    RunEvent(12104860, slot=2, args=(7, 7, 3, 150, 482, 492, 8030), arg_types="hihiiii")
    RunEvent(12104860, slot=3, args=(8, 8, 4, 200, 483, 493, 8020), arg_types="hihiiii")
    RunEvent(12104860, slot=4, args=(9, 9, 5, 200, 484, 494, 8040), arg_types="hihiiii")
    RunEvent(12104870)
    RunEvent(12100400)
    RunEvent(12100410, slot=0, args=(7002, 2101000, 9462, 10010171))
    RunEvent(12100410, slot=1, args=(7030, 2101010, 9403, 10010171))
    RunEvent(12100410, slot=2, args=(7030, 2101020, 9403, 10010171))
    RunEvent(12100410, slot=3, args=(7030, 2101030, 9403, 10010171))
    RunEvent(9401)
    RunEvent(12100990)
    RunEvent(12105000, slot=0, args=(2100950, 12105030))
    RunEvent(12105000, slot=1, args=(2100951, 12105031))
    RunEvent(12105000, slot=2, args=(2100952, 12105032))
    RunEvent(12105000, slot=3, args=(2100953, 12105033))
    RunEvent(12105004, slot=3, args=(2100231, 12105034))
    RunEvent(12105020)
    RunEvent(12105021)
    RunEvent(12105022)
    RunEvent(12105023)
    RunEvent(12105024)
    RunEvent(12105040)
    RunEvent(12101000, slot=0, args=(4110, 2100211, 1, 10), arg_types="iiBB")
    RunEvent(12101000, slot=1, args=(4111, 2100211, 2, 13), arg_types="iiBB")
    RunEvent(12101000, slot=2, args=(4112, 2100211, 3, 15), arg_types="iiBB")
    RunEvent(12101000, slot=3, args=(4113, 2100212, 0, 15), arg_types="iiBB")
    RunEvent(12101000, slot=4, args=(4114, 2100212, 1, 12), arg_types="iiBB")
    RunEvent(12101000, slot=5, args=(4115, 2100212, 2, 11), arg_types="iiBB")
    RunEvent(12101000, slot=6, args=(4116, 2100212, 3, 15), arg_types="iiBB")
    RunEvent(12101000, slot=7, args=(4117, 2100213, 0, 15), arg_types="iiBB")
    RunEvent(12101000, slot=8, args=(4118, 2100213, 1, 15), arg_types="iiBB")
    RunEvent(12101000, slot=9, args=(4119, 2100213, 2, 15), arg_types="iiBB")
    RunEvent(12101010)
    RunEvent(12105043)
    RunEvent(12101020)
    RunEvent(12101021)
    RunEvent(12101022)
    RunEvent(12101024)
    RunEvent(12101026)
    RunEvent(12101028)
    RunEvent(12105010)
    RunEvent(12105011)
    RunEvent(12105012)
    RunEvent(12105013)
    RunEvent(12105014)
    RunEvent(12105015)
    RunEvent(12105016)
    RunEvent(12105310, slot=0, args=(94005001, 2100954))
    RunEvent(12105310, slot=1, args=(94105001, 2100955))
    RunEvent(12105310, slot=2, args=(94205001, 2100956))
    RunEvent(12105310, slot=3, args=(94305001, 2100957))
    RunEvent(12105310, slot=4, args=(94405001, 2100958))
    RunEvent(12105310, slot=5, args=(94505001, 2100959))
    RunEvent(12105310, slot=6, args=(94605001, 2100960))
    RunEvent(12100110)
    RunEvent(12105200)
    RunEvent(12100115)
    RunEvent(12100116)
    RunEvent(12100117)
    RunEvent(12100120)
    RunEvent(12100121)
    RunEvent(12100123)
    RunEvent(12100112)
    RunEvent(12100113)
    RunEvent(12100114)
    RunEvent(12100160)
    RunEvent(12100162)
    RunEvent(12100163)
    RunEvent(12100164)
    RunEvent(12100165)
    DisableHealthBar(2100600)
    RunEvent(12105060)
    RunEvent(12105062)
    RunEvent(12105070, slot=0, args=(72100141, 6011, 20), arg_types="iiB")
    RunEvent(12105070, slot=1, args=(72100142, 6012, 21), arg_types="iiB")
    RunEvent(12105070, slot=2, args=(72100143, 6013, 22), arg_types="iiB")
    RunEvent(12105070, slot=3, args=(72100144, 6014, 23), arg_types="iiB")
    RunEvent(12105070, slot=4, args=(72100145, 6015, 24), arg_types="iiB")
    RunEvent(12105070, slot=5, args=(72100146, 6016, 25), arg_types="iiB")
    RunEvent(12105070, slot=6, args=(72100147, 6017, 26), arg_types="iiB")
    RunEvent(12105070, slot=7, args=(72100148, 6018, 27), arg_types="iiB")
    RunEvent(12105070, slot=8, args=(72100149, 6019, 28), arg_types="iiB")
    RunEvent(12105070, slot=9, args=(72100150, 6020, 0), arg_types="iiB")
    RunEvent(12105070, slot=10, args=(72100151, 6021, 0), arg_types="iiB")
    RunEvent(12105070, slot=11, args=(72100152, 6022, 0), arg_types="iiB")
    RunEvent(12105070, slot=12, args=(72100153, 6023, 0), arg_types="iiB")
    RunEvent(12105070, slot=13, args=(72100154, 6024, 0), arg_types="iiB")
    RunEvent(12105070, slot=14, args=(72100155, 6025, 0), arg_types="iiB")
    RunEvent(12100020, slot=0, args=(4900, 6071, 1))
    RunEvent(12100020, slot=1, args=(4901, 6072, 1))
    RunEvent(12100020, slot=2, args=(4902, 6073, 1))
    RunEvent(12100020, slot=3, args=(4903, 6074, 0))
    RunEvent(12100020, slot=4, args=(4904, 6075, 0))
    RunEvent(12100020, slot=5, args=(4905, 6076, 0))
    RunEvent(12100020, slot=6, args=(4906, 6077, 0))
    RunEvent(12100020, slot=7, args=(4907, 6078, 0))
    RunEvent(12100020, slot=8, args=(4908, 6079, 0))
    RunEvent(12100020, slot=9, args=(4909, 6080, 0))
    RunEvent(12100020, slot=10, args=(4910, 6081, 0))
    RunEvent(12100020, slot=11, args=(4911, 6082, 0))
    RunEvent(12100020, slot=12, args=(4912, 6083, 0))
    RunEvent(12100020, slot=13, args=(4913, 6084, 0))
    RunEvent(12100020, slot=14, args=(4914, 6085, 0))
    RunEvent(12105064)
    RunEvent(12101100)
    RunEvent(12105300)
    AddSpecialEffect(PLAYER, 9121, affect_npc_part_hp=False)
    SkipLinesIfFlagOn(1, 12101802)
    AddSpecialEffect(PLAYER, 9120, affect_npc_part_hp=False)
    RunEvent(12100330)


def Preconstructor():
    """ 50: Event 50 """
    SkipLinesIfFlagOff(2, 12101020)
    DisableBackread(2100215)
    DisableBackread(2100220)
    SkipLinesIfFlagOff(2, 12101021)
    DisableBackread(2100216)
    DisableBackread(2100221)
    SkipLinesIfFlagOn(2, 9462)
    DisableBackread(2100800)
    DisableBackread(2100810)
    SkipLinesIfFlagOn(1, 12101802)
    EnableFlag(2100)
    GotoIfFlagOff(Label.L0, 1003)
    DisableFlag(1003)
    DisableFlag(72100110)
    DisableFlag(72100111)
    DisableFlag(72100112)
    DisableFlag(72100113)
    DisableFlag(72100114)
    GotoIfFlagOff(Label.L1, 9462)
    EnableFlag(1002)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(1000)

    # --- 0 --- #
    DefineLabel(0)
    RunEvent(12100100, slot=0, args=(1000, 1019))
    RunEvent(12100101, slot=0, args=(1000, 1019))
    RunEvent(12100140, slot=0, args=(1020, 1039))
    RunEvent(12100141, slot=0, args=(1020, 1039))
    RunEvent(12100142, slot=0, args=(1020, 1039))
    RunEvent(12100143, slot=0, args=(1020, 1039))
    RunEvent(12100144, slot=0, args=(1020, 1039))
    RunEvent(12100145, slot=0, args=(1020, 1039))
    RunEvent(12100146)
    DisableAnimations(2100200)
    DisableAnimations(2100201)
    DisableAnimations(2100202)
    DisableAnimations(2100203)
    DisableAnimations(2100211)
    DisableAnimations(2100212)
    DisableAnimations(2100219)
    DisableAnimations(2100214)
    DisableAnimations(2100215)
    DisableAnimations(2100216)
    DisableAnimations(2100217)
    DisableAnimations(2100218)
    DisableAnimations(2100220)
    DisableAnimations(2100221)
    DisableAnimations(2100222)
    DisableAnimations(2100230)
    DisableAnimations(2100231)
    DisableAnimations(2100950)
    DisableAnimations(2100951)
    DisableAnimations(2100952)
    DisableAnimations(2100953)
    DisableAnimations(2100954)
    DisableAnimations(2100955)
    DisableAnimations(2100956)
    DisableAnimations(2100957)
    DisableAnimations(2100958)
    DisableAnimations(2100959)
    DisableAnimations(2100960)
    DisableGravity(2100200)
    DisableGravity(2100201)
    DisableGravity(2100202)
    DisableGravity(2100203)
    DisableGravity(2100211)
    DisableGravity(2100212)
    DisableGravity(2100219)
    DisableGravity(2100214)
    DisableGravity(2100215)
    DisableGravity(2100216)
    DisableGravity(2100217)
    DisableGravity(2100218)
    DisableGravity(2100220)
    DisableGravity(2100221)
    DisableGravity(2100222)
    DisableGravity(2100230)
    DisableGravity(2100231)
    DisableGravity(2100950)
    DisableGravity(2100951)
    DisableGravity(2100952)
    DisableGravity(2100953)
    DisableGravity(2100954)
    DisableGravity(2100955)
    DisableGravity(2100956)
    DisableGravity(2100957)
    DisableGravity(2100958)
    DisableGravity(2100959)
    DisableGravity(2100960)
    DisableCharacterCollision(2100200)
    DisableCharacterCollision(2100201)
    DisableCharacterCollision(2100202)
    DisableCharacterCollision(2100203)
    DisableCharacterCollision(2100211)
    DisableCharacterCollision(2100212)
    DisableCharacterCollision(2100219)
    DisableCharacterCollision(2100214)
    DisableCharacterCollision(2100215)
    DisableCharacterCollision(2100216)
    DisableCharacterCollision(2100217)
    DisableCharacterCollision(2100218)
    DisableCharacterCollision(2100220)
    DisableCharacterCollision(2100221)
    DisableCharacterCollision(2100222)
    DisableCharacterCollision(2100230)
    DisableCharacterCollision(2100231)
    DisableCharacterCollision(2100950)
    DisableCharacterCollision(2100951)
    DisableCharacterCollision(2100952)
    DisableCharacterCollision(2100953)
    DisableCharacterCollision(2100954)
    DisableCharacterCollision(2100955)
    DisableCharacterCollision(2100956)
    DisableCharacterCollision(2100957)
    DisableCharacterCollision(2100958)
    DisableCharacterCollision(2100959)
    DisableCharacterCollision(2100960)
    SkipLinesIfFlagOff(2, 12411000)
    DisableBackread(2100800)
    DisableBackread(2100810)


def Event9401():
    """ 9401: Event 9401 """
    DisableNetworkSync()
    EndIfClient()
    EndIfThisEventOn()
    EnableFlag(9180)
    PlayCutscene(21000000, skippable=True, fade_out=True, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    EnableFlag(12417810)


def Event12100000():
    """ 12100000: Event 12100000 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 12101800)
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 2103601)
    IfStandingOnCollision(-1, 2103602)
    IfStandingOnCollision(-1, 2103603)
    IfStandingOnCollision(-1, 2103604)
    IfStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 9900)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    DeleteVFX(2103300, erase_root_only=True)
    DeleteVFX(2103500, erase_root_only=True)
    DeleteVFX(2103501, erase_root_only=True)
    DeleteVFX(2103502, erase_root_only=True)
    DeleteVFX(2103503, erase_root_only=True)
    DeleteVFX(2103504, erase_root_only=True)
    DeleteVFX(2103505, erase_root_only=True)
    DeleteVFX(2103506, erase_root_only=True)
    DeleteVFX(2103507, erase_root_only=True)
    DeleteVFX(2103510, erase_root_only=True)
    DeleteVFX(2103511, erase_root_only=True)
    DeleteVFX(2103512, erase_root_only=True)
    DeleteVFX(2103513, erase_root_only=True)
    DeleteVFX(2103514, erase_root_only=True)
    DeleteVFX(2103515, erase_root_only=True)
    DeleteVFX(2103516, erase_root_only=True)
    DeleteVFX(2103517, erase_root_only=True)
    DeleteVFX(2103518, erase_root_only=True)
    DeleteVFX(2103519, erase_root_only=True)
    DeleteVFX(2103520, erase_root_only=True)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutscene(21000020, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    AwardAchievement(2)
    RunEvent(12100450)
    RunEvent(12100451)
    RunEvent(12100452)
    WaitFrames(1)
    IncrementNewGameCycle(1)
    EnableFlag(6604)
    EnableFlag(6601)
    EnableFlag(6603)
    EnableFlag(22)


def Event12100002():
    """ 12100002: Event 12100002 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 12101850)
    IfStandingOnCollision(-1, 2103601)
    IfStandingOnCollision(-1, 2103602)
    IfStandingOnCollision(-1, 2103603)
    IfStandingOnCollision(-1, 2103604)
    IfStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(5.0)
    EnableFlag(9180)
    WaitFrames(1)
    DeleteVFX(2103300, erase_root_only=True)
    DeleteVFX(2103500, erase_root_only=True)
    DeleteVFX(2103501, erase_root_only=True)
    DeleteVFX(2103502, erase_root_only=True)
    DeleteVFX(2103503, erase_root_only=True)
    DeleteVFX(2103504, erase_root_only=True)
    DeleteVFX(2103505, erase_root_only=True)
    DeleteVFX(2103506, erase_root_only=True)
    DeleteVFX(2103507, erase_root_only=True)
    GotoIfPlayerGender(Label.L0, Gender.Male)
    PlayCutscene(21000030, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(21001030, skippable=True, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(9180)
    AwardAchievement(3)
    RunEvent(12100450)
    RunEvent(12100451)
    RunEvent(12100452)
    WaitFrames(1)
    IncrementNewGameCycle(1)
    EnableFlag(6604)
    EnableFlag(6602)
    EnableFlag(6603)
    EnableFlag(23)


def Event12100010():
    """ 12100010: Event 12100010 """
    IfFlagOff(1, 9403)
    IfCharacterInsideRegion(1, PLAYER, region=2102100)
    IfConditionTrue(0, input_condition=1)
    DisableObject(2101010)
    EnableObject(2101011)
    DisableObject(2101020)
    EnableObject(2101021)
    DisableObject(2101030)
    EnableObject(2101031)


def Event12100020(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12100020: Event 12100020 """
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    SkipLinesIfEqual(1, left=arg_8_11, right=0)
    DisableFlag(arg_4_7)
    IfPlayerHasGood(0, arg_0_3, including_box=False)
    EnableFlag(arg_4_7)


def Event12100100(_, arg_0_3: int, arg_4_7: int):
    """ 12100100: Event 12100100 """
    IfFlagOff(1, 1003)
    IfFlagOn(1, 9462)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1002)


def Event12100101(_, arg_0_3: int, arg_4_7: int):
    """ 12100101: Event 12100101 """
    IfCharacterDead(0, 2100700)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1003)
    SaveRequest()


def Event12100110():
    """ 12100110: Event 12100110 """
    DisableFlag(72100105)
    DisableFlag(72100106)
    DisableFlag(72100107)
    DisableFlag(12100510)
    IfFlagOff(-1, 9401)
    IfPlayerInsightAmountEqual(-1, 0)
    GotoIfConditionTrue(Label.L9, input_condition=-1)
    EnableFlag(12100105)
    EnableFlag(9404)
    IfFlagOn(1, 13501800)
    IfFlagOff(1, 72100116)
    IfConditionTrue(-2, input_condition=1)
    IfFlagOn(2, 13601800)
    IfFlagOff(2, 72100117)
    IfFlagOn(-3, 1026)
    IfFlagOn(-3, 1027)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(-2, input_condition=2)
    EndIfConditionTrue(-2)
    EndIfFlagOn(1000)
    GotoIfFlagOn(Label.L0, 1001)
    EndIfFlagOn(1002)
    GotoIfFlagOn(Label.L4, 1003)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagOn(2, 100)
    DisableFlagRange((12100500, 12100509))
    EnableRandomFlagInRange((12100500, 12100509))
    SkipLinesIfFlagOff(1, 12105034)
    DisableFlagRange((12100501, 12100502))
    GotoIfFlagOn(Label.L1, 12100500)
    GotoIfFlagOn(Label.L2, 12100501)
    GotoIfFlagOn(Label.L3, 12100502)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Move(2100700, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9009, loop=True)
    Goto(Label.L8)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(12100510)
    Move(2100700, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9000, loop=True)
    Goto(Label.L8)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(12100510)
    SkipLinesIfFlagOn(2, 6600)
    DisableFlag(12100502)
    End()
    Move(2100700, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9000, loop=True)
    Goto(Label.L8)

    # --- 4 --- #
    DefineLabel(4)
    GotoIfFlagOn(Label.L5, 12100500)
    GotoIfFlagOn(Label.L6, 12100501)
    GotoIfFlagOn(Label.L7, 12100502)
    Move(2100700, destination=2102300, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 5 --- #
    DefineLabel(5)
    Move(2100700, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 6 --- #
    DefineLabel(6)
    Move(2100700, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 7 --- #
    DefineLabel(7)
    Move(2100700, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 8 --- #
    DefineLabel(8)
    RunEvent(12100111)
    End()

    # --- 9 --- #
    DefineLabel(9)
    Move(2100700, destination=2102304, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9011, loop=True)
    EnableFlag(12105100)


def Event12100111():
    """ 12100111: Event 12100111 """
    GotoIfFlagOn(Label.L0, 12100500)
    GotoIfFlagOn(Label.L1, 12100501)
    GotoIfFlagOn(Label.L1, 12100502)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(72100105)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagOff(9802)
    SkipLinesIfFlagOn(3, 102)
    DisableFlagRange((12100520, 12100524))
    EnableRandomFlagInRange((12100520, 12100524))
    EndIfFlagOff(12100520)
    EnableFlag(72100105)
    End()


def Event12100112():
    """ 12100112: Event 12100112 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 72100100)
    GotoIfFlagOn(Label.L0, 1003)
    GotoIfFlagOn(Label.L1, 12105100)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2100700, radius=1.0)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    RotateToFaceEntity(PLAYER, 2100700, animation=101290)
    IfCharacterHuman(2, PLAYER)
    IfEntityWithinDistance(2, PLAYER, 2100700, radius=1.0)
    IfConditionTrue(-1, input_condition=2)
    IfFramesElapsed(-1, 89)
    IfConditionTrue(0, input_condition=-1)

    # --- 2 --- #
    DefineLabel(2)
    RotateToFaceEntity(PLAYER, 2100700, animation=101270)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagOff(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(19)
    DisableFlag(72100101)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(3, PLAYER)
    IfEntityWithinDistance(3, PLAYER, 2100700, radius=1.5)
    GotoIfConditionTrue(Label.L3, input_condition=3)
    RotateToFaceEntity(PLAYER, 2100700, animation=101290)
    IfCharacterHuman(4, PLAYER)
    IfEntityWithinDistance(4, PLAYER, 2100700, radius=1.5)
    IfConditionTrue(-2, input_condition=4)
    IfFramesElapsed(-2, 89)
    IfConditionTrue(0, input_condition=-2)

    # --- 3 --- #
    DefineLabel(3)
    RotateToFaceEntity(PLAYER, 2100700, animation=101280)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagOff(0, 72100100)
    ForceAnimation(PLAYER, 101282)
    WaitFrames(25)
    DisableFlag(72100101)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHuman(5, PLAYER)
    IfEntityWithinDistance(5, PLAYER, 2100700, radius=2.0)
    GotoIfConditionTrue(Label.L4, input_condition=5)
    RotateToFaceEntity(PLAYER, 2100700, animation=101290)
    IfCharacterHuman(6, PLAYER)
    IfEntityWithinDistance(6, PLAYER, 2100700, radius=2.0)
    IfConditionTrue(0, input_condition=6)

    # --- 4 --- #
    DefineLabel(4)
    RotateToFaceEntity(PLAYER, 2100700, animation=101270)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagOff(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(19)
    DisableFlag(72100101)
    Restart()


def Event12100113():
    """ 12100113: Event 12100113 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(1)
    IfHealthEqual(-1, 2100700, 0.0)
    IfFlagOn(-1, 12105100)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    EnableFlag(72100102)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(0, 72100100)
    RotateToFaceEntity(2100700, PLAYER, animation=7021)
    WaitFrames(0)
    EnableFlag(72100102)
    WaitFrames(89)
    ForceAnimation(2100700, 9010, loop=True)
    IfFlagOff(0, 72100100)
    ForceAnimation(2100700, 7020)
    DisableFlag(72100102)
    WaitFrames(92)
    Restart()


def Event12100114():
    """ 12100114: Event 12100114 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 7500)
    CreateTemporaryVFX(178, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=1)
    DisableFlag(7500)
    Restart()


def Event12100115():
    """ 12100115: Event 12100115 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(2)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2100700, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    IfHealthEqual(-1, 2100700, 0.0)
    IfFlagOn(-1, 12105100)
    IfFlagOn(-1, 72100105)
    EndIfConditionTrue(-1)
    IfCharacterHasSpecialEffect(2, 2100700, 151)
    GotoIfConditionFalse(Label.L0, input_condition=2)
    RotateToFaceEntity(2100700, PLAYER, animation=7010)
    WaitFrames(89)
    IfCharacterHasSpecialEffect(3, 2100700, 152)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    RotateToFaceEntity(2100700, PLAYER, animation=7012)
    WaitFrames(0)

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)


def Event12100116():
    """ 12100116: Event 12100116 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 72100108)
    DisableFlag(72100108)
    IfCharacterHasSpecialEffect(1, 2100700, 151)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(2100700, PLAYER, animation=7011)
    WaitFrames(89)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(2, 2100700, 152)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    RotateToFaceEntity(2100700, PLAYER, animation=7013)
    WaitFrames(0)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHasSpecialEffect(3, 2100700, 153)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    RotateToFaceEntity(2100700, PLAYER, animation=7019)
    WaitFrames(89)

    # --- 2 --- #
    DefineLabel(2)
    Wait(0.0)


def Event12100117():
    """ 12100117: Event 12100117 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2100700, 160)
    IfFlagOn(1, 12100118)
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(2, PLAYER, 161)
    IfCharacterHasSpecialEffect(3, PLAYER, 162)
    IfCharacterHasSpecialEffect(4, PLAYER, 163)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    RotateToFaceEntity(2100700, PLAYER, animation=7001)
    WaitFrames(1)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    RotateToFaceEntity(2100700, PLAYER, animation=7000)
    WaitFrames(1)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(2100700, PLAYER, animation=7026)
    WaitFrames(39)
    RotateToFaceEntity(2100700, PLAYER, animation=7025)
    Restart()


def Event12100120():
    """ 12100120: Event 12100120 """
    EndIfThisEventOn()


def Event12100121():
    """ 12100121: Event 12100121 """
    IfPlayerHasGood(0, 4300, including_box=True)
    EnableFlag(12100122)
    IfPlayerDoesNotHaveGood(0, 4300, including_box=True)
    DisableFlag(12100122)
    Restart()


def Event12100123():
    """ 12100123: Event 12100123 """
    DisableNetworkSync()
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72100114)
    IfCharacterHasSpecialEffect(1, 2100700, 160)
    IfFlagOn(1, 72100114)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100700, 7030)
    IfFlagOn(0, 72100112)
    AwardItemLot(14000, host_only=False)
    RemoveGoodFromPlayer(4300, quantity=1)


def Event12100140(_, arg_0_3: int, arg_4_7: int):
    """ 12100140: Event 12100140 """
    IfFlagOn(1, 1020)
    IfFlagOn(1, 9403)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1021)


def Event12100141(_, arg_0_3: int, arg_4_7: int):
    """ 12100141: Event 12100141 """
    IfFlagOn(1, 1022)
    IfFlagOn(1, 9800)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1023)


def Event12100142(_, arg_0_3: int, arg_4_7: int):
    """ 12100142: Event 12100142 """
    IfFlagOn(1, 1024)
    IfFlagOn(-1, 12301800)
    IfFlagOn(-1, 9801)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1025)


def Event12100143(_, arg_0_3: int, arg_4_7: int):
    """ 12100143: Event 12100143 """
    IfFlagOff(1, 1029)
    IfFlagOff(1, 1030)
    IfFlagOn(1, 9462)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1028)


def Event12100144(_, arg_0_3: int, arg_4_7: int):
    """ 12100144: Event 12100144 """
    IfFlagOff(1, 1030)
    IfFlagOn(1, 12101802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1029)
    SaveRequest()


def Event12100145(_, arg_0_3: int, arg_4_7: int):
    """ 12100145: Event 12100145 """
    IfFlagOn(0, 12101800)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1030)
    SaveRequest()


def Event12100146():
    """ 12100146: Event 12100146 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    SetDistanceLimitForConversationStateChanges(2100800, distance=17.0)
    IfFlagOn(0, 1029)
    SetDistanceLimitForConversationStateChanges(2100800, distance=80.0)


def Event12100160():
    """ 12100160: Event 12100160 """
    DisableFlag(72100133)
    DisableFlag(72100134)
    DisableFlag(72100135)
    DisableFlagRange((12105800, 12105809))
    IfCharacterBackreadEnabled(0, 2100600)
    GotoIfFlagOn(Label.L0, 1020)
    GotoIfFlagOn(Label.L1, 1021)
    GotoIfFlagOn(Label.L0, 1022)
    GotoIfFlagOn(Label.L1, 1023)
    GotoIfFlagOn(Label.L0, 1024)
    GotoIfFlagOn(Label.L1, 1025)
    GotoIfFlagOn(Label.L0, 1026)
    GotoIfFlagOn(Label.L0, 1027)
    GotoIfFlagOn(Label.L2, 1028)
    GotoIfFlagOn(Label.L3, 1029)
    GotoIfFlagOn(Label.L3, 1030)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2100600)
    RunEvent(12100161)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Move(2100600, destination=2102310, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(2100600, 9002, loop=True)
    Move(2100600, destination=2102312, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(2100600)


def Event12100161():
    """ 12100161: Event 12100161 """
    IfFlagOn(1, 13601800)
    IfFlagOff(1, 72100117)
    EndIfConditionTrue(1)
    GotoIfFlagOn(Label.L1, 1027)
    GotoIfFlagOn(Label.L0, 1026)
    SkipLinesIfFlagOn(2, 100)
    EnableRandomFlagInRange((12105800, 12105804))
    EndIfFlagOff(12105800)
    EnableFlag(72100133)
    EnableCharacter(2100600)
    ForceAnimation(2100600, 9000, loop=True)
    Move(2100600, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagOn(2, 100)
    EnableRandomFlagInRange((12105800, 12105809))
    EndIfFlagOff(12105800)
    EnableFlag(72100133)
    EnableCharacter(2100600)
    ForceAnimation(2100600, 9000, loop=True)
    Move(2100600, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagOn(2, 100)
    EnableRandomFlagInRange((12105800, 12105809))
    EndIfFlagOff(12105800)
    EnableFlag(72100133)
    EnableCharacter(2100600)
    ForceAnimation(2100600, 9000, loop=True)
    Move(2100600, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)


def Event12100162():
    """ 12100162: Event 12100162 """
    GotoIfFlagOff(Label.L0, 9403)
    DisableObject(2101010)
    EnableObject(2101011)
    DisableObject(2101020)
    EnableObject(2101021)
    DisableObject(2101030)
    EnableObject(2101031)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101010)
    DisableObject(2101011)
    EnableObject(2101020)
    DisableObject(2101021)
    EnableObject(2101030)
    DisableObject(2101031)


@RestartOnRest
def Event12100163():
    """ 12100163: Event 12100163 """
    DisableFlag(12100163)
    IfFlagOff(1, 1028)
    IfFlagOff(1, 1029)
    IfFlagOff(1, 1030)
    IfHasTAEEvent(1, 2100600, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12100163)


def Event12100164():
    """ 12100164: Event 12100164 """
    DisableSoapstoneMessage(2103000)
    DisableSoapstoneMessage(2103001)
    SkipLinesIfFlagOff(2, 1024)
    SkipLinesIfFlagOn(1, 5000)
    EnableSoapstoneMessage(2103000)
    IfFlagOn(-1, 1026)
    IfFlagOn(-1, 1027)
    SkipLinesIfConditionFalse(2, -1)
    SkipLinesIfFlagOn(1, 52400480)
    EnableSoapstoneMessage(2103001)


def Event12100165():
    """ 12100165: Event 12100165 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72100136)
    IfFlagOn(0, 72100136)
    ForceAnimation(2100600, 7000)
    WaitFrames(129)
    ForceAnimation(2100600, 9003, loop=True)


def Event12100180():
    """ 12100180: Event 12100180 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(0, 72100130)
    EnableFlag(9180)
    WaitFrames(1)
    DeleteVFX(2103300, erase_root_only=True)
    DeleteVFX(2103500, erase_root_only=True)
    DeleteVFX(2103501, erase_root_only=True)
    DeleteVFX(2103502, erase_root_only=True)
    DeleteVFX(2103503, erase_root_only=True)
    DeleteVFX(2103504, erase_root_only=True)
    DeleteVFX(2103505, erase_root_only=True)
    DeleteVFX(2103506, erase_root_only=True)
    DeleteVFX(2103507, erase_root_only=True)
    IncrementNewGameCycle(1)
    GotoIfPlayerGender(Label.L0, Gender.Male)
    PlayCutscene(21000010, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(21001010, skippable=True, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(9180)
    AwardAchievement(1)
    EnableFlag(6604)
    RunEvent(12100450)
    RunEvent(12100451)
    RunEvent(12100452)
    WaitFrames(1)
    EnableFlag(21)
    EnableFlag(6600)
    EnableFlag(6603)


def Event12100300():
    """ 12100300: Event 12100300 """
    GotoIfFlagOn(Label.L5, 12101852)
    GotoIfFlagOn(Label.L4, 9462)
    GotoIfFlagOn(Label.L3, 9802)
    GotoIfFlagOn(Label.L2, 9801)
    GotoIfFlagOn(Label.L1, 9800)
    GotoIfFlagOff(Label.L0, 9800)

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101310)
    DisableObject(2101311)
    EnableObject(2101300)
    DisableObject(2101301)
    DeleteVFX(2103300, erase_root_only=False)
    DeleteVFX(2103500, erase_root_only=False)
    DeleteVFX(2103501, erase_root_only=False)
    DeleteVFX(2103502, erase_root_only=False)
    DeleteVFX(2103503, erase_root_only=False)
    DeleteVFX(2103504, erase_root_only=False)
    DeleteVFX(2103505, erase_root_only=False)
    DeleteVFX(2103506, erase_root_only=False)
    DeleteVFX(2103507, erase_root_only=False)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101310)
    DisableObject(2101311)
    EnableObject(2101300)
    DisableObject(2101301)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableObject(2101310)
    EnableObject(2101311)
    DisableObject(2101300)
    EnableObject(2101301)


def Event12100310():
    """ 12100310: Event 12100310 """
    GotoIfFlagOn(Label.L1, 9462)
    IfPlayerInsightAmountGreaterThanOrEqual(-1, 50)
    IfFlagOn(-1, 9802)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    EnableSoundEvent(2103900)
    DisableSoundEvent(2103901)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableSoundEvent(2103900)
    EnableSoundEvent(2103901)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableSoundEvent(2103900)
    DisableSoundEvent(2103901)


def Event12100330():
    """ 12100330: Event 12100330 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagOn(-1, 5051)
    IfFlagOn(-1, 6660)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(5051)
    EnableFlag(6660)


def Event12100350(_, arg_0_3: int, arg_4_7: int):
    """ 12100350: Event 12100350 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event12100400():
    """ 12100400: Event 12100400 """
    EndIfFlagOff(9462)
    EndOfAnimation(2101000, 1)


def Event12100410(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12100410: Event 12100410 """
    DisableNetworkSync()
    IfActionButtonParam(-1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagOn(-1, arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(arg_8_11)
    DisplayDialog(
        arg_12_15,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12100450():
    """ 12100450: Event 12100450 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerDoesNotHaveGood(1, 4103, including_box=False)
    SkipLinesIfConditionTrue(1, 1)
    EnableFlag(6630)
    IfPlayerDoesNotHaveGood(2, 4104, including_box=False)
    SkipLinesIfConditionTrue(1, 2)
    EnableFlag(6631)
    IfPlayerDoesNotHaveGood(3, 4105, including_box=False)
    SkipLinesIfConditionTrue(1, 3)
    EnableFlag(6632)
    IfPlayerDoesNotHaveGood(4, 4102, including_box=False)
    SkipLinesIfConditionTrue(1, 4)
    EnableFlag(6633)
    IfPlayerDoesNotHaveGood(5, 4110, including_box=False)
    SkipLinesIfConditionTrue(1, 5)
    EnableFlag(6640)
    IfPlayerDoesNotHaveGood(6, 4112, including_box=False)
    SkipLinesIfConditionTrue(1, 6)
    EnableFlag(6641)
    IfPlayerDoesNotHaveGood(7, 4113, including_box=False)
    SkipLinesIfConditionTrue(1, 7)
    EnableFlag(6642)
    IfPlayerDoesNotHaveGood(8, 4111, including_box=False)
    SkipLinesIfConditionTrue(1, 8)
    EnableFlag(6643)
    IfPlayerDoesNotHaveGood(9, 4118, including_box=False)
    SkipLinesIfConditionTrue(1, 9)
    EnableFlag(6644)
    IfPlayerDoesNotHaveGood(10, 4114, including_box=False)
    SkipLinesIfConditionTrue(1, 10)
    EnableFlag(6645)
    IfPlayerDoesNotHaveGood(11, 4115, including_box=False)
    SkipLinesIfConditionTrue(1, 11)
    EnableFlag(6646)
    IfPlayerDoesNotHaveGood(12, 4116, including_box=False)
    SkipLinesIfConditionTrue(1, 12)
    EnableFlag(6647)
    IfPlayerDoesNotHaveGood(13, 4119, including_box=False)
    SkipLinesIfConditionTrue(1, 13)
    EnableFlag(6648)
    IfPlayerDoesNotHaveGood(14, 4117, including_box=False)
    SkipLinesIfConditionTrue(1, 14)
    EnableFlag(6649)
    End()


def Event12100451():
    """ 12100451: Event 12100451 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 50000400)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6300)
    IfFlagOn(2, 50000600)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6301)
    IfFlagOn(3, 50000800)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6302)
    IfFlagOn(4, 50001100)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6303)
    IfFlagOn(5, 50001300)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6304)
    IfFlagOn(6, 50001610)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6305)
    IfFlagOn(7, 50002110)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6306)
    IfFlagOn(8, 50003400)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6307)
    IfFlagOn(9, 50003500)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6308)
    IfFlagOn(10, 52200380)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6309)
    IfFlagOn(11, 52420640)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6310)
    IfFlagOn(12, 52420690)
    SkipLinesIfConditionFalse(1, 12)
    EnableFlag(6311)
    IfFlagOn(13, 52410640)
    SkipLinesIfConditionFalse(1, 13)
    EnableFlag(6312)
    IfFlagOn(14, 52420120)
    SkipLinesIfConditionFalse(1, 14)
    EnableFlag(6313)
    IfFlagOn(15, 52600390)
    SkipLinesIfConditionFalse(1, 15)
    EnableFlag(6314)
    IfFlagOn(-1, 52600300)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6315)
    IfFlagOn(-2, 52700180)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6316)
    IfFlagOn(-3, 52700200)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6317)
    IfFlagOn(-4, 52700380)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6318)
    IfFlagOn(-5, 52700540)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6319)
    IfFlagOn(-6, 52700570)
    SkipLinesIfConditionFalse(1, -6)
    EnableFlag(6320)
    IfFlagOn(-7, 52700950)
    SkipLinesIfConditionFalse(1, -7)
    EnableFlag(6321)
    IfFlagOn(-8, 52800050)
    SkipLinesIfConditionFalse(1, -8)
    EnableFlag(6322)
    IfFlagOn(-9, 52800140)
    SkipLinesIfConditionFalse(1, -9)
    EnableFlag(6323)
    IfFlagOn(-10, 52800350)
    SkipLinesIfConditionFalse(1, -10)
    EnableFlag(6324)
    IfFlagOn(-11, 53200010)
    SkipLinesIfConditionFalse(1, -11)
    EnableFlag(6325)
    IfFlagOn(-12, 53200640)
    SkipLinesIfConditionFalse(1, -12)
    EnableFlag(6326)
    IfFlagOn(-13, 53300110)
    SkipLinesIfConditionFalse(1, -13)
    EnableFlag(6327)
    IfFlagOn(-14, 53300150)
    SkipLinesIfConditionFalse(1, -14)
    EnableFlag(6328)
    IfFlagOn(-15, 53300320)
    SkipLinesIfConditionFalse(1, -15)
    EnableFlag(6329)


def Event12100452():
    """ 12100452: Event 12100452 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 53300420)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6330)
    IfFlagOn(2, 53300480)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6331)
    IfFlagOn(3, 9458)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6332)
    IfFlagOn(4, 12400861)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6333)
    IfFlagOn(5, 50003100)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6334)
    IfFlagOn(6, 50001500)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6335)
    IfFlagOn(7, 52605000)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6336)
    IfFlagOn(8, 50000200)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6340)
    IfFlagOn(9, 50001820)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6341)
    IfFlagOn(10, 50001910)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6342)
    IfFlagOn(11, 50002260)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6677)


def Event12100990():
    """ 12100990: Event 12100990 """
    DisableNetworkSync()
    EndIfClient()
    EndIfThisEventOn()
    IfStandingOnCollision(0, 2103600)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 0, PlayLogMultiplayerType.HostOnly)


def Event12100800():
    """ 12100800: Event 12100800 """
    GotoIfFlagOff(Label.L0, 12101850)
    DisableCharacter(2100810)
    DisableCharacter(2100800)
    SkipLinesIfClient(2)
    DisableObject(2101800)
    DeleteVFX(2103800, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagOff(Label.L1, 12101852)
    DisableCharacter(2100800)
    End()

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagOff(Label.L2, 12101800)
    DisableCharacter(2100810)
    DisableCharacter(2100800)
    SkipLinesIfClient(2)
    DisableObject(2101800)
    DeleteVFX(2103800, erase_root_only=False)
    End()

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagOff(Label.L3, 12101802)
    DisableCharacter(2100810)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(2100810)
    DisableCharacter(2100800)
    SkipLinesIfClient(2)
    DisableObject(2101800)
    DeleteVFX(2103800, erase_root_only=False)


def Event12101800():
    """ 12101800: Event 12101800 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableSoundEvent(2103802)
    DisableSoundEvent(2103803)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(12104809)
    IfHealthEqual(0, 2100800, 0.0)
    EnableFlag(12104809)
    IfCharacterDead(1, 2100800)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFlagOn(2, 9900)
    KillBoss(2100800)
    SkipLines(1)
    HandleMinibossDefeat(2100800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    SkipLinesIfFlagOn(2, 6642)
    AwardItemLot(15000, host_only=False)
    SkipLines(1)
    AwardItemLot(15005, host_only=False)
    StopPlayLogMeasurement(2100000)
    StopPlayLogMeasurement(2100001)
    StopPlayLogMeasurement(2100010)
    CreatePlayLog(22)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 34, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def Event12101801():
    """ 12101801: Event 12101801 """
    DisableNetworkSync()
    EndIfFlagOn(12101800)
    IfFlagOn(1, 12101800)
    IfCharacterBackreadDisabled(2, 2100800)
    IfHealthLessThanOrEqual(2, 2100800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2102800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def Event12101802():
    """ 12101802: Event 12101802 """
    EndIfFlagOn(12101800)
    EndIfThisEventOn()
    DisableCharacter(2100800)
    DisableFlag(72100131)
    IfFlagOn(0, 72100131)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutscene(
        21000040,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=2102808,
        move_to_map=HUNTERS_DREAM,
    )
    WaitFrames(1)
    DisableFlag(9180)
    EnableCharacter(2100800)
    DisableCharacter(2100600)
    EnableFlag(12104800)
    DisableFlag(2100)
    EndIfFlagOn(9343)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9343)


def Event12101803():
    """ 12101803: Event 12101803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12104800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2100800)
    DisableCharacter(2100600)
    EnableFlag(12104800)
    EnableFlag(12101802)


def Event12104810():
    """ 12104810: Event 12104810 """
    EndIfFlagOn(12101800)
    GotoIfFlagOn(Label.L0, 12101802)
    IfFlagOff(1, 12101800)
    IfFlagOn(1, 12101802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2101800)
    CreateVFX(2103800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 12101800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=2100800, entity=2101800)
    IfFlagOn(3, 12101800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2102801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12104800)
    Restart()


def Event12104811():
    """ 12104811: Event 12104811 """
    DisableNetworkSync()
    EndIfFlagOn(12101800)
    IfFlagOff(1, 12101800)
    IfFlagOn(1, 12101802)
    IfFlagOn(1, 12104800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=2100800, entity=2101800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12104801)
    Restart()


def Event12104802():
    """ 12104802: Event 12104802 """
    EndIfFlagOn(12101800)
    DisableAI(2100800)
    DisableHealthBar(2100800)
    EnableInvincibility(2100800)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12104800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2100800, UpdateAuthority.Normal)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12104800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2100800, 7500, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2100800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2100800, 7501, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2100800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2100800)
    EnableBossHealthBar(2100800, name=804000, slot=0)
    DisableInvincibility(2100800)
    SetCharacterEventTarget(2100800, 2100801)
    CreatePlayLog(64)
    StartPlayLogMeasurement(2100010, 80, overwrite=True)


def Event12104803():
    """ 12104803: Event 12104803 """
    DisableNetworkSync()
    EndIfFlagOn(12101800)
    GotoIfThisEventOn(Label.L0)
    DisableSoundEvent(2103802)
    DisableSoundEvent(2103803)
    IfFlagOff(1, 12101800)
    IfFlagOn(1, 12104802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12104801)
    IfCharacterInsideRegion(1, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(2103900)
    DisableSoundEvent(2103901)
    EnableBossMusic(2103802)
    IfHasTAEEvent(2, 2100800, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 12101800)
    IfFlagOn(2, 12104802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12104801)
    IfCharacterInsideRegion(2, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2103802)
    WaitFrames(0)
    EnableBossMusic(2103803)


def Event12104804():
    """ 12104804: Event 12104804 """
    DisableNetworkSync()
    EndIfFlagOn(12101800)
    IfHealthGreaterThan(1, 2100800, 0.0)
    IfEntityWithinDistance(1, PLAYER, 2100800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, 2100800, 0.0)
    IfEntityBeyondDistance(2, PLAYER, 2100800, radius=10.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Restart()


def Event12104805():
    """ 12104805: Event 12104805 """
    DisableNetworkSync()
    EndIfFlagOn(12101800)
    IfFlagOn(0, 12104809)
    DisableBossMusic(2103802)
    DisableBossMusic(2103803)
    DisableBossMusic(-1)


def Event12104807():
    """ 12104807: Event 12104807 """
    EndIfFlagOn(12101800)
    IfHealthLessThan(0, 2100800, 0.5)
    AICommand(2100800, command_id=100, slot=0)
    IfHasTAEEvent(0, 2100800, tae_event_id=100)
    CancelSpecialEffect(2100800, 5305)
    AICommand(2100800, command_id=-1, slot=0)
    ReplanAI(2100800)
    Wait(0.10000000149011612)
    AICommand(2100800, command_id=1, slot=1)


def Event12104808():
    """ 12104808: Event 12104808 """
    EndIfFlagOn(12101800)
    IfHasTAEEvent(0, 2100800, tae_event_id=20)
    CancelSpecialEffect(2100800, 5526)
    Wait(0.10000000149011612)
    Restart()


def Event12101850():
    """ 12101850: Event 12101850 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableSoundEvent(2103812)
    DisableSoundEvent(2103813)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2100810)
    EnableFlag(12104859)
    DisplayBanner(BannerType.NightmareSlain)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Wait(3.0)
    KillBoss(2100810)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(5,))
    StopPlayLogMeasurement(2100011)
    CreatePlayLog(22)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 96, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def Event12101851():
    """ 12101851: Event 12101851 """
    DisableNetworkSync()
    EndIfFlagOn(12101850)
    IfFlagOn(1, 12101850)
    IfCharacterBackreadDisabled(2, 2100810)
    IfHealthLessThanOrEqual(2, 2100810, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2102800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def Event12101852():
    """ 12101852: Event 12101852 """
    EndIfFlagOn(12101850)
    EndIfThisEventOn()
    IfFlagOn(1, 12101800)
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 2103601)
    IfStandingOnCollision(-1, 2103602)
    IfStandingOnCollision(-1, 2103603)
    IfStandingOnCollision(-1, 2103604)
    IfStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 9900)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableFlag(9180)
    WaitFrames(1)
    DeleteVFX(2103510, erase_root_only=True)
    DeleteVFX(2103511, erase_root_only=True)
    DeleteVFX(2103512, erase_root_only=True)
    DeleteVFX(2103513, erase_root_only=True)
    DeleteVFX(2103514, erase_root_only=True)
    DeleteVFX(2103515, erase_root_only=True)
    DeleteVFX(2103516, erase_root_only=True)
    DeleteVFX(2103517, erase_root_only=True)
    DeleteVFX(2103518, erase_root_only=True)
    DeleteVFX(2103519, erase_root_only=True)
    DeleteVFX(2103520, erase_root_only=True)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        21000050,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=2102809,
        move_to_map=HUNTERS_DREAM,
    )
    SkipLines(1)
    PlayCutscene(
        21000050,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=2102809,
        move_to_map=HUNTERS_DREAM,
    )
    WaitFrames(1)
    DisableFlag(9180)
    CreateVFX(2103510)
    CreateVFX(2103511)
    CreateVFX(2103512)
    CreateVFX(2103513)
    CreateVFX(2103514)
    CreateVFX(2103515)
    CreateVFX(2103516)
    CreateVFX(2103517)
    CreateVFX(2103518)
    CreateVFX(2103519)
    CreateVFX(2103520)
    DisableObject(2101310)
    EnableObject(2101311)
    DisableObject(2101300)
    EnableObject(2101301)
    EnableCharacter(2100810)
    EnableFlag(12104850)
    EndIfFlagOn(9307)
    RunEvent(9350, slot=0, args=(5,))
    EnableFlag(9307)


def Event12101853():
    """ 12101853: Event 12101853 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12104850)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DisableObject(2101310)
    EnableObject(2101311)
    DisableObject(2101300)
    EnableObject(2101301)
    EnableCharacter(2100810)
    EnableFlag(12104850)
    EnableFlag(12101852)


def Event12104880():
    """ 12104880: Event 12104880 """
    EndIfFlagOn(12101850)
    GotoIfFlagOn(Label.L0, 12101852)
    IfFlagOff(1, 12101850)
    IfFlagOn(1, 12101852)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2101800)
    CreateVFX(2103800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 12101850)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=2100800, entity=2101800)
    IfFlagOn(3, 12101850)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2102801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12104850)
    Restart()


def Event12104881():
    """ 12104881: Event 12104881 """
    DisableNetworkSync()
    EndIfFlagOn(12101850)
    IfFlagOff(1, 12101850)
    IfFlagOn(1, 12101852)
    IfFlagOn(1, 12104850)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=2100800, entity=2101800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12104851)
    Restart()


def Event12104852():
    """ 12104852: Event 12104852 """
    EndIfFlagOn(12101850)
    DisableAI(2100810)
    DisableHealthBar(2100810)
    EnableInvincibility(2100810)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12104850)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2100810, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12104850)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2100810, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2100810)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2100810, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2100810)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2100810)
    EnableBossHealthBar(2100810, name=540000, slot=0)
    DisableInvincibility(2100810)
    CreatePlayLog(128)
    StartPlayLogMeasurement(2100011, 146, overwrite=True)


def Event12104853():
    """ 12104853: Event 12104853 """
    DisableNetworkSync()
    EndIfFlagOn(12101850)
    GotoIfThisEventOn(Label.L0)
    DisableSoundEvent(2103812)
    DisableSoundEvent(2103813)
    IfFlagOff(1, 12101850)
    IfFlagOn(1, 12101852)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12104851)
    IfCharacterInsideRegion(1, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(2103900)
    DisableSoundEvent(2103901)
    EnableBossMusic(2103812)
    IfHasTAEEvent(0, 2100810, tae_event_id=500)
    IfFlagOff(2, 12101850)
    IfFlagOn(2, 12101852)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12104851)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2103812)
    WaitFrames(0)
    EnableBossMusic(2103813)


def Event12104854():
    """ 12104854: Event 12104854 """
    DisableNetworkSync()
    EndIfFlagOn(12101850)
    IfHealthGreaterThan(1, 2100810, 0.0)
    IfEntityWithinDistance(1, PLAYER, 2100810, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, 2100810, 0.0)
    IfEntityBeyondDistance(2, PLAYER, 2100810, radius=12.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Restart()


def Event12104855():
    """ 12104855: Event 12104855 """
    DisableNetworkSync()
    EndIfFlagOn(12101850)
    IfFlagOn(0, 12104859)
    DisableBossMusic(2103812)
    DisableBossMusic(2103813)
    DisableBossMusic(-1)


def Event12104860(
    _,
    arg_0_1: short,
    arg_4_7: int,
    arg_8_9: short,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 12104860: Event 12104860 """
    EndIfFlagOn(12101850)
    CreateNPCPart(
        2100810,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(2100810, npc_part_id=arg_4_7, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, 2100810, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(3, 2100810, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(
        2100810,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(2100810, npc_part_id=arg_4_7, material_sfx_id=60, material_vfx_id=60)
    ResetAnimation(2100810, disable_interpolation=False)
    ForceAnimation(2100810, arg_24_27)
    AddSpecialEffect(2100810, arg_16_19, affect_npc_part_hp=False)
    CancelSpecialEffect(2100810, arg_20_23)
    ReplanAI(2100810)
    Wait(30.0)
    AICommand(2100810, command_id=10, slot=1)
    ReplanAI(2100810)
    IfHasTAEEvent(0, 2100810, tae_event_id=300)
    SetNPCPartHealth(2100810, npc_part_id=arg_4_7, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2100810, arg_20_23, affect_npc_part_hp=False)
    CancelSpecialEffect(2100810, arg_16_19)
    AICommand(2100810, command_id=-1, slot=1)
    ReplanAI(2100810)
    WaitFrames(10)
    Restart()


def Event12104870():
    """ 12104870: Event 12104870 """
    DisableNetworkSync()
    IfHasTAEEvent(0, 2100810, tae_event_id=10)
    EnableImmortality(PLAYER)
    IfCharacterHasSpecialEffect(-1, PLAYER, 5570)
    IfFramesElapsed(-1, 70)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(5)
    DisableImmortality(PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=PLAYER, attacker=2100810)
    IfTimeElapsed(-1, 10.0)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 5572)
    Restart()


@RestartOnRest
def Event12105000(_, arg_0_3: int, arg_4_7: int):
    """ 12105000: Event 12105000 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, arg_4_7)
    ForceAnimation(arg_0_3, 7000)
    WaitFrames(109)
    ForceAnimation(arg_0_3, 7001, loop=True)
    IfFlagOff(0, arg_4_7)
    ForceAnimation(arg_0_3, 7002)
    WaitFrames(74)
    Restart()


@RestartOnRest
def Event12105004(_, arg_0_3: int, arg_4_7: int):
    """ 12105004: Event 12105004 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, arg_4_7)
    Move(arg_0_3, destination=2102305, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(arg_0_3, 5401, affect_npc_part_hp=False)
    ForceAnimation(arg_0_3, 7000)
    WaitFrames(109)
    ForceAnimation(arg_0_3, 7001, loop=True)
    IfFlagOff(0, arg_4_7)
    ForceAnimation(arg_0_3, 7002)
    WaitFrames(74)
    Restart()


@RestartOnRest
def Event12105010():
    """ 12105010: Event 12105010 """
    DisableObject(2101200)
    DisableObject(2101201)
    DisableObject(2101202)
    DisableObject(2101203)
    DisableObject(2101204)
    DisableObject(2101205)
    DisableObject(2101206)
    DisableObject(2101207)
    DisableObject(2101208)
    IfFlagOn(10, 94005500)
    IfFlagRangeAnyOn(10, (94005100, 94005101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94005500)
    IfFlagRangeAnyOn(11, (94005103, 94005104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94005500)
    IfFlagOn(12, 94005102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94005503)
    GotoIfFlagOn(Label.L4, 94005504)
    GotoIfFlagOn(Label.L5, 94005505)
    GotoIfFlagOn(Label.L6, 94005502)
    GotoIfFlagOn(Label.L7, 94005507)
    GotoIfFlagOn(Label.L8, 94005501)
    IfFlagOn(1, 94005500)
    IfFlagRangeAnyOn(1, (94005100, 94005101))
    IfFlagOn(2, 94005500)
    IfFlagRangeAnyOn(2, (94005103, 94005104))
    IfFlagOn(3, 94005500)
    IfFlagOn(3, 94005102)
    IfFlagOn(4, 94005503)
    IfFlagOn(5, 94005504)
    IfFlagOn(6, 94005505)
    IfFlagOn(7, 94005502)
    IfFlagOn(8, 94005507)
    IfFlagOn(9, 94005501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(350, anchor_entity=2100954, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101200)
    IfFlagOff(0, 94005500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101201)
    IfFlagOff(0, 94005500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101202)
    IfFlagOff(0, 94005500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101203)
    IfFlagOff(0, 94005503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101204)
    IfFlagOff(0, 94005504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101205)
    IfFlagOff(0, 94005505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101206)
    IfFlagOff(0, 94005502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101207)
    IfFlagOff(0, 94005507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101208)
    IfFlagOff(0, 94005501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(351, anchor_entity=2100954, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def Event12105011():
    """ 12105011: Event 12105011 """
    DisableObject(2101210)
    DisableObject(2101211)
    DisableObject(2101212)
    DisableObject(2101213)
    DisableObject(2101214)
    DisableObject(2101215)
    DisableObject(2101216)
    DisableObject(2101217)
    DisableObject(2101218)
    IfFlagOn(10, 94105500)
    IfFlagRangeAnyOn(10, (94105100, 94105101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94105500)
    IfFlagRangeAnyOn(11, (94105103, 94105104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94105500)
    IfFlagOn(12, 94105102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94105503)
    GotoIfFlagOn(Label.L4, 94105504)
    GotoIfFlagOn(Label.L5, 94105505)
    GotoIfFlagOn(Label.L6, 94105502)
    GotoIfFlagOn(Label.L7, 94105507)
    GotoIfFlagOn(Label.L8, 94105501)
    IfFlagOn(1, 94105500)
    IfFlagRangeAnyOn(1, (94105100, 94105101))
    IfFlagOn(2, 94105500)
    IfFlagRangeAnyOn(2, (94105103, 94105104))
    IfFlagOn(3, 94105500)
    IfFlagOn(3, 94105102)
    IfFlagOn(4, 94105503)
    IfFlagOn(5, 94105504)
    IfFlagOn(6, 94105505)
    IfFlagOn(7, 94105502)
    IfFlagOn(8, 94105507)
    IfFlagOn(9, 94105501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(350, anchor_entity=2100955, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101210)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101211)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101212)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101213)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101214)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101215)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101216)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101217)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101218)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(351, anchor_entity=2100955, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def Event12105012():
    """ 12105012: Event 12105012 """
    DisableObject(2101220)
    DisableObject(2101221)
    DisableObject(2101222)
    DisableObject(2101223)
    DisableObject(2101224)
    DisableObject(2101225)
    DisableObject(2101226)
    DisableObject(2101227)
    DisableObject(2101228)
    IfFlagOn(10, 94205500)
    IfFlagRangeAnyOn(10, (94205100, 94205101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94205500)
    IfFlagRangeAnyOn(11, (94205103, 94205104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94205500)
    IfFlagOn(12, 94205102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94205503)
    GotoIfFlagOn(Label.L4, 94205504)
    GotoIfFlagOn(Label.L5, 94205505)
    GotoIfFlagOn(Label.L6, 94205502)
    GotoIfFlagOn(Label.L7, 94205507)
    GotoIfFlagOn(Label.L8, 94205501)
    IfFlagOn(1, 94205500)
    IfFlagRangeAnyOn(1, (94205100, 94205101))
    IfFlagOn(2, 94205500)
    IfFlagRangeAnyOn(2, (94205103, 94205104))
    IfFlagOn(3, 94205500)
    IfFlagOn(3, 94205102)
    IfFlagOn(4, 94205503)
    IfFlagOn(5, 94205504)
    IfFlagOn(6, 94205505)
    IfFlagOn(7, 94205502)
    IfFlagOn(8, 94205507)
    IfFlagOn(9, 94205501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(350, anchor_entity=2100956, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101220)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101221)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101222)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101223)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101224)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101225)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101226)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101227)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101228)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(351, anchor_entity=2100956, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def Event12105013():
    """ 12105013: Event 12105013 """
    DisableObject(2101230)
    DisableObject(2101231)
    DisableObject(2101232)
    DisableObject(2101233)
    DisableObject(2101234)
    DisableObject(2101235)
    DisableObject(2101236)
    DisableObject(2101237)
    DisableObject(2101238)
    IfFlagOn(10, 94305500)
    IfFlagRangeAnyOn(10, (94305100, 94305101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94305500)
    IfFlagRangeAnyOn(11, (94305103, 94305104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94305500)
    IfFlagOn(12, 94305102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94305503)
    GotoIfFlagOn(Label.L4, 94305504)
    GotoIfFlagOn(Label.L5, 94305505)
    GotoIfFlagOn(Label.L6, 94305502)
    GotoIfFlagOn(Label.L7, 94305507)
    GotoIfFlagOn(Label.L8, 94305501)
    IfFlagOn(1, 94305500)
    IfFlagRangeAnyOn(1, (94305100, 94305101))
    IfFlagOn(2, 94305500)
    IfFlagRangeAnyOn(2, (94305103, 94305104))
    IfFlagOn(3, 94305500)
    IfFlagOn(3, 94305102)
    IfFlagOn(4, 94305503)
    IfFlagOn(5, 94305504)
    IfFlagOn(6, 94305505)
    IfFlagOn(7, 94305502)
    IfFlagOn(8, 94305507)
    IfFlagOn(9, 94305501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(350, anchor_entity=2100957, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101230)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101231)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101232)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101233)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101234)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101235)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101236)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101237)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101238)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(351, anchor_entity=2100957, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def Event12105014():
    """ 12105014: Event 12105014 """
    DisableObject(2101240)
    DisableObject(2101241)
    DisableObject(2101242)
    DisableObject(2101243)
    DisableObject(2101244)
    DisableObject(2101245)
    DisableObject(2101246)
    DisableObject(2101247)
    DisableObject(2101248)
    IfFlagOn(10, 94405500)
    IfFlagRangeAnyOn(10, (94405100, 94405101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94405500)
    IfFlagRangeAnyOn(11, (94405103, 94405104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94405500)
    IfFlagOn(12, 94405102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94405503)
    GotoIfFlagOn(Label.L4, 94405504)
    GotoIfFlagOn(Label.L5, 94405505)
    GotoIfFlagOn(Label.L6, 94405502)
    GotoIfFlagOn(Label.L7, 94405507)
    GotoIfFlagOn(Label.L8, 94405501)
    IfFlagOn(1, 94405500)
    IfFlagRangeAnyOn(1, (94405100, 94405101))
    IfFlagOn(2, 94405500)
    IfFlagRangeAnyOn(2, (94405103, 94405104))
    IfFlagOn(3, 94405500)
    IfFlagOn(3, 94405102)
    IfFlagOn(4, 94405503)
    IfFlagOn(5, 94405504)
    IfFlagOn(6, 94405505)
    IfFlagOn(7, 94405502)
    IfFlagOn(8, 94405507)
    IfFlagOn(9, 94405501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(350, anchor_entity=2100958, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101240)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101241)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101242)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101243)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101244)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101245)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101246)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101247)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101248)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(351, anchor_entity=2100958, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def Event12105015():
    """ 12105015: Event 12105015 """
    DisableObject(2101250)
    DisableObject(2101251)
    DisableObject(2101252)
    DisableObject(2101253)
    DisableObject(2101254)
    DisableObject(2101255)
    DisableObject(2101256)
    DisableObject(2101257)
    DisableObject(2101258)
    IfFlagOn(10, 94505500)
    IfFlagRangeAnyOn(10, (94505100, 94505101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94505500)
    IfFlagRangeAnyOn(11, (94505103, 94505104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94505500)
    IfFlagOn(12, 94505102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94505503)
    GotoIfFlagOn(Label.L4, 94505504)
    GotoIfFlagOn(Label.L5, 94505505)
    GotoIfFlagOn(Label.L6, 94505502)
    GotoIfFlagOn(Label.L7, 94505507)
    GotoIfFlagOn(Label.L8, 94505501)
    IfFlagOn(1, 94505500)
    IfFlagRangeAnyOn(1, (94505100, 94505101))
    IfFlagOn(2, 94505500)
    IfFlagRangeAnyOn(2, (94505103, 94505104))
    IfFlagOn(3, 94505500)
    IfFlagOn(3, 94505102)
    IfFlagOn(4, 94505503)
    IfFlagOn(5, 94505504)
    IfFlagOn(6, 94505505)
    IfFlagOn(7, 94505502)
    IfFlagOn(8, 94505507)
    IfFlagOn(9, 94505501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(350, anchor_entity=2100959, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101250)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101251)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101252)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101253)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101254)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101255)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101256)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101257)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101258)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(351, anchor_entity=2100959, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def Event12105016():
    """ 12105016: Event 12105016 """
    DisableObject(2101260)
    DisableObject(2101261)
    DisableObject(2101262)
    DisableObject(2101263)
    DisableObject(2101264)
    DisableObject(2101265)
    DisableObject(2101266)
    DisableObject(2101267)
    DisableObject(2101268)
    IfFlagOn(10, 94605500)
    IfFlagRangeAnyOn(10, (94605100, 94605101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94605500)
    IfFlagRangeAnyOn(11, (94605103, 94605104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94605500)
    IfFlagOn(12, 94605102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94605503)
    GotoIfFlagOn(Label.L4, 94605504)
    GotoIfFlagOn(Label.L5, 94605505)
    GotoIfFlagOn(Label.L6, 94605502)
    GotoIfFlagOn(Label.L7, 94605507)
    GotoIfFlagOn(Label.L8, 94605501)
    IfFlagOn(1, 94605500)
    IfFlagRangeAnyOn(1, (94605100, 94605101))
    IfFlagOn(2, 94605500)
    IfFlagRangeAnyOn(2, (94605103, 94605104))
    IfFlagOn(3, 94605500)
    IfFlagOn(3, 94605102)
    IfFlagOn(4, 94605503)
    IfFlagOn(5, 94605504)
    IfFlagOn(6, 94605505)
    IfFlagOn(7, 94605502)
    IfFlagOn(8, 94605507)
    IfFlagOn(9, 94605501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(350, anchor_entity=2100960, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101260)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101261)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101262)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101263)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101264)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101265)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101266)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101267)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101268)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(351, anchor_entity=2100960, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def Event12105020():
    """ 12105020: Event 12105020 """
    IfFlagOn(-1, 12417810)
    IfFlagOn(-1, 12417830)
    IfFlagOn(-1, 12417850)
    IfFlagOn(-1, 12417870)
    IfFlagOn(-1, 12407810)
    IfFlagOn(-1, 12407830)
    IfFlagOn(-1, 12427810)
    IfFlagOn(-1, 12427830)
    IfFlagOn(-1, 12427850)
    IfFlagOn(-1, 12307810)
    IfFlagOn(-1, 12307830)
    IfFlagOn(-1, 12307850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105030)
    IfFlagOn(-2, 12417810)
    IfFlagOn(-2, 12417830)
    IfFlagOn(-2, 12417850)
    IfFlagOn(-2, 12417870)
    IfFlagOn(-2, 12407810)
    IfFlagOn(-2, 12407830)
    IfFlagOn(-2, 12427810)
    IfFlagOn(-2, 12427830)
    IfFlagOn(-2, 12427850)
    IfFlagOn(-2, 12307810)
    IfFlagOn(-2, 12307830)
    IfFlagOn(-2, 12307850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105030)
    Restart()


@RestartOnRest
def Event12105021():
    """ 12105021: Event 12105021 """
    IfFlagOn(-1, 12207810)
    IfFlagOn(-1, 12207830)
    IfFlagOn(-1, 12707810)
    IfFlagOn(-1, 12707830)
    IfFlagOn(-1, 13207810)
    IfFlagOn(-1, 13207850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105031)
    IfFlagOn(-2, 12207810)
    IfFlagOn(-2, 12207830)
    IfFlagOn(-2, 12707810)
    IfFlagOn(-2, 12707830)
    IfFlagOn(-2, 13207810)
    IfFlagOn(-2, 13207850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105031)
    Restart()


@RestartOnRest
def Event12105022():
    """ 12105022: Event 12105022 """
    IfFlagOn(-1, 12807810)
    IfFlagOn(-1, 12807830)
    IfFlagOn(-1, 12807850)
    IfFlagOn(-1, 12807870)
    IfFlagOn(-1, 12507810)
    IfFlagOn(-1, 12507830)
    IfFlagOn(-1, 12507850)
    IfFlagOn(-1, 12117810)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105032)
    IfFlagOn(-2, 12807810)
    IfFlagOn(-2, 12807830)
    IfFlagOn(-2, 12807850)
    IfFlagOn(-2, 12807870)
    IfFlagOn(-2, 12507810)
    IfFlagOn(-2, 12507830)
    IfFlagOn(-2, 12507850)
    IfFlagOn(-2, 12117810)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105032)
    Restart()


@RestartOnRest
def Event12105023():
    """ 12105023: Event 12105023 """
    IfFlagOn(-1, 13207830)
    IfFlagOn(-1, 13207870)
    IfFlagOn(-1, 13307810)
    IfFlagOn(-1, 13307830)
    IfFlagOn(-1, 12607810)
    IfFlagOn(-1, 12607830)
    IfFlagOn(-1, 12607850)
    IfFlagOn(-1, 12607870)
    IfFlagOn(-1, 13307810)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105033)
    IfFlagOn(-2, 13207830)
    IfFlagOn(-2, 13207870)
    IfFlagOn(-2, 13307810)
    IfFlagOn(-2, 13307830)
    IfFlagOn(-2, 12607810)
    IfFlagOn(-2, 12607830)
    IfFlagOn(-2, 12607850)
    IfFlagOn(-2, 12607870)
    IfFlagOn(-2, 13307810)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105033)
    Restart()


@RestartOnRest
def Event12105024():
    """ 12105024: Event 12105024 """
    IfFlagOn(-1, 13407810)
    IfFlagOn(-1, 13407830)
    IfFlagOn(-1, 13407850)
    IfFlagOn(-1, 13407870)
    IfFlagOn(-1, 13507810)
    IfFlagOn(-1, 13507830)
    IfFlagOn(-1, 13507850)
    IfFlagOn(-1, 13607810)
    IfFlagOn(-1, 13607830)
    IfFlagOn(-1, 13607850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105034)
    IfFlagOn(-2, 13407810)
    IfFlagOn(-2, 13407830)
    IfFlagOn(-2, 13407850)
    IfFlagOn(-2, 13407870)
    IfFlagOn(-2, 13507810)
    IfFlagOn(-2, 13507830)
    IfFlagOn(-2, 13507850)
    IfFlagOn(-2, 13607810)
    IfFlagOn(-2, 13607830)
    IfFlagOn(-2, 13607850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105034)
    Restart()


@RestartOnRest
def Event12105040():
    """ 12105040: Event 12105040 """
    ForceAnimation(2100211, 7001, loop=True)
    ForceAnimation(2100212, 7002, loop=True)
    ForceAnimation(2100213, 7041, loop=True)
    IfFlagOn(0, 12105041)
    ForceAnimation(2100211, 7005)
    ForceAnimation(2100212, 7006)
    ForceAnimation(2100213, 7045)
    WaitFrames(29)
    ForceAnimation(2100211, 7003, loop=True)
    ForceAnimation(2100212, 7004, loop=True)
    ForceAnimation(2100213, 7043, loop=True)
    IfFlagOff(0, 12105041)
    ForceAnimation(2100211, 7007)
    ForceAnimation(2100212, 7008)
    ForceAnimation(2100213, 7047)
    WaitFrames(28)
    Restart()


def Event12101000(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """ 12101000: Event 12101000 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, arg_4_7)
    SetDisplayMask(arg_4_7, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(arg_4_7, bit_index=arg_9_9, switch_type=OnOffChange.On)
    IfPlayerHasGood(0, arg_0_3, including_box=False)
    SetDisplayMask(arg_4_7, bit_index=arg_8_8, switch_type=OnOffChange.Off)
    SetDisplayMask(arg_4_7, bit_index=arg_9_9, switch_type=OnOffChange.Off)


def Event12101010():
    """ 12101010: Event 12101010 """
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    SkipLinesIfFlagOff(1, 9800)
    EnableFlag(5900)
    SkipLinesIfFlagOff(1, 9801)
    EnableFlag(5901)
    SkipLinesIfFlagOff(1, 9802)
    EnableFlag(5902)
    SkipLinesIfFlagOff(1, 12801800)
    EnableFlag(5903)
    SkipLinesIfFlagOff(1, 12601800)
    EnableFlag(5904)
    SkipLinesIfFlagOff(1, 6603)
    EnableFlagRange((5900, 5904))


@RestartOnRest
def Event12105043():
    """ 12105043: Event 12105043 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 12100320)
    ForceAnimation(2100219, 7030, loop=True)
    EndIfClient()
    IfPlayerInsightAmountGreaterThanOrEqual(0, 1)
    EnableFlag(12100320)
    ForceAnimation(2100219, 7031)
    WaitFrames(30)
    EnableFlag(12105045)
    WaitFrames(79)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12105045)
    ForceAnimation(2100219, 7032, loop=True)
    IfFlagOn(0, 12105044)
    ForceAnimation(2100219, 7034)
    WaitFrames(29)
    ForceAnimation(2100219, 7035, loop=True)
    IfFlagOff(0, 12105044)
    ForceAnimation(2100219, 7036)
    WaitFrames(28)
    Restart()


def Event12101020():
    """ 12101020: Event 12101020 """
    GotoIfThisEventOn(Label.L0)
    ForceAnimation(2100215, 7013, loop=True)
    ForceAnimation(2100220, 7013, loop=True)
    IfCharacterBackreadEnabled(1, 2100215)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2100215, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100215, 7014)
    ForceAnimation(2100220, 7014)
    WaitFrames(30)
    EnableFlag(12105050)
    WaitFrames(79)
    ForceAnimation(2100215, 7011, loop=True)
    ForceAnimation(2100220, 7011, loop=True)
    IfFlagOn(-1, 72101000)
    IfFlagOn(-1, 72101001)
    IfFlagOn(-1, 72101002)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(12105050)
    EnableFlag(12101020)
    ForceAnimation(2100215, 7012)
    ForceAnimation(2100220, 7012)
    WaitFrames(49)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2100215)
    DisableBackread(2100220)


def Event12101021():
    """ 12101021: Event 12101021 """
    GotoIfThisEventOn(Label.L0)
    ForceAnimation(2100216, 7023, loop=True)
    ForceAnimation(2100221, 7023, loop=True)
    IfCharacterBackreadEnabled(1, 2100216)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2100216, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100216, 7024)
    ForceAnimation(2100221, 7024)
    WaitFrames(30)
    EnableFlag(12105051)
    WaitFrames(79)
    ForceAnimation(2100216, 7021, loop=True)
    ForceAnimation(2100221, 7021, loop=True)
    IfFlagOn(-1, 72101010)
    IfFlagOn(-1, 72101011)
    IfConditionTrue(0, input_condition=-1)
    EventValueOperation(
        source_flag=12104010,
        source_flag_bit_count=8,
        operand=10,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    StoreItemAmountSpecifiedByFlagValue(ItemType.Good, 900, flag=12104020, bit_count=8)
    EventValueOperation(
        source_flag=12104010,
        source_flag_bit_count=8,
        operand=0,
        target_flag=12104020,
        target_flag_bit_count=8,
        calculation_type=CalculationType.Subtract,
    )
    IfEventValueEqual(0, 0, bit_count=1, value=0)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    GivePlayerItemAmountSpecifiedByFlagValue(ItemType.Good, 900, flag=12104010, bit_count=8)
    DisableFlag(12105051)
    EnableFlag(12101021)
    ForceAnimation(2100216, 7022)
    ForceAnimation(2100221, 7022)
    WaitFrames(49)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2100216)
    DisableBackread(2100221)


def Event12101022():
    """ 12101022: Event 12101022 """
    GotoIfFlagOn(Label.L0, 6620)
    ForceAnimation(2100230, 7053, loop=True)
    IfCharacterBackreadEnabled(1, 2100230)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2100230, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100230, 7054)
    WaitFrames(30)
    EnableFlag(12105052)
    WaitFrames(79)
    ForceAnimation(2100230, 7051, loop=True)
    IfFlagOn(0, 12101023)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10000, host_only=False)
    DisableFlag(12105052)
    ForceAnimation(2100230, 7052)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100230, 7053, loop=True)


def Event12101024():
    """ 12101024: Event 12101024 """
    GotoIfFlagOn(Label.L0, 6622)
    ForceAnimation(2100231, 7053, loop=True)
    IfCharacterBackreadEnabled(1, 2100231)
    IfFlagOn(1, 12100105)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100231, 7054)
    WaitFrames(30)
    EnableFlag(12105054)
    WaitFrames(79)
    ForceAnimation(2100231, 7051, loop=True)
    IfFlagOn(0, 12101025)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10010, host_only=False)
    DisableFlag(12105054)
    ForceAnimation(2100231, 7052)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100231, 7053, loop=True)


def Event12101026():
    """ 12101026: Event 12101026 """
    GotoIfFlagOn(Label.L0, 6670)
    IfCharacterBackreadEnabled(1, 2100230)
    IfFlagOn(1, 12101022)
    IfFlagOn(1, 12100105)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    ForceAnimation(2100230, 7054)
    WaitFrames(30)
    EnableFlag(12105056)
    WaitFrames(79)
    ForceAnimation(2100230, 7051, loop=True)
    IfFlagOn(0, 12101027)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10050, host_only=False)
    DisableFlag(12105056)
    ForceAnimation(2100230, 7052)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100230, 7053, loop=True)


def Event12101028():
    """ 12101028: Event 12101028 """
    GotoIfFlagOn(Label.L0, 50000100)
    IfCharacterBackreadEnabled(1, 2100231)
    IfFlagOn(1, 12101024)
    IfFlagOn(1, 9801)
    IfFlagOn(1, 6899)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    ForceAnimation(2100231, 7054)
    WaitFrames(30)
    EnableFlag(12105058)
    WaitFrames(79)
    ForceAnimation(2100231, 7051, loop=True)
    IfFlagOn(0, 12101029)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10040, host_only=False)
    DisableFlag(12105058)
    ForceAnimation(2100231, 7052)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100231, 7053, loop=True)


def Event12101100():
    """ 12101100: Event 12101100 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 6899)
    IfFlagOn(1, 9801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12101101)


@RestartOnRest
def Event12105060():
    """ 12105060: Event 12105060 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(12105061)
    IfFlagOn(0, 72100140)
    EnableFlag(12105061)
    DisableFlag(72100140)
    DisableFlagRange((6011, 6025))
    RotateToFaceEntity(PLAYER, 2100218, animation=101310)
    Wait(1.0)
    ForceAnimation(2100218, 7003)
    WaitFrames(39)
    SetDisplayMask(2100218, bit_index=20, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=23, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=26, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=27, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=28, switch_type=OnOffChange.On)
    ForceAnimation(2100218, 7004)
    WaitFrames(49)
    ForceAnimation(2100218, 7001, loop=True)
    Restart()


def Event12105062():
    """ 12105062: Event 12105062 """
    DisableNetworkSync()
    GotoIfFlagOn(Label.L0, 12105063)
    ForceAnimation(2100218, 0, loop=True)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    SkipLinesIfFlagOff(1, 6011)
    SetDisplayMask(2100218, bit_index=20, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6012)
    SetDisplayMask(2100218, bit_index=21, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6013)
    SetDisplayMask(2100218, bit_index=22, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6014)
    SetDisplayMask(2100218, bit_index=23, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6015)
    SetDisplayMask(2100218, bit_index=24, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6016)
    SetDisplayMask(2100218, bit_index=25, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6017)
    SetDisplayMask(2100218, bit_index=26, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6018)
    SetDisplayMask(2100218, bit_index=27, switch_type=OnOffChange.Off)
    SkipLinesIfFlagOff(1, 6019)
    SetDisplayMask(2100218, bit_index=28, switch_type=OnOffChange.Off)
    IfFlagOn(-1, 6071)
    IfFlagOn(-1, 6072)
    IfFlagOn(-1, 6073)
    IfFlagOn(-1, 6074)
    IfFlagOn(-1, 6075)
    IfFlagOn(-1, 6076)
    IfFlagOn(-1, 6077)
    IfFlagOn(-1, 6078)
    IfFlagOn(-1, 6079)
    IfFlagOn(-1, 6080)
    IfFlagOn(-1, 6081)
    IfFlagOn(-1, 6082)
    IfFlagOn(-1, 6083)
    IfFlagOn(-1, 6084)
    IfFlagOn(-1, 6085)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(2100218, 7004)
    WaitFrames(89)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100218, 7001, loop=True)
    IfCharacterHuman(14, PLAYER)
    EndIfConditionFalse(14)
    EnableFlag(12105063)
    IfFlagOn(-1, 6071)
    IfFlagOn(-1, 6072)
    IfFlagOn(-1, 6073)
    IfFlagOn(-1, 6074)
    IfFlagOn(-1, 6075)
    IfFlagOn(-1, 6076)
    IfFlagOn(-1, 6077)
    IfFlagOn(-1, 6078)
    IfFlagOn(-1, 6079)
    IfFlagOn(-1, 6080)
    IfFlagOn(-1, 6081)
    IfFlagOn(-1, 6082)
    IfFlagOn(-1, 6083)
    IfFlagOn(-1, 6084)
    IfFlagOn(-1, 6085)
    IfConditionFalse(0, input_condition=-1)
    DisableFlag(12105063)
    ForceAnimation(2100218, 7003)
    WaitFrames(39)
    Restart()


def Event12105064():
    """ 12105064: Event 12105064 """
    DisableNetworkSync()
    ForceAnimation(2100232, 7053, loop=True)
    EndIfClient()
    IfFlagOn(1, 6900)
    IfFlagOff(1, 6071)
    IfFlagOn(2, 6901)
    IfFlagOff(2, 6072)
    IfFlagOn(3, 6902)
    IfFlagOff(3, 6073)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(2100232, 7054)
    WaitFrames(30)
    WaitFrames(79)
    ForceAnimation(2100232, 7051, loop=True)
    IfCharacterHuman(4, PLAYER)
    IfActionButtonParam(4, action_button_id=6025, entity=2100232)
    IfConditionTrue(0, input_condition=4)
    SkipLinesIfFlagOn(3, 6071)
    SkipLinesIfFlagOff(2, 6900)
    AwardItemLot(2100900, host_only=False)
    EnableFlag(6071)
    SkipLinesIfFlagOn(3, 6072)
    SkipLinesIfFlagOff(2, 6901)
    AwardItemLot(2100910, host_only=False)
    EnableFlag(6072)
    SkipLinesIfFlagOn(3, 6073)
    SkipLinesIfFlagOff(2, 6902)
    AwardItemLot(2100920, host_only=False)
    EnableFlag(6073)
    ForceAnimation(2100232, 7052)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2100232)


@RestartOnRest
def Event12105070(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar):
    """ 12105070: Event 12105070 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(12105061)
    IfFlagOn(0, arg_0_3)
    EnableFlag(12105061)
    DisableFlag(arg_0_3)
    DisableFlagRange((6011, 6025))
    RotateToFaceEntity(PLAYER, 2100218, animation=101310)
    Wait(1.0)
    ForceAnimation(2100218, 7003)
    WaitFrames(39)
    EnableFlag(arg_4_7)
    SetDisplayMask(2100218, bit_index=20, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=23, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=26, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=27, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=28, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=arg_8_8, switch_type=OnOffChange.Off)
    ForceAnimation(2100218, 7004)
    WaitFrames(49)
    ForceAnimation(2100218, 7001, loop=True)
    Restart()


def Event12105200():
    """ 12105200: Event 12105200 """
    DisableFlag(12105200)
    IfCharacterHasSpecialEffect(0, 2100700, 153)
    WaitFrames(1)


def Event12105210():
    """ 12105210: Event 12105210 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 70000100)
    DisableFlag(70000100)
    CancelSpecialEffect(PLAYER, 2200)
    CancelSpecialEffect(PLAYER, 2210)
    CancelSpecialEffect(PLAYER, 2220)
    Restart()


def Event12105300():
    """ 12105300: Event 12105300 """
    DisableNetworkSync()
    EndIfClient()
    SkipLinesIfFlagOff(1, 5020)
    EnableFlag(6228)
    SkipLinesIfFlagOff(1, 5021)
    EnableFlag(6235)
    IfFlagOn(-1, 5023)
    IfFlagOn(-1, 70009200)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6242)
    SkipLinesIfFlagOff(1, 5027)
    EnableFlag(6249)
    IfFlagOn(-2, 5029)
    IfFlagOn(-2, 70009220)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6256)
    SkipLinesIfFlagOff(1, 5022)
    EnableFlag(6236)
    IfFlagOn(-3, 5025)
    IfFlagOn(-3, 70009210)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6243)
    SkipLinesIfFlagOff(1, 5028)
    EnableFlag(6251)
    IfFlagOn(-4, 5031)
    IfFlagOn(-4, 70009230)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6258)
    IfFlagOn(-5, 5033)
    IfFlagOn(-5, 70009240)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6259)


@RestartOnRest
def Event12105310(_, arg_0_3: int, arg_4_7: int):
    """ 12105310: Event 12105310 """
    IfFlagOn(0, arg_0_3)
    WaitFrames(31)
    ForceAnimation(arg_4_7, 7000)
    WaitFrames(109)
    ForceAnimation(arg_4_7, 7001, loop=True)
    IfFlagOff(0, arg_0_3)
    ForceAnimation(arg_4_7, 7002)
    WaitFrames(74)
    Restart()


def Event12107000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12107000: Event 12107000 """
    EndIfClient()
    IfFlagOn(0, arg_0_3)
    RotateToFaceEntity(PLAYER, arg_4_7, animation=101164)
    Wait(4.0)
    WarpPlayerToRespawnPoint(arg_8_11)


def Event12107100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12107100: Event 12107100 """
    EndIfClient()
    IfFlagOn(0, arg_0_3)
    Wait(4.0)
    DisableFlag(9020)
    DisableFlag(9021)
    DisableFlag(9022)
    DisableFlag(9023)
    DisableFlag(9024)
    DisableFlag(9025)
    DisableFlag(9026)
    EnableFlag(arg_8_11)
    DisableFlag(arg_0_3)
    End()
    RotateToFaceEntity(PLAYER, arg_4_7, animation=101164)


def Event12107200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12107200: Event 12107200 """
    IfFlagOn(0, arg_0_3)
    DisableFlag(arg_0_3)
    WarpPlayerToRespawnPoint(arg_4_7)
    EnableFlag(arg_8_11)
