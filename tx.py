
from application_client.ton_transaction import  CommentPayload
from tonsdk.utils import to_nano, bytes_to_b64str, Address
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

from client import TonCenterTonClient

from tonsdk.utils import Address, to_nano

def mainCoinTransfer():
    """your wallet mnemonics"""
    mnemonics = ['always', 'crystal', 'grab', 'glance', 'cause', 'dismiss', 'answer', 'expose', 'once', 'session',
                 'tunnel', 'topic', 'defense', 'such', 'army', 'smile', 'exhibit', 'misery', 'runway', 'tone', 'want',
                 'primary', 'piano', 'language']
    mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2,
                                                             workchain=0)
    forward_payload = CommentPayload("12345")
    client = TonCenterTonClient()
    result = client.seqno(wallet.address.to_string())
    query = wallet.create_transfer_message(
        "UQAON8ELGmF7Fa3Sdm2RsU5Lw2CNnZo9QVeXoF_07lTYqlk_",
        to_nano(0.01, "ton"),
        631,  # owner wallet seqno
        payload=forward_payload.to_message_body_cell()
    )
    boc = bytes_to_b64str(query["message"].to_boc(False))

    # message = client.send_boc(query["message"].to_boc(False))
    # print(message)



if __name__ == '__main__':
    mainCoinTransfer()
