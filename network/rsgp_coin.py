from clove.network.bitcoin import Bitcoin


class Rsgpcoin(Bitcoin):
    """
    Class with all the necessary RSGPcoin (RSGP) network information based on
    https://github.com/ulandort/rsgprepo/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'rsgpcoin'
    symbols = ('RSGP', )
    seeds = ('node.walletbuilders.com')
    port = 19529


class RsgpcoinTestNet(Rsgpcoin):
    """
    Class with all the necessary RSGPcoin (RSGP) testing network information based on
    https://github.com/ulandort/rsgprepo/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'test-rsgpcoin'
    seeds = ()
    port = 29529
