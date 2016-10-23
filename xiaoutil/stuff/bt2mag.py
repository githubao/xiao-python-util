# !/bin/python

# import bencode, hashlib, base64, urllib
#
# torrent = open('C:\\Users\\BaoQiang\\Desktop\\123.torrent', 'rb').read()
# metadata = bencode.bdecode(torrent)
# hashcontents = bencode.bencode(metadata['info'])
# digest = hashlib.sha1(hashcontents).digest()
# b32hash = base64.b32encode(digest)
# params = {'xt': 'urn:btih:%s' % b32hash,
#       'dn': metadata['info']['name'],
#       'tr': metadata['announce'],
#       'xl': metadata['info']['length']}
#       # 'xl': metadata['info'].__len__}
# paramstr = urllib.urlencode(params)
# magneturi = 'magnet:?%s' % paramstr
# print magneturi

# import libtorrent as bt
# info = bt.torrent_info('123.torrent')
# print "magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name())