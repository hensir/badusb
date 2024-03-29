# 用于创建对话框中的按钮的字典 同时存储了对应的十六进制数值 用于后期define
DialogKeyPushButton = {
    "01": "ErrorRollOver", "02": "POSTFail", "03": "ErrorUndefined", "35": "GraveAccentandTilde", "4C": "DeleteForward",
    "64": "\and|", "65": "Application", "66": "Power", "68": "F13", "69": "F14", "6A": "F15", "6B": "F16", "6C": "F17",
    "6D": "F18", "6E": "F19", "6F": "F20", "70": "F21", "71": "F22", "72": "F23", "73": "F24", "74": "Execute",
    "75": "Help", "76": "Menu", "77": "Select", "78": "Stop", "79": "Again", "7A": "Undo", "7B": "Cut", "7C": "Copy",
    "7D": "Paste", "7E": "Find", "7F": "Mute", "80": "VolumeUp", "81": "VolumeDown", "82": "LockingCapsLock",
    "83": "LockingNumLock", "84": "LockingScrollLock", "87": "International1", "88": "International2",
    "89": "International3", "8A": "International4", "8B": "International5", "8C": "International6",
    "8D": "International7", "8E": "International8", "8F": "International9", "90": "LANG1", "91": "LANG2",
    "92": "LANG3", "93": "LANG4", "94": "LANG5", "95": "LANG6", "96": "LANG7", "97": "LANG8", "98": "LANG9",
    "99": "AlternateErase", "9A": "SysReq/Attention", "9B": "Cancel", "9C": "Clear", "9D": "Prior", "9E": "Return",
    "9F": "Separator", "A0": "Out", "A1": "Oper", "A2": "Clear/Again", "A3": "CrSel/Props", "A4": "ExSel",
    "E4": "RightControl", "E5": "RightShift", "E6": "RightAlt", "E7": "RightGUI", "53": "NumLockandClear", "54": "/",
    "55": "*", "56": "-", "57": "+", "58": "ENTER", "59": "1andEnd", "5A": "2andDownArrow", "5B": "3andPageDn",
    "5C": "4andLeftArrow", "5D": "5", "5E": "6andRightArrow", "5F": "7andHome", "60": "8andUpArrow", "61": "9andPageUp",
    "62": "0andInsert", "63": ".andDelete", "67": "=", "85": "Comma", "86": "EqualSign", "B0": "00", "B1": "000",
    "B6": "(", "B7": ")", "B8": "{", "B9": "}", "BA": "Tab", "BB": "Backspace", "BC": "A", "BD": "B", "BE": "C",
    "BF": "D", "C0": "E", "C1": "F", "C2": "XOR", "C3": "∧", "C4": "%", "C5": "<", "C6": ">", "C7": "&&", "C8": "&&&&",
    "C9": "|", "CA": "||", "CB": ":", "CC": "#", "CD": "Space", "CE": "@", "CF": "!", "D0": "MemoryStore",
    "D1": "MemoryRecall", "D2": "MemoryClear", "D3": "MemoryAdd", "D4": "MemorySubtract", "D5": "MemoryMultiply",
    "D6": "MemoryDivide", "D7": "+/-", "D8": "Clear", "D9": "ClearEntry", "DA": "Binary", "DB": "Octal",
    "DC": "Decimal", "DD": "Hexadecimal"}

