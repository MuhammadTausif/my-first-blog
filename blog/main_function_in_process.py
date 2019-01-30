import sqlite3
from os import path
from sqlite3 import Error

ROOT = path.dirname(path.realpath(__file__))

parameter1 = {'SeriesC_pn 001', 'SeriesC_pn 002', 'SeriesC_pn 003', 'SeriesC_pn 004', 'SeriesC_pn 005',
              'SeriesC_pn 006', 'SeriesC_pn 007', 'SeriesC_pn 008', 'SeriesC_pn 009', 'SeriesC_pn 010',
              'SeriesC_pn 011', 'SeriesC_pn 012', 'SeriesC_pn 013', 'SeriesC_pn 014', 'SeriesC_pn 015',
              'SeriesC_pn 016', 'SeriesC_pn 017', 'SeriesC_pn 018', 'SeriesC_pn 019', 'SeriesC_pn 020',
              'SeriesC_pn 021', 'SeriesC_pn 022', 'SeriesC_pn 023', 'SeriesC_pn 024', 'SeriesC_pn 025',
              'SeriesC_pn 026', 'SeriesC_pn 027', 'SeriesC_pn 028', 'SeriesC_pn 029', 'SeriesC_pn 030',
              'SeriesC_pn 031', 'SeriesC_pn 032', 'SeriesC_pn 033', 'SeriesC_pn 034', 'SeriesC_pn 035',
              'SeriesC_pn 036', 'SeriesC_pn 037', 'SeriesC_pn 038', 'SeriesC_pn 039', 'SeriesC_pn 040',
              'SeriesC_pn 041', 'SeriesC_pn 042', 'SeriesC_pn 043', 'SeriesC_pn 044', 'SeriesC_pn 045',
              'SeriesC_pn 046', 'SeriesC_pn 047', 'SeriesC_pn 048', 'SeriesC_pn 049', 'SeriesC_pn 050',
              'SeriesC_pn 051', 'SeriesC_pn 052', 'SeriesC_pn 053', 'SeriesC_pn 054', 'SeriesC_pn 055',
              'SeriesC_pn 056', 'SeriesC_pn 057', 'SeriesC_pn 058', 'SeriesC_pn 059', 'SeriesC_pn 060',
              'SeriesC_pn 061', 'SeriesC_pn 062', 'SeriesC_pn 063', 'SeriesC_pn 064', 'SeriesC_pn 065',
              'SeriesC_pn 066', 'SeriesC_pn 067', 'SeriesC_pn 068', 'SeriesC_pn 069', 'SeriesC_pn 070',
              'SeriesC_pn 071', 'SeriesC_pn 072', 'SeriesC_pn 073', 'SeriesC_pn 074', 'SeriesC_pn 075',
              'SeriesC_pn 076', 'SeriesC_pn 077', 'SeriesC_pn 078', 'SeriesC_pn 079', 'SeriesC_pn 080',
              'SeriesC_pn 081', 'SeriesC_pn 082', 'SeriesC_pn 083', 'SeriesC_pn 084', 'SeriesC_pn 085',
              'SeriesC_pn 086', 'SeriesC_pn 087', 'SeriesC_pn 088', 'SeriesC_pn 089', 'SeriesC_pn 090',
              'SeriesC_pn 091', 'SeriesC_pn 092', 'SeriesC_pn 093', 'SeriesC_pn 094', 'SeriesC_pn 095',
              'SeriesC_pn 096', 'SeriesC_pn 097', 'SeriesC_pn 098', 'SeriesC_pn 099', 'SeriesC_pn 100',
              'SeriesC_pn 101', 'SeriesC_pn 102', 'SeriesC_pn 103', 'SeriesC_pn 104', 'SeriesC_pn 105',
              'SeriesC_pn 106', 'SeriesC_pn 107', 'SeriesC_pn 108', 'SeriesC_pn 109', 'SeriesC_pn 110',
              'SeriesC_pn 111', 'SeriesC_pn 112', 'SeriesC_pn 113', 'SeriesC_pn 114', 'SeriesC_pn 115',
              'SeriesC_pn 116', 'SeriesC_pn 117', 'SeriesC_pn 118', 'SeriesC_pn 119', 'SeriesC_pn 120',
              'SeriesC_pn 121', 'Series D part number 1', 'Series D part number 2', 'Series D part number 3',
              'Series D part number 4', 'Series D part number 5', 'Series D part number 6', 'Series D part number 7',
              'Series D part number 88', 'Series D part number 89', 'Series D part number 90',
              'Series D part number 91', 'Series D part number 92', 'Series D part number 8', 'Series D part number 9',
              'Series D part number 10', 'Series D part number 11', 'Series D part number 12',
              'Series D part number 13', 'Series D part number 14', 'Series D part number 15',
              'Series D part number 16', 'Series D part number 17', 'Series D part number 93',
              'Series D part number 94', 'Series D part number 95', 'Series D part number 18',
              'Series D part number 19', 'Series D part number 20', 'Series D part number 21',
              'Series D part number 22', 'Series D part number 23', 'Series D part number 24',
              'Series D part number 25', 'Series D part number 26', 'Series D part number 27',
              'Series D part number 28', 'Series D part number 29', 'Series D part number 30',
              'Series D part number 31', 'Series D part number 32', 'Series D part number 33',
              'Series D part number 34', 'Series D part number 96', 'Series D part number 97',
              'Series D part number 98', 'Series D part number 99', 'Series D part number 35',
              'Series D part number 36', 'Series D part number 37', 'Series D part number 38',
              'Series D part number 39', 'Series D part number 40', 'Series D part number 41',
              'Series D part number 42', 'Series D part number 43', 'Series D part number 44',
              'Series D part number 45', 'Series D part number 46', 'Series D part number 47',
              'Series D part number 48', 'Series D part number 49', 'Series D part number 50',
              'Series D part number 51', 'Series D part number 52', 'Series D part number 53',
              'Series D part number 54', 'Series D part number 55', 'Series D part number 56',
              'Series D part number 57', 'Series D part number 58', 'Series D part number 59',
              'Series D part number 60', 'Series D part number 61', 'Series D part number 62',
              'Series D part number 63', 'Series D part number 64', 'Series D part number 65',
              'Series D part number 66', 'Series D part number 67', 'Series D part number 68',
              'Series D part number 69', 'Series D part number 100', 'Series D part number 101',
              'Series D part number 70', 'Series D part number 71', 'Series D part number 72',
              'Series D part number 73', 'Series D part number 74', 'Series D part number 75',
              'Series D part number 76', 'Series D part number 77', 'Series D part number 78',
              'Series D part number 79', 'Series D part number 80', 'Series D part number 81',
              'Series D part number 82', 'Series D part number 83', 'Series D part number 84',
              'Series D part number 85', 'Series D part number 86', 'Series D part number 87',
              'Series D part number 150', 'Series D part number 154', 'Series D part number 158',
              'Series D part number 159', 'Series D part number 160', 'Series D part number 161', 'SeriesA_pn 001',
              'SeriesA_pn 002', 'SeriesA_pn 003', 'SeriesA_pn 004', 'SeriesA_pn 005', 'SeriesA_pn 006',
              'SeriesA_pn 007', 'SeriesA_pn 008', 'SeriesA_pn 009', 'SeriesA_pn 010', 'SeriesA_pn 011',
              'SeriesA_pn 012', 'SeriesA_pn 013', 'SeriesA_pn 014', 'SeriesA_pn 015', 'SeriesA_pn 016',
              'SeriesA_pn 017', 'SeriesA_pn 018', 'SeriesA_pn 019', 'SeriesA_pn 020', 'SeriesA_pn 021',
              'SeriesA_pn 022', 'SeriesA_pn 023', 'SeriesA_pn 024', 'SeriesA_pn 025', 'SeriesA_pn 026',
              'SeriesA_pn 027', 'SeriesA_pn 028', 'SeriesA_pn 029', 'SeriesA_pn 030', 'SeriesA_pn 031',
              'SeriesA_pn 032', 'SeriesA_pn 033', 'SeriesA_pn 034', 'SeriesA_pn 035', 'SeriesA_pn 036',
              'SeriesA_pn 037', 'SeriesA_pn 038', 'SeriesA_pn 039', 'SeriesA_pn 040', 'SeriesA_pn 041',
              'SeriesA_pn 042', 'SeriesA_pn 043', 'SeriesA_pn 044', 'SeriesA_pn 045', 'SeriesA_pn 046',
              'SeriesA_pn 047', 'SeriesA_pn 048', 'SeriesA_pn 049', 'SeriesA_pn 050', 'SeriesA_pn 051',
              'SeriesA_pn 052', 'SeriesA_pn 053', 'SeriesA_pn 054', 'SeriesA_pn 055', 'SeriesA_pn 056',
              'SeriesA_pn 057', 'SeriesA_pn 058', 'SeriesA_pn 059', 'SeriesA_pn 060', 'SeriesA_pn 061',
              'SeriesA_pn 062', 'SeriesA_pn 063', 'SeriesA_pn 064', 'SeriesA_pn 065', 'SeriesA_pn 066',
              'SeriesA_pn 067', 'SeriesA_pn 068', 'SeriesA_pn 069', 'SeriesA_pn 070', 'SeriesA_pn 071',
              'SeriesA_pn 072', 'co_1', 'co_2', 'co_3', 'co_4', 'co_5', 'co_6', 'co_7', 'co_8', 'co_9', 'co_10',
              'co_11', 'co_12', 'co_13', 'co_14', 'co_15', 'co_16', 'co_17', 'co_18', 'co_19', 'co_20', 'co_21',
              'co_22', 'co_23', 'co_24', 'co_25', 'co_26', 'co_27', 'co_28', 'co_29', 'co_30', 'co_31', 'co_32',
              'co_33', 'co_34', 'co_35', 'co_36', 'co_37', 'co_38', 'co_39', 'co_40', 'co_41', 'co_42', 'co_43',
              'co_44', 'co_45', 'co_46', 'co_47', 'co_48', 'co_49', 'co_50', 'co_51', 'co_52', 'co_53', 'co_54',
              'co_55', 'co_56', 'co_57', 'co_58', 'co_59', 'co_60', 'co_61', 'co_62', 'co_63', 'co_64', 'co_65',
              'co_66', 'co_67', 'co_68', 'co_69', 'co_70', 'co_71', 'co_72', 'co_73', 'co_74', 'co_75', 'co_76',
              'co_77', 'co_78', 'co_79', 'co_80', 'co_81', 'co_82', 'co_83', 'co_84', 'co_85', 'co_86', 'co_87',
              'co_88', 'co_89', 'co_90', 'co_91', 'co_92', 'co_93', 'co_94', 'co_95', 'co_96', 'co_97', 'co_98',
              'co_99', 'co_100', 'co_101', 'co_102', 'co_103', 'co_104', 'co_105', 'co_106', 'co_107', 'co_108',
              'co_109', 'co_110', 'co_111', 'co_112', 'co_113', 'co_114', 'co_115', 'co_116', 'co_117', 'co_118',
              'co_119', 'co_120', 'co_121', 'co_122', 'co_123', 'co_124', 'co_125', 'co_126', 'co_127', 'co_128',
              'co_129', 'co_130', 'co_131', 'co_132', 'co_133', 'co_134', 'co_135', 'co_136', 'co_137', 'co_138',
              'co_139', 'co_140', 'co_141', 'co_142', 'co_143', 'co_144', 'co_145', 'co_146', 'co_147', 'co_148',
              'co_149', 'co_150', 'co_151', 'co_152', 'co_153', 'co_154', 'co_155', 'co_156', 'co_157', 'co_158',
              'co_159', 'co_160', 'co_161', 'co_162', 'co_163', 'co_164', 'co_165', 'co_166', 'co_167', 'co_168',
              'co_169', 'co_170', 'co_171', 'co_172', 'co_173', 'co_174', 'co_175', 'co_176', 'co_177', 'co_178',
              'co_179', 'co_180', 'co_181', 'co_182', 'co_183', 'co_184', 'co_185', 'co_186', 'co_187', 'co_188',
              'co_189', 'co_190', 'co_191', 'co_192', 'co_193', 'co_194', 'co_195', 'co_196', 'co_197', 'co_198',
              'co_199', 'co_200', 'co_201', 'co_202', 'co_203', 'co_204', 'co_205', 'co_206', 'co_207', 'co_208',
              'co_209', 'co_210', 'co_211', 'co_212', 'co_213', 'co_214', 'co_215', 'co_216', 'co_217', 'co_218',
              'co_219', 'co_220', 'co_221', 'co_222', 'co_223', 'co_224', 'co_225', 'co_226', 'co_227', 'co_228',
              'co_229', 'co_230', 'co_231', 'co_232', 'co_233', 'co_234', 'co_235', 'co_236', 'co_237', 'co_238',
              'co_239', 'co_240', 'None', 'SeriesB_pn 001', 'SeriesB_pn 002', 'SeriesB_pn 003', 'SeriesB_pn 004',
              'SeriesB_pn 005', 'SeriesB_pn 006', 'SeriesB_pn 007', 'SeriesB_pn 008', 'SeriesB_pn 009',
              'SeriesB_pn 010', 'SeriesB_pn 011', 'SeriesB_pn 012', 'SeriesB_pn 013', 'SeriesB_pn 014',
              'SeriesB_pn 015', 'SeriesB_pn 016', 'SeriesB_pn 017', 'SeriesB_pn 018', 'SeriesB_pn 019',
              'SeriesB_pn 020', 'SeriesB_pn 021', 'SeriesB_pn 022', 'SeriesB_pn 023', 'SeriesB_pn 024',
              'SeriesB_pn 025', 'SeriesB_pn 026', 'SeriesB_pn 027', 'SeriesB_pn 028', 'SeriesB_pn 029',
              'SeriesB_pn 030', 'SeriesB_pn 031', 'SeriesB_pn 032', 'SeriesB_pn 033', 'SeriesB_pn 034',
              'SeriesB_pn 035', 'SeriesB_pn 036', 'SeriesB_pn 037', 'SeriesB_pn 038', 'SeriesB_pn 039',
              'SeriesB_pn 040', 'SeriesB_pn 041', 'SeriesB_pn 042', 'SeriesB_pn 043', 'SeriesB_pn 044',
              'SeriesB_pn 045', 'SeriesB_pn 046', 'SeriesB_pn 047', 'SeriesB_pn 048', 'SeriesB_pn 049',
              'SeriesB_pn 050', 'SeriesB_pn 051', 'SeriesB_pn 052', 'SeriesB_pn 053', 'SeriesB_pn 054',
              'SeriesB_pn 055', 'SeriesB_pn 056', 'SeriesB_pn 057', 'SeriesB_pn 058', 'SeriesB_pn 059',
              'SeriesB_pn 060', 'SeriesB_pn 061', 'SeriesB_pn 062', 'SeriesB_pn 063', 'Series D part number 102',
              'Series D part number 103', 'Series D part number 104', 'Series D part number 105',
              'Series D part number 106', 'Series D part number 107', 'Series D part number 108',
              'Series D part number 109', 'Series D part number 110', 'Series D part number 111',
              'Series D part number 112', 'Series D part number 113', 'Series D part number 114',
              'Series D part number 115', 'Series D part number 116', 'Series D part number 117',
              'Series D part number 118', 'Series D part number 119', 'Series D part number 120',
              'Series D part number 121', 'Series D part number 122', 'Series D part number 123',
              'Series D part number 124', 'Series D part number 125', 'Series D part number 126',
              'Series D part number 127', 'Series D part number 128', 'Series D part number 129',
              'Series D part number 130', 'Series D part number 131', 'Series D part number 132',
              'Series D part number 133', 'Series D part number 134', 'Series D part number 135',
              'Series D part number 136', 'Series D part number 137', 'Series D part number 138',
              'Series D part number 139', 'Series D part number 140', 'Series D part number 141',
              'Series D part number 142', 'Series D part number 143', 'Series D part number 144',
              'Series D part number 145', 'Series D part number 146', 'Series D part number 147',
              'Series D part number 148', 'Series D part number 149', 'Series D part number 151',
              'Series D part number 152', 'Series D part number 153', 'Series D part number 155',
              'Series D part number 156', 'Series D part number 157'}
