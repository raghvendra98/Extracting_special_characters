from fontTools.ttLib import TTFont
#
# def get_font_characters(font_path):
#     with TTFont(font_path) as font:
#         characters = {chr(y[0]) for x in font["cmap"].tables for y in x.cmap.items()}
#         characters1 = list(characters)
#         characters2 = list(dict.fromkeys(characters1))
#         # characters2 = str(len(characters1)) + "  "
#         # for item in characters1:
#         #     for items in item:
#         #         characters2 = characters2 + str(items) + ' '
#         #         # characters2 = str(characters2)
#     return characters2
# # print(get_font_characters("db_hindi_mast_4.ttf"))

def get_all_font_characters(font_path):
    chars = []
    with TTFont('db_hindi_mast_4.ttf', 0, ignoreDecompileErrors=True) as ttf:
        for x in ttf["cmap"].tables:
            for (code, _) in x.cmap.items():
                chars.append(chr(code))
    return chars