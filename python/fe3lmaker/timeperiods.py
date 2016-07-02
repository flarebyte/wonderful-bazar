#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-03-07.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import devutils

#http://en.wikipedia.org/wiki/List_of_time_periods
timeperiods={
"0c9d2792-67b0-4029-8bc0-896fee6542d7":('67b0', '0c9d2792-67b0-4029-8bc0-896fee6542d7', 'First Century', 'First Century', ['First Century','1C']),
"5bd3e770-5d73-4c47-a601-61f9c8d54d4a":('5d73', '5bd3e770-5d73-4c47-a601-61f9c8d54d4a', 'Second Century', 'Second Century', ['Second Century','2C']),
"e0db7d58-0e0d-4c5e-aca6-9460651d18cb":('0e0d', 'e0db7d58-0e0d-4c5e-aca6-9460651d18cb', 'MuromachiPeriod', 'Muromachi period', ['Muromachi period']),
"fb875be7-44cd-4f17-8baa-f2673691f55c":('44cd', 'fb875be7-44cd-4f17-8baa-f2673691f55c', 'Third Century', 'Third Century', ['Third Century','3C']),
"12e65065-0aa9-4486-b89d-43c1d72bf252":('0aa9', '12e65065-0aa9-4486-b89d-43c1d72bf252', 'Fourth Century', 'Fourth Century', ['Fourth Century','4C']),
"a8a98726-7081-45e5-a170-6b3a1cef3e3b":('7081', 'a8a98726-7081-45e5-a170-6b3a1cef3e3b', 'InformationAge', 'Information Age', ['Information Age']),
"e2de5b0c-a22d-411d-a18a-879d34ac8551":('a22d', 'e2de5b0c-a22d-411d-a18a-879d34ac8551', 'HoysalaEmpire', 'Hoysala Empire', ['Hoysala Empire']),
"c6a238d4-9f89-4223-9e7e-96b106dd633b":('9f89', 'c6a238d4-9f89-4223-9e7e-96b106dd633b', 'MiddlePaleolithic', 'Middle Paleolithic', ['Middle Paleolithic']),
"66508070-3cb5-4571-a9a3-60a44361435f":('3cb5', '66508070-3cb5-4571-a9a3-60a44361435f', 'Fifth Century', 'Fifth Century', ['Fifth Century','5C']),
"13c42279-a2f4-40bd-a22e-09304805bb4a":('a2f4', '13c42279-a2f4-40bd-a22e-09304805bb4a', 'VikingAge', 'Viking Age', ['Viking Age']),
"a68fb522-a7b9-4019-b0a6-b28fd2bc9607":('a7b9', 'a68fb522-a7b9-4019-b0a6-b28fd2bc9607', 'StoneAge', 'Stone Age', ['Stone Age']),
"d1755551-6bb4-4d02-89e0-204feb1878d2":('6bb4', 'd1755551-6bb4-4d02-89e0-204feb1878d2', 'LateIntermediate', 'Late Intermediate', ['Late Intermediate']),
"4e3bf87a-634e-4482-9cc4-222702e28c1b":('634e', '4e3bf87a-634e-4482-9cc4-222702e28c1b', 'SuiDynasty', 'Sui Dynasty', ['Sui Dynasty']),
"b5a9e44c-9ae4-42f7-9d5e-47077aa6b941":('9ae4', 'b5a9e44c-9ae4-42f7-9d5e-47077aa6b941', 'GildedAge', 'Gilded Age', ['Gilded Age']),
"d0eb42b4-759e-47b4-a820-2620cd9151e2":('759e', 'd0eb42b4-759e-47b4-a820-2620cd9151e2', 'HighMiddleAges', 'High Middle Ages', ['High Middle Ages']),
"d5db609f-2b01-4d76-bd1c-07c15a7a7010":('2b01', 'd5db609f-2b01-4d76-bd1c-07c15a7a7010', 'NapoleonicEra', 'Napoleonic Era', ['Napoleonic Era']),
"c177de59-f74d-4b98-85f8-0a627defaa35":('f74d', 'c177de59-f74d-4b98-85f8-0a627defaa35', 'Mesolithic', 'Mesolithic', ['Mesolithic']),
"119d4fa3-21e7-4150-aea1-25dddcdc3a55":('21e7', '119d4fa3-21e7-4150-aea1-25dddcdc3a55', 'AncientGreece', 'Ancient Greece', ['Ancient Greece']),
"17c4edb4-3a8e-4c82-890c-585e39bb0260":('3a8e', '17c4edb4-3a8e-4c82-890c-585e39bb0260', 'Seventh Century', 'Seventh Century', ['Seventh Century','7C']),
"dd4c761e-cf8e-4a98-86e2-878f76dde659":('cf8e', 'dd4c761e-cf8e-4a98-86e2-878f76dde659', 'Chenla', 'Chenla', ['Chenla']),
"9c76e768-1506-45b7-b4ce-6f3d7aa20406":('1506', '9c76e768-1506-45b7-b4ce-6f3d7aa20406', 'NewKingdom', 'New Kingdom', ['New Kingdom']),
"b8c9193f-db79-48fa-8fe6-cbd6673e2e2d":('db79', 'b8c9193f-db79-48fa-8fe6-cbd6673e2e2d', 'YayoiPeriod', 'Yayoi period', ['Yayoi period']),
"53ff55b7-58e6-4199-a29b-1eb322f68a90":('58e6', '53ff55b7-58e6-4199-a29b-1eb322f68a90', 'OldKingdom', 'Old Kingdom', ['Old Kingdom']),
"82c03ca1-3426-4022-ade1-9dd24f4bca2d":('3426', '82c03ca1-3426-4022-ade1-9dd24f4bca2d', 'LateMiddleAges', 'Late Middle Ages', ['Late Middle Ages']),
"4f91932d-a6f8-499b-8783-13b70f63d2e8":('a6f8', '4f91932d-a6f8-499b-8783-13b70f63d2e8', 'MachineAge', 'Machine Age', ['Machine Age']),
"694b459b-ae02-46b5-9d64-6ab8a6ed92be":('ae02', '694b459b-ae02-46b5-9d64-6ab8a6ed92be', 'HistoricalPeriod', 'Historical period', ['Historical period']),
"19a4e702-177e-434c-ae85-8d9e2f0f6616":('177e', '19a4e702-177e-434c-ae85-8d9e2f0f6616', 'Tarumanagara', 'Tarumanagara', ['Tarumanagara']),
"dec4bbcc-044a-488b-9538-4b48150b6914":('044a', 'dec4bbcc-044a-488b-9538-4b48150b6914', 'Eighth Century', 'Eighth Century', ['Eighth Century','8C']),
"c66ec508-5711-43d3-8394-c1a6899d074f":('5711', 'c66ec508-5711-43d3-8394-c1a6899d074f', 'PetrineEra', 'Petrine Era', ['Petrine Era']),
"b590a152-c8be-494e-9688-64fc52fbeac5":('c8be', 'b590a152-c8be-494e-9688-64fc52fbeac5', 'KamakuraPeriod', 'Kamakura period', ['Kamakura period']),
"65cb3232-76c3-4ed9-b9ff-2f86499b3674":('76c3', '65cb3232-76c3-4ed9-b9ff-2f86499b3674', 'EarlyIntermediate', 'Early Intermediate', ['Early Intermediate']),
"3165bec8-e997-4b7e-b577-ea70d5f9e5ab":('e997', '3165bec8-e997-4b7e-b577-ea70d5f9e5ab', 'MingDynasty', 'Ming Dynasty', ['Ming Dynasty']),
"145038c2-559c-49e0-bbbe-7a013f1d47e1":('559c', '145038c2-559c-49e0-bbbe-7a013f1d47e1', 'Ninth Century', 'Ninth Century', ['Ninth Century']),
"faf67a3d-d408-4d60-b910-285e1e73a578":('d408', 'faf67a3d-d408-4d60-b910-285e1e73a578', 'KhmerEmpire', 'Khmer Empire', ['Khmer Empire']),
"e51c1ec5-2715-43d1-a206-62408d74149b":('2715', 'e51c1ec5-2715-43d1-a206-62408d74149b', 'KingdomOfMataram', 'Kingdom of Mataram', ['Kingdom of Mataram']),
"15512b42-ecb7-49a0-b5ad-adff4e05ce29":('ecb7', '15512b42-ecb7-49a0-b5ad-adff4e05ce29', 'BronzeAge', 'Bronze Age', ['Bronze Age']),
"d1dd78d7-0877-4f02-beff-2166b07fe802":('0877', 'd1dd78d7-0877-4f02-beff-2166b07fe802', 'Tenth Century', 'Tenth Century', ['Tenth Century','10C']),
"4d63bd7a-62e7-4337-b832-9f81408f086e":('62e7', '4d63bd7a-62e7-4337-b832-9f81408f086e', 'Eleventh Century', 'Eleventh Century', ['Eleventh Century','11C']),
"7cff8267-6d3f-4b5d-8535-822b5c38f969":('6d3f', '7cff8267-6d3f-4b5d-8535-822b5c38f969', 'HeianPeriod', 'Heian period', ['Heian period']),
"f083493a-f650-48e0-8b8f-e4738fcefb31":('f650', 'f083493a-f650-48e0-8b8f-e4738fcefb31', 'Paleolithic', 'Paleolithic', ['Paleolithic']),
"b2090d05-8a76-4229-b360-fbf7d3960919":('8a76', 'b2090d05-8a76-4229-b360-fbf7d3960919', 'Mesopotamia', 'Mesopotamia', ['Mesopotamia']),
"b3d89676-7cf2-45f8-8f96-01befde7fd7e":('7cf2', 'b3d89676-7cf2-45f8-8f96-01befde7fd7e', 'MughalEmpire', 'Mughal Empire', ['Mughal Empire']),
"667f91a1-9a4c-4d79-b30a-3993437d63ec":('9a4c', '667f91a1-9a4c-4d79-b30a-3993437d63ec', 'AncientRome', 'Ancient Rome', ['Ancient Rome']),
"b4690579-cd97-470e-9a75-4df1d5106e17":('cd97', 'b4690579-cd97-470e-9a75-4df1d5106e17', 'LiaoDynasty', 'Liao Dynasty', ['Liao Dynasty']),
"1a3aad89-324d-4f9f-84bc-5936e2ee010e":('324d', '1a3aad89-324d-4f9f-84bc-5936e2ee010e', 'IndustrialRevolution', 'Industrial Revolution', ['Industrial Revolution']),
"d1aa2307-edd2-44d7-9d0d-ad9396e8d2af":('edd2', 'd1aa2307-edd2-44d7-9d0d-ad9396e8d2af', 'KingdomOfSunda ', 'Kingdom of Sunda ', ['Kingdom of Sunda']),
"58616686-2f00-497a-b1c7-f5719439fd92":('2f00', '58616686-2f00-497a-b1c7-f5719439fd92', 'Prehistory', 'Prehistory', ['Prehistory']),
"5b72999b-ac18-4bc8-8dda-df4ec39d4975":('ac18', '5b72999b-ac18-4bc8-8dda-df4ec39d4975', 'ClassicEras', 'Classic and Postclassic eras', ['Classic and Postclassic eras']),
"7cc26428-4a4a-4e64-b99c-61b1d851eab1":('4a4a', '7cc26428-4a4a-4e64-b99c-61b1d851eab1', 'Singhasari', 'Singhasari', ['Singhasari']),
"e6206b57-72d8-4c69-960c-45692e7db34c":('72d8', 'e6206b57-72d8-4c69-960c-45692e7db34c', 'HoloceneEpoch', 'Holocene epoch', ['Holocene epoch']),
"330988de-9981-4706-a5cb-236457c99f93":('9981', '330988de-9981-4706-a5cb-236457c99f93', 'ColdWar', 'Cold War', ['Cold War']),
"1498fe93-2b1d-4fd0-a8b4-37b76218f021":('2b1d', '1498fe93-2b1d-4fd0-a8b4-37b76218f021', 'RomanticEra', 'Romantic Era', ['Romantic Era']),
"1e2b212a-f3eb-4312-a6c9-5997f2b6d67a":('f3eb', '1e2b212a-f3eb-4312-a6c9-5997f2b6d67a', 'MeijiPeriod', 'Meiji period', ['Meiji period']),
"6b2a4f48-fb31-4a77-b419-818eb7c833b7":('fb31', '6b2a4f48-fb31-4a77-b419-818eb7c833b7', 'QingDynasty', 'Qing dynasty', ['Qing dynasty']),
"6b86e9a8-f402-476e-b7c0-d978355ef8fb":('f402', '6b86e9a8-f402-476e-b7c0-d978355ef8fb', 'VedicPeriod', 'Vedic period', ['Vedic period']),
"9b8f1c85-ae6d-4fb8-b418-57ec5a38d5f8":('ae6d', '9b8f1c85-ae6d-4fb8-b418-57ec5a38d5f8', 'JinDynasty', 'Jin Dynasty', ['Jin Dynasty']),
"067614b3-e1fa-4f05-b33e-09aaeae4d298":('e1fa', '067614b3-e1fa-4f05-b33e-09aaeae4d298', 'Twelfth Century', 'Twelfth Century', ['Twelfth Century']),
"13df5393-bbd4-4a82-accc-4f68f3fc4278":('bbd4', '13df5393-bbd4-4a82-accc-4f68f3fc4278', 'AtomicAge', 'Atomic Age', ['Atomic Age']),
"6b94dd33-8a8a-45cb-b21c-62bb96f783b8":('8a8a', '6b94dd33-8a8a-45cb-b21c-62bb96f783b8', 'Neolithic', 'Neolithic', ['Neolithic']),
"25e22ec4-c371-48c2-a6cd-ab6ea995ca01":('c371', '25e22ec4-c371-48c2-a6cd-ab6ea995ca01', 'Kediri', 'Kediri', ['Kediri']),
"08a71b53-27dc-4831-9025-43c94bc29b72":('27dc', '08a71b53-27dc-4831-9025-43c94bc29b72', 'JacobeanEra', 'Jacobean Era', ['Jacobean Era']),
"ac0f4f2b-aa7d-43ba-80cf-34253685d414":('aa7d', 'ac0f4f2b-aa7d-43ba-80cf-34253685d414', 'LowerPaleolithic', 'Lower Paleolithic', ['Lower Paleolithic']),
"2370b813-b20b-4dba-aef1-11d71401bfed":('b20b', '2370b813-b20b-4dba-aef1-11d71401bfed', 'DarkAge', 'Dark Age', ['Dark Age']),
"c55adc16-06ae-406a-8ea1-79fc783d4f37":('06ae', 'c55adc16-06ae-406a-8ea1-79fc783d4f37', 'ElizabethanPeriod', 'Elizabethan period', ['Elizabethan period']),
"62e00d9a-88e5-456a-a7b5-e1aeb697bb17":('88e5', '62e00d9a-88e5-456a-a7b5-e1aeb697bb17', 'WWI', 'World War I', ['World War I','WWI']),
"34138405-f909-417f-89be-8715494996ea":('f909', '34138405-f909-417f-89be-8715494996ea', 'XIII Century', 'XIII Century', ['XIII Century','13C']),
"5f216bf8-b821-40b1-b392-7fb97bf2f682":('b821', '5f216bf8-b821-40b1-b392-7fb97bf2f682', 'SpaceAge', 'Space Age', ['Space Age']),
"6804c402-53a6-47d0-9b6b-6ac142ecf3c1":('53a6', '6804c402-53a6-47d0-9b6b-6ac142ecf3c1', 'IslamicGoldenAge', 'Islamic Golden Age', ['Islamic Golden Age']),
"d216abbf-73f6-4ca7-b774-82cf4191ed0e":('73f6', 'd216abbf-73f6-4ca7-b774-82cf4191ed0e', 'XIV Century', 'XIV Century', ['XIV Century','14C']),
"f2083a26-ec35-4923-8f55-cb1989833847":('ec35', 'f2083a26-ec35-4923-8f55-cb1989833847', 'XV Century', 'XV Century', ['XV Century','15C']),
"6a1662da-8961-45cc-b4c5-c8f3105178d2":('8961', '6a1662da-8961-45cc-b4c5-c8f3105178d2', 'NaraPeriod', 'Nara period', ['Nara period']),
"dac4d30d-6861-4c57-a21e-59df4d719d0e":('6861', 'dac4d30d-6861-4c57-a21e-59df4d719d0e', 'MigrationPeriod', 'Migration period', ['Migration period']),
"8e03d925-a376-48e0-be0c-477187926bdd":('a376', '8e03d925-a376-48e0-be0c-477187926bdd', 'XVI Century', 'XVI Century', ['XVI Century','16C']),
"944f189b-c51e-4de9-842a-b86a0dbb7536":('c51e', '944f189b-c51e-4de9-842a-b86a0dbb7536', 'TokugawaShogunate', 'Tokugawa shogunate', ['Tokugawa shogunate']),
"3fcbf0ce-0b88-4ae9-b111-78172a99f5bc":('0b88', '3fcbf0ce-0b88-4ae9-b111-78172a99f5bc', 'CopperAge', 'Copper Age', ['Copper Age']),
"ba01220e-e248-409d-9d86-927461b71efd":('e248', 'ba01220e-e248-409d-9d86-927461b71efd', 'XVII Century', 'XVII Century', ['XVII Century','17C']),
"20d74140-3f89-483c-9222-481d7b737522":('3f89', '20d74140-3f89-483c-9222-481d7b737522', 'AgeOfOil', 'Age of Oil', ['Age of Oil']),
"f4f97f06-553f-4341-a73f-61af7896f5db":('553f', 'f4f97f06-553f-4341-a73f-61af7896f5db', 'PalaEmpire', 'Pala Empire', ['Pala Empire']),
"2495012f-6e4d-4320-9970-9fea28d40c37":('6e4d', '2495012f-6e4d-4320-9970-9fea28d40c37', 'XVIII Century', 'XVIII Century', ['XVIII Century','18C']),
"479dc27f-9386-42f7-aae2-02ebb92fd882":('9386', '479dc27f-9386-42f7-aae2-02ebb92fd882', 'Middle Kingdom', 'Middle Kingdom', ['Middle Kingdom']),
"9f7d291d-8cc2-4bd8-9843-3ac5d2845271":('8cc2', '9f7d291d-8cc2-4bd8-9843-3ac5d2845271', 'TangDynasty', 'Tang Dynasty', ['Tang Dynasty']),
"ce2825d9-e86d-491f-9612-87d2903bfd61":('e86d', 'ce2825d9-e86d-491f-9612-87d2903bfd61', 'AgeOfDiscovery', 'Age of Discovery', ['Age of Discovery']),
"7a3251c4-aecc-4760-9455-e5ec623c2b65":('aecc', '7a3251c4-aecc-4760-9455-e5ec623c2b65', 'ProtestantReformation', 'Protestant Reformation', ['Protestant Reformation']),
"e6655617-32a1-4b10-84bd-e49f8527e74d":('32a1', 'e6655617-32a1-4b10-84bd-e49f8527e74d', 'Rashtrakuta', 'Rashtrakuta', ['Rashtrakuta']),
"7dc117d5-55b8-4c11-a8be-b1cde1f4f1be":('55b8', '7dc117d5-55b8-4c11-a8be-b1cde1f4f1be', 'GeorgianEra', 'Georgian Era', ['Georgian Era']),
"7afc6865-0755-4e26-b1bf-72decfc27a5f":('0755', '7afc6865-0755-4e26-b1bf-72decfc27a5f', 'CopticPeriod', 'Coptic period', ['Coptic period']),
"f2c4bd5a-2a3a-4abb-b2f1-4bf1240e58f6":('2a3a', 'f2c4bd5a-2a3a-4abb-b2f1-4bf1240e58f6', 'GuptaEmpire', 'Gupta Empire', ['Gupta Empire']),
"5477a33a-c71a-48d1-afa7-11135fc6f45a":('c71a', '5477a33a-c71a-48d1-afa7-11135fc6f45a', 'IronAge', 'Iron Age', ['Iron Age']),
"c5b986b8-2ef3-4af5-9e14-4f9f06ab8989":('2ef3', 'c5b986b8-2ef3-4af5-9e14-4f9f06ab8989', 'EdwardianPeriod', 'Edwardian period', ['Edwardian period']),
"e464c309-16a5-4a73-b649-25e8b7d2b151":('16a5', 'e464c309-16a5-4a73-b649-25e8b7d2b151', 'XIX Century', 'XIX Century', ['XIX Century','19C']),
"7a69c0c6-39b9-45fe-84f7-1bcce9cbc811":('39b9', '7a69c0c6-39b9-45fe-84f7-1bcce9cbc811', 'KofunPeriod', 'Kofun period', ['Kofun period']),
"e5ccef1b-08fb-4aac-b76d-343527fada17":('08fb', 'e5ccef1b-08fb-4aac-b76d-343527fada17', 'UpperPalaeolithic', 'Upper Palaeolithic', ['Upper Palaeolithic']),
"9a8def64-bd26-42f4-9159-a8dbc81fa421":('bd26', '9a8def64-bd26-42f4-9159-a8dbc81fa421', 'AgeOfEnlightenment', 'The Age of Enlightenment', ['The Age of Enlightenment']),
"71cc2cd8-ddc0-4685-8ab3-30d8390b9a2f":('ddc0', '71cc2cd8-ddc0-4685-8ab3-30d8390b9a2f', 'IndusValleyCivilization', 'Indus Valley Civilization', ['Indus Valley Civilization']),
"84bb0833-aad6-4a0f-a87c-5cee00194f16":('aad6', '84bb0833-aad6-4a0f-a87c-5cee00194f16', 'PostModern', 'Post-Modern', ['Post-Modern']),
"6be3393d-9e92-43c9-932d-85f4e736f08d":('9e92', '6be3393d-9e92-43c9-932d-85f4e736f08d', 'XX Century', 'XX Century', ['XX Century','20C']),
"b36aa02e-5d08-4f7c-9db7-dfe437fe8867":('5d08', 'b36aa02e-5d08-4f7c-9db7-dfe437fe8867', 'ZhouDynasty', 'Zhou Dynasty', ['Zhou Dynasty']),
"559ddffa-fb88-4a09-a96d-c997929b1809":('fb88', '559ddffa-fb88-4a09-a96d-c997929b1809', 'WWII', 'World War II', ['World War II','WWII']),
"41a86894-54a2-4b92-ab68-4d86f93bf515":('54a2', '41a86894-54a2-4b92-ab68-4d86f93bf515', 'Epipaleolithic', 'Epipaleolithic', ['Epipaleolithic']),
"579ffbf8-4b82-4620-9069-10b4d8a63817":('4b82', '579ffbf8-4b82-4620-9069-10b4d8a63817', 'WesternXia', 'Western Xia', ['Western Xia']),
"8c340121-accb-4d60-ae49-9f95d353d2d4":('accb', '8c340121-accb-4d60-ae49-9f95d353d2d4', 'PeriodOfFiveDynastiesAndTenKingdoms', 'Period of Five Dynasties and Ten Kingdoms', ['Period of Five Dynasties and Ten Kingdoms']),
"c53e3165-eafd-4aa2-a98b-6645d115d18b":('eafd', 'c53e3165-eafd-4aa2-a98b-6645d115d18b', 'MiddleHorizon', 'Middle Horizon', ['Middle Horizon']),
"25beff23-4dd1-4512-b854-61f283b351fc":('4dd1', '25beff23-4dd1-4512-b854-61f283b351fc', 'ProgressiveEra', 'Progressive era', ['Progressive era']),
"2bc1f078-4daf-440e-8d73-3232bce517fb":('4daf', '2bc1f078-4daf-440e-8d73-3232bce517fb', 'SongDynasty', 'Song Dynasty', ['Song Dynasty']),
"94b4396f-e445-4988-9578-0577ea4f1b73":('e445', '94b4396f-e445-4988-9578-0577ea4f1b73', 'Sixth Century', 'Sixth Century', ['Sixth Century','6C']),
"d7ebac67-1855-46bd-9d27-d60232527f15":('1855', 'd7ebac67-1855-46bd-9d27-d60232527f15', 'ShangDynasty', 'Shang Dynasty', ['Shang Dynasty']),
"21408bdc-afd5-452f-ad9e-0c1a5420c334":('afd5', '21408bdc-afd5-452f-ad9e-0c1a5420c334', 'Renaissance', 'Renaissance', ['Renaissance']),
"a8d50c62-1ad3-4c18-affd-588cd3c892e6":('1ad3', 'a8d50c62-1ad3-4c18-affd-588cd3c892e6', 'KakatiyaEmpire', 'Kakatiya Empire', ['Kakatiya Empire']),
"b27b0c21-f544-4af8-9a2b-06b7aac81010":('f544', 'b27b0c21-f544-4af8-9a2b-06b7aac81010', 'ModernEra', 'Modern era', ['Modern era']),
"d9517bea-2f9d-47e1-ad7e-1b0950ea0d46":('2f9d', 'd9517bea-2f9d-47e1-ad7e-1b0950ea0d46', 'Srivijaya', 'Srivijaya', ['Srivijaya']),
"e7f59afd-af72-408f-b259-7089d14dc5cd":('af72', 'e7f59afd-af72-408f-b259-7089d14dc5cd', 'AzuchiMomoyamaPeriod', 'Azuchi-Momoyama period', ['Azuchi-Momoyama period']),
"d9c8b0eb-638f-4588-b8b9-1a2a36b37b0f":('638f', 'd9c8b0eb-638f-4588-b8b9-1a2a36b37b0f', 'Majapahit', 'Majapahit', ['Majapahit']),
"dc7e0b30-191f-4c0f-a10c-ada0ecb3460d":('191f', 'dc7e0b30-191f-4c0f-a10c-ada0ecb3460d', 'SpanishHegemony', 'Spanish hegemony', ['Spanish hegemony']),
"42ff0ed4-d7ad-45d4-a8bf-5b74c4ddf44a":('d7ad', '42ff0ed4-d7ad-45d4-a8bf-5b74c4ddf44a', 'InterwarPeriod', 'Interwar period', ['Interwar period']),
"68b54c00-45c9-49c2-9630-c2835376746a":('45c9', '68b54c00-45c9-49c2-9630-c2835376746a', 'YuanDynasty', 'Yuan Dynasty', ['Yuan Dynasty']),
"64c45366-2e0b-468a-acb4-8ad03c8df229":('2e0b', '64c45366-2e0b-468a-acb4-8ad03c8df229', 'BritishHegemony', 'British hegemony', ['British hegemony']),
"46c0abd4-b143-419d-8b96-9ede8e0dcbff":('b143', '46c0abd4-b143-419d-8b96-9ede8e0dcbff', 'Colonialism', 'colonialism', ['colonialism']),
"bf8e2109-237f-483f-a688-5e662e5d6729":('237f', 'bf8e2109-237f-483f-a688-5e662e5d6729', 'PleistoceneEpoch', 'Pleistocene epoch', ['Pleistocene epoch']),
"136deeca-3b41-478f-96bf-5d2a27ab824f":('3b41', '136deeca-3b41-478f-96bf-5d2a27ab824f', 'VictorianEra', 'Victorian era', ['Victorian era']),
"8efe8b1c-0c31-4aff-90df-2f2f12222ce3":('0c31', '8efe8b1c-0c31-4aff-90df-2f2f12222ce3', 'Sailendra', 'Sailendra', ['Sailendra']),
"32949538-fee7-45f7-a48d-f90605af2667":('fee7', '32949538-fee7-45f7-a48d-f90605af2667', 'XXI Century', 'XXI Century', ['XXI Century','21C']),
"0aa74f03-b695-477b-819f-5142b84b320f":('b695', '0aa74f03-b695-477b-819f-5142b84b320f', 'LateHorizon', 'Late Horizon', ['Late Horizon']),
"c1abdea5-61b0-4f7a-8c47-c5cf9d149ffd":('61b0', 'c1abdea5-61b0-4f7a-8c47-c5cf9d149ffd', 'AsukaPeriod', 'Asuka period', ['Asuka period']),
"87000219-6b5c-49ab-9bc0-ba0ba38a01a6":('6b5c', '87000219-6b5c-49ab-9bc0-ba0ba38a01a6', 'OttomanEmpire', 'Ottoman Empire', ['Ottoman Empire']),
}