parameter2 = {'None', 'SeriesC_pn 075', 'SeriesC_pn 076', 'SeriesC_pn 077', 'SeriesC_pn 078', 'SeriesC_pn 079',
              'SeriesC_pn 080', 'SeriesC_pn 081', 'SeriesC_pn 082', 'SeriesC_pn 083', 'SeriesC_pn 084',
              'SeriesC_pn 085', 'SeriesC_pn 086', 'SeriesC_pn 087', 'SeriesC_pn 088', 'SeriesC_pn 089',
              'SeriesC_pn 090', 'SeriesC_pn 091', 'SeriesC_pn 092', 'SeriesC_pn 093', 'SeriesC_pn 094',
              'SeriesC_pn 095', 'SeriesC_pn 096', 'SeriesC_pn 097', 'SeriesC_pn 098', 'SeriesC_pn 099',
              'SeriesC_pn 100', 'SeriesC_pn 101', 'SeriesC_pn 102', 'SeriesC_pn 103', 'SeriesC_pn 104',
              'SeriesC_pn 105', 'SeriesC_pn 106', 'SeriesC_pn 107', 'SeriesC_pn 108', 'SeriesC_pn 109',
              'SeriesC_pn 110', 'SeriesC_pn 111', 'SeriesC_pn 112', 'SeriesC_pn 113', 'SeriesC_pn 114',
              'SeriesC_pn 115', 'SeriesC_pn 116', 'SeriesC_pn 117', 'SeriesC_pn 118', 'SeriesC_pn 119',
              'SeriesC_pn 120', 'SeriesC_pn 121', 'Series D part number 1', 'Series D part number 2',
              'Series D part number 3', 'Series D part number 4', 'Series D part number 5', 'Series D part number 6',
              'Series D part number 7', 'Series D part number 8', 'Series D part number 9', 'Series D part number 10',
              'Series D part number 11', 'Series D part number 12', 'Series D part number 13',
              'Series D part number 14', 'Series D part number 15', 'Series D part number 16',
              'Series D part number 17', 'Series D part number 18', 'Series D part number 19',
              'Series D part number 20', 'Series D part number 21', 'Series D part number 22',
              'Series D part number 23', 'Series D part number 24', 'Series D part number 25',
              'Series D part number 26', 'Series D part number 27', 'Series D part number 28',
              'Series D part number 29', 'Series D part number 30', 'Series D part number 31',
              'Series D part number 32', 'Series D part number 33', 'Series D part number 34',
              'Series D part number 35', 'Series D part number 36', 'Series D part number 37',
              'Series D part number 38', 'Series D part number 39', 'Series D part number 40',
              'Series D part number 41', 'Series D part number 42', 'Series D part number 43',
              'Series D part number 44', 'Series D part number 45', 'Series D part number 46',
              'Series D part number 47', 'Series D part number 48', 'Series D part number 49',
              'Series D part number 50', 'Series D part number 51', 'Series D part number 52',
              'Series D part number 53', 'Series D part number 54', 'Series D part number 55',
              'Series D part number 56', 'Series D part number 57', 'Series D part number 58',
              'Series D part number 59', 'Series D part number 60', 'Series D part number 61',
              'Series D part number 62', 'Series D part number 63', 'Series D part number 64',
              'Series D part number 65', 'Series D part number 66', 'Series D part number 67',
              'Series D part number 68', 'Series D part number 69', 'Series D part number 70',
              'Series D part number 71', 'Series D part number 72', 'Series D part number 73',
              'Series D part number 74', 'Series D part number 75', 'Series D part number 76',
              'Series D part number 77', 'Series D part number 78', 'Series D part number 79',
              'Series D part number 80', 'Series D part number 81', 'Series D part number 82',
              'Series D part number 83', 'Series D part number 84', 'Series D part number 85',
              'Series D part number 86', 'Series D part number 87', 'Series D part number 88',
              'Series D part number 89', 'Series D part number 90', 'Series D part number 91',
              'Series D part number 92', 'Series D part number 93', 'Series D part number 94',
              'Series D part number 95', 'Series D part number 96', 'Series D part number 97',
              'Series D part number 98', 'Series D part number 99', 'Series D part number 100',
              'Series D part number 101', 'Series D part number 102', 'Series D part number 103',
              'Series D part number 104', 'Series D part number 105', 'Series D part number 106',
              'Series D part number 107', 'Series D part number 108', 'Series D part number 109',
              'Series D part number 110', 'Series D part number 111', 'Series D part number 112',
              'Series D part number 113', 'Series D part number 114', 'Series D part number 115',
              'Series D part number 116', 'Series D part number 117', 'Series D part number 118',
              'Series D part number 119', 'Series D part number 120', 'Series D part number 121',
              'Series D part number 122', 'Series D part number 123', 'Series D part number 124',
              'Series D part number 125', 'Series D part number 126', 'Series D part number 127',
              'Series D part number 128', 'Series D part number 129', 'Series D part number 130',
              'Series D part number 131', 'Series D part number 132', 'Series D part number 133',
              'Series D part number 134', 'Series D part number 135', 'Series D part number 136',
              'Series D part number 137', 'Series D part number 138', 'Series D part number 139',
              'Series D part number 140', 'Series D part number 141', 'Series D part number 142',
              'Series D part number 143', 'Series D part number 144', 'Series D part number 145',
              'Series D part number 146', 'Series D part number 147', 'Series D part number 148',
              'Series D part number 149', 'Series D part number 150', 'Series D part number 151',
              'Series D part number 152', 'Series D part number 153', 'Series D part number 154',
              'Series D part number 155', 'Series D part number 156', 'Series D part number 157',
              'Series D part number 158', 'Series D part number 159', 'Series D part number 160',
              'Series D part number 161', 'SeriesA_pn 001', 'SeriesA_pn 002', 'SeriesA_pn 003', 'SeriesA_pn 004',
              'SeriesA_pn 005', 'SeriesA_pn 006', 'SeriesA_pn 007', 'SeriesA_pn 008', 'SeriesA_pn 009',
              'SeriesA_pn 010', 'SeriesA_pn 011', 'SeriesA_pn 012', 'SeriesA_pn 013', 'SeriesA_pn 014',
              'SeriesA_pn 015', 'SeriesA_pn 016', 'SeriesA_pn 017', 'SeriesA_pn 018', 'SeriesA_pn 019',
              'SeriesA_pn 020', 'SeriesA_pn 021', 'SeriesA_pn 022', 'SeriesA_pn 023', 'SeriesA_pn 024',
              'SeriesA_pn 025', 'SeriesA_pn 026', 'SeriesA_pn 027', 'SeriesA_pn 028', 'SeriesA_pn 029',
              'SeriesA_pn 030', 'SeriesA_pn 031', 'SeriesA_pn 032', 'SeriesA_pn 033', 'SeriesA_pn 034',
              'SeriesA_pn 035', 'SeriesA_pn 036', 'SeriesA_pn 037', 'SeriesA_pn 038', 'SeriesA_pn 039',
              'SeriesA_pn 040', 'SeriesA_pn 041', 'SeriesA_pn 042', 'SeriesA_pn 043', 'SeriesA_pn 044',
              'SeriesA_pn 045', 'SeriesA_pn 046', 'SeriesA_pn 047', 'SeriesA_pn 048', 'SeriesA_pn 049',
              'SeriesA_pn 050', 'SeriesA_pn 051', 'SeriesA_pn 052', 'SeriesA_pn 053', 'SeriesA_pn 054',
              'SeriesA_pn 055', 'SeriesA_pn 056', 'SeriesA_pn 057', 'SeriesA_pn 058', 'SeriesA_pn 059',
              'SeriesA_pn 060', 'SeriesA_pn 061', 'SeriesA_pn 062', 'SeriesA_pn 063', 'SeriesA_pn 064',
              'SeriesA_pn 065', 'SeriesA_pn 066', 'SeriesA_pn 067', 'SeriesA_pn 068', 'SeriesA_pn 069',
              'SeriesA_pn 070', 'SeriesA_pn 071', 'SeriesA_pn 072', 'SeriesB_pn 001', 'SeriesB_pn 002',
              'SeriesB_pn 003', 'SeriesB_pn 004', 'SeriesB_pn 005', 'SeriesB_pn 006', 'SeriesB_pn 007',
              'SeriesB_pn 008', 'SeriesB_pn 009', 'SeriesB_pn 010', 'SeriesB_pn 011', 'SeriesB_pn 012',
              'SeriesB_pn 013', 'SeriesB_pn 014', 'SeriesB_pn 015', 'SeriesB_pn 016', 'SeriesB_pn 017',
              'SeriesB_pn 018', 'SeriesB_pn 019', 'SeriesB_pn 020', 'SeriesB_pn 021', 'SeriesB_pn 022',
              'SeriesB_pn 023', 'SeriesB_pn 024', 'SeriesB_pn 025', 'SeriesB_pn 026', 'SeriesB_pn 027',
              'SeriesB_pn 028', 'SeriesB_pn 029', 'SeriesB_pn 030', 'SeriesB_pn 031', 'SeriesB_pn 032',
              'SeriesB_pn 033', 'SeriesB_pn 034', 'SeriesB_pn 035', 'SeriesB_pn 036', 'SeriesB_pn 037',
              'SeriesB_pn 038', 'SeriesB_pn 039', 'SeriesB_pn 040', 'SeriesB_pn 041', 'SeriesB_pn 042',
              'SeriesB_pn 043', 'SeriesB_pn 044', 'SeriesB_pn 045', 'SeriesB_pn 046', 'SeriesB_pn 047',
              'SeriesB_pn 048', 'SeriesB_pn 049', 'SeriesB_pn 050', 'SeriesB_pn 051', 'SeriesB_pn 052',
              'SeriesB_pn 053', 'SeriesB_pn 054', 'SeriesB_pn 055', 'SeriesB_pn 056', 'SeriesB_pn 057',
              'SeriesB_pn 058', 'SeriesB_pn 059', 'SeriesB_pn 060', 'SeriesB_pn 061', 'SeriesB_pn 062',
              'SeriesB_pn 063', 'SeriesC_pn 001', 'SeriesC_pn 002', 'SeriesC_pn 003', 'SeriesC_pn 004',
              'SeriesC_pn 005', 'SeriesC_pn 006', 'SeriesC_pn 007', 'SeriesC_pn 008', 'SeriesC_pn 009',
              'SeriesC_pn 010', 'SeriesC_pn 011', 'SeriesC_pn 012', 'SeriesC_pn 013', 'SeriesC_pn 014',
              'SeriesC_pn 015', 'SeriesC_pn 016', 'SeriesC_pn 017', 'SeriesC_pn 018', 'SeriesC_pn 019',
              'SeriesC_pn 020', 'SeriesC_pn 021', 'SeriesC_pn 022', 'SeriesC_pn 023', 'SeriesC_pn 024',
              'SeriesC_pn 025', 'SeriesC_pn 026', 'SeriesC_pn 027', 'SeriesC_pn 028', 'SeriesC_pn 029',
              'SeriesC_pn 030', 'SeriesC_pn 031', 'SeriesC_pn 032', 'SeriesC_pn 033', 'SeriesC_pn 034',
              'SeriesC_pn 035', 'SeriesC_pn 036', 'SeriesC_pn 037', 'SeriesC_pn 038', 'SeriesC_pn 039',
              'SeriesC_pn 040', 'SeriesC_pn 041', 'SeriesC_pn 042', 'SeriesC_pn 043', 'SeriesC_pn 044',
              'SeriesC_pn 045', 'SeriesC_pn 046', 'SeriesC_pn 047', 'SeriesC_pn 048', 'SeriesC_pn 049',
              'SeriesC_pn 050', 'SeriesC_pn 051', 'SeriesC_pn 052', 'SeriesC_pn 053', 'SeriesC_pn 054',
              'SeriesC_pn 055', 'SeriesC_pn 056', 'SeriesC_pn 057', 'SeriesC_pn 058', 'SeriesC_pn 059',
              'SeriesC_pn 060', 'SeriesC_pn 061', 'SeriesC_pn 062', 'SeriesC_pn 063', 'SeriesC_pn 064',
              'SeriesC_pn 065', 'SeriesC_pn 066', 'SeriesC_pn 067', 'SeriesC_pn 068', 'SeriesC_pn 069',
              'SeriesC_pn 070', 'SeriesC_pn 071', 'SeriesC_pn 072', 'SeriesC_pn 073'}

