#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-03-08.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import devutils

arttopics={
"a9eb578b-6bcc-42fb-b2ab-10db1649caa3":('6bcc', 'a9eb578b-6bcc-42fb-b2ab-10db1649caa3', 'photo', 'Photography', ['Photography','Picture','Photograph','Photo']),
"ad22103b-aacc-4967-940f-c38bc19e5bfe":('aacc', 'ad22103b-aacc-4967-940f-c38bc19e5bfe', 'mixmedia', 'Mixmedia art', ['Mixmedia art']),
"cff22e53-916a-4efa-9995-f89108b5ca22":('916a', 'cff22e53-916a-4efa-9995-f89108b5ca22', 'alternative', 'Alternative art', ['Alternative art']),
"59c4d8d1-9e92-4450-ae16-6f45d70032e9":('9e92', '59c4d8d1-9e92-4450-ae16-6f45d70032e9', 'etching', 'Etching', ['Etching']),
"25cb97ba-4e40-43af-a8a3-a649b422d9a8":('4e40', '25cb97ba-4e40-43af-a8a3-a649b422d9a8', 'architecture', 'Architecture', ['Architecture']),
"7428d55f-83a7-4c2a-8b05-f4d171f3a0d4":('83a7', '7428d55f-83a7-4c2a-8b05-f4d171f3a0d4', 'litho', 'Lithography', ['Lithography']),
"1ce4f522-a59f-4e4c-92ae-ec1de8121dda":('a59f', '1ce4f522-a59f-4e4c-92ae-ec1de8121dda', 'street', 'Street art', ['Street art']),
"8b0ffa68-03b0-48a4-8c94-805c41f5e2fb":('03b0', '8b0ffa68-03b0-48a4-8c94-805c41f5e2fb', 'craft', 'Craft', ['Craft']),
"0c24e6ee-f4e2-475f-a6ec-fb64d30f0e2a":('f4e2', '0c24e6ee-f4e2-475f-a6ec-fb64d30f0e2a', 'textile', 'Textiles', ['Textile']),
"6e5f1a86-bc40-4eeb-bcbb-4cbe01274788":('bc40', '6e5f1a86-bc40-4eeb-bcbb-4cbe01274788', 'furniture', 'Furniture', ['Furniture']),
"a288113e-2ec2-4992-a045-08328d7e6267":('2ec2', 'a288113e-2ec2-4992-a045-08328d7e6267', 'typo', 'Typography', ['Typography']),
"03178046-0e4c-49e7-8368-9a4aaa0e8d5f":('0e4c', '03178046-0e4c-49e7-8368-9a4aaa0e8d5f', 'filmmaking', 'Filmmaking', ['Filmmaking']),
"f173ca42-6a6e-4fe4-8dd4-28da6268783d":('6a6e', 'f173ca42-6a6e-4fe4-8dd4-28da6268783d', 'sculpture', 'Sculptures', ['Sculpture']),
"0f08e50a-556e-405c-9d64-afd90be9edf4":('556e', '0f08e50a-556e-405c-9d64-afd90be9edf4', 'illustration', 'Illustrations', ['Illustrations']),
"c642143b-bb53-47a2-9d70-58e612ac63d7":('bb53', 'c642143b-bb53-47a2-9d70-58e612ac63d7', 'painting', 'Paintings', ['Painting']),
"2ccda09f-218a-4aee-8ca1-910a8fb962f5":('218a', '2ccda09f-218a-4aee-8ca1-910a8fb962f5', 'conceptual', 'Conceptual art', ['Conceptual art']),
"13367835-0933-469b-a419-e38bb7b35a05":('0933', '13367835-0933-469b-a419-e38bb7b35a05', 'graphic', 'Graphic art', ['Graphic art']),
"505d7f0e-3ca8-42ff-b4c4-f09757ef0e7f":('3ca8', '505d7f0e-3ca8-42ff-b4c4-f09757ef0e7f', 'drawing', 'Drawings', ['Drawing']),
"b4a31fdb-a93f-4d21-ae09-2d42313a1734":('a93f', 'b4a31fdb-a93f-4d21-ae09-2d42313a1734', 'digital', 'Digital art', ['Digital art']),
"647229d6-8436-4d53-a06f-dad823e5fcbf":('8436', '647229d6-8436-4d53-a06f-dad823e5fcbf', 'comic', 'Comics', ['Comic']),
"322931d0-7207-4916-b0ab-b8e1cfb9e47e":('7207', '322931d0-7207-4916-b0ab-b8e1cfb9e47e', 'installation', 'Installation art', ['Installation art']),
"b431bbba-8ad5-4f61-8a5a-408fe235d9a9":('8ad5', 'b431bbba-8ad5-4f61-8a5a-408fe235d9a9', 'deco', 'Decorative arts', ['Decorative art']),
"69b7ea4a-40ea-4635-a087-7987f567d8aa":('40ea', '69b7ea4a-40ea-4635-a087-7987f567d8aa', 'fashion', 'Fashion', ['Fashion']),
"2a19fe1c-80d1-4b3b-8a40-32f91948f82c":('80d1', '2a19fe1c-80d1-4b3b-8a40-32f91948f82c', 'antiquities', 'Antiquities', ['Antiquities']),
"b57da004-3a63-4acd-baa6-0b547a7b37d3":('3a63', 'b57da004-3a63-4acd-baa6-0b547a7b37d3', 'watercolour', 'Watercolour', ['Watercolour','Watercolor','Aquarelle']),
"4b5e0890-ff93-41d3-8daf-03e1aba1fbcd":('ff93', '4b5e0890-ff93-41d3-8daf-03e1aba1fbcd', 'ceramic', 'Ceramic', ['Ceramic']),
"56b9bc25-2ff8-431c-ac2d-bb01b28cdc5b":('2ff8', '56b9bc25-2ff8-431c-ac2d-bb01b28cdc5b', 'miniature', 'Miniature', ['Miniature']),
"2959c24e-bb0c-43fb-920e-0dd7f8d0d421":('bb0c', '2959c24e-bb0c-43fb-920e-0dd7f8d0d421', 'print', 'Printmaking', ['Printmaking',"Print"]),
"dcc03c62-cbc3-4fe3-af32-d1c134f6ec63":('cbc3', 'dcc03c62-cbc3-4fe3-af32-d1c134f6ec63', 'coin', 'Coin', ['Coin']),
"6db36cb5-4054-4420-9afc-0b684a80b1ba":('4054', '6db36cb5-4054-4420-9afc-0b684a80b1ba', 'medal', 'Medal', ['Medal','Medallion']),
"160d6aff-aa1b-4d6c-9779-119a01fa97e7":('aa1b', '160d6aff-aa1b-4d6c-9779-119a01fa97e7', 'jewellery', 'Jewellery', ['Jewellery','Jewelry']),
"abd9b846-d0c7-4d62-9406-695da31f9e85":('d0c7', 'abd9b846-d0c7-4d62-9406-695da31f9e85', 'costume', 'Costume', ['Costume','Wardrobe','Dress']),
"906ae76d-7708-4984-ae8b-812ea1db638e":('7708', '906ae76d-7708-4984-ae8b-812ea1db638e', 'film', 'Film', ['Film','Movie']),
"952c99cd-6597-4551-bd72-c08659a4f2c7":('6597', '952c99cd-6597-4551-bd72-c08659a4f2c7', 'caricature', 'Caricature', ['Caricature']),
}