PERIOD_YEAR_START,PERIOD_YEAR_END,PERIOD_COUNTRIES,PERIOD_OLD_COUNTRIES=range(4)

timeperiodsrange={
"e0db7d58-0e0d-4c5e-aca6-9460651d18cb":(1333,1573,["JP"],[]), # Muromachi period
"a8a98726-7081-45e5-a170-6b3a1cef3e3b":(1970,2025,[],[]), # Information Age
"e2de5b0c-a22d-411d-a18a-879d34ac8551":(1026,1343,["IN"],[]), # Hoysala Empire
"c6a238d4-9f89-4223-9e7e-96b106dd633b":(-300000,-30000,[],[]), # Middle Paleolithic
"13c42279-a2f4-40bd-a22e-09304805bb4a":(793,1066,["EU"],[]), # Viking Age
"a68fb522-a7b9-4019-b0a6-b28fd2bc9607":(-2000000,-4000,["EU"],[]), # Stone Age
"d1755551-6bb4-4d02-89e0-204feb1878d2":(1000,1476,["PE"],[]), # Late Intermediate
"4e3bf87a-634e-4482-9cc4-222702e28c1b":(None,None,["EU"],[]), # Sui Dynasty
"b5a9e44c-9ae4-42f7-9d5e-47077aa6b941":(None,None,["EU"],[]), # Gilded Age
"d0eb42b4-759e-47b4-a820-2620cd9151e2":(None,None,["EU"],[]), # High Middle Ages
"d5db609f-2b01-4d76-bd1c-07c15a7a7010":(None,None,["EU"],[]), # Napoleonic Era
"c177de59-f74d-4b98-85f8-0a627defaa35":(None,None,["EU"],[]), # Mesolithic
"119d4fa3-21e7-4150-aea1-25dddcdc3a55":(None,None,["EU"],[]), # Ancient Greece
"dd4c761e-cf8e-4a98-86e2-878f76dde659":(None,None,["EU"],[]), # Chenla
"9c76e768-1506-45b7-b4ce-6f3d7aa20406":(None,None,["EU"],[]), # New Kingdom
"b8c9193f-db79-48fa-8fe6-cbd6673e2e2d":(None,None,["EU"],[]), # Yayoi period
"53ff55b7-58e6-4199-a29b-1eb322f68a90":(None,None,["EU"],[]), # Old Kingdom
"82c03ca1-3426-4022-ade1-9dd24f4bca2d":(None,None,["EU"],[]), # Late Middle Ages
"4f91932d-a6f8-499b-8783-13b70f63d2e8":(None,None,["EU"],[]), # Machine Age
"694b459b-ae02-46b5-9d64-6ab8a6ed92be":(None,None,["EU"],[]), # Historical period
"19a4e702-177e-434c-ae85-8d9e2f0f6616":(None,None,["EU"],[]), # Tarumanagara
"c66ec508-5711-43d3-8394-c1a6899d074f":(None,None,["EU"],[]), # Petrine Era
"b590a152-c8be-494e-9688-64fc52fbeac5":(None,None,["EU"],[]), # Kamakura period
"65cb3232-76c3-4ed9-b9ff-2f86499b3674":(None,None,["EU"],[]), # Early Intermediate
"3165bec8-e997-4b7e-b577-ea70d5f9e5ab":(None,None,["EU"],[]), # Ming Dynasty
"faf67a3d-d408-4d60-b910-285e1e73a578":(None,None,["EU"],[]), # Khmer Empire
"e51c1ec5-2715-43d1-a206-62408d74149b":(None,None,["EU"],[]), # Kingdom of Mataram
"15512b42-ecb7-49a0-b5ad-adff4e05ce29":(None,None,["EU"],[]), # Bronze Age
"7cff8267-6d3f-4b5d-8535-822b5c38f969":(None,None,["EU"],[]), # Heian period
"f083493a-f650-48e0-8b8f-e4738fcefb31":(None,None,["EU"],[]), # Paleolithic
"b2090d05-8a76-4229-b360-fbf7d3960919":(-3500,-559,["EU"],[]), # Mesopotamia
"b3d89676-7cf2-45f8-8f96-01befde7fd7e":(None,None,["EU"],[]), # Mughal Empire
"667f91a1-9a4c-4d79-b30a-3993437d63ec":(None,None,["EU"],[]), # Ancient Rome
"b4690579-cd97-470e-9a75-4df1d5106e17":(None,None,["EU"],[]), # Liao Dynasty
"1a3aad89-324d-4f9f-84bc-5936e2ee010e":(None,None,["EU"],[]), # Industrial Revolution
"d1aa2307-edd2-44d7-9d0d-ad9396e8d2af":(None,None,["EU"],[]), # Kingdom of Sunda 
"58616686-2f00-497a-b1c7-f5719439fd92":(None,None,["EU"],[]), # Prehistory
"5b72999b-ac18-4bc8-8dda-df4ec39d4975":(None,None,["EU"],[]), # Classic and Postclassic eras
"7cc26428-4a4a-4e64-b99c-61b1d851eab1":(None,None,["EU"],[]), # Singhasari
"e6206b57-72d8-4c69-960c-45692e7db34c":(None,None,["EU"],[]), # Holocene epoch
"330988de-9981-4706-a5cb-236457c99f93":(None,None,["EU"],[]), # Cold War
"1498fe93-2b1d-4fd0-a8b4-37b76218f021":(None,None,["EU"],[]), # Romantic Era
"6b2a4f48-fb31-4a77-b419-818eb7c833b7":(None,None,["EU"],[]), # Qing dynasty
"6b86e9a8-f402-476e-b7c0-d978355ef8fb":(None,None,["EU"],[]), # Vedic period
"9b8f1c85-ae6d-4fb8-b418-57ec5a38d5f8":(None,None,["EU"],[]), # Jin Dynasty
"13df5393-bbd4-4a82-accc-4f68f3fc4278":(None,None,["EU"],[]), # Atomic Age
"6b94dd33-8a8a-45cb-b21c-62bb96f783b8":(None,None,["EU"],[]), # Neolithic
"25e22ec4-c371-48c2-a6cd-ab6ea995ca01":(None,None,["EU"],[]), # Kediri
"08a71b53-27dc-4831-9025-43c94bc29b72":(None,None,["EU"],[]), # Jacobean Era
"ac0f4f2b-aa7d-43ba-80cf-34253685d414":(None,None,["EU"],[]), # Lower Paleolithic
"2370b813-b20b-4dba-aef1-11d71401bfed":(None,None,["EU"],[]), # Dark Age
"c55adc16-06ae-406a-8ea1-79fc783d4f37":(None,None,["EU"],[]), # Elizabethan period
"62e00d9a-88e5-456a-a7b5-e1aeb697bb17":(None,None,["EU"],[]), # World War I
"5f216bf8-b821-40b1-b392-7fb97bf2f682":(None,None,["EU"],[]), # Space Age
"6804c402-53a6-47d0-9b6b-6ac142ecf3c1":(None,None,["EU"],[]), # Islamic Golden Age
"6a1662da-8961-45cc-b4c5-c8f3105178d2":(None,None,["EU"],[]), # Nara period
"dac4d30d-6861-4c57-a21e-59df4d719d0e":(None,None,["EU"],[]), # Migration period
"944f189b-c51e-4de9-842a-b86a0dbb7536":(None,None,["EU"],[]), # Tokugawa shogunate
"3fcbf0ce-0b88-4ae9-b111-78172a99f5bc":(None,None,["EU"],[]), # Copper Age
"20d74140-3f89-483c-9222-481d7b737522":(None,None,["EU"],[]), # Age of Oil
"f4f97f06-553f-4341-a73f-61af7896f5db":(None,None,["EU"],[]), # Pala Empire
"479dc27f-9386-42f7-aae2-02ebb92fd882":(None,None,["EU"],[]), # Middle Kingdom
"9f7d291d-8cc2-4bd8-9843-3ac5d2845271":(None,None,["EU"],[]), # Tang Dynasty
"ce2825d9-e86d-491f-9612-87d2903bfd61":(None,None,["EU"],[]), # Age of Discovery
"7a3251c4-aecc-4760-9455-e5ec623c2b65":(None,None,["EU"],[]), # Protestant Reformation
"e6655617-32a1-4b10-84bd-e49f8527e74d":(None,None,["EU"],[]), # Rashtrakuta
"7dc117d5-55b8-4c11-a8be-b1cde1f4f1be":(None,None,["EU"],[]), # Georgian Era
"7afc6865-0755-4e26-b1bf-72decfc27a5f":(None,None,["EU"],[]), # Coptic period
"f2c4bd5a-2a3a-4abb-b2f1-4bf1240e58f6":(None,None,["EU"],[]), # Gupta Empire
"5477a33a-c71a-48d1-afa7-11135fc6f45a":(None,None,["EU"],[]), # Iron Age
"c5b986b8-2ef3-4af5-9e14-4f9f06ab8989":(None,None,["EU"],[]), # Edwardian period
"7a69c0c6-39b9-45fe-84f7-1bcce9cbc811":(None,None,["EU"],[]), # Kofun period
"e5ccef1b-08fb-4aac-b76d-343527fada17":(None,None,["EU"],[]), # Upper Palaeolithic
"9a8def64-bd26-42f4-9159-a8dbc81fa421":(None,None,["EU"],[]), # The Age of Enlightenment
"71cc2cd8-ddc0-4685-8ab3-30d8390b9a2f":(None,None,["EU"],[]), # Indus Valley Civilization
"84bb0833-aad6-4a0f-a87c-5cee00194f16":(None,None,["EU"],[]), # Post-Modern
"b36aa02e-5d08-4f7c-9db7-dfe437fe8867":(None,None,["EU"],[]), # Zhou Dynasty
"559ddffa-fb88-4a09-a96d-c997929b1809":(None,None,["EU"],[]), # World War II
"41a86894-54a2-4b92-ab68-4d86f93bf515":(None,None,["EU"],[]), # Epipaleolithic
"579ffbf8-4b82-4620-9069-10b4d8a63817":(None,None,["EU"],[]), # Western Xia
"8c340121-accb-4d60-ae49-9f95d353d2d4":(None,None,["EU"],[]), # Period of Five Dynasties and Ten Kingdoms
"c53e3165-eafd-4aa2-a98b-6645d115d18b":(None,None,["EU"],[]), # Middle Horizon
"25beff23-4dd1-4512-b854-61f283b351fc":(None,None,["EU"],[]), # Progressive era
"2bc1f078-4daf-440e-8d73-3232bce517fb":(None,None,["EU"],[]), # Song Dynasty
"d7ebac67-1855-46bd-9d27-d60232527f15":(None,None,["EU"],[]), # Shang Dynasty
"21408bdc-afd5-452f-ad9e-0c1a5420c334":(None,None,["EU"],[]), # Renaissance
"a8d50c62-1ad3-4c18-affd-588cd3c892e6":(None,None,["EU"],[]), # Kakatiya Empire
"b27b0c21-f544-4af8-9a2b-06b7aac81010":(None,None,["EU"],[]), # Modern era
"d9517bea-2f9d-47e1-ad7e-1b0950ea0d46":(None,None,["EU"],[]), # Srivijaya
"e7f59afd-af72-408f-b259-7089d14dc5cd":(None,None,["EU"],[]), # Azuchi-Momoyama period
"d9c8b0eb-638f-4588-b8b9-1a2a36b37b0f":(None,None,["EU"],[]), # Majapahit
"dc7e0b30-191f-4c0f-a10c-ada0ecb3460d":(None,None,["EU"],[]), # Spanish hegemony
"42ff0ed4-d7ad-45d4-a8bf-5b74c4ddf44a":(None,None,["EU"],[]), # Interwar period
"68b54c00-45c9-49c2-9630-c2835376746a":(None,None,["EU"],[]), # Yuan Dynasty
"64c45366-2e0b-468a-acb4-8ad03c8df229":(None,None,["EU"],[]), # British hegemony
"46c0abd4-b143-419d-8b96-9ede8e0dcbff":(None,None,["EU"],[]), # colonialism
"bf8e2109-237f-483f-a688-5e662e5d6729":(None,None,["EU"],[]), # Pleistocene epoch
"136deeca-3b41-478f-96bf-5d2a27ab824f":(None,None,["EU"],[]), # Victorian era
"8efe8b1c-0c31-4aff-90df-2f2f12222ce3":(None,None,["EU"],[]), # Sailendra
"1e2b212a-f3eb-4312-a6c9-5997f2b6d67a":(None,None,["EU"],[]), # Meiji period
"0aa74f03-b695-477b-819f-5142b84b320f":(None,None,["EU"],[]), # Late Horizon
"c1abdea5-61b0-4f7a-8c47-c5cf9d149ffd":(None,None,["EU"],[]), # Asuka period
"87000219-6b5c-49ab-9bc0-ba0ba38a01a6":(None,None,["EU"],[]), # Ottoman Empire
}