keyword1 = {'cap', 'tool', 'None', 'drawing', '3D', 'stp', 'mate', 'used', 'use'}
keyword2 = {'None', 'protection', '2D', 'drawing', 'together', 'with'}

def create_connection():
    try:
        # conn = sqlite3.connect(path.join(ROOT, "corpus.db"))
        conn = sqlite3.connect(path.join(ROOT, "answers.db"))
        conn = sqlite3.connect('answers.db')

        return conn
    except Error as e:
        print(e)

    return None

def get_distinct_items():
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        sql ="SELECT DISTINCT parameter1 from corpus"
        cur.execute(sql)
        rows = cur.fetchall()
        items = ["%s" % x for x in rows]
        items.append('partnumber123')
        items.append('product123')
        items.append('product456')

    return items


def get_distinct_items_and_save():
    conn = create_connection()
    conn = sqlite3.connect(path.join(ROOT, "answers.db"))
    with conn:
        cur = conn.cursor()
        sql = "SELECT DISTINCT keyword1 from answers"
        cur.execute(sql)
        rows = cur.fetchall()
        items = ["%s" % x for x in rows]
        # items.append('partnumber123')
        # items.append('product123')
        # items.append('product456')

        f = open('items_keyword1_from_answers.txt', 'w')
        for item in items:
            f.write("'" + item + "',")
        f.close()

    return items


