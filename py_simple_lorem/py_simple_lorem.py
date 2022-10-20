#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
py_simple_lorem Copyright 2022, Andrew Spangler
Simple, compressed Lorem Ipsum generator. Get a different output each time.
"""

__author__ = "Andrew Spangler"
__copyright__ = "Copyright 2022, Andrew Spangler"
__description__ = (
    "Simple, compressed Lorem Ipsum generator. Get a different output each time."
)
__credits__ = ["Andrew Spangler"]
__license__ = "GPLv3+"
__maintainer__ = "Andrew Spangler"
__requirements__ = [""]
__url__ = "https://github.com/AndrewSpangler/"
__version__ = "0.0.1"

import io, random, zipfile


compressed_lorem = b'PK\x03\x04\x14\x00\x00\x00\x08\x00\x05\xa6\x01U\r\xd4 {Z(\x00\x00@\x1f\x01\x00\x0f\x00\x00\x00lorem_ipsum.txt\xb5]\xd9V\xe3\xc8\xb2}\xf7W\xe8\x03\xee\xe2\x1fh0\xdd\x9c\x05n\xaa\x0c\xbc\xablQ\xad\xb3<\xd0\x1e\xf8\xfe\x9b\x19CfJ\xca!"\xc5y\xe9\xd5U\x05\xb6\x94\x19s\xec\xd8\xf1t<u\xfb\xa6\xff<_\xf7\xcd\xf6\xb8;\x9e\x9as\x7fi\xda}w\xf9\xbffs<\x9c\xbb\xcd\xa5\xbb\\OM\xbb\xed?\xfb\xf3\xa6?\xfcn\xba]o\xfe\xf1\xdcm\xcd/4]\x7f=\xef\x8f\xdb\xe6\xd2\xed?\xcd/\xf7\x87M\xbf\xed\xb7\xd7\xc3\xa5\xb9^\x9a]\xfb\xcb||\xd3]\xf0\xa3\xbbf\xdf\xfe>\xb4M\xbb\xeb\xff\xbd\xb67\xcd\xbb\xfd$\xfc\x93\xf9\x91s\xfb\xbb\xbf\\\xfas\xd3o\x07\xdf\xfcy=]\xcf\xf6\xd3>\xda\xeb\xa6\xffu=\xdf4K\xfb{\xe7M\xb7\xebN\xfd\xd9\xfc\xb2\xf9\xdc\xab\xf9\xbf\xe6\xb3\xdb\xed\xba\xc3\xa5\x83\xbf\xfb\xbc\xee\xbe\xfaC{\x1a\xfe\xed?\xed\xaf\xfe\xd2\x9a\xc7\xdb\x1fO\xbf\xfa\xe6b~\xedb\xbf\xdf\xbc\xcf\xc1|\xa3\xfd\xf4\xff\\\xcf\x97\xa3yb\xf3\xe7\xa6;\xf4\xe6\\\xfav\xdf|]w\x9f\xd7K{\xe9\xcc\xa3\xdc4\xb7\xd7\xdf\xe6wz\xf3\xa9\xa7\xad9\xb9/x\x93\xee\xda\xc3Y\xf4\x87\xe1w\xee\xdb\xf3\xb9m>w\xed\xa6;\xb5\xe6,\xcc\x8f5\xd7\x9d\xf9\xeaM\xdf\x99\xef[\xf5\xe7\xbe1\x87wi\x9b\x1d\xdc\xc6\xfe\xb8\xdb\x99\x1f\xc1c\xda\xdbW\xb7\xffz\xe9/\xe6\x80w\xdd\xd1\xbc\xff\xef\xee|i\xcft4_\xfdWw:\x99c\xddl\xae\xfbs{\xb0\xdf\x7f\xe8\xcf;\xfb\x9f><\xa6\x9b\xe6qk\xfe\xf2\xd7?\x8d\xf9$\xfba\xe6\xa4\xf9\xf4w\xf4\xf2\xf7\xf6]\xf7m\xb7\xe9\x0em\xf0\x94\xcd\xbeo\xba\xdf\xe6\xe7\xf8\xa4\xffiO\xdd\xc5|ig\x0ecM\x12\x13<&\xfc,\xca\x13\x1e\xf4\xe1xh\xda\xd3\xe6z\xd3<]\xed7\x99#;\x98\xaf\xb0\xf7\x8d_M\xb2\xf1q2"\xd6\xefvF<\xee\xe1\xd7\xf1\x1d\xed\xaf\xc3]|\x9e\xda\xce\\\x95\xf9\xd6\xd5\xf5\xb0\x01Y\xb9\x9e\xce\xf6\xd7;\xfb!|f\xe6\x9d\xfb\x8f\xee\xb0\xb5\xcf\xdd\x1fn\x9a\xe7\xa3\xbd\x8c\xc6\xbc\xd3\x06\x84\xead\xa4ts\xdd\xd9\xdf\x83\xaf\x86\x97\xfa2\x92\xd1\x05\xefl\xce\x1a\xae\xf8ww2G\xd7\x9a\x9f\xb7\x17w2Oi\xbe\xf6\xeb\xb8\xbb^>[+\xe4\x1b\xf3\x11\xbb\xd6\\\x1d\x1c\x86\xd1\x0b\x16\x84\x83\xe2f\xcd3\xf2\xa9\xbb\x8f\xfe\xb5k\x0f[V\x11\xfbV\x17{; D(q\xa1\x0e\x98[7\xeft\xb9\xee\xad~t{sFF0?\xdaMo\xbe\xb1\xc7\x971\xbf\x14\x1c\xf0b\xf1\x06\xafj\xde\xf4\x02zk\xb5\xd6\xde\x11\x9c\xf6\xf9\xb8mw\xf6\xc8:\xd0\x0e\xfa\x93ybx\x08s\x1e\xe6>\xcd\xd9\xd0\xb9\xe377\xe6\xc1\xd0\x10\x90T\xffkE\xdd\xdd\x05\xbcC`H\xf0\xbc?OG\xf3\xe8N\xfbArO\xff\x1c\x0f\x1b\xd0t+q\xe6\x8b\xaf\xed\xd6\xc8\x86\x112sx\x9b\xc6\xdc\xe0\xa7\xfd`R\x03\x16Wx\xa8\x8f\xeeD\xef\xfey<_;ct\xe0\xc6\xac2\xfb\xb7d)2Z\xbf\xff\xecN\xe6\x97\xae\xbf{\xf3\xf0V9n\x9aW\xb4e\xc7\xd3\xa6o\xb6\xed\xa7\xb59$\x15\xe6\xeb\xcd\xb3\xf6$\n\x07+\x81\xd6\x0e\xb6\xd6\x1a\xdc4/\xf0&\xfe\x01\xf8\xc8\xe1\x83P\x0c\xcc\xc9\x9a\xa3\x81#\xe5K\xfd2/a\xbebw\xdd\x93\xaa\xf0\xad\x93`\x9b\xeb\xb5\x82}q\x8f@\xf6\x0fT\xec\xf7\xa9\xfd\xea\xcd\xd1\x18\xcd7w\xb4\xe9\xedS\xb5\x97#(\xfb\xbb\xd3\xb0\xcd\xc9\x9c\x92}\xd0\x8fn\x87\xe7\xc6\x02D\xea\x0f\'\x17\xb5\x19F\x96\xfd\xbb\xe3\x85\x193\x0c*~\xa5\xf7^,^\xd2Wh.\x07\xfe\x8e\xffH\x97a?\x99\xecV`?v2\xd3\x80\x1f\xe2\x8d\x8d\x93\x16\xf3\x12\xe60Q.\xc1\x08\x1aSG\xba\x8d\x87I\xf6\xcdX\xaf\xb31\xd0\xf0U\xee\xf0QC\xed)\xe1\x89{;\xe0\x9d\xc4\xe1j\xbf\xde\x1d\x9a\xd5u\xa70\xc7m\x7ft\x9ao\x8cB\x7f\xe8[{m\xa0\x03\xf0\x91\xa84\xf6\xe7\xe9j\xf9\xa7\xe1G\xa6\xc7q\xc1g\x84\xdb\xf3jc\xe5\x13\xfe\xbe\xdf\x8e\x1d\x10\x19!\xf3/\xc6C\xd9O\xa0\xefa\x97\xcej\xca\x7f6?uAs2\xf0W\x81\x8an\x8e{\xf3\x80\xc7\x06\x85\xe5b\xee\xfa6\xa9~\xde)\x18\xf7\xfd\xd5\x82\xa5c\x1dD\xc9\x06\xe7\xf5V\xd4$4\xa97\xcd\x03ie?O\xab\xe9,@*\xcdil\xcc\xcb]\xc2w\xfc\xd5\xff2\xd6\xc9\xda\xcd\xc7H\x18\x94\x8b\x82\xc6\xee\xd2\xbe\x01x\xa9+<\x83ua\xf6\t\xafR3\x8b\x12\x85w\xb9\xed\x7f\x9b\'>\xf7\xfb\x81\xed\xbdZW\x06\x81\x8b\xfb\xa8\xa39\x88\x13\x07\x19\xa0\xda]6<\xb0\x8e\xc6\xfe\xa8\xff\x04\x13\x90\xd8\x0f\xa7\x0f"\x9ds\xefo>\xeb\xa6\xf9a%\xf4\x1fsL\'c\x17\x9cg\x07\xb5\xc4\xaf4j\xb7\x8b\x85\x92\xc6*\xb2T@\x18\xe5>Vp\x1d\xc1\xfdg\\\r\xcb\xa8\xd1\x0b\x94K\x12z\xf3[\xff\x18_\x81\x01\xdf\xf9l\xed\xd4\x93\xce\x9c\xacX*\x137b\xae\xcb\xfa\xf3M\x7f\xb9n\xed3n\xc8\xd2;\xebB\x17a?\xc9~\x8f\xff\n\xbc,\xa3\xc0\x87\xac+\xb0\xfe\xcf\x1e\x9a\xfff8C\xf4\xaaV\xcevG\x13`[C\x19Zl\xaf+\xe6b!\xe6\x1b\x06y\xe4q\xc1:\xda[0W\xc4\xa1\xa9\xf9k\x16\x1e\xfc\xb3\xd5\xa3mo\xa3\xf3LXc\xc5\x03c.\xd6Q\x0e\xbd1`\xb1r\x0e\xef\x87\xa1\x92\xb9\x9cOs\xc3\xe6\x85:\x17\xd3;Kf\xdc\x168\x19\xffa\xe6:\xed\x15\x1a\xedC\xf7s\x18\xdc\n\xeb\x03\x9c\t[+0\xc5\xad\xf1"&\x18\x06\xab\xe2\xa5k\x0b\xc1\xcbr\x10\x1e\x92Yg\xcbr\x1e\\*\x87j\xac\xc3\xce\xcb\xd9\xbb6\x1ant\xc7\x05\xde^\xb8\xe1\x039\xf8\xe2\xcb\\\r\xff\x16\xec\xba\xbf,\xf2\x1f.\x16\xf94Z\xd3\x9b\xbf\xc7\x98\xe4-\x1bv\xc2\x11\xfb\x83\xa2\xa8\x80\xcfr\xe4\xb0!3CI\x003\xe4\x15n\x1d\xfa}>"L\x84\xf8i|\x1at6\x91Qw\x00\x13\xccgbT\xec\xe7\xf5r2?F\xaek\xe0V\xcc\xf7{\x9b\x83\x19\x08\xb9Po\xf4\x9d\xb5\xc2\xbb6\xb6\xf77\xfe&Xas\x13\x17\xabf\x10\xc6\xf0\xdb\x91\xb1\x07\x01\xa0\xd7"7}\xf1\xa7\x05zc\x13\xb7\xbf\xd1\xc8\xc1\x8b\xc3\x89\xa3\xa9\xc6_\xa9>\x01\xf3\x8b\xf8\xffV\xc9\xfa\xdfWkT\xcc\xe7\xed7\xc7\x93}6\x17\xc2\x82\xbc\x84\xa1\x05i\x849\x04r\xaa\xfe\x84|r\x06a\xb0\x13@4\x19d\xacI\xc8I3o\x9a?)\x1e$#\xf9a\xec+\xdc\xb7K>\xc1B\x91\xbc\x87\x97\xe3M\x8c5,\xe6\x9c\x8a\xd1\x8c}\xea\xffu*\xbe\xe6\x9b\xf1\xb1\x05{\x11#k\xcb\xb8\xb2\x90\x0br\x12c\xfc\x7f)3\xceE\xb9\xe6\x1de\xdf\x83\x1fm\x03~\xfa)\xc9)\xde4\x7fP\xb8\xbf3jx:z\x91\xb5B\x01&\xe2\x18\x88\xacu\xd5FE\xda=)\xaf\r\xa7\xbc\x9c\x81+\x1e\xd9\x9e.\xe5Al\xbe\x82/\x83R\xd2\xb3\x9f\xbb\xb2vz\x91\xe7\xd0\xf45\x1a\x91\xa2/\xb2\xea\r2L\xf1\x96\r\t>\xf5\x8e\xc5\x058F\xad\xad_\x10\xa6\xdd\x0f\xde\x9b;\x81\xf2\xd1\x96\xa2Z\xc3f\xe5\xbfP\x05\xa2\x9a\x07\xc4\x0b\xceR\xf33uW\xcc\xe7rI\xaa\xb58\x1b\xeb"X\xa0\xf0YHK\xf0\x0f\xa8\xd1\x9c\xca\xd9r\x05\xfc\x8e\xf9x\xe7\xdf\xbd;\xc4\xfa\r\xdc\x83\xb9\xc1\xb4\n\x07A\xfez\x10saT\x08E\x11L\xcdBKEe\x05s\'\xc1\xdfr\xb9\x0b\x0e\x03\xc5\x10\xcd\xcbW{\xeamDf\xa5\x19\x92\x83w\x16M>s\xf7+6\xeb\xb5\xa6\xb9\x8b\x9d\x95y\x11\xf2\xbd\xbbd92\x1f\x87/K\x96*0\xdb\xd6\xec\xdf4O\xc9o\xb2\xf6"\x10\x9e\xaf\xac\x97A\x0fV\xc8\x18\xc5%\x05\xaf\x93Y?\xeb\xa2\x12\x7f\x94\xec\xc4\xf1~\xe0\x99\xed\xa9\x16\xebq\xf4\xe8\x98\x81\xe2u\xdaO\xc6\xd7"\x93\x84\xe2d\xcb\x07\x1c\xad\x91\xb3\xb2Z}51\x94u\x7f\xf4d(]\xee\xd2\x9c\xbaz+I\xa2\x0fa\x1c\xfa\xf7\x9b\xe6.\xb8[\xfa\xd2>\xf8:\x88R\x17\x8bu"\x8d%]\x057M)\x14E\x11\x14\x86LR\x01\x9b\x94|K\x05\xe0\x05_\x17\x85\x03\x0f\x19\x95\xc1\xa9\xe8\x03\xbf\x04\xb9\x15\n\xc51/\xf4\x8a\xe7\xde\x05\xbf\x1a\xbefO\xa6\xc5\xaa\xb5ygs\xb8\xed\xc9\x9cP\xdf\x81\xcf\xb4j\xef\xcb\x92h\x8b\xd0\xba\xe7\xcb\x1bV\xefK\x155\x08H\xd0\x00\x83\xe1\x05+\x12\x84\xed\x9f\xc7\x8by\x08\n$\xf6\xf0\x01\xe81\xa8\xa4\x07\xa7\xe2\xeb\xf5/3\xf2\x81\xc5\xe2UT\xb6\x83g\xe6@\x83kl\xbe\x10\xd1r\x11\x0c~\x11mq\xa8 \\\x9f\xda\xe6\x8a\xce\xde\x0c\x1b\xfb1\xae\xa7\x82\xc3\xbbJ\xbc\xf1\xf7\xe6Kw\xc9\xf8\x83\r\x15|\x96\xd1\'\xacg\xb3qx>\xee\xactt\x18P\xe3A\xda3\xa4_\xf2\xa2c+\x89\xf5:\x82\'\xc8\xe1\xfe\xd2\x9a\x0bo\xac\xd0\xf3\xb1\xd4Q\xb4omQ\xf0\xd7.f\xc7\x14\x994\x1b,\xa9\xb3\x87F\xfa\x9d\xa5A\xf3\x9e-\xcc\xf8\x9a\x88\xab\xe4\x855\x16\xf8\x11*\xfc\x93D\xfbh\xc0x\x87\xa1\xf3Q\x06\xb5\r(?D\xb7\xef\xfc\xc8{u\xe5\x1fBcY\xda\x03E>2\xed \x1c\x1cI\xdb?\x90\xde\x831\x06y\xc5\xfb\x05-0Jd\x04\x91L\xe8Q\x17\xc5\xdc4?u\n5\xecT\xf8\x16\x97W/o\xd5\x9c\x12\x9c\x15\xd9\x9a\x15\t\x8e\x8f\x02\xb3@\xf9\x93\x0by[\xb2\xc0\xb6\xd2Y\x8c!\xfe7j\xcc\t.\xb7 Q\xa4\xc7\xe9\x9a\xd5\x05\xbaf\xca3\xd2\x05\x0f\xfa\xa4\xe0o\xbd\\R\x16\xf2\x9c\xef96m \xae\xb2\xd2CV\xe20\xa9rWn\x9f\x19^r_,\xe6`t\x86\x97\xb5\xcd\xdd\xa8\t\xbaF\xd5\x06\xf7v\x87b!\xa6(\xfbda\xae\x97\xa0[\xe1\xa3\r\xacTzq\xb16eP\xa1\x83X\xefV\xd7\n\x13{\xf8\xb1i\x1e\xc6W-\x9a\x91C\x0b5T2\x1d\xd6\xcb\x1b\x9f\x86%\x18\xeb\xd5\xdc\xd58[\x02u\xe0{qLn\x8f\x86\xcf\xdb\x05\x85\x02[\xe4\xcb\xb4a54\x91\xa9\x94K\xf67\xcd_\x1c\xf5\xd9l\xf4\xd2qm\xe4|q\x8e\xe6,\x0e^m\xec4\xee\x7f\x8f*3A\x83\xe3\xb7\xa4\x18c$\xad\xdc\x946\xb2<TX\x88\x1f?"\xfd\x11\xb0\x9c\x9a"\xc0{PM \xbb\xe3\xdc\xb3\xad\x04\xf0\xf7\xdaH\x96e\x82\x1e\xcd\x1d\x14\x96\xb3Q\x86I\xd5\xcc\x91m{\xee\x83bR&02T\xdd\t\x0b\xb0\xdcO\xbe\x15\x02\x0c\x82\x84\x06\x10&y\x17\xb7X\xdc\xa3\xada\xf3\xe1\xff\xef"\xe9\xb2=\x95M!>U\x9b3Zp\x0b\x10\x90\xd0\xc9\x06\x85g\x1b\x8b|d\x8a\x1b\xfe^\xf8_t\x85\x93\xc7\x83\xb7[\x18\xf1\xb8`0\xb0X\xa4\xb3\xf8\r\xe0\xc2\xe1<CH\x8e\xb6\xc9o\xaet\x1a!b\xe5\x00\xcc,6\xf8\xcc\xb7X\xf3\x85\xae\x00\xfc\x82/\x1d\xedG},x$\xe7\x841o\x9eQ \x0b+\xa1i\xe7\xeb\xfc\x14\xc4\x98\\\xe3\xe2\xd0Ua/\xa3a\xa4\x97\x8cd*K_\x11d\xbdX\xd4\x80\xd3\xe0 \xdc\xa94\x9c\xb5\xb7\xee\xce]\xbf\x0e\xb2=o\xdf\xdc\xff\xe0a\xe3\x7f\x03\xcf\xf2\x9e\xc6\xa1`qLqw\xd6\xa7F\x92\\=j\xc7\x06o\xe9\x06\xfa\xa4\\\xf9\xe8\x9e\xea3\x8e\xe00\xa2\x8aQ\x85uS\x9d\xa6\xe2m\xf5\x8b\x8d\x07\xaaP`4A\x15\x82 \x01\xd5jP_x\xf2\xee\x19+\x0b5\x96\xcaf\xc3\x1b(\x1d\x83L\xd0\x17s>D\xbf\xed\xc3X\xa7\xa5\xe4z\xded9\xed\\Q\x1fgL\xba\xf4\xc3&D\xa3\x04+^k\x1c\x95:2\xb1\x91u\xf6\x00W\xdcx\x8f\x1d\x86[\xdcL\x86\x87\xf0\xe0\x9c\xbb2\x1e-\xd3pd\xd1e\xd8JF{8\xd2\xc8\xc3\xf3\xb2\x8d#\x86\x89d\xee\n\xa4.Hc\xc3g\r\x92\x16#|\x84p\xb2\xb5\x18\x17\x13s5\xbf\x84i\xb2/\x80\x8e\x8b\xf1\x97\x03\xe0\x84\x95]\xaa\x83b\x0e\xfe.Q\xa6A\xe1b\x9f)v\x0b\x1b\x1b^f\xde\xb5v@*\xf2\x1e\xb9Gn<\xac\xc8\xf9\xd0\x9e\xb3[,\xd5\xc2\x1d~\x04\xd1\x19\xc02\xc0\xad]|\xddYT|\x11`\xa8\xe8$\x19\xee\xe6`\x04\x83\x90\x0f\x9aI\x9c\x17\xb5\xe1?\x85\xef\xc8\x11\x07Z>\x04\x85\xb1[mS5x=`\xd6&\xaf\xabAM*\xf8g\x8c\x86\x10x\xe6\x1a\xf9\xdc\xffB\x05\xb5\x087\x1d\xd2\x16\xda\x86\x95\x06\x91\xb0x\x89c\xb7\xefJe;\x17\xe2\xb5\x08\xe22\x82\x10\xedj;k0\xc6\xabd\xa1\r\xf6\xd0\xeecm\x9e\xc1\x8bp,m\xb5\x15]:\xa9\xa9\x8f\x0c\x7f\xf6\x8c\xc6q\xf0!\x8e\x8cO\x08\x16\xe0<\xec\xe0\xec=\xe1\x1d>E\xe5Y#Q\xd1\xa0\x86$\xaaT\x03\xbe\xd5T\xe4\xd1\xcaR\xfe~\x9f6\x8dT\x92\x06\x88X\xcd\xb1A\xfd\xe2^\x1agf\xabd\x9c#\xb7\x03\xe8\xe1\x00_\x81\x82&\xe8\x93CCbT)\xf3Z\xe1\x85\x1a\x93\xd2a^\xe1\x9bta3s\x0c\x126\xba\xc6\x11cx\x19-\xc3C\xbcA?\x07\xe0K\x8eC\xf9<\xac\xbf0&(\xe8\x9cC\xd9H\xde\x82\rb@\xc2_\xa4B\n\x1f\xe1\xaa\x9e\xf7V\x98\xde\xf9\xe8fN|\xcf\xa5\x89\xd7\x19\xc8M\x0cB\xd9\xfc\x84\xd5\xb5<\x9a\xfa\xdd\xf9\xe4\x00@\x17\xd4B\xfb\xa9\xc3\xf9\x86\x1a\xbb.\xf1X,\x96a\xcb<\xf0]\xf0\xd2\x0c\x1e~K\xc4#\xd6\xadR\x86;\xed\x9a\xba>\xfb\xe0\x1d\xfa\xc1$\x86\x97\x07Ii\xd2F\x1f\xa8zl\x13\xbe\\\xf9\x80.\xd4y(\x16\xc3]\x15\xae\x02e5\x04E}\xa5\n\x15u]"\x08J\xb2\xa84\xe8g\x80\x03\xf2]\x9a\xf8LB\xd0\xc0\xbf\x8bC@\xc7\x15@\x1d\xf8&k\x06\x00\xc5p\x9f\xa8^\xd9\x03\xb6\x11\xc1\x9d\xa6\xb8D\xfdl\x93\x0fd\xc2\x9a?\x15\xae\xce\xc1\xee!\xab\xbb\x93a%\'\xad\x83\xfaDK\x01\xd1quVi\xec\x93\x02\xb03\x04;\xdd\xfa\xc8TR_\x07Q\xa0}\xa5k\x08d\xe0p\xf4OY\x99W\x06\x04\x08+\xbdg\xd9A{\xf4\x8cz\xd2E>\x16\xe5\x9a\x03\x02|f\xd8j;+\x1a\xabO\x0e\x0c\x19\xc5o0p}T\x83\xb2\xc6\xf7\xdf2<\xdd\xd6\xd9\xc7\x1d\x0f\x08i\xd1\xb7\xa6\xa1-\xef\n\xdc\x86\xd1\xd6\x07\xdf\xdac\xe3!k\\\x8b\x1a\x01\xf1\xe9\xb4@(\xb0\x8e\xb6\x8ef\x8aAz\x9cs\xc5\xdf<$c\xab8.\rF\x13\xc4Fn\xf8\xddd\x077Y,\x10Cnl\x93\r\xb3>\x87\x07\xef\xb7,\xe4\xd4\xd3\x94\xa0/\xdf\xf3\xc1\xabw\xcc\xa21-\x92\xa5\xc4\x94Uj\xc4\x15\xa1\xac\x9bD\x03XR\'\xb7\x08=\x11\xc6\xdb{S\x8c\t\xb4\x13/AW\x0f\x87B\xc2\x12\x02\xf8\x8b~0\xe2\x04>/\t\xe1.u\xb8\xddk\xb9^\xc0x\xe0S\rq\x7f) \xd2s=bq\\\x91\xe8,\x92D^2X@c\xe3\x8auC\xdf\x84\xfc\x16\x8c\xf5*\x97\xfa\x8c\x86!6<\xf5\x80Nu\x83\xf7v\xc9\x83\x1b\xb1\xfc,\x00\xbb\xfd)n\x98Mp\x1b\x10GV\tXi\xde\xd5\x8f!}\xa5\xc1\xad\x8b\xc5\xa3V$\xe6z\xb3wu2(\x84\x01\x8c\xfa\x0c\xd6-\x0fCR\xcd<\xdb\x1c\x04\xd1\xb3`\xbc,g\xb0\\\x00\xb7)U\xa9c\x03\xb2\xc3\x14\xdd\x03\x84\x12\x1f6\xca\x92\xa2\xedRr\xac\x9a\xf1\xad\x10)D\xe1\x846\xb3\xfd39"l\xf4\xc1\xbe\xfe/\x0e,\xad\x9a\xf1\xc8\xd99\x81\x19\xbf\xd5\xc2>\xc4E\xf8\xe1\xc4Lt\xc81h3+\xa6\x92\xbc\xc3\xf2%\x0b\xdf\xc7B\x9c\x16\x14\xa2@\xaf^\xea\xec(\x94\x1cV\xa5\x99F\xc2\x88\xb2\xaes\xf8\x06\x17\xc9.\x0ca-\xca\xe0\x91AK\xf6\x01.\xc5\xb7\xa4\xf9\x99w\xe1\xe4\xf9\x0c\x9c\xec\x18\xd6\xb7\x8e\xd5HY\x89Q\xaaG\x8e\x97\x9d\xc3}bH\xd5\xd9\x89q\xbf\xa3<?\x11\x14\xb3\x84\x95\x85\xb16\xac\xd4i\xf7\xdf\x99a\x9e\x11\xfcF\x10.\xe4\xd8\x08\xde\xf2\x0f\x1f\x86\xcf\xf0\xc3s\x86f\xb8!i\xcd\xfdF\xecd\xc0mj\xba\xe3<\xb5\x91/\x9c\x07e\x82\x8d\x9f\x01\x7f\xcd\xc2D\xe2\x83{\x04\xa6\xca\xcf\xff\x8c\x10y\x88O\x1c\xd6Y]\x9f\x0b\x02\x06\xce$\xc1k\xbc0-\x84 G"\x81\x88\xf6v\xfc\\\\\xf3,e49\xb0\xa2\xd3\xe3\x8e\x1c\x08\x8d!\x15\x87\x05\xf1[\xd7"\x0b\x9e\x1cS\x0f\xa6\x942\xc0\x088\\y3\xdeH\xdf\x11F0\xe2S\x0e|\x12\x00\xf5\xed\xebpP\xf2)\xaa)p\xeb-\x95\xd5x\x8fu\'lH\xff\xd4\x83\xf1}\n\xc9\xadJ\xd9<\x7f1\xf6\'\xb6\x00\xf6Y`p\xc1,:\t\xa7\x1bf\x8b\xc5\xe0>\xb0L\x9c\x88\x80Od\x87\xc4H\x9dl\r*@\xc2\xa5\xf1\x8e&\xd5.\xe0$80\xa7\xa6t\t8#\xed\xd9\x9b\x9f\xcb\x99\xc22\x96\x9ci,"\xa3\xe5\x89\xa2\xbed\xd2\xc7Y\x83[\x01|7di\xf9\x1f@\xf4\x1dd\xef]:\xc3\xf2\r\x01\x97\xcb\x12\xb6\xaa\xf1\x80\xf0\xbc\xdaz\xeb\x11N7\xa5\x06\r\xc9\x0b\x85~\xc3GZ^\xd1A{aLKy\x1a\x85\xd1\xcc%R\xbf\x04\x89\xc6V\xc0y \x90=1\x92\xdf\xe5\xf8\x888\xa1\xa2 \x0f\x10r6\xe6Z\x07\x8f\xd1\xa2(`\xf7\xa2]3.)\x8a\xc3X,\x9d\x85\xf3p\xd7\x02\xe4\xdbF:J\xd8\xea2\xcf$@\xfd\xc6\xe8Y\xd4t\xe9\x15\xe96\xfa\xfaQ\xb5U\x02\xf0\x08\xc7.\xd9\xfe\x90\xd6\x9c\x92\xb4\x11y\x12\x00F\xbb\x9b\xd7w\xb1>\x99i\xb6^\xce\x14Q\x9c\xb1\xcc#\xc7]u-5\x9b\xbd\xce\x0c{\xaeS\xbd?\x82S\x80\x17\xe9\xc9\x92\xff7\xc63(\xe7G\xf2\xe2\x8b\xee\xd6B\xd2L\xb8\xc3\r;Am\x8e\xaa_\xf1\t`\x7fi\xcf\x93\x81]L$\xc9^\xb1\xbd\xe1\x9c\n\xb1$0\x0b\x0e\x02\xf7\xdf(\x9co\\\x89\x05\x97\x13\x08z`\x10l\xe8\x10DM\xaf\xe5QU.\x98\xe3\x9b}(i\x84n\xa5\xcd\xc5\t;V\xf3P*\x9dN\xc9\x81\x86\x1a\x10\x14\xfb\xad|\x9d\x87T`\xb3\xacB`!WB\xa8]l\xdc\xfdG\xc4\x11\xbb\xf8\xec\xae\xd0\xae\r;\x83]\x1cq\xe1\xb0\x9d\xa1\x10B\xed\x11\xd0PF\xca\xff\x8dGJ\x12\xcc\x98\xac\xb0\xa2\xca\xd2\x07C2 }\x0f\xc2\xc9\x02\x93v\xcc\xa8\x10\xdd&y\x18RH\xb3)u\x98\x8e\x17\xe3IT\x80\xe5\x8e\xcc \xa7\x04\xcc\x9a0L\xa6I\x04\x1fn\xa0\xed\x0fd|b8\xb0^\xbb\xaa\x9c\xbeqX\xe89\xd1\xa45\x1b\xd2\x82\xfa\xad\x8e\x03@\x83:\x92\xe2\xad\xc9\x05\xb1\x8fd\xf5J\x13\xbf\x06\xf4\xa4SlQr\\\xf0YS9I\xb0\x15\xbc\x89:\xde/rj\x80\xa7\xf28\xae\xc3|\x10\xbf\xd9{\xfdd\xcdbqW\x90IWeRA\xf7\x9d\x9e\x06\x9c\x04k\ro\xa7\xef\x91J\xf8]\x08A=\xad#\xa3\xc4\xe6\xd0\xe7\xe2j\xf6\x8cYM5h\xda\xc8f\x06\xb3\x17\xc0\r\xd6\nZj.hQ\xeaJ\x17\x15\x8cP\x15\xc7I\xd4hR\xd7`/\x86d<]\x19\x92"\xa8\x08\x19\xb0\x06_4@\x8f\xa2\x0e\xf2\xb2L-6\xcb[\x99\x84k\x80\xff\ra\xf1Rv\x90\x9f\xf2\xc4f\xa5\xe9\x1bP\xe9\x1d=\x968\xe3L3\x8d(\xb9\xb0_$\xf2\xe8\xa1\x91_J\x96\n\x04Z\x91Ba\xf0\xefj\xd9.^\x88\xf2\xd2\x0e\x8a*R\x98\xde\x80\x10\xd6\xeb \xf6F\xc1\\\x9f#\x89zX\x9e\x88P\'\xa5\xe9\'i\xd8@\x8c\x14\x8e$qA\xa9;O\x8f\x94\xcb\xc9\xa9\x17\xb0W\x93_r,XO\x19\x01\x9d\xc3B\x81.\xb0\x9b"\xae\xaa\xd8\x81\xbbL@4x\xe2\xeb>\xaai"\n\xde\x84<\xabR\xc6\xd7rY\x03\xdc\xdd:\t\x83\x97\xd5\xba\x8a]3E\x05\x98\xa2\xbc7U\xc8A\x8c}O%\xdaM\x93\xea\xe4gO\\\xb26\x98K,\xce\xb4\xc1)\xae\x02\xcb\x80vv\xc4k8oFz\x08lO\xf7\x99\xec\r\xb2\xfa+\xc9\xd3T\x80j\x9bi\x84\xa3v$\xcd\xe8\x96\x85c\x86/\xb2\x82F\xa9\xe6\xab\x9c\x9b\x1c\x05F\x18O\xe4S\xeb\x105.\xe7\xd7Z,\xfe\x90\xcc\xc3\x84\x01\x80\xb4\xff\xf8\x1e\xe1 \xf6v\x83\r\x89\x86\xfag\x98k\xb0u_\xe9\xec\xd7\xad\xb6R\xe1\xeah\xf2\x04\x9d\xc2\x0c\x1bE\x80\xf2|\x0c\x00\xed\x01?\xd06\xc1\x8c\x13d\xbe\xb9\x1e\x867g\xe3\xcep\x86\xf7/\xb6\xa9%x$+;_\xa5\x11\xb1\xc5\xe2\x87\x8aE\xfa\xb6\x08[1\xdf\xf9\x8fEr\xb3\xbdi)f\xff\x91O\x83Js&\x95\x93<\xa1k]\xe5\xd6\xc0\x04\x0c\xe1\xe2}-\x14\x7f=\xca\x8a\xd6,3\x8f\xd1BbL(!a+ #\xe7\xa5`\x8e\xa5\xf3Pr(L>\xb4\xaa\xe5\r\xb7\xf6\xe6\xb6\xf4\x13\x8b\xc5J\xc5U\\\x86\xfd\xd7\xd2\x88\xdf)GWC`\x95\xd4\x13\xd6\xcf29\xe2\x80U5\xfd\x8e\x9e\xb2I\x96\xe1\xe8a\xc9\xb4@(c\x8aMf\xa6\xac\x15/\x16/\xb3\xb9\xf3\xc44\xf7#\xb3\x14.\xdf\xf8\x14On\xbc\x0eC$i}\xa2\xc2 \xd7\xcc\xc4\xd2\x1dM\xf9$\xb5c\xbd\x89b\x06\x16\xb3\xe6\xd8\x96\xe5\x84\xa1\xa9\x19\xd5\xcd\xa1y\xfa&\xacS\xac\x93\xe4\x13\xb1\x91"\xc7\x96\xa3N+\xff\x12\x93g\x0e<\xa3\xdb\x19q\x01g\x82\xfb\xd5.\x9c\xc3\xb5.v\x93\xd1\x8f\x19\x8fWU\xbb\xd0m>\xc8\xcf\x99\xbc\xd5\x02\xb9\x96\xda\xa21ep\x7fD\xe7\x83\x92\\\xa1BF\xf0i\xc6>\'Kw%\xd2\xd7$\xc5\x1cu\xb1\xa9\x15n=h\x1a\xe9\x1egT\x8e\xccBR}>\x98\xea\x8a\xe1\r\xeah\x95\x03n\x8e\xa5\x9eG\x94ZV\xe5\x08A\xb2\xf9\xafDe\r\xed#\xa8q\x05\xe7\xce\xef\xbeL\xb0G\x15u\xf2\xcf\x12\x15\x08\xcf\x8d\x946\xce\xf9\xfe\xfdK\x0c\xae&\x8d_\x1f\n[\x81\xc4\x04\xd1\x8bE\x8dc\x11.\xb0\x1b\x96\x8e\xacX\x81\x0c\xb8m"\xd0\x89/4\x9d\x9e\xeaR\xd3\x10\nzW1p\xf5\xbfC\r>\x8b\x17\x05\xe6}\xbb\xa4\xa7\xe5\xabO\xafs\x00\xf3FHJ\xba\x95\xa3\x8d\x80\xda\x96\x94N\t\xdc\xbd{q\xa7\x1e\xa2\x16p\x16\x84%\xde\xe7\xf5\xa4\x9f\xe0\xba\xabc&\xa3\xd4\xf5N\xc7T\xf4V\r\xa9\x19\x17b\x19%\x1d_\x1f;\xb8\x05A\xb0V\x80\xa4e\xdbm\xbew}\xae\xe5\xefw\xc3W\xf3\xb8\xe2V\xf3G\xbf\xd3m\x87\xef\xe97\xac\xeb6Xb\xa4(I?l\xedv\x1be\xa67\xa6\xe09V\t\xaf\xa1\x9c\xac\'\x05Y\xea\x18=\xa0\x87\xf4\xa1\xa0\x05\xf6\xe1\xdf8I\x1d\xf1\xab\x9b\x9c/\xf8\x18d\xa7zW,Y\xa6\xc8HFI\x97.\xa1\xbbR\x9b\x9e\x93\xe3U8\x02\x94\x81r?O\x0e!\x00)\x8a&&\x92\xbb\x10\x1d\xca*Q<,\rA\x88\xb0\x00\x01\x05\x12\xaeR\xcc\xf1\x08\x15\x99n\'\x90\x90\xa0r\x07\x13<m.%\xe1I+\xc1\x1e\xe6Z`\xeacE!\xd6\xd7\xd8\xdeBv-@\x9e:\x0b\xd5\xa5\xa9\xf2\x1d\x01oi\xd6(\x0e\xd9\x86\x803Y\x8d\x91\xa2%\xc5\xd8+\x92\x10\x16X_\xc8\r\x06\x1d\xe6\x04\x87:P\xfe\xb8\xa8\xb7L\xd1\xe2?\x97\xb9X\x8bp\xfe\xec\n\x9c\x108\x9c\x18\xfa\xa6\xb9\xa5V\x8d\xfa\xe4\xee\xf8\xdfj\x9e\xa7\xe7\xd2\x1a\xfa\xbb\x8a.\xa4\x1c\xab\xc2\xfc\x87\xa9\xc0i\x1c\xbe\x06U\xdca;61\xde8\\{[G"YB}\xd6\xee\xa0\x00O\xdc\xc9\xa0,#\xf1.\xcfuF\xf7\xfd\xd2\xbd\xa8\xf8\x04\xc3\n\xfaR\xc7H9\x99\x89\x88\xf6\x14C\xd6\xa59 \xcc\xe9\xe3V\x10\x8d\x17xx\xfc\xf6\x8c8\xe3#oI\xd7&\x12\xf2\x0e\x99\xeb\x83\xdciX\x01\x15,\xb5\xe5\x84\xeb/\x81\xb3\x1e\xedW\x96\x8d\xed@5\x1a\r\xd9\xd3\xece\x0b\x8a\xf5\x94b\x98\x15\x8d\xea\x1e+\x07\x07\xaa\xb1\x80\xb6\xc6YA\xe0\xf3.\xa9\x86\xc5vb?H\x1a\xdc1\xa0\x8f\xf5q\xd9\x02j\xfa\xe6\x9d\x07\xce\xac\xc5\x18\xe07&\xee\xbaf\\bP%\xe0D\xa0+\xe7\xea\xaf\xe9E\xbe\xb9\x81$A\xaa\x91\x07`\x0c\x8de\x08\x05\xff,.)|\x16\xe9\x9e\xc3sK\xda-\xe3m\xe7\x9e\xa2L\x92\xed\x8dn\xef\xa1:\x1eT\xc0\xa2J]&\xbb\x98(\xb7\xa3&:\xe9\xb7\xac\xd882ocI\x00VL\xa3\x92y\x0c\xb2X\xe1\'\xb6u\r\xb0\x1c\x9a\xde\x93uWA\xc4<\xda\xb2Q\x04\x8d8\x96\x8c"i\xd3\x9c\x9d\xf0\x95\xcd\xc70\xe5\xd7\xff\xca*\xb3\xe5 \x99RC%\xf7\\(\xc8\x86\xfbRe-q\xd6\xeb<0s\xce.\xcf\xec\xb4\x01\xa5\xc0\xe5\n8\xe3n\xb4\xfa\x10g\xd9R\x12\xe0I\xe9U\x92\xd3\xe7ZB\xec\x02TK\xbe\x18\xcb\x13\xd9e0M\xe8I\xf3\xec\xdc\xc3\x11\x1b\x01\xfa\xd7.}\x9b.\xfaHO\xf8\xb9\x19\xebB!!\x05`\xb0\x96ZLV\xab!\xf3\x17\x11U\xcd\x18\xea\xf0\xf8\x91\xcf\xaa\x1e&\xa5\xccC\nNW1\xfd7\xcf\xca\xa2\xef}\x86\x16/\xb3\xf3uf`\xac"\xf8\x0c\xd9\xc2\xdf\x8a\xc8\xa8t\x18R\xb9\xfb\xe7\x9b\xf6\xc2(\xa6\xce\xfc\xf5axR^I\x9c\t\xdf\xc8\xd6\x1c\xb4\xa5\xf3\x1a\xaf\xe0\xb0\xe3\xa7\xef\xc0\xcd\x08\xa4l\xb8\xc00\xdd\xd0\xbd+\xd6\xa5\xd6\xb1-\xc9\x85\x05C+1\x18g\xb4\x0fCM\xd1\xab\\\xdb\xe2\xe04E\xa6\x10\xea\xa9|\x95g\x7fn\xa3L\xe9\xde\xf6\x8c\xd0\x93A\xeeVBt/\x16o:\x8es<})\x0e<X\xd7\x96\x85>0\x0fJj\xed]\x91\x04\xaf\x16\xa5R\xcbN\x11\xe0\xae\xc4\r\xa8\xe0E%\x9aS [\xf4\x1b\xa1\xeb\x1b\x9b\x7fh\xcb|\xc5\\|n\xd9\xf3Q\x8cu\x0fy\xcaf\xed\x8eW\xacF\t\xf7\x8aj\x87\xf79\x95z\xc8\xac"\x81\xce\x14)\x1b\x9b\x04\xb8rT\x97\x80\x90\xe8V\xbc\xcd\xf4\xb9ro^\xb3\x94\xce\xa3c\t\x8c\x1a*\n\x8c\x9bhG|\xe0\xba\x8b\xdb\x84\xc3YOW%\xcb\xac\x95F\xc2,!SK\x18\x89sB\x1c\xd9\x91\x1b\xa3\xfca,P`\x97gos\x0c\x08\xc7\x9fE\x0c\xd7\x8c\x17\xad\x1fC~\x1c\x96\xad\nc\x1dPio\xc5\xc4A\x18\x05\x88w\x96/\xa3\xd5e\xac\xdf3\xe8\xfb\xef\xf8\xb4\xbac\xbeL G \xc3z\xceb"\x07\xc3\xe2e\xae\xf2\xf2\x0cB\x11\r\xee\xad=\xd4\xd9s\x1du!=<\xc7\xaeb1\x80\x1e\xda^5\xfe\xea\x97V\x94WG\x8cr\x07\xba0\x06~\t(\xd2A\x11\xfa\x19@\xff\xa9+\x10!\xe24d\x11^\xfd\xf6eN\xcc\x19{h^\xb3\xbdI\x076\xd5\r\x04\xa1H\x0e\x8b\xf355h^\xc1T\xdeT\xed\xdb\xdae\x92\x1f\xe8\xaf\x8fi\x8a\xb1\xd2\x97H-D\xcb\xe7U\xf3w\xce\xe9,g\x90g\xbb\x1d\xdd\xe9\xaa\xa1\x8b\xf5f.\x1cy\xccb\xbe(\x95\xf5\xbb\xa9\xff(/\x9d\xad\x8e7\xfcC)\xb9\xd1},\xa4\x88m\xb2\xae!U\x00&\n\x81\xc96k2\x1eo\x05\x82\xd7D."\x18\xa3q\xa9}y\xff\xda\x8f\xaa!i\xf4a\xba\xd101\xc0:\xd8\xd4\xe5\x071\xa2\x18\xeb`\xdcT\xb7\x1e\xd6\x8dw\x17\xac\xd5\xeb\x1c\x85|\xcer\x14\xf8\xe5\xe7\x89u\\\x05\xd6\xf3A\xb7\xa3X+\r\xa7\x00\xf3\x18\xf1e\x969\x80\xfe}8u\xe7\xbd\xf6}\x81"pT\x9d\x02\xa9P\xa4\xd0\xb7qP\xeb\xb0]v[\x1a\xa0\ng3\xbe\xb2l\x02A\xa4 \x86\x06\xdb\xb6\x8f4\r}+\xeed\x1b\x0b\x81v!\xbd\xc2\x12\xbc~\xc7\xdc\x9cL\xca$\xa4\xd0\xcf\x11&\x02\x01\xd2\x16\xee?\x0eDUv\xd9\xb1\x8d\xaf\xf2x~\xfe\xc7\x89\xda_\xb2U\xa9\xa5a!+T\x19\x12\xde\x1f2\xaaN\xef\xfa\xca\xaf\xee\x177\xfc!1\xf0\xe3\x1dd\xe2\x05\x92\x92\xd4\x0c\xed7\xec\xfa\x11U\xb1J\x8c.8\x89\x13\x82OeK\x16&L\xa9\xea\xb0\xd4AM\x8aH\xfd\xecte\xd8\xc3\xcc,\xdc\x89\x8c`\xb8\xf2z\xb2)\x95e#\x8f\x0cT\x0e&\xb0\xb2\xcb\xbc\n\xb5\x95\x87\xfc\x06\x91lh>\xccg\xe7\xb3\x98\xfd![\xe7\xac\x00\xc8\xda\xf9\x92<\xca\xa6\xb4I\xca\xda"1\xc7\xbd\x1d\xf6\xa2`\xe5\xa3\xb8>m\x8c\xd4\xb7\x1d\xd4_\xf9\xbcsP\xad\x99\x90\x96\x94:X\xc1\xda\xc7R\xa8\x16\xce\xd2R{lT\xdc\xc4\xdfKtE\x84l{\xc9\x86\xe2\x9d\xa8\xe8\xca\xa1\xfey\xde\xfc\x92\xbc\x88\x14a\xa4tlm{\x19Pn\xd0](\x8dK\x07[\x90\xe5\xaecP\xe4\xf3W\x9e\xdf\xa1\x95\x1eg\x121\xffQ\x95j-G?\r\xb22^(wt\xb0\x8fHh\x0f\x16.\xad\x1fR\x16zf\x9a\x92/\x8c \xd0\x187\x0f\xcb\x94j\x1errV\xb7L\xa7\xe3,\x82\x859\x83>\xad\x9d\xa8\x1b\xec\x99q\x87V\xd8\xf6M\xa3 \xa5X\x80+\xd4\xaa\x05\x19\xb4\x868\xbfZ\xb0\x18(\x15AA\xcfy\x86\x95\x01\xa9\xa9h\x83\x1a\xe8\x8f\x9c\x03\xbd\xd8\x82F^d\x19\x1b`"\xc8\x92\xee\xdd\xd1\xa6[\xbe\xc1S\xc7\xc2\x08\xbe)\xbbfR\npJNJ\r\xf8\xa3\xe24&\xb9=\xf4\xcb\xc9\xfa\xadX\xedB\r$\x98Cg/\x9c\xce\x0byZ\x18\xe5U\xc1\xae\xa7\xda\xc2\'\xec\xf2\x13<"\x89\xabcmu\x04\x06\xd3\xb9l\xc6\xc8\x17H\x14\xc2\x95\xe1\xe2\x8e\x9e\xcf\x16\xca\xe1R\xd0\xf8\xbbh\x08\x1e\xb9\xfb\xa1Z\xcb\x99\x1a\xd4\x0e\xe9%d{[\xc5E\x04+n\xfa\x01\xf8\x81\xa0\x81\x16\xcfY&\x1d\x16U\xe6"#\xaa\x165LqCKq,\xe4\xe8+\xd6\x82\xd2\xdf\xcc6W\x83x\xd0\xf2\n\xde\x91\\p\x91UP0`\xb9\x95l\x94d\xf4q\x14\xe8\xba\xce1\xa3\r\xda\xe92@\xf6c:+\x81\xeb\xca\xf2\xab\x8eX\x0fy\xa4\xfbRZ\x84\xe9Z\xcdq\x0f"\xe1\x96\xd1D\xa0\x01"\xf0A\x9dj/U3(\xc4\x05,3\xae\x81\x00GZ\xee\x18\x1e\xdc\xe7)\xcd\xa6I\xff7\x90\x8c \xb5=&p\xac9_\xc2M\xbeAf\xb9\x16\x99\x84\x1f\x85~7\xf5A\xd6ib\xabP\n#\xfb\xce\x83\x04y\xc2\xc5C\xefb/\x98\xc8\xdd\xcb}\x0f\xcc\x9d\xa4\x9c8c4\x8d\xab\xf1\'\x19\x80]\xa4\x1d\x10\x06,%\x93\xfa4\xc9\xf4\xaa[\xcb6.\xb5\xc8G\xc0\xc6M\xe7\xb0f\x17^\x9e\x13\x95\t\xc0\xa6\xb0ns\x80\xa2\x87\x98W\x06TN6\xd3\xd4\xab\xc5\'+)\x17\x0bE\xe2\xe6\xd8\r\xef\xa3\x13\xf7\xa5U%\x8f\x01\x8f\xe9!\xbbv\x1b\xd5CN\x84\x18-\x15\x06\xf5\xc929\x96[4\x9f1\x84\\C\xd4\x11;\x89\xd2W\xe7\x96e\xe0}\xcd\xbe\xb6\x00\x00$`\xd5\x98\xf8%\rE\x9f8\xb1\x0f!\x00\xf4P\xd8@w?\xc9\x91?\x99\xb56\n\x8f\xb6\x13\xe2\xb1\xfaXf\xb6\'\xfc\xe6\xe1\xbdF<\x83t3\x8b\x8a+\x1f\xf4`+\x85<M\xd6\xab\xfb\xd0WJ\xabG\xc4\x93\xa5\xcef\xb8\xbe\xaaH\x1a\xfd^\xdc\xa2\xb0\x94\xf0\xd9gX\xa6]f\x92^\xc5\x13\xe7\x93\x95R]F\xb7>2\xc6\x153P\xbe\xbasn\xb4D\xcd\xc2\xe3\xc8^\xe7&-b\xc24\xd2\xb9\xf8\xd2K!\x0eI\x819\xff\xa1\'\xaa\xaa\xd9\x94\xf6X\xde24&\xc5,-#\x18\xe8Y\xbe\xa7\x82\x80\x9a\xe4\xfe\xacY\xdbbh\x8dRb\xe8\xbd0\xb5\x9f\xcd\xcb\xab\xa3)\xcdF\xe5\x04\x06 \x83\x9f2\x97\xa9,\xf6\x07\xe2v\x9f]6\x1e\xc4N\x13\x9e\xd5\xe0,\x13\x00\xae\x10r8\x9e"\xb1\xa5\xced]J\xc7\x17\xf8]3\x03\xa5\xb9\xd2A\'\xbc\x02\xf8Q"\x0c\xaa\xa6\x1d\xc8\xd6\xbfpP\xe1:k\xc4\xdf!\xc3z\x19\x8f\x0enl\xca/\xbf\x987\xff^\xb1\xf4\xeb\xa6\xf9\x8f\x1cl&a`\xf6\x90\xcc\x87\xfc6\xa0U<\x91\x93\x06oC\xdcuEd\x104\xc7\xa3#\xe9\t\x0e\xb0iF\xf2m\x03\xa7\x1cN\xfe\x8c\xf0\x1e\xc9\xa6\xdc\xe7\xca\xcfbq\x97\x03\x92\x8diuY\xb8z\xcf\xf4!\x9a\x83\xf9\x91\x9f\x81fI"\x88\x81\x86\xa9V\xb0\xfd\x06Q\xd6\xd4\xfa\x1f_Z\xb2\xb3P\x97\xf2(9\xe4\x07\xc5\xf6t_K\x15\xa4x"\xaa\n\xc6<\x18O\x86M\xd7Z\xa4ii\x07uin2\xb7\xe1\x9d\xe7\xc3\xc0\xa0N0D\x94\xa9\x06e\xa3\xeb\xb0c\xf9\xf2=}\x91e\xd9\x02\xbeT\xf0<;\xb6\x1c\x01\x9f\xe7\xcb\x0c>}k[\xa0+\xf0\xab\x06\xd9Gg\xf0,\xbb\xd7\xaa\xeeo\x89\xa7d=g\xb9\x07\xb1n\n\x17\xf8E*\x8f\xb6N \xcf\xfa\x87\xf5`\x8f\xc7\xcdXT{\xb8\x12:<i\x17y%X\xc4\xa2\xc1v\x84\xa3@\xf1Jq\x9cG\x15\xec\xd7W\xddr\xf2Q\xafO\x80\xcd\xbc+Kq\x8c\xa0\xa3\xc8\xcc\x9b_\xebu/b\x94y/o\xf8@#0\x82\xfa\x08j\xb4\xc2\x05\x84o\xa5\xe2\xb3\xf7\xd9F\xdc\x8b\xfce\xef\x12\xe4*FK\x98(n\x12\x14\x89T\xf4\xfb\x9eh\xeaY\x89\x84\x1b\x90\x10G"\x12\x11\x86\x89\xdb|\xf9.\xa6\xef\'\xc8V\xe7<\n7B\xacE\xcc\xb2\xaf\xaa\xee\xf8J\xb1Y\xcf\xb2l\xe6\xf1\x17a\x11\xf8\xb3~\xc7\xaa\x9e\x9d\xf6\xbd\xce\xf20\x8aIO\xean\xcb\'\x9a\x02\xb4\xaf:\xfe,4\xfc&j\xeb\x105\xe7\xe4Z\x12\xee&\xe9j\xe3\xe2\xb9B\t\xa0C8K@=\xb6N\x8bu\xfcKY\xbf\xb3\x0f\xc9\xe3&+\xc1\xeaz\xe7\x1a\x94-V\x18s|,B\xb6\x93\xc0]\x8b\x07\xd8e\xb9m\x85\xa1\x00\x92s\xd5q\x1b\xddf\x88E\xe7\xd0\xb0\xac\xf5\xc4\xb7\x18\x00\xf6\xb5ss?E\xdc\x0bZr^&\x82\x17U\xf9\x0b}Y4\xe3_\xd5t\xfc\x9e-\xf6Y\x04FHs\xc2\x85\x91\xb2b\xfb\xc3d\x12X0\x94\xa7D\xd0\xd32\x12]\xf4t\xa7\xdf\xee\xb3\x12!\xf9\xa5\xb3e\x15\x10\x9b\xc5\xe2I\xb6\xbe\xb3\xa6\t\xcaa\xfft\x1a\xa19d\x981]\x04\x11\xa1wv\xe4Z\x1e\x84w\xf1\xa3\xe0\xf9\xb5\x18\x13\x99f\xa5\xf4\xbb\x0e\xbe\x95.\xbbj\n\x85\x91*\xeb\xe3\xa6\xb7\xe2\xa6\xddpgd \xba\x00\xa1<\x83\xe6\xa5\'W\xb8O\xcd\xc3\x88)gc\xaa\x81U\xf3\x14_7\xb3i\x1d4\xd4\x8b\xca@\xb9\x82/(_MaO\xd0\xea\xc81\xc7\xc7\xa2\x1b\x0bG\x17\xf4\x9eZ\x81\x14\xad\x91\x04\xd0\x93<\xd0\x05\xc5\xb6C\x1e&4\x90\xb2Al\x8e\x10\x9f5\xb8\xab\xac\x99\xc1\xd6ai\xfb\xa2g,\xd9UAfi\xc7C\xed\xd2\xcdU\x16\x9a#(\xe6,\x85\xdd\xf2q\xf1\xaf\x02kU\xd5\xb6\x82\xb8\xadK\xadUy)\x8e8T:\x87\xa7\xe80]\xaa\xc9\xf7\xac\x9b}\r\xf0\x06\xe1\xda\x96Bc\x97\xde\x82\xaa6\xd2\x12"MV\x0fL\xb2}\xf5\x83\x08\x83\x95\xdf\x9e\xa7e\xedz\x92,1\xaaZ\xc0\xfcVk\xfd\x9a`\x0b\xfb\xd4\x00e\x88\xe0\xc2:\xd9p\x8b\x937\xa6\xa9\xb1U(\xfdWN\xb0\x05\xdf\xc3\x93f\xefB\x8ciU\xb9\\N\xa4|+\'Q\x8aI\xa0.\xab\x11\xed\xc9\xd3F\x088\xe2"\'V\xc5\xe7\x0b\xb4\x82\xc2\xaa\xfb\x08uva\xba\x86\xf8\xd2\x14\x1bpD\x18\xce\x17\x1d"e\xc0J\xc1C \xb2\xca\xc5J\xc3\xac`\xc7*%\xbbBBH_\xd8\xaf\x11o6{\xd1$W\xc3\xf7\x0bI\x01R\xeb7\xd4\xb1<\x05\xb0\xb9\xc6X$7B\xb6\xcf\xe8\xfa\x9e\n\xa2\xdc9\x04\'6"+\x0c\x9c\xb3\x8f,\xed2\xf0\xac\x19\x979$\xceF\x96~(Z\xc3\xc4\xbc,IG\xa1\xe6\xf5C\x82\x7f.1\xc2\x95\xab\xa1\xd43\xb8j\xf9\xb4\x94\x00\x83ud\x8d\x07\xf3\x10\'\x19\x19\x05e\n\x1e\xffMU\xacP\xf1\xbd\r\x0bY\x0b@\x07\xa1\xb4\xf1\x98\xda\xa0\x94$R\xf9\x1bJ\xa0\x03K8YT\xa3\x9f,\xf1\xf5\x8a\xd4t75\x90\x85s8\x15\x1c\xa8."\x89\xb7(\x10K\x19\x8eYoM\xf0j\x05\xd8ia\x7f\x08\xe8i\xe4,g\xbeC\xfd\xa2j\x8b\xce\xd9\x0b\xfd*\xe5\x06\xc5Y-@t\x0c\x03\xa3\xdc\xd9\xafd\xf1\xdc\x88\xd8w\x9d+\x9c\xb8\x92\xfb\xeb(\x16cXl\xb9\x94=\x00\x80\x85\x14a\xa2a\x01]v"\xe20\xcd\xec5\xd7\x0c\x97R\xe3\xe3 \xa1_yU\x07\xeax\xb2\x1c\xacll\x0f\x01*X\x03\xb7\x14\xb6\x15\xc0\xc8"d+\xdb=\xe1\\i>\xa8.\x80n\x7f\n\xa6\xd2\xf2\x954\x9c\xd3\xfb\xa8*\x9d\x08\xbb\xbf#T\x82\xa4+\x1d\xcd\xed\xea\n\x18\xe3E\x05\x83\xa1\x0bj\x85\x14\xf8J\x87\xdf\xc3C\x00\xc3)\x06B:\xfe-\xa6\xbd|\x94\xad\x13\xa7n\xd4J\xbcTj)\x07\xf9\xca\xa8\xb0^\xea\xd77\xd7S\x1b/\x162n\xe3\xc0\xf1\xa5\\A-\xd7y\x81\xed\x81\x9c~\xed\x1a\xbd\x1a\x8e99v\x15\xbc\xa5t\xa617p\xea\x8b\xe9ib,\xdaJTX\xd0\xb6\xae\xa3:\xc4Y\x83\x18\xd72\xdea\xb8 3\x1b\x87\x19\x91J\xeam.\xb6\xf1D^\xc5\x012\xb7\x01.YR\x1b\xe1\x9d\x92\x16`d2kw\x01\xf2\xb2Fi\x0cQY\xa8_\xe5\x10x1`\xb6~\x89\x13\x0f\xdf\xe6\xe6+\x1c\xce\xea\xef\x88\xe3\r\xc6\x9e\xeaja\xc6s\xd7\xccKz\xa7};\xed\xf8\r\xe7\x81\x8c\x84*\xe2\xd4<m\xf2\xb3v\xf5\x9b:\xcb\xf7U\xe2\x1f\x05&\x03\x04:\x9cS\xcbs&Kf\x92f\x19mA\x82\xb2*X\xb2\xb4\x922 -E\xee\x9f3\xe0\x99\xbb\x9c\xb5\xf3\xdb\xa3\xc2xa\x83\xf7\x9cX\xff\xb6\xcc\x95UX\xf3\x1d\xce\xb8\x95x=\x83\xcd\x07\xca\x19\x83\x06\xa2\xd5\xc2\xe6\xc2\x0ch\xb2\xcc\x08r\xe7\xe9\xf1(\x9a\r\x01H\xac\xc9\x8f\xf2\xde\xd7\xb3\x04?\x91\xa6\x88\x0c\x87\xf4\xb6\x02\xd9g\xa3\xc5+\xb63\xdb\xc6\x08\x05\x19f1\xe3pk^q\xd7cV\xb2E\x19\xba\xb5\xabh\x0e\x84\xf0\x8c\xf1\xed"\xf7\xc9\x02@\x18\xe7\xfb\xf9\x86\xe2<\xb4\x84\xfa\xf2I\xbb\x18\\\xc5\'\x87f\xe3,\x1cx\x08\xb0pwj\x10S\xaaw\x0f#O\xa5\x04%K+\x11\x0b\xd5\xd2\xbb\xcc\x87\xdbf\x1e\x0b;\xfd\xf8l\x86\x95\xad\x1f\x83MoE4=E\x0c\x95\xec\xc6\xf6\xcf\xdb\xa2\x8f[+f\'\xc6\xe8\x01-jn\xc4lT"\xae*\x157\x97e\xbc`\xcdrbR\xd88\x83G\x9cv\xff}Dz\x84\xd78\xb7\xa3\xf5=\xc16O\x98\n\xd9\x7f\x9c\x8bX,\x96r\x84K]\xd4|\xaf\x18y\xcaF\xed\xb7\x1a\xf7\xe3\x8b\xc3\xb7%\x82\x8dI\xab@\xb8\x8c\xd5\xe6+\x15\xcb\x8fnK\x83\r\xd1\xf5\xc4!t:\xbd\n\x8c;{\xef*\x8a\xba\xca\xc9\xf0\x1f\xd1`\xcc+:\xbbe2O\x1f\xe3:\xa0r\x05y\xba\xb5\xc8!r\x9b\xc4?\xb3\xf75\xe2.EKA6\x9a%\xaaJo2{P0N\xbd\xd6\xb0\x17W\x12=S\xd4U\\u\xf4\xaeEJ\xc5\xd7\x0bO\x80\xc4\xba\x96h\xe0\xb6b\xba\x01\xeeY8\xd9\xffX\x9a;\x950P\xfb\x96Q[LV\xc3\xd6I\xae\x8c=j\xd8\x08\x07o\x08L\x91\'\xed\xf2\x99\xce:3\x15\xa6\xc1w\xc6\x01\xd1\xccQ\xb0U\x91\xd3\xf8\xa7\xab\xde\xd7\xf82\x83E\x96\xd9:\xf0$S\xed\xf1|K1\xbc\xe3\xfcxv\xbc\x99\xe7\x8a\x13\xe9)\x0c\x86\x9d\xc4\x9c\x95\x11k\xc1\x12\x80\xe1\xf2\xb9[!)\xd9\x88+tX\x0c\xd0\xd0\xd6\x05\x14\xcc\x95\xf1\xdfc\x99\xc5|B\x9d\xca\'\x1bA\xa7k\xab\xf0o\xe3\xf0\x80\x083\xc8\xde\x06\xb6^%;CXT\xad\xfc\xfdT$\xaf\x93\xdd\'\xc2\xf2\x80\x1b\xa5\xd7\x03\x08\x15\xdc%\x0f\xa5\x10e\xad\xdf2$\xcd\x1c\xa2\xb8\r[\x0e\x15\x9d&\xc0:\xb2\xe3T\xea\x9d\xcc4\xafX\xb5\x05O\x86\xd4\xd5@\xdf\x82\x0c\xe8m\x16#O\xc0\x93_\x96\x8c\xb9\x84\x81\x12\x82\xf9w=\x86^\x8a\x99Wl\x1d\xfd\x16\xa2\xadu\x9c\x1c\xcf\xcb\xec\xef\x8e\xda\xe6k\x8d\xf9\xe5\xf2\xae`\xed\xfc\xd8\xcbC?!\x89Dp$\x7f\xf0\x07*t/\xd5PTN\x05\xc2\x894\xad\xe4\x80\x02OH4K\xbb]\xdcz\xc24Qn2\x8c\xc1m\xbe\x1fy\x02\xa6[\xa9<@\xa3\xfb\x90\xde\x07\xe5\x83\xee\x8a\xda\xc4\xb2\xe2\xf8\x97\x9a\xa9[j\xb3\xfe\x9cl\xdc\x90\x0f\x08\x7fK\x10\xbbX\xdc\x17F\xd1&4:|\x99\xf5\xdc\xed\xf39\xf6\xb3\xd5\xc69|u\x9a\x15cA\x1dZ\xdc\xb5\xbd\xcbn\'F\x83\xb6\xc96\x10\xaa\xa7\x0c\xbd_-\x91*\xe4\x0bE\xc3H\xd0Q%\xcb\xac\xc9\xec\xf5&\xac3\xf1\xdd\xe2\xc1|QX\xfc\x15O\xf1\xcc\xe2\xaa\x06\xb8\x85\xbe\x1e\x94\x9a\xb0\x14\x98K\x97\xfa\x19=\x96\x1dK\x8a\xfbE\xbc\x8d32\xcb=\xd9\xe3\xee\x9a\xcb9\xb2\xacLWi\xc8s[\xe2zT\xf0\xc3\x06\x80\x98\x8b\x88t\xb7\xb2\xfa\x1bg\'\x1e\xb4=\xf3\xf3\xc9A\x13\xf0\\\xa9/t\xbe\x9f\x82>\xa0v?\x9b\x13\x16\xe1\xea\x17\xa0\x98,4\x8ae\x84\xb8\xb9b\xe8\x832\x1c\x8fcA\x15+\x1aY\xcc\xa5{\xe6\x82(\xe7Q]>V\x19\xfe(\xc8\xb3\n\x9f\xa2\x1a\x8e\x0fS\x8b\xad\x80m*d\x15\xe6\xfdF\x9d\x92\x95\x1a\x8e\xe6\xae\x9eK\x96\x82\xb7\x12\xf7\x99\xc5[i\x87\xe9\xff\x1fPK\x01\x02\x14\x00\x14\x00\x00\x00\x08\x00\x05\xa6\x01U\r\xd4 {Z(\x00\x00@\x1f\x01\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb6\x81\x00\x00\x00\x00lorem_ipsum.txtPK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00=\x00\x00\x00\x87(\x00\x00\x00\x00'

# def make_byte_zip(target):
#     """Function to turn a folder into a byte-encoded zip"""
#     files = []
#     for f in os.scandir(target):
#         if f.is_file:
#             files.append(f)
#     with zipfile.ZipFile(
#         data := io.BytesIO(), "w", compresslevel=9, compression=zipfile.ZIP_DEFLATED
#     ) as z:
#         name = os.path.relpath(f.path, target)
#         z.write(f.path, name)
#     return data.getvalue()
# print(make_byte_zip("lorem_folder"))


def load_file_from_bytedata(bytedata, file):
    """Function to load a file from a byte-encoded zip"""
    with zipfile.ZipFile(data := io.BytesIO(bytedata)) as z:
        with z.open(file, "r") as f:
            return f.read().decode()


LOREM = load_file_from_bytedata(compressed_lorem, "lorem_ipsum.txt")
LOREM_SPLIT = LOREM.split("\n\n")
SPLIT_COUNT = len(LOREM_SPLIT)


def lorem(count=1):
    """Returns a given number of paragraphs of Lorem Ipsum."""
    OUT = ""
    for i in range(count):
        OUT += LOREM_SPLIT[(i + random.randint(0, 100)) % SPLIT_COUNT] + "\n\n"
    return OUT.strip()


if __name__ == "__main__":
    import sys, argparse

    try:
        if len(sys.argv) > 1:
            parser = argparse.ArgumentParser()
            parser.add_argument(
                "count", nargs="?", help="Number of paragraphs to return.", type=int
            )
            args = parser.parse_args()
            count = args.count
        else:
            count = 1
    except ValueError:
        print("Argument must be an integer")
        sys.exit(1)

    try:
        print(lorem(count))
    except Exception as e:
        sys.exit(1)

    sys.exit(0)