DKPB = {"ErrorRollOver": "01", "POSTFail": "02", "ErrorUndefined": "03", "GraveAccentandTilde": "35",
        "DeleteForward": "4C", "\and|": "64", "Application": "65", "Power": "66", "F13": "68", "F14": "69", "F15": "6A",
        "F16": "6B", "F17": "6C", "F18": "6D", "F19": "6E", "F20": "6F", "F21": "70", "F22": "71", "F23": "72",
        "F24": "73", "Execute": "74", "Help": "75", "Menu": "76", "Select": "77", "Stop": "78", "Again": "79",
        "Undo": "7A", "Cut": "7B", "Copy": "7C", "Paste": "7D", "Find": "7E", "Mute": "7F", "VolumeUp": "80",
        "VolumeDown": "81", "LockingCapsLock": "82", "LockingNumLock": "83", "LockingScrollLock": "84",
        "International1": "87", "International2": "88", "International3": "89", "International4": "8A",
        "International5": "8B", "International6": "8C", "International7": "8D", "International8": "8E",
        "International9": "8F", "LANG1": "90", "LANG2": "91", "LANG3": "92", "LANG4": "93", "LANG5": "94",
        "LANG6": "95", "LANG7": "96", "LANG8": "97", "LANG9": "98", "AlternateErase": "99", "SysReq/Attention": "9A",
        "Cancel": "9B", "Clear": "9C", "Prior": "9D", "Return": "9E", "Separator": "9F", "Out": "A0", "Oper": "A1",
        "Clear/Again": "A2", "CrSel/Props": "A3", "ExSel": "A4", "NumLockandClear": "53", "/": "54", "*": "55",
        "-": "56", "+": "57", "ENTER": "58", "1andEnd": "59", "2andDownArrow": "5A", "3andPageDn": "5B",
        "4andLeftArrow": "5C", "5": "5D", "6andRightArrow": "5E", "7andHome": "5F", "8andUpArrow": "60",
        "9andPageUp": "61", "0andInsert": "62", ".andDelete": "63", "=": "67", "Comma": "85", "EqualSign": "86",
        "00": "B0", "000": "B1", "(": "B6", ")": "B7", "{": "B8", "}": "B9", "PTab": "BA", "PBackspace": "BB",
        "A": "BC", "B": "BD", "C": "BE", "D": "BF", "E": "C0", "F": "C1", "XOR": "C2", "∧": "C3", "%": "C4", "<": "C5",
        ">": "C6", "&&": "C7", "&&&&": "C8", "|": "C9", "||": "CA", ":": "CB", "#": "CC", "Space": "CD", "@": "CE",
        "!": "CF", "MemoryStore": "D0", "MemoryRecall": "D1", "MemoryClear": "D2", "MemoryAdd": "D3",
        "MemorySubtract": "D4", "MemoryMultiply": "D5", "MemoryDivide": "D6", "+/-": "D7", "PClear": "D8",
        "ClearEntry": "D9", "Binary": "DA", "Octal": "DB", "Decimal": "DC", "Hexadecimal": "DD", "Tab": "2B",
        "Backspace": "BB", "CapsLock": "39", "Esc": "29", "PrintScreen": "46", "ScrollLock": "47", "Pause|Break": "48",
        "Home": "4A", "End": "4D", "Insert": "49", "Delete": "4C", "PageUp": "4B", "PageDown": "4E", "UpArrow": "52",
        "DownArrow": "51", "LeftArrow": "50", "RightArrow": "4F"}

# SelectDialog中要输入 数字键上面的符号需要加上上档键的列表
NeedShift = {"~": "`", "!": "1", "@": "2", "#": "3", "$": "4", "%": "5", "^": "6", "&": "7", "*": "8", "(": "9",
             ")": "0", "_": "-", "+": "=", "{": "[", "}": "]", "|": "\\", ":": ";", "\"": "'", "<": ",", ">": ".",
             "?": "/"}

# 这是一个全局替换
GlobalReplacement = {"Ctrl": "MOD_CONTROL_LEFT", "Shift": "MOD_SHIFT_LEFT", "Alt": "MOD_ALT_LEFT",
                     "Win": "MOD_GUI_LEFT", "R_Ctrl": "MOD_CONTROL_RIGHT", "R_Shift": "MOD_SHIFT_RIGHT",
                     "R_Alt": "MOD_ALT_RIGHT", "R_Win": "MOD_GUI_RIGHT", "A": "KEY_A", "B": "KEY_B", "C": "KEY_C",
                     "D": "KEY_D", "E": "KEY_E", "F": "KEY_F", "G": "KEY_G", "H": "KEY_H", "I": "KEY_I", "J": "KEY_J",
                     "K": "KEY_K", "L": "KEY_L", "M": "KEY_M", "N": "KEY_N", "O": "KEY_O", "P": "KEY_P", "Q": "KEY_Q",
                     "R": "KEY_R", "S": "KEY_S", "T": "KEY_T", "U": "KEY_U", "V": "KEY_V", "W": "KEY_W", "X": "KEY_X",
                     "Y": "KEY_Y", "Z": "KEY_Z", "1": "KEY_1", "2": "KEY_2", "3": "KEY_3", "4": "KEY_4", "5": "KEY_5",
                     "6": "KEY_6", "7": "KEY_7", "8": "KEY_8", "9": "KEY_9", "0": "KEY_0", "F1": "KEY_F1",
                     "F2": "KEY_F2", "F3": "KEY_F3", "F4": "KEY_F4", "F5": "KEY_F5", "F6": "KEY_F6", "F7": "KEY_F7",
                     "F8": "KEY_F8", "F9": "KEY_F9", "F10": "KEY_F10", "F11": "KEY_F11", "F12": "KEY_F12",
                     "Enter": "KEY_ENTER", "Space": "KEY_SPACE"}