def get_distinct_answer(parameter1, keyword1, parameter2, keyword2):
    conn = sqlite3.connect('answers.db')
    with conn:
        cur = conn.cursor()
        sql = 'SELECT detailed_answer from answers'
        if (parameter2 == '' and keyword2 == ''):
            sql = "SELECT DISTINCT detailed_answer from answers " \
                  "WHERE parameter1 = '" + parameter1 + "' AND " \
                                                        "parameter2 is null AND " \
                                                        "keyword1 = '" + keyword1 + "' AND " \
                                                                                    "keyword2 is null"
        elif (parameter2 == ''):
            sql = "SELECT DISTINCT detailed_answer from answers " \
                  "WHERE parameter1 = '" + parameter1 + "' AND " \
                                                        "parameter2 is null AND " \
                                                        "keyword1 = '" + keyword1 + "' AND " \
                                                                                    "keyword2 = '" + keyword2 + "' "
        else:
            sql = "SELECT DISTINCT detailed_answer from answers " \
                  "WHERE parameter1 = '" + parameter1 + "' AND " \
                                                        "parameter2 = '" + parameter1 + "' AND " \
                                                                                        "keyword1 = '" + keyword1 + "' AND " \
                                                                                                                    "keyword2 = '" + keyword2 + "' "
        cur.execute(sql)
        rows = cur.fetchall()
        if (len(rows) > 0):
            return rows[0]
        else:
            return 'None'


