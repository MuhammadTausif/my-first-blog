import sqlite3
from sqlite3 import Error
from os import path

ROOT = path.dirname(path.realpath(__file__))

# parameters = {'SeriesC_pn 022', 'Series D part number 8', 'co_97', 'co_202', 'SeriesC_pn 096', 'SeriesA_pn 029', 'SeriesC_pn 058', 'co_83', 'co_88', 'co_214', 'Series D part number 23', 'Series D part number 53', 'SeriesC_pn 024', 'SeriesC_pn 093', 'SeriesB_pn 039', 'SeriesB_pn 061', 'SeriesA_pn 001', 'Series D part number 106', 'SeriesC_pn 033', 'Series D part number 18', 'SeriesB_pn 009', 'Series D part number 147', 'co_206', 'SeriesA_pn 063', 'co_175', 'Series D part number 20', 'SeriesA_pn 034', 'co_157', 'SeriesC_pn 007', 'co_192', 'SeriesC_pn 082', 'Series D part number 85', 'co_230', 'SeriesC_pn 098', 'Series D part number 134', 'SeriesA_pn 024', 'Series D part number 61', 'co_20', 'co_39', 'co_43', 'Series D part number 118', 'co_21', 'co_167', 'Series D part number 127', 'co_164', 'SeriesB_pn 029', 'Series D part number 93', 'SeriesA_pn 021', 'co_193', 'SeriesC_pn 111', 'SeriesA_pn 049', 'co_61', 'Series D part number 110', 'SeriesC_pn 001', 'co_31', 'Series D part number 28', 'co_68', 'SeriesB_pn 012', 'co_225', 'co_220', 'co_153', 'SeriesC_pn 040', 'SeriesC_pn 046', 'SeriesA_pn 014', 'co_32', 'SeriesC_pn 055', 'Series D part number 137', 'co_96', 'Series D part number 83', 'Series D part number 154', 'co_138', 'co_170', 'co_194', 'co_4', 'SeriesA_pn 056', 'SeriesA_pn 070', 'co_141', 'SeriesB_pn 026', 'co_133', 'Series D part number 51', 'co_8', 'Series D part number 9', 'co_196', 'Series D part number 15', 'co_238', 'co_73', 'SeriesC_pn 043', 'co_106', 'SeriesC_pn 020', 'co_155', 'Series D part number 39', 'co_159', 'SeriesC_pn 059', 'co_128', 'Series D part number 100', 'SeriesC_pn 056', 'co_232', 'co_113', 'SeriesC_pn 026', 'SeriesA_pn 068', 'co_25', 'Series D part number 131', 'SeriesA_pn 045', 'SeriesB_pn 005', 'Series D part number 59', 'co_212', 'co_116', 'co_102', 'SeriesA_pn 016', 'co_27', 'co_197', 'Series D part number 58', 'SeriesC_pn 003', 'SeriesB_pn 050', 'SeriesA_pn 041', 'SeriesB_pn 055', 'co_148', 'SeriesB_pn 034', 'SeriesB_pn 058', 'Series D part number 132', 'co_229', 'co_161', 'Series D part number 112', 'SeriesA_pn 036', 'co_231', 'SeriesC_pn 070', 'SeriesB_pn 015', 'co_144', 'co_112', 'SeriesC_pn 107', 'SeriesC_pn 045', 'co_181', 'co_123', 'co_81', 'SeriesB_pn 042', 'SeriesB_pn 008', 'SeriesC_pn 083', 'co_173', 'Series D part number 128', 'Series D part number 38', 'SeriesC_pn 030', 'Series D part number 48', 'SeriesC_pn 110', 'SeriesA_pn 020', 'Series D part number 79', 'co_218', 'co_77', 'co_190', 'SeriesC_pn 100', 'co_6', 'Series D part number 46', 'Series D part number 108', 'SeriesC_pn 032', 'SeriesB_pn 023', 'Series D part number 142', 'co_98', 'co_130', 'co_94', 'co_176', 'Series D part number 69', 'Series D part number 22', 'SeriesA_pn 053', 'SeriesB_pn 057', 'SeriesB_pn 013', 'co_201', 'SeriesC_pn 014', 'Series D part number 26', 'Series D part number 4', 'SeriesB_pn 043', 'Series D part number 68', 'Series D part number 11', 'SeriesB_pn 059', 'co_203', 'Series D part number 54', 'SeriesC_pn 005', 'SeriesC_pn 034', 'Series D part number 65', 'co_152', 'co_178', 'co_233', 'SeriesA_pn 047', 'co_163', 'SeriesC_pn 031', 'co_28', 'co_82', 'Series D part number 140', 'co_30', 'Series D part number 146', 'co_187', 'Series D part number 78', 'SeriesA_pn 044', 'co_86', 'SeriesC_pn 050', 'Series D part number 105', 'SeriesA_pn 025', 'SeriesA_pn 061', 'SeriesB_pn 016', 'SeriesC_pn 013', 'co_104', 'SeriesA_pn 006', 'SeriesB_pn 051', 'Series D part number 91', 'SeriesB_pn 044', 'co_120', 'co_76', 'Series D part number 92', 'co_38', 'SeriesA_pn 031', 'co_41', 'SeriesC_pn 092', 'SeriesA_pn 040', 'co_227', 'SeriesC_pn 108', 'SeriesB_pn 060', 'SeriesB_pn 002', 'co_3', 'Series D part number 10', 'SeriesA_pn 027', 'Series D part number 111', 'SeriesA_pn 033', 'co_171', 'Series D part number 30', 'SeriesC_pn 009', 'SeriesB_pn 003', 'co_195', 'Series D part number 124', 'co_42', 'SeriesC_pn 078', 'Series D part number 5', 'SeriesB_pn 037', 'SeriesA_pn 042', 'co_122', 'Series D part number 143', 'Series D part number 52', 'SeriesB_pn 048', 'Series D part number 138', 'SeriesA_pn 066', 'SeriesC_pn 006', 'co_121', 'Series D part number 155', 'SeriesB_pn 052', 'co_131', 'co_199', 'SeriesA_pn 035', 'co_209', 'SeriesA_pn 022', 'Series D part number 94', 'Series D part number 86', 'Series D part number 97', 'co_69', 'Series D part number 116', 'co_78', 'SeriesC_pn 077', 'Series D part number 60', 'SeriesA_pn 023', 'SeriesA_pn 071', 'Series D part number 102', 'co_119', 'Series D part number 72', 'co_213', 'Series D part number 103', 'co_66', 'SeriesA_pn 039', 'co_118', 'SeriesC_pn 052', 'SeriesA_pn 013', 'Series D part number 139', 'SeriesC_pn 008', 'co_140', 'Series D part number 89', 'co_52', 'SeriesC_pn 112', 'Series D part number 43', 'SeriesA_pn 038', 'SeriesA_pn 037', 'co_174', 'SeriesB_pn 019', 'Series D part number 47', 'SeriesA_pn 058', 'co_10', 'co_46', 'Series D part number 56', 'SeriesA_pn 051', 'SeriesB_pn 031', 'SeriesA_pn 005', 'co_91', 'Series D part number 57', 'SeriesC_pn 017', 'SeriesC_pn 102', 'SeriesC_pn 069', 'co_211', 'Series D part number 74', 'Series D part number 148', 'SeriesC_pn 065', 'SeriesA_pn 017', 'SeriesC_pn 073', 'co_55', 'co_182', 'SeriesC_pn 064', 'co_151', 'Series D part number 88', 'co_143', 'co_222', 'SeriesC_pn 047', 'co_70', 'co_100', 'co_185', 'co_168', 'Series D part number 120', 'SeriesC_pn 048', 'co_71', 'co_154', 'SeriesB_pn 053', 'co_137', 'Series D part number 45', 'Series D part number 96', 'SeriesC_pn 042', 'SeriesA_pn 043', 'Series D part number 55', 'co_29', 'co_165', 'Series D part number 36', 'SeriesA_pn 048', 'Series D part number 157', 'SeriesC_pn 067', 'Series D part number 125', 'Series D part number 136', 'Series D part number 81', 'Series D part number 104', 'co_172', 'Series D part number 41', 'SeriesB_pn 020', 'Series D part number 73', 'co_198', 'co_240', 'co_147', 'co_40', 'SeriesC_pn 087', 'Series D part number 71', 'co_239', 'SeriesA_pn 008', 'Series D part number 35', 'SeriesC_pn 021', 'co_7', 'Series D part number 82', 'co_107', 'Series D part number 32', 'Series D part number 37', 'SeriesA_pn 052', 'co_101', 'co_56', 'Series D part number 2', 'Series D part number 76', 'Series D part number 24', 'co_127', 'Series D part number 27', 'co_108', 'co_217', 'SeriesB_pn 033', 'co_15', 'co_36', 'Series D part number 122', 'SeriesA_pn 059', 'Series D part number 70', 'Series D part number 44', 'Series D part number 156', 'SeriesC_pn 075', 'co_158', 'co_160', 'SeriesB_pn 045', 'Series D part number 33', 'Series D part number 159', 'co_23', 'co_117', 'co_145', 'co_179', 'Series D part number 121', 'SeriesC_pn 084', 'Series D part number 115', 'SeriesC_pn 118', 'SeriesB_pn 024', 'SeriesA_pn 002', 'SeriesB_pn 017', 'SeriesC_pn 071', 'SeriesC_pn 036', 'SeriesA_pn 007', 'co_191', 'Series D part number 6', 'SeriesC_pn 028', 'SeriesC_pn 115', 'co_75', 'co_92', 'co_90', 'co_35', 'SeriesB_pn 040', 'Series D part number 63', 'SeriesC_pn 066', 'SeriesA_pn 011', 'Series D part number 135', 'SeriesC_pn 099', 'co_200', 'co_166', 'Series D part number 13', 'SeriesC_pn 063', 'SeriesC_pn 018', 'co_58', 'SeriesC_pn 044', 'co_124', 'SeriesC_pn 103', 'co_9', 'co_156', 'co_22', 'Series D part number 87', 'SeriesC_pn 019', 'Series D part number 107', 'Series D part number 98', 'SeriesB_pn 027', 'co_109', 'co_24', 'co_204', 'co_224', 'SeriesC_pn 060', 'co_183', 'co_93', 'SeriesB_pn 062', 'SeriesA_pn 028', 'SeriesC_pn 104', 'SeriesA_pn 064', 'SeriesC_pn 089', 'SeriesC_pn 101', 'SeriesC_pn 117', 'co_132', 'co_208', 'SeriesA_pn 065', 'SeriesC_pn 035', 'SeriesC_pn 114', 'Series D part number 1', 'co_54', 'co_114', 'SeriesC_pn 054', 'Series D part number 67', 'SeriesB_pn 011', 'SeriesC_pn 116', 'SeriesA_pn 010', 'SeriesC_pn 038', 'co_125', 'SeriesC_pn 080', 'SeriesC_pn 097', 'co_186', 'SeriesC_pn 037', 'SeriesC_pn 039', 'co_64', 'co_60', 'None', 'SeriesC_pn 011', 'co_11', 'Series D part number 123', 'co_5', 'Series D part number 145', 'co_65', 'co_34', 'co_149', 'Series D part number 152', 'SeriesC_pn 119', 'SeriesC_pn 029', 'SeriesC_pn 027', 'SeriesC_pn 023', 'SeriesA_pn 062', 'co_95', 'Series D part number 64', 'co_37', 'co_210', 'SeriesA_pn 018', 'co_223', 'SeriesC_pn 109', 'co_228', 'co_236', 'co_57', 'co_80', 'co_79', 'co_1', 'Series D part number 158', 'SeriesB_pn 035', 'SeriesC_pn 081', 'co_16', 'SeriesB_pn 063', 'Series D part number 117', 'co_62', 'SeriesC_pn 088', 'SeriesA_pn 019', 'Series D part number 149', 'Series D part number 90', 'co_216', 'SeriesC_pn 105', 'Series D part number 42', 'SeriesB_pn 046', 'Series D part number 109', 'SeriesA_pn 046', 'SeriesC_pn 002', 'co_105', 'co_221', 'SeriesC_pn 121', 'SeriesB_pn 007', 'Series D part number 150', 'co_63', 'Series D part number 101', 'Series D part number 80', 'Series D part number 144', 'SeriesB_pn 014', 'co_169', 'co_136', 'SeriesB_pn 036', 'SeriesC_pn 072', 'co_226', 'co_110', 'SeriesA_pn 069', 'SeriesA_pn 067', 'SeriesC_pn 091', 'SeriesA_pn 030', 'Series D part number 84', 'SeriesC_pn 113', 'co_49', 'SeriesC_pn 090', 'Series D part number 17', 'SeriesC_pn 025', 'co_135', 'SeriesB_pn 006', 'SeriesC_pn 049', 'co_126', 'SeriesC_pn 074', 'SeriesA_pn 057', 'co_188', 'SeriesB_pn 041', 'co_33', 'SeriesC_pn 015', 'co_67', 'co_72', 'co_150', 'co_48', 'co_184', 'SeriesC_pn 095', 'co_26', 'SeriesB_pn 032', 'Series D part number 130', 'co_177', 'SeriesA_pn 050', 'SeriesA_pn 054', 'SeriesC_pn 004', 'Series D part number 133', 'Series D part number 99', 'SeriesC_pn 057', 'Series D part number 50', 'co_53', 'co_74', 'co_2', 'Series D part number 49', 'co_99', 'co_50', 'co_180', 'SeriesB_pn 018', 'co_234', 'Series D part number 16', 'SeriesC_pn 106', 'Series D part number 29', 'co_134', 'co_146', 'SeriesC_pn 012', 'SeriesC_pn 053', 'SeriesB_pn 010', 'Series D part number 34', 'SeriesC_pn 086', 'SeriesB_pn 028', 'co_115', 'SeriesC_pn 010', 'SeriesA_pn 072', 'SeriesB_pn 047', 'SeriesA_pn 055', 'co_89', 'Series D part number 126', 'co_189', 'Series D part number 113', 'co_84', 'Series D part number 114', 'SeriesA_pn 015', 'co_14', 'Series D part number 19', 'Series D part number 31', 'SeriesC_pn 076', 'co_44', 'SeriesC_pn 061', 'SeriesC_pn 120', 'Series D part number 129', 'Series D part number 62', 'Series D part number 119', 'SeriesA_pn 003', 'co_129', 'SeriesA_pn 060', 'Series D part number 95', 'SeriesB_pn 056', 'SeriesB_pn 021', 'SeriesC_pn 085', 'co_18', 'Series D part number 66', 'Series D part number 151', 'co_85', 'Series D part number 153', 'Series D part number 141', 'Series D part number 14', 'co_162', 'co_111', 'SeriesB_pn 022', 'Series D part number 3', 'co_139', 'SeriesA_pn 032', 'co_59', 'Series D part number 25', 'SeriesB_pn 049', 'Series D part number 161', 'SeriesC_pn 051', 'SeriesB_pn 038', 'SeriesA_pn 009', 'co_87', 'Series D part number 40', 'Series D part number 21', 'SeriesB_pn 030', 'co_215', 'SeriesC_pn 041', 'co_205', 'SeriesB_pn 054', 'SeriesC_pn 094', 'co_103', 'co_142', 'Series D part number 75', 'co_12', 'Series D part number 12', 'SeriesC_pn 068', 'SeriesC_pn 016', 'SeriesC_pn 062', 'Series D part number 160', 'Series D part number 7', 'co_47', 'co_51', 'co_207', 'co_219', 'SeriesB_pn 001', 'SeriesB_pn 025', 'co_19', 'SeriesB_pn 004', 'co_235', 'co_13', 'SeriesC_pn 079', 'co_45', 'co_237', 'SeriesA_pn 012', 'SeriesA_pn 026', 'co_17', 'Series D part number 77', 'SeriesA_pn 004'}
# keywords = {'stp', 'with', 'tool', 'use', 'cap', 'None', 'mate', '2D', 'used', 'drawing', '3D', 'protection', 'together'}
parameters = {}
keywords = {}

