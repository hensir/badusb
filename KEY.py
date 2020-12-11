"""
Show是用来在窗口上显示的 比如43号plus会显示一个 +
Input则是程序真正放到TextEdit中的符号
没错 这个DigiKeyboard参考头文件.h 没有声明完的常量
它们的命名规则就会用Qt提供的这个命名
"""

KeyShowdict = {
    32: "Space",  # Key_Space
    33: "!",  # Key_Exclam
    34: "\"",  # Key_QuoteDbl
    35: "#",  # Key_NumberSign
    36: "$",  # Key_Dollar
    37: "%",  # Key_Percent
    38: "&",  # Key_Ampersand
    39: "'",  # Key_Apostrophe
    40: "(",  # Key_ParenLeft
    41: ")",  # Key_ParenRight
    42: "*",  # Key_Asterisk
    43: "+",  # Key_Plus
    44: ",",  # Key_Comma
    45: "-",  # Key_Minus
    46: ".",  # Key_Period
    47: "/",  # Key_Slash
    48: "0",  # Key_0
    49: "1",  # Key_1
    50: "2",  # Key_2
    51: "3",  # Key_3
    52: "4",  # Key_4
    53: "5",  # Key_5
    54: "6",  # Key_6
    55: "7",  # Key_7
    56: "8",  # Key_8
    57: "9",  # Key_9
    58: ":",  # Key_Colon
    59: ";",  # Key_Semicolon
    60: "<",  # Key_Less
    61: "=",  # Key_Equal
    62: ">",  # Key_Greater
    63: "?",  # Key_Question
    64: "@",  # Key_At
    65: "A",  # Key_A
    66: "B",  # Key_B
    67: "C",  # Key_C
    68: "D",  # Key_D
    69: "E",  # Key_E
    70: "F",  # Key_F
    71: "G",  # Key_G
    72: "H",  # Key_H
    73: "I",  # Key_I
    74: "J",  # Key_J
    75: "K",  # Key_K
    76: "L",  # Key_L
    77: "M",  # Key_M
    78: "N",  # Key_N
    79: "O",  # Key_O
    80: "P",  # Key_P
    81: "Q",  # Key_Q
    82: "R",  # Key_R
    83: "S",  # Key_S
    84: "T",  # Key_T
    85: "U",  # Key_U
    86: "V",  # Key_V
    87: "W",  # Key_W
    88: "X",  # Key_X
    89: "Y",  # Key_Y
    90: "Z",  # Key_Z
    91: "[",  # Key_BracketLeft
    92: "\\",  # Key_Backslash
    93: "]",  # Key_BracketRight
    94: "^",  # Key_AsciiCircum
    95: "_",  # Key_Underscore
    96: "`",  # Key_QuoteLeft
    123: "{",  # Key_BraceLeft
    124: "|",  # Key_Bar
    125: "}",  # Key_BraceRight
    126: "~",  # Key_AsciiTilde
    160: "",  # Key_nobreakspace
    161: "",  # Key_exclamdown
    162: "",  # Key_cent
    163: "",  # Key_sterling
    164: "",  # Key_currency
    165: "",  # Key_yen
    166: "",  # Key_brokenbar
    167: "",  # Key_section
    168: "",  # Key_diaeresis
    169: "",  # Key_copyright
    170: "",  # Key_ordfeminine
    171: "",  # Key_guillemotleft
    172: "",  # Key_notsign
    173: "",  # Key_hyphen
    174: "",  # Key_registered
    175: "",  # Key_macron
    176: "",  # Key_degree
    177: "",  # Key_plusminus
    178: "",  # Key_twosuperior
    179: "",  # Key_threesuperior
    180: "",  # Key_acute
    181: "",  # Key_mu
    182: "",  # Key_paragraph
    183: "",  # Key_periodcentered
    184: "",  # Key_cedilla
    185: "",  # Key_onesuperior
    186: "",  # Key_masculine
    187: "",  # Key_guillemotright
    188: "",  # Key_onequarter
    189: "",  # Key_onehalf
    190: "",  # Key_threequarters
    191: "",  # Key_questiondown
    192: "",  # Key_Agrave
    193: "",  # Key_Aacute
    194: "",  # Key_Acircumflex
    195: "",  # Key_Atilde
    196: "",  # Key_Adiaeresis
    197: "",  # Key_Aring
    198: "",  # Key_AE
    199: "",  # Key_Ccedilla
    200: "",  # Key_Egrave
    201: "",  # Key_Eacute
    202: "",  # Key_Ecircumflex
    203: "",  # Key_Ediaeresis
    204: "",  # Key_Igrave
    205: "",  # Key_Iacute
    206: "",  # Key_Icircumflex
    207: "",  # Key_Idiaeresis
    208: "",  # Key_ETH
    209: "",  # Key_Ntilde
    210: "",  # Key_Ograve
    211: "",  # Key_Oacute
    212: "",  # Key_Ocircumflex
    213: "",  # Key_Otilde
    214: "",  # Key_Odiaeresis
    215: "",  # Key_multiply
    216: "",  # Key_Ooblique
    217: "",  # Key_Ugrave
    218: "",  # Key_Uacute
    219: "",  # Key_Ucircumflex
    220: "",  # Key_Udiaeresis
    221: "",  # Key_Yacute
    222: "",  # Key_THORN
    223: "",  # Key_ssharp
    247: "",  # Key_division
    255: "",  # Key_ydiaeresis
    16777216: "Esc",  # Key_Escape
    16777217: "Tab",  # Key_Tab
    16777218: "Tab",  # Key_Backtab
    16777219: "Backspace",  # Key_Backspace
    16777220: "Enter",  # Key_Return
    16777221: "Enter",  # Key_Enter
    16777222: "Insert",  # Key_Insert
    16777223: "Delete",  # Key_Delete
    16777224: "Pause",  # Key_Pause
    16777225: "Print",  # Key_Print
    16777226: "SysReq",  # Key_SysReq
    16777227: "Clear",  # Key_Clear
    16777232: "Home",  # Key_Home
    16777233: "End",  # Key_End
    16777234: "←",  # Key_Left
    16777235: "↑",  # Key_Up
    16777236: "→",  # Key_Right
    16777237: "↓",  # Key_Down
    16777238: "PageUp",  # Key_PageUp
    16777239: "PageDown",  # Key_PageDown
    16777248: "Shift",  # Key_Shift
    16777249: "Ctrl",  # Key_Control
    16777250: "Win",  # Key_Meta
    16777251: "Alt",  # Key_Alt
    16777252: "CapsLock",  # Key_CapsLock
    16777253: "NumLock",  # Key_NumLock
    16777254: "ScrollLock",  # Key_ScrollLock
    16777264: "F1",  # Key_F1
    16777265: "F2",  # Key_F2
    16777266: "F3",  # Key_F3
    16777267: "F4",  # Key_F4
    16777268: "F5",  # Key_F5
    16777269: "F6",  # Key_F6
    16777270: "F7",  # Key_F7
    16777271: "F8",  # Key_F8
    16777272: "F9",  # Key_F9
    16777273: "F10",  # Key_F10
    16777274: "F11",  # Key_F11
    16777275: "F12",  # Key_F12
    16777276: "F13",  # Key_F13
    16777277: "F14",  # Key_F14
    16777278: "F15",  # Key_F15
    16777279: "F16",  # Key_F16
    16777280: "F17",  # Key_F17
    16777281: "F18",  # Key_F18
    16777282: "F19",  # Key_F19
    16777283: "F20",  # Key_F20
    16777284: "F21",  # Key_F21
    16777285: "F22",  # Key_F22
    16777286: "F23",  # Key_F23
    16777287: "F24",  # Key_F24
    16777288: "F25",  # Key_F25
    16777289: "F26",  # Key_F26
    16777290: "F27",  # Key_F27
    16777291: "F28",  # Key_F28
    16777292: "F29",  # Key_F29
    16777293: "F30",  # Key_F30
    16777294: "F31",  # Key_F31
    16777295: "F32",  # Key_F32
    16777296: "F33",  # Key_F33
    16777297: "F34",  # Key_F34
    16777298: "F35",  # Key_F35
    16777299: "",  # Key_Super_L
    16777300: "",  # Key_Super_R
    16777301: "Menu",  # Key_Menu
    16777302: "",  # Key_Hyper_L
    16777303: "",  # Key_Hyper_R
    16777304: "",  # Key_Help
    16777305: "",  # Key_Direction_L
    16777312: "",  # Key_Direction_R
    16777313: "",  # Key_Back
    16777314: "",  # Key_Forward
    16777315: "",  # Key_Stop
    16777316: "",  # Key_Refresh
    16777328: "",  # Key_VolumeDown
    16777329: "",  # Key_VolumeMute
    16777330: "",  # Key_VolumeUp
    16777331: "",  # Key_BassBoost
    16777332: "",  # Key_BassUp
    16777333: "",  # Key_BassDown
    16777334: "",  # Key_TrebleUp
    16777335: "",  # Key_TrebleDown
    16777344: "",  # Key_MediaPlay
    16777345: "",  # Key_MediaStop
    16777346: "",  # Key_MediaPrevious
    16777347: "",  # Key_MediaNext
    16777348: "",  # Key_MediaRecord
    16777349: "",  # Key_MediaPause
    16777350: "",  # Key_MediaTogglePlayPause
    16777360: "",  # Key_HomePage
    16777361: "",  # Key_Favorites
    16777362: "",  # Key_Search
    16777363: "",  # Key_Standby
    16777364: "",  # Key_OpenUrl
    16777376: "",  # Key_LaunchMail
    16777377: "",  # Key_LaunchMedia
    16777378: "",  # Key_Launch0
    16777379: "",  # Key_Launch1
    16777380: "",  # Key_Launch2
    16777381: "",  # Key_Launch3
    16777382: "",  # Key_Launch4
    16777383: "",  # Key_Launch5
    16777384: "",  # Key_Launch6
    16777385: "",  # Key_Launch7
    16777386: "",  # Key_Launch8
    16777387: "",  # Key_Launch9
    16777388: "",  # Key_LaunchA
    16777389: "",  # Key_LaunchB
    16777390: "",  # Key_LaunchC
    16777391: "",  # Key_LaunchD
    16777392: "",  # Key_LaunchE
    16777393: "",  # Key_LaunchF
    16777394: "",  # Key_MonBrightnessUp
    16777395: "",  # Key_MonBrightnessDown
    16777396: "",  # Key_KeyboardLightOnOff
    16777397: "",  # Key_KeyboardBrightnessUp
    16777398: "",  # Key_KeyboardBrightnessDown
    16777399: "",  # Key_PowerOff
    16777400: "",  # Key_WakeUp
    16777401: "",  # Key_Eject
    16777402: "",  # Key_ScreenSaver
    16777403: "",  # Key_WWW
    16777404: "",  # Key_Memo
    16777405: "",  # Key_LightBulb
    16777406: "",  # Key_Shop
    16777407: "",  # Key_History
    16777408: "",  # Key_AddFavorite
    16777409: "",  # Key_HotLinks
    16777410: "",  # Key_BrightnessAdjust
    16777411: "",  # Key_Finance
    16777412: "",  # Key_Community
    16777413: "",  # Key_AudioRewind
    16777414: "",  # Key_BackForward
    16777415: "",  # Key_ApplicationLeft
    16777416: "",  # Key_ApplicationRight
    16777417: "",  # Key_Book
    16777418: "",  # Key_CD
    16777419: "",  # Key_Calculator
    16777420: "",  # Key_ToDoList
    16777421: "",  # Key_ClearGrab
    16777422: "",  # Key_Close
    16777423: "",  # Key_Copy
    16777424: "",  # Key_Cut
    16777425: "",  # Key_Display
    16777426: "",  # Key_DOS
    16777427: "",  # Key_Documents
    16777428: "",  # Key_Excel
    16777429: "",  # Key_Explorer
    16777430: "",  # Key_Game
    16777431: "",  # Key_Go
    16777432: "",  # Key_iTouch
    16777433: "",  # Key_LogOff
    16777434: "",  # Key_Market
    16777435: "",  # Key_Meeting
    16777436: "",  # Key_MenuKB
    16777437: "",  # Key_MenuPB
    16777438: "",  # Key_MySites
    16777439: "",  # Key_News
    16777440: "",  # Key_OfficeHome
    16777441: "",  # Key_Option
    16777442: "",  # Key_Paste
    16777443: "",  # Key_Phone
    16777444: "",  # Key_Calendar
    16777445: "",  # Key_Reply
    16777446: "",  # Key_Reload
    16777447: "",  # Key_RotateWindows
    16777448: "",  # Key_RotationPB
    16777449: "",  # Key_RotationKB
    16777450: "",  # Key_Save
    16777451: "",  # Key_Send
    16777452: "",  # Key_Spell
    16777453: "",  # Key_SplitScreen
    16777454: "",  # Key_Support
    16777455: "",  # Key_TaskPane
    16777456: "",  # Key_Terminal
    16777457: "",  # Key_Tools
    16777458: "",  # Key_Travel
    16777459: "",  # Key_Video
    16777460: "",  # Key_Word
    16777461: "",  # Key_Xfer
    16777462: "",  # Key_ZoomIn
    16777463: "",  # Key_ZoomOut
    16777464: "",  # Key_Away
    16777465: "",  # Key_Messenger
    16777466: "",  # Key_WebCam
    16777467: "",  # Key_MailForward
    16777468: "",  # Key_Pictures
    16777469: "",  # Key_Music
    16777470: "",  # Key_Battery
    16777471: "",  # Key_Bluetooth
    16777472: "",  # Key_WLAN
    16777473: "",  # Key_UWB
    16777474: "",  # Key_AudioForward
    16777475: "",  # Key_AudioRepeat
    16777476: "",  # Key_AudioRandomPlay
    16777477: "",  # Key_Subtitle
    16777478: "",  # Key_AudioCycleTrack
    16777479: "",  # Key_Time
    16777480: "",  # Key_Hibernate
    16777481: "",  # Key_View
    16777482: "",  # Key_TopMenu
    16777483: "",  # Key_PowerDown
    16777484: "",  # Key_Suspend
    16777485: "",  # Key_ContrastAdjust
    16777486: "",  # Key_LaunchG
    16777487: "",  # Key_LaunchH
    16777488: "",  # Key_TouchpadToggle
    16777489: "",  # Key_TouchpadOn
    16777490: "",  # Key_TouchpadOff
    16777491: "",  # Key_MicMute
    16777492: "",  # Key_Red
    16777493: "",  # Key_Green
    16777494: "",  # Key_Yellow
    16777495: "",  # Key_Blue
    16777496: "",  # Key_ChannelUp
    16777497: "",  # Key_ChannelDown
    16777498: "",  # Key_Guide
    16777499: "",  # Key_Info
    16777500: "",  # Key_Settings
    16777501: "",  # Key_MicVolumeUp
    16777502: "",  # Key_MicVolumeDown
    16777504: "",  # Key_New
    16777505: "",  # Key_Open
    16777506: "",  # Key_Find
    16777507: "",  # Key_Undo
    16777508: "",  # Key_Redo
    16781571: "",  # Key_AltGr
    16781600: "",  # Key_Multi_key
    16781601: "",  # Key_Kanji
    16781602: "",  # Key_Muhenkan
    16781603: "",  # Key_Henkan
    16781604: "",  # Key_Romaji
    16781605: "",  # Key_Hiragana
    16781606: "",  # Key_Katakana
    16781607: "",  # Key_Hiragana_Katakana
    16781608: "",  # Key_Zenkaku
    16781609: "",  # Key_Hankaku
    16781610: "",  # Key_Zenkaku_Hankaku
    16781611: "",  # Key_Touroku
    16781612: "",  # Key_Massyo
    16781613: "",  # Key_Kana_Lock
    16781614: "",  # Key_Kana_Shift
    16781615: "",  # Key_Eisu_Shift
    16781616: "",  # Key_Eisu_toggle
    16781617: "",  # Key_Hangul
    16781618: "",  # Key_Hangul_Start
    16781619: "",  # Key_Hangul_End
    16781620: "",  # Key_Hangul_Hanja
    16781621: "",  # Key_Hangul_Jamo
    16781622: "",  # Key_Hangul_Romaja
    16781623: "",  # Key_Codeinput
    16781624: "",  # Key_Hangul_Jeonja
    16781625: "",  # Key_Hangul_Banja
    16781626: "",  # Key_Hangul_PreHanja
    16781627: "",  # Key_Hangul_PostHanja
    16781628: "",  # Key_SingleCandidate
    16781629: "",  # Key_MultipleCandidate
    16781630: "",  # Key_PreviousCandidate
    16781631: "",  # Key_Hangul_Special
    16781694: "",  # Key_Mode_switch
    16781904: "",  # Key_Dead_Grave
    16781905: "",  # Key_Dead_Acute
    16781906: "",  # Key_Dead_Circumflex
    16781907: "",  # Key_Dead_Tilde
    16781908: "",  # Key_Dead_Macron
    16781909: "",  # Key_Dead_Breve
    16781910: "",  # Key_Dead_Abovedot
    16781911: "",  # Key_Dead_Diaeresis
    16781912: "",  # Key_Dead_Abovering
    16781913: "",  # Key_Dead_Doubleacute
    16781914: "",  # Key_Dead_Caron
    16781915: "",  # Key_Dead_Cedilla
    16781916: "",  # Key_Dead_Ogonek
    16781917: "",  # Key_Dead_Iota
    16781918: "",  # Key_Dead_Voiced_Sound
    16781919: "",  # Key_Dead_Semivoiced_Sound
    16781920: "",  # Key_Dead_Belowdot
    16781921: "",  # Key_Dead_Hook
    16781922: "",  # Key_Dead_Horn
    16781923: "",  # Key_Dead_Stroke
    16781924: "",  # Key_Dead_Abovecomma
    16781925: "",  # Key_Dead_Abovereversedcomma
    16781926: "",  # Key_Dead_Doublegrave
    16781927: "",  # Key_Dead_Belowring
    16781928: "",  # Key_Dead_Belowmacron
    16781929: "",  # Key_Dead_Belowcircumflex
    16781930: "",  # Key_Dead_Belowtilde
    16781931: "",  # Key_Dead_Belowbreve
    16781932: "",  # Key_Dead_Belowdiaeresis
    16781933: "",  # Key_Dead_Invertedbreve
    16781934: "",  # Key_Dead_Belowcomma
    16781935: "",  # Key_Dead_Currency
    16781952: "",  # Key_Dead_a
    16781953: "",  # Key_Dead_A
    16781954: "",  # Key_Dead_e
    16781955: "",  # Key_Dead_E
    16781956: "",  # Key_Dead_i
    16781957: "",  # Key_Dead_I
    16781958: "",  # Key_Dead_o
    16781959: "",  # Key_Dead_O
    16781960: "",  # Key_Dead_u
    16781961: "",  # Key_Dead_U
    16781962: "",  # Key_Dead_Small_Schwa
    16781963: "",  # Key_Dead_Capital_Schwa
    16781964: "",  # Key_Dead_Greek
    16781968: "",  # Key_Dead_Lowline
    16781969: "",  # Key_Dead_Aboveverticalline
    16781970: "",  # Key_Dead_Belowverticalline
    16781971: "",  # Key_Dead_Longsolidusoverlay
    16842751: "",  # Key_MediaLast
    16842752: "",  # Key_Select
    16842753: "",  # Key_Yes
    16842754: "",  # Key_No
    16908289: "",  # Key_Cancel
    16908290: "",  # Key_Printer
    16908291: "",  # Key_Execute
    16908292: "",  # Key_Sleep
    16908293: "",  # Key_Play
    16908294: "",  # Key_Zoom
    16908298: "",  # Key_Exit
    17825792: "",  # Key_Context1
    17825793: "",  # Key_Context2
    17825794: "",  # Key_Context3
    17825795: "",  # Key_Context4
    17825796: "",  # Key_Call
    17825797: "",  # Key_Hangup
    17825798: "",  # Key_Flip
    17825799: "",  # Key_ToggleCallHangup
    17825800: "",  # Key_VoiceDial
    17825801: "",  # Key_LastNumberRedial
    17825824: "",  # Key_Camera
    17825825: "",  # Key_CameraFocus
    33554431: ""  # Key_unknown
}
KeyInputdict = {
    32: "Key_Space",
    33: "Key_Exclam",
    34: "Key_QuoteDbl",
    35: "Key_NumberSign",
    36: "Key_Dollar",
    37: "Key_Percent",
    38: "Key_Ampersand",
    39: "Key_Apostrophe",
    40: "Key_ParenLeft",
    41: "Key_ParenRight",
    42: "Key_Asterisk",
    43: "Key_Plus",
    44: "Key_Comma",
    45: "Key_Minus",
    46: "Key_Period",
    47: "Key_Slash",
    48: "Key_0",
    49: "Key_1",
    50: "Key_2",
    51: "Key_3",
    52: "Key_4",
    53: "Key_5",
    54: "Key_6",
    55: "Key_7",
    56: "Key_8",
    57: "Key_9",
    58: "Key_Colon",
    59: "Key_Semicolon",
    60: "Key_Less",
    61: "Key_Equal",
    62: "Key_Greater",
    63: "Key_Question",
    64: "Key_At",
    65: "Key_A",
    66: "Key_B",
    67: "Key_C",
    68: "Key_D",
    69: "Key_E",
    70: "Key_F",
    71: "Key_G",
    72: "Key_H",
    73: "Key_I",
    74: "Key_J",
    75: "Key_K",
    76: "Key_L",
    77: "Key_M",
    78: "Key_N",
    79: "Key_O",
    80: "Key_P",
    81: "Key_Q",
    82: "Key_R",
    83: "Key_S",
    84: "Key_T",
    85: "Key_U",
    86: "Key_V",
    87: "Key_W",
    88: "Key_X",
    89: "Key_Y",
    90: "Key_Z",
    91: "Key_BracketLeft",
    92: "Key_Backslash",
    93: "Key_BracketRight",
    94: "Key_AsciiCircum",
    95: "Key_Underscore",
    96: "Key_QuoteLeft",
    123: "Key_BraceLeft",
    124: "Key_Bar",
    125: "Key_BraceRight",
    126: "Key_AsciiTilde",
    160: "Key_nobreakspace",
    161: "Key_exclamdown",
    162: "Key_cent",
    163: "Key_sterling",
    164: "Key_currency",
    165: "Key_yen",
    166: "Key_brokenbar",
    167: "Key_section",
    168: "Key_diaeresis",
    169: "Key_copyright",
    170: "Key_ordfeminine",
    171: "Key_guillemotleft",
    172: "Key_notsign",
    173: "Key_hyphen",
    174: "Key_registered",
    175: "Key_macron",
    176: "Key_degree",
    177: "Key_plusminus",
    178: "Key_twosuperior",
    179: "Key_threesuperior",
    180: "Key_acute",
    181: "Key_mu",
    182: "Key_paragraph",
    183: "Key_periodcentered",
    184: "Key_cedilla",
    185: "Key_onesuperior",
    186: "Key_masculine",
    187: "Key_guillemotright",
    188: "Key_onequarter",
    189: "Key_onehalf",
    190: "Key_threequarters",
    191: "Key_questiondown",
    192: "Key_Agrave",
    193: "Key_Aacute",
    194: "Key_Acircumflex",
    195: "Key_Atilde",
    196: "Key_Adiaeresis",
    197: "Key_Aring",
    198: "Key_AE",
    199: "Key_Ccedilla",
    200: "Key_Egrave",
    201: "Key_Eacute",
    202: "Key_Ecircumflex",
    203: "Key_Ediaeresis",
    204: "Key_Igrave",
    205: "Key_Iacute",
    206: "Key_Icircumflex",
    207: "Key_Idiaeresis",
    208: "Key_ETH",
    209: "Key_Ntilde",
    210: "Key_Ograve",
    211: "Key_Oacute",
    212: "Key_Ocircumflex",
    213: "Key_Otilde",
    214: "Key_Odiaeresis",
    215: "Key_multiply",
    216: "Key_Ooblique",
    217: "Key_Ugrave",
    218: "Key_Uacute",
    219: "Key_Ucircumflex",
    220: "Key_Udiaeresis",
    221: "Key_Yacute",
    222: "Key_THORN",
    223: "Key_ssharp",
    247: "Key_division",
    255: "Key_ydiaeresis",
    16777216: "Key_Escape",
    16777217: "Key_Tab",
    16777218: "Key_Backtab",
    16777219: "Key_Backspace",
    16777220: "Key_Return",
    16777221: "Key_Enter",
    16777222: "Key_Insert",
    16777223: "Key_Delete",
    16777224: "Key_Pause",
    16777225: "Key_Print",
    16777226: "Key_SysReq",
    16777227: "Key_Clear",
    16777232: "Key_Home",
    16777233: "Key_End",
    16777234: "Key_Left",
    16777235: "Key_Up",
    16777236: "Key_Right",
    16777237: "Key_Down",
    16777238: "Key_PageUp",
    16777239: "Key_PageDown",
    16777248: "Key_Shift",
    16777249: "Key_Ctrl",
    16777250: "Key_Meta",
    16777251: "Key_Alt",
    16777252: "Key_CapsLock",
    16777253: "Key_NumLock",
    16777254: "Key_ScrollLock",
    16777264: "Key_F1",
    16777265: "Key_F2",
    16777266: "Key_F3",
    16777267: "Key_F4",
    16777268: "Key_F5",
    16777269: "Key_F6",
    16777270: "Key_F7",
    16777271: "Key_F8",
    16777272: "Key_F9",
    16777273: "Key_F10",
    16777274: "Key_F11",
    16777275: "Key_F12",
    16777276: "Key_F13",
    16777277: "Key_F14",
    16777278: "Key_F15",
    16777279: "Key_F16",
    16777280: "Key_F17",
    16777281: "Key_F18",
    16777282: "Key_F19",
    16777283: "Key_F20",
    16777284: "Key_F21",
    16777285: "Key_F22",
    16777286: "Key_F23",
    16777287: "Key_F24",
    16777288: "Key_F25",
    16777289: "Key_F26",
    16777290: "Key_F27",
    16777291: "Key_F28",
    16777292: "Key_F29",
    16777293: "Key_F30",
    16777294: "Key_F31",
    16777295: "Key_F32",
    16777296: "Key_F33",
    16777297: "Key_F34",
    16777298: "Key_F35",
    16777299: "Key_Super_L",
    16777300: "Key_Super_R",
    16777301: "Key_Menu",
    16777302: "Key_Hyper_L",
    16777303: "Key_Hyper_R",
    16777304: "Key_Help",
    16777305: "Key_Direction_L",
    16777312: "Key_Direction_R",
    16777313: "Key_Back",
    16777314: "Key_Forward",
    16777315: "Key_Stop",
    16777316: "Key_Refresh",
    16777328: "Key_VolumeDown",
    16777329: "Key_VolumeMute",
    16777330: "Key_VolumeUp",
    16777331: "Key_BassBoost",
    16777332: "Key_BassUp",
    16777333: "Key_BassDown",
    16777334: "Key_TrebleUp",
    16777335: "Key_TrebleDown",
    16777344: "Key_MediaPlay",
    16777345: "Key_MediaStop",
    16777346: "Key_MediaPrevious",
    16777347: "Key_MediaNext",
    16777348: "Key_MediaRecord",
    16777349: "Key_MediaPause",
    16777350: "Key_MediaTogglePlayPause",
    16777360: "Key_HomePage",
    16777361: "Key_Favorites",
    16777362: "Key_Search",
    16777363: "Key_Standby",
    16777364: "Key_OpenUrl",
    16777376: "Key_LaunchMail",
    16777377: "Key_LaunchMedia",
    16777378: "Key_Launch0",
    16777379: "Key_Launch1",
    16777380: "Key_Launch2",
    16777381: "Key_Launch3",
    16777382: "Key_Launch4",
    16777383: "Key_Launch5",
    16777384: "Key_Launch6",
    16777385: "Key_Launch7",
    16777386: "Key_Launch8",
    16777387: "Key_Launch9",
    16777388: "Key_LaunchA",
    16777389: "Key_LaunchB",
    16777390: "Key_LaunchC",
    16777391: "Key_LaunchD",
    16777392: "Key_LaunchE",
    16777393: "Key_LaunchF",
    16777394: "Key_MonBrightnessUp",
    16777395: "Key_MonBrightnessDown",
    16777396: "Key_KeyboardLightOnOff",
    16777397: "Key_KeyboardBrightnessUp",
    16777398: "Key_KeyboardBrightnessDown",
    16777399: "Key_PowerOff",
    16777400: "Key_WakeUp",
    16777401: "Key_Eject",
    16777402: "Key_ScreenSaver",
    16777403: "Key_WWW",
    16777404: "Key_Memo",
    16777405: "Key_LightBulb",
    16777406: "Key_Shop",
    16777407: "Key_History",
    16777408: "Key_AddFavorite",
    16777409: "Key_HotLinks",
    16777410: "Key_BrightnessAdjust",
    16777411: "Key_Finance",
    16777412: "Key_Community",
    16777413: "Key_AudioRewind",
    16777414: "Key_BackForward",
    16777415: "Key_ApplicationLeft",
    16777416: "Key_ApplicationRight",
    16777417: "Key_Book",
    16777418: "Key_CD",
    16777419: "Key_Calculator",
    16777420: "Key_ToDoList",
    16777421: "Key_ClearGrab",
    16777422: "Key_Close",
    16777423: "Key_Copy",
    16777424: "Key_Cut",
    16777425: "Key_Display",
    16777426: "Key_DOS",
    16777427: "Key_Documents",
    16777428: "Key_Excel",
    16777429: "Key_Explorer",
    16777430: "Key_Game",
    16777431: "Key_Go",
    16777432: "Key_iTouch",
    16777433: "Key_LogOff",
    16777434: "Key_Market",
    16777435: "Key_Meeting",
    16777436: "Key_MenuKB",
    16777437: "Key_MenuPB",
    16777438: "Key_MySites",
    16777439: "Key_News",
    16777440: "Key_OfficeHome",
    16777441: "Key_Option",
    16777442: "Key_Paste",
    16777443: "Key_Phone",
    16777444: "Key_Calendar",
    16777445: "Key_Reply",
    16777446: "Key_Reload",
    16777447: "Key_RotateWindows",
    16777448: "Key_RotationPB",
    16777449: "Key_RotationKB",
    16777450: "Key_Save",
    16777451: "Key_Send",
    16777452: "Key_Spell",
    16777453: "Key_SplitScreen",
    16777454: "Key_Support",
    16777455: "Key_TaskPane",
    16777456: "Key_Terminal",
    16777457: "Key_Tools",
    16777458: "Key_Travel",
    16777459: "Key_Video",
    16777460: "Key_Word",
    16777461: "Key_Xfer",
    16777462: "Key_ZoomIn",
    16777463: "Key_ZoomOut",
    16777464: "Key_Away",
    16777465: "Key_Messenger",
    16777466: "Key_WebCam",
    16777467: "Key_MailForward",
    16777468: "Key_Pictures",
    16777469: "Key_Music",
    16777470: "Key_Battery",
    16777471: "Key_Bluetooth",
    16777472: "Key_WLAN",
    16777473: "Key_UWB",
    16777474: "Key_AudioForward",
    16777475: "Key_AudioRepeat",
    16777476: "Key_AudioRandomPlay",
    16777477: "Key_Subtitle",
    16777478: "Key_AudioCycleTrack",
    16777479: "Key_Time",
    16777480: "Key_Hibernate",
    16777481: "Key_View",
    16777482: "Key_TopMenu",
    16777483: "Key_PowerDown",
    16777484: "Key_Suspend",
    16777485: "Key_ContrastAdjust",
    16777486: "Key_LaunchG",
    16777487: "Key_LaunchH",
    16777488: "Key_TouchpadToggle",
    16777489: "Key_TouchpadOn",
    16777490: "Key_TouchpadOff",
    16777491: "Key_MicMute",
    16777492: "Key_Red",
    16777493: "Key_Green",
    16777494: "Key_Yellow",
    16777495: "Key_Blue",
    16777496: "Key_ChannelUp",
    16777497: "Key_ChannelDown",
    16777498: "Key_Guide",
    16777499: "Key_Info",
    16777500: "Key_Settings",
    16777501: "Key_MicVolumeUp",
    16777502: "Key_MicVolumeDown",
    16777504: "Key_New",
    16777505: "Key_Open",
    16777506: "Key_Find",
    16777507: "Key_Undo",
    16777508: "Key_Redo",
    16781571: "Key_AltGr",
    16781600: "Key_Multi_key",
    16781601: "Key_Kanji",
    16781602: "Key_Muhenkan",
    16781603: "Key_Henkan",
    16781604: "Key_Romaji",
    16781605: "Key_Hiragana",
    16781606: "Key_Katakana",
    16781607: "Key_Hiragana_Katakana",
    16781608: "Key_Zenkaku",
    16781609: "Key_Hankaku",
    16781610: "Key_Zenkaku_Hankaku",
    16781611: "Key_Touroku",
    16781612: "Key_Massyo",
    16781613: "Key_Kana_Lock",
    16781614: "Key_Kana_Shift",
    16781615: "Key_Eisu_Shift",
    16781616: "Key_Eisu_toggle",
    16781617: "Key_Hangul",
    16781618: "Key_Hangul_Start",
    16781619: "Key_Hangul_End",
    16781620: "Key_Hangul_Hanja",
    16781621: "Key_Hangul_Jamo",
    16781622: "Key_Hangul_Romaja",
    16781623: "Key_Codeinput",
    16781624: "Key_Hangul_Jeonja",
    16781625: "Key_Hangul_Banja",
    16781626: "Key_Hangul_PreHanja",
    16781627: "Key_Hangul_PostHanja",
    16781628: "Key_SingleCandidate",
    16781629: "Key_MultipleCandidate",
    16781630: "Key_PreviousCandidate",
    16781631: "Key_Hangul_Special",
    16781694: "Key_Mode_switch",
    16781904: "Key_Dead_Grave",
    16781905: "Key_Dead_Acute",
    16781906: "Key_Dead_Circumflex",
    16781907: "Key_Dead_Tilde",
    16781908: "Key_Dead_Macron",
    16781909: "Key_Dead_Breve",
    16781910: "Key_Dead_Abovedot",
    16781911: "Key_Dead_Diaeresis",
    16781912: "Key_Dead_Abovering",
    16781913: "Key_Dead_Doubleacute",
    16781914: "Key_Dead_Caron",
    16781915: "Key_Dead_Cedilla",
    16781916: "Key_Dead_Ogonek",
    16781917: "Key_Dead_Iota",
    16781918: "Key_Dead_Voiced_Sound",
    16781919: "Key_Dead_Semivoiced_Sound",
    16781920: "Key_Dead_Belowdot",
    16781921: "Key_Dead_Hook",
    16781922: "Key_Dead_Horn",
    16781923: "Key_Dead_Stroke",
    16781924: "Key_Dead_Abovecomma",
    16781925: "Key_Dead_Abovereversedcomma",
    16781926: "Key_Dead_Doublegrave",
    16781927: "Key_Dead_Belowring",
    16781928: "Key_Dead_Belowmacron",
    16781929: "Key_Dead_Belowcircumflex",
    16781930: "Key_Dead_Belowtilde",
    16781931: "Key_Dead_Belowbreve",
    16781932: "Key_Dead_Belowdiaeresis",
    16781933: "Key_Dead_Invertedbreve",
    16781934: "Key_Dead_Belowcomma",
    16781935: "Key_Dead_Currency",
    16781952: "Key_Dead_a",
    16781953: "Key_Dead_A",
    16781954: "Key_Dead_e",
    16781955: "Key_Dead_E",
    16781956: "Key_Dead_i",
    16781957: "Key_Dead_I",
    16781958: "Key_Dead_o",
    16781959: "Key_Dead_O",
    16781960: "Key_Dead_u",
    16781961: "Key_Dead_U",
    16781962: "Key_Dead_Small_Schwa",
    16781963: "Key_Dead_Capital_Schwa",
    16781964: "Key_Dead_Greek",
    16781968: "Key_Dead_Lowline",
    16781969: "Key_Dead_Aboveverticalline",
    16781970: "Key_Dead_Belowverticalline",
    16781971: "Key_Dead_Longsolidusoverlay",
    16842751: "Key_MediaLast",
    16842752: "Key_Select",
    16842753: "Key_Yes",
    16842754: "Key_No",
    16908289: "Key_Cancel",
    16908290: "Key_Printer",
    16908291: "Key_Execute",
    16908292: "Key_Sleep",
    16908293: "Key_Play",
    16908294: "Key_Zoom",
    16908298: "Key_Exit",
    17825792: "Key_Context1",
    17825793: "Key_Context2",
    17825794: "Key_Context3",
    17825795: "Key_Context4",
    17825796: "Key_Call",
    17825797: "Key_Hangup",
    17825798: "Key_Flip",
    17825799: "Key_ToggleCallHangup",
    17825800: "Key_VoiceDial",
    17825801: "Key_LastNumberRedial",
    17825824: "Key_Camera",
    17825825: "Key_CameraFocus",
    33554431: "Key_unknown",
}
DialogKeyPushButton = {
    "01": "ErrorRollOver",
    "02": "POSTFail",
    "03": "ErrorUndefined",
    "35": "GraveAccentandTilde",
    "49": "Insert",
    "4A": "Home",
    "4B": "PageUp",
    "4C": "DeleteForward",
    "4D": "End",
    "4E": "PageDown",
    "4F": "RightArrow",
    "50": "LeftArrow",
    "51": "DownArrow",
    "52": "UpArrow",
    "64": "\and|",
    "65": "Application",
    "66": "Power",
    "68": "F13",
    "69": "F14",
    "6A": "F15",
    "6B": "F16",
    "6C": "F17",
    "6D": "F18",
    "6E": "F19",
    "6F": "F20",
    "70": "F21",
    "71": "F22",
    "72": "F23",
    "73": "F24",
    "74": "Execute",
    "75": "Help",
    "76": "Menu",
    "77": "Select",
    "78": "Stop",
    "79": "Again",
    "7A": "Undo",
    "7B": "Cut",
    "7C": "Copy",
    "7D": "Paste",
    "7E": "Find",
    "7F": "Mute",
    "80": "VolumeUp",
    "81": "VolumeDown",
    "82": "LockingCapsLock",
    "83": "LockingNumLock",
    "84": "LockingScrollLock",
    "87": "International1",
    "88": "International2",
    "89": "International3",
    "8A": "International4",
    "8B": "International5",
    "8C": "International6",
    "8D": "International7",
    "8E": "International8",
    "8F": "International9",
    "90": "LANG1",
    "91": "LANG2",
    "92": "LANG3",
    "93": "LANG4",
    "94": "LANG5",
    "95": "LANG6",
    "96": "LANG7",
    "97": "LANG8",
    "98": "LANG9",
    "99": "AlternateErase",
    "9A": "SysReq/Attention",
    "9B": "Cancel",
    "9C": "Clear",
    "9D": "Prior",
    "9E": "Return",
    "9F": "Separator",
    "A0": "Out",
    "A1": "Oper",
    "A2": "Clear/Again",
    "A3": "CrSel/Props",
    "A4": "ExSel",
    "E0": "LeftControl",
    "E1": "LeftShift",
    "E2": "LeftAlt",
    "E3": "LeftGUI",
    "E4": "RightControl",
    "E5": "RightShift",
    "E6": "RightAlt",
    "E7": "RightGUI",
    "53": "NumLockandClear",
    "54": "/",
    "55": "*",
    "56": "-",
    "57": "+",
    "58": "ENTER",
    "59": "1andEnd",
    "5A": "2andDownArrow",
    "5B": "3andPageDn",
    "5C": "4andLeftArrow",
    "5D": "5",
    "5E": "6andRightArrow",
    "5F": "7andHome",
    "60": "8andUpArrow",
    "61": "9andPageUp",
    "62": "0andInsert",
    "63": ".andDelete",
    "67": "=",
    "85": "Comma",
    "86": "EqualSign",
    "B0": "00",
    "B1": "000",
    "B6": "(",
    "B7": ")",
    "B8": "{",
    "B9": "}",
    "BA": "Tab",
    "BB": "Backspace",
    "BC": "A",
    "BD": "B",
    "BE": "C",
    "BF": "D",
    "C0": "E",
    "C1": "F",
    "C2": "XOR",
    "C3": "∧",
    "C4": "%",
    "C5": "<",
    "C6": ">",
    "C7": "&&",
    "C8": "&&&&",
    "C9": "|",
    "CA": "||",
    "CB": ":",
    "CC": "#",
    "CD": "Space",
    "CE": "@",
    "CF": "!",
    "D0": "MemoryStore",
    "D1": "MemoryRecall",
    "D2": "MemoryClear",
    "D3": "MemoryAdd",
    "D4": "MemorySubtract",
    "D5": "MemoryMultiply",
    "D6": "MemoryDivide",
    "D7": "+/-",
    "D8": "Clear",
    "D9": "ClearEntry",
    "DA": "Binary",
    "DB": "Octal",
    "DC": "Decimal",
    "DD": "Hexadecimal",
}