def get_answer_working(var_question):

    var_items = get_distinct_items()

    var_questoin = var_question.lower()

    selected_items = []
    selected_keyword = []

    keywords_category1 = ['cap','protection', 'tool','available','there','blue','accessories']
    keywords_category2_1 = ['stp','3D', 'drawing','datasheet']
    keywords_category2_2 = ['drawing','2D', 'send','share']
    keywords_category2 = keywords_category2_1 + keywords_category2_2
    keywords_category3_1 = ['mate', 'used', 'use', 'can', 'do']
    keywords_category3_2 = ['together','with', 'togather', 'combined','fit' ]
    keywords_category3 = keywords_category3_1 + keywords_category3_2

    all_keywords = set(keywords_category1) | set(keywords_category2_1) | set(keywords_category2_2)  | set(keywords_category3_1)  | set(keywords_category3_2)  | set(keywords_category2_1)

    for x in var_items:
        if(x.lower() in var_questoin.lower()):
            selected_items.append(x.lower())
            for y in selected_items:
                if y.lower() in x.lower():
                    if y.lower() != x.lower():
                        selected_items.remove(y.lower())
                if x.lower() in y.lower():
                    if y.lower() != x.lower():
                        selected_items.remove(x.lower())

    for x in all_keywords:
        if(x.lower() in var_questoin.lower()):
            selected_keyword.append(x.lower())

    if len(selected_items)==1:
        if(  len(set(keywords_category1) & set(selected_keyword)) > 0):
            if(set(selected_keyword) & {'available','there'}):
                return selected_items[0] + ' ' + selected_keyword[1]+ ' is available.'
            else:
                return selected_items[0] + ' ' +selected_keyword[0]+ ' is available.'
        elif(  len(set(keywords_category2) & set(selected_keyword)) > 0):
            if(set(selected_keyword) & {'send','share'}):
                return 'Please download it from following <a>link</a>.'
    elif len(selected_items) == 2:
        if( len(set(keywords_category3) & set(selected_keyword)) > 0):
            return selected_items[0] + ' and ' + selected_items[1] + ' can be ' + selected_keyword[1]