def create_connection():
    try:
        conn = sqlite3.connect(path.join(ROOT, "answers_small.db"))
        return conn
    except Error as e:
        print(e)

    return None

def get_distinct_items( colmun_name):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        sql ="SELECT DISTINCT "+ colmun_name +" from answers"
        cur.execute(sql)
        rows = cur.fetchall()
        items = ["%s" % x for x in rows]

    return items

def genaric_keywords_iteration(cur, selected_item_1, selected_item_2, selected_keywords ):
    for i in range(len(selected_keywords)):
        for j in range(i + 1, len(selected_keywords)):
            sql =" SELECT detailedanswer from answers WHERE parameter1 = '"+ selected_item_1 +"' AND parameter2 = '"+ selected_item_2 +"' and keyword1 = '"+selected_keywords[i]+"' AND keyword2 = '"+selected_keywords[j]+"'"
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows)> 0:
                return (rows[0])[0]
            sql =" SELECT detailedanswer from answers WHERE parameter1 = '"+ selected_item_1 +"' AND parameter2 = '"+ selected_item_2 +"' and keyword1 = '"+selected_keywords[j]+"' AND keyword2 = '"+selected_keywords[i]+"'"
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows)> 0:
                return (rows[0])[0]
    return False

def genaric_cat3(cur, selected_items, selected_keywords):
    for i in range(len(selected_items)):
        for j in range(i + 1, len(selected_items)):
            answer = genaric_keywords_iteration(cur, selected_items[i], selected_items[j], selected_keywords)
            if(answer):
                return answer
            answer = genaric_keywords_iteration(cur, selected_items[j], selected_items[i], selected_keywords)
            if (answer):
                return answer
    return False