def get_answer(var_question):
    var_questoin = var_question.lower()

    selected_parameter1 = []
    selected_parameter2 = []
    selected_keyword1 = []
    selected_keyword2 = []

    for x in parameter1:
        if (x.lower() in var_questoin.lower()):
            selected_parameter1.append(x.lower())
            for y in selected_parameter1:
                if y.lower() in x.lower():
                    if y.lower() != x.lower():
                        selected_parameter1.remove(y.lower())
                if x.lower() in y.lower():
                    if y.lower() != x.lower():
                        selected_parameter1.remove(x.lower())

    for x in parameter2:
        if (x.lower() in var_questoin.lower()):
            selected_parameter2.append(x.lower())
            for y in selected_parameter2:
                if y.lower() in x.lower():
                    if y.lower() != x.lower():
                        selected_parameter2.remove(y.lower())
                if x.lower() in y.lower():
                    if y.lower() != x.lower():
                        selected_parameter2.remove(x.lower())

    for x in keyword1:
        if (x.lower() in var_questoin.lower()):
            selected_keyword1.append(x.lower())

    for x in keyword2:
        if (x.lower() in var_questoin.lower()):
            selected_keyword2.append(x.lower())

    if len(selected_parameter1) == 1:
        if len(selected_parameter2) == 0:
            # Catagory1 and Catagory 2
            print(selected_parameter1)
        elif len(selected_parameter2) == 1:
            # Catagory3
            print(selected_parameter1)

    # if len(selected_items) == 1:
    #     if (len(set(keywords_category1) & set(selected_keyword)) > 0):
    #         if (set(selected_keyword) & {'available', 'there'}):
    #             return selected_items[0] + ' ' + selected_keyword[1] + ' is available.'
    #         else:
    #             return selected_items[0] + ' ' + selected_keyword[0] + ' is available.'
    #     elif (len(set(keywords_category2) & set(selected_keyword)) > 0):
    #         if (set(selected_keyword) & {'send', 'share'}):
    #             return 'Please download it from following <a>link</a>.'
    # elif len(selected_items) == 2:
    #     if (len(set(keywords_category3) & set(selected_keyword)) > 0):
    #         return selected_items[0] + ' and ' + selected_items[1] + ' can be ' + selected_keyword[1]


# Practice

var_questoin = 'What is the right cap for SeriesC_pn 001?'
var_questoin = 'What is the right cap for SeriesC_pn 002?'
var_questoin = 'Share 3D drawing Series D part number 157?'
# var_questoin = 'What is the right cap for SeriesA_pn 007?'
# var_questoin = 'What is the right cap for SeriesA_pn 001?'
# var_questoin= 'What is the right cap for Series D part number 1?'
# var_questoin = 'SeriesC_pn 001 and SeriesC_pn 002 can be combined?'
# var_questoin = 'What is the correct protection cap for SeriesC_pn 001?'
# var_questoin ="Send	the	datasheet	of	product123?"
# var_questoin= 'What is the right cap for SeriesC_pn 001?'
var_questoin = 'Is	partnumber123	available	in	blue?'
var_questoin = 'What is the right cap for Series D part number 54?'
var_questoin = 'Can	product123	and	product456	be	combined?'
var_questoin = 'Do SeriesA_pn 006 and SeriesC_pn 080 mate together?'
var_questoin = 'Do SeriesC_pn 004 and Series D part number 92 mate together?'
var_questoin = 'What is the right cap for SeriesC_pn 004?'
# var_questoin = 'Is	partnumber123	available	in	blue?'
# var_questoin = 'Is	there	accessories	for	partnumber123?'
# var_questoin = 'Send	the	datasheet	of	product123'
# var_questoin = 'Can	product123	and	product456	be	combined?'
# var_questoin = 'Do	product123	and	product456	fit	together?'


print(get_answer(var_questoin))
# get_distinct_items_and_save()
# print(get_distinct_answer('SeriesC_pn 001', 'cap', '', 'protection'))
# print(get_distinct_answer('SeriesC_pn 026', 'drawing', '', '2D'))

# while True:
#    print(get_answer(input('Question: ')))