def execute_sql(selected_items, selected_keyword):

    conn = create_connection()
    with conn:
        cur = conn.cursor()
        if len(selected_items) == 1:
            if len(selected_keyword) == 1:
                # Four attempts
                sql = "SELECT detailedanswer FROM answers WHERE  keyword1 = '"+selected_keyword[0]+"' AND parameter1 = '"+selected_items[0]+"' AND keyword2 is NULL AND parameter2 is NULL"
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows)>0:
                    return (rows[0])[0]
                else:
                    sql = "SELECT detailedanswer FROM answers WHERE  keyword2 = '"+selected_keyword[0]+"' AND parameter1 = '"+selected_items[0]+"' AND keyword1 is NULL AND parameter2 is NULL"
                    cur.execute(sql)
                    rows = cur.fetchall()
                    if len(rows)>0:
                        return (rows[0])[0]
                    else:
                        sql = "SELECT detailedanswer FROM answers WHERE  keyword1 = '"+selected_keyword[0]+"' AND parameter2 = '"+selected_items[0]+"' AND keyword2 is NULL AND parameter1 is NULL"
                        cur.execute(sql)
                        rows = cur.fetchall()
                        if len(rows)>0:
                            return (rows[0])[0]
                        else:
                            sql = "SELECT detailedanswer FROM answers WHERE  keyword2 = '"+selected_keyword[0]+"' AND parameter2 = '"+selected_items[0]+"' AND keyword1 is NULL AND parameter1 is NULL"
                            cur.execute(sql)
                            rows = cur.fetchall()
                            if len(rows)>0:
                                return (rows[0])[0]
            elif len(selected_keyword) == 2:
                # Four attempts
                sql = "SELECT detailedanswer FROM answers WHERE  lower(keyword1) = '"+selected_keyword[0]+"' AND parameter1 = '"+selected_items[0]+"' AND keyword2 = '"+selected_keyword[1]+"' AND parameter2 is NULL"
                # print(sql)
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) > 0:
                    return (rows[0])[0]
                else:
                    sql = "SELECT detailedanswer FROM answers WHERE  lower(keyword1) = '"+selected_keyword[0]+"' AND parameter2 = '"+selected_items[0]+"' AND keyword2 = '"+selected_keyword[1]+"' AND parameter1 is NULL"
                    # print(sql)
                    cur.execute(sql)
                    rows = cur.fetchall()
                    if len(rows) > 0:
                        return (rows[0])[0]
                    else:
                        sql = "SELECT detailedanswer FROM answers WHERE  lower(keyword2) = '"+selected_keyword[0]+"' AND parameter1 = '"+selected_items[0]+"' AND keyword1 = '"+selected_keyword[1]+"' AND parameter2 is NULL"
                        # print(sql)
                        cur.execute(sql)
                        rows = cur.fetchall()
                        if len(rows) > 0:
                            return (rows[0])[0]
                        else:
                            sql = "SELECT detailedanswer FROM answers WHERE  lower(keyword2) = '"+selected_keyword[0]+"' AND parameter2 = '"+selected_items[0]+"' AND keyword1 = '"+selected_keyword[1]+"' AND parameter1 is NULL"
                            # print(sql)
                            cur.execute(sql)
                            rows = cur.fetchall()
                            if len(rows) > 0:
                                return (rows[0])[0]

        elif len(selected_items) == 2:
            if len(selected_keyword) == 1:
                # Four attempts
                sql = "SELECT detailedanswer FROM answers WHERE  keyword1 = '"+selected_keyword[0]+"' AND parameter1 = '"+selected_items[0]+"' AND keyword2 is NULL AND parameter2 = '"+selected_items[1]+"'"
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) > 0:
                    return (rows[0])[0]
                else:
                    sql = "SELECT detailedanswer FROM answers WHERE  keyword1 = '"+selected_keyword[0]+"' AND parameter2 = '"+selected_items[0]+"' AND keyword2 is NULL AND parameter1 = '"+selected_items[1]+"'"
                    cur.execute(sql)
                    rows = cur.fetchall()
                    if len(rows) > 0:
                        return (rows[0])[0]
                    else:
                        sql = "SELECT detailedanswer FROM answers WHERE  keyword2 = '"+selected_keyword[0]+"' AND parameter1 = '"+selected_items[0]+"' AND keyword1 is NULL AND parameter2 = '"+selected_items[1]+"'"
                        cur.execute(sql)
                        rows = cur.fetchall()
                        if len(rows) > 0:
                            return (rows[0])[0]
                        else:
                            sql = "SELECT detailedanswer FROM answers WHERE  keyword2 = '"+selected_keyword[0]+"' AND parameter2 = '"+selected_items[0]+"' AND keyword1 is NULL AND parameter1 = '"+selected_items[1]+"'"
                            cur.execute(sql)
                            rows = cur.fetchall()
                            if len(rows) > 0:
                                return (rows[0])[0]
            elif len(selected_keyword) >= 2:
                return genaric_cat3(cur, selected_items, selected_keyword)
    return False

def get_answer(var_question):

    var_items_1 = get_distinct_items('parameter1')
    var_items_2 = get_distinct_items('parameter2')
    var_items = set( var_items_1 ) | set(var_items_2)

    var_keywords_1 = get_distinct_items('keyword1')
    var_keywords_2 = get_distinct_items('keyword2')
    all_keywords = set( var_keywords_1 ) | set(var_keywords_2)

    var_questoin = var_question.lower()
    selected_items = []
    selected_keyword = []

    for x in var_items:
        if(x.lower() in var_questoin.lower()):
            selected_items.append(x.lower())
            for y in selected_items:
                if y.lower() in x.lower():
                    if y.lower() != x.lower():
                        selected_items.remove(y.lower())
                if x.lower() in y.lower():
                    if y.lower() != x.lower():
                        if x.lower() in selected_items:
                            selected_items.remove(x.lower())

    for x in all_keywords:
        if(x.lower() in var_questoin.lower()):
            selected_keyword.append(x.lower())
            for y in selected_keyword:
                if y.lower() in x.lower():
                    if y.lower() != x.lower():
                        selected_keyword.remove(y.lower())
                if x.lower() in y.lower():
                    if y.lower() != x.lower():
                        if x.lower() in selected_keyword:
                            selected_keyword.remove(x.lower())

    return execute_sql(selected_items, selected_keyword)

# while True:
#     print(get_answer(input('Q: ')))

# SeriesA_pn 044 can be used together with SeriesA_pn 043
