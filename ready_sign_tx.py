from os import write
from application_client.ton_transaction import Transaction, SendMode, CommentPayload,  JettonTransferPayload,StateInit
from tonsdk.contract.token.ft import JettonWallet
from tonsdk.utils import to_nano, bytes_to_b64str, Address
from tonsdk.contract.wallet import Wallets, WalletVersionEnum


def jettonTransferTx():
    """your wallet mnemonics"""
    mnemonics = ['always', 'crystal', 'grab', 'glance', 'cause', 'dismiss', 'answer', 'expose', 'once', 'session',
                 'tunnel', 'topic', 'defense', 'such', 'army', 'smile', 'exhibit', 'misery', 'runway', 'tone', 'want',
                 'primary', 'piano', 'language']
    mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2,
                                                              workchain=0)

    forward_payload = CommentPayload("12345")
    payload = JettonTransferPayload(amount=100000000,
                                    to=Address('UQAON8ELGmF7Fa3Sdm2RsU5Lw2CNnZo9QVeXoF_07lTYqlk_'),
                                    response_destination=Address('UQAON8ELGmF7Fa3Sdm2RsU5Lw2CNnZo9QVeXoF_07lTYqlk_'),
                                    query_id=10000000,
                                    forward_amount=100000,
                                    forward_payload=forward_payload.to_message_body_cell()
                                    )


    state_init = wallet.create_state_init()
    state = StateInit(code=state_init['code'], data=state_init['data'])

    tx = Transaction(Address("UQAON8ELGmF7Fa3Sdm2RsU5Lw2CNnZo9QVeXoF_07lTYqlk_"),
                     SendMode.PAY_GAS_SEPARATLY, 0, 1686176000, True, 100000000, state_init=state, payload=payload,
                     subwallet_id=698983191)

    print(tx.state_init.to_cell().bytes_hash().hex())

    print("应该生成的hash========")
    print(tx.transfer_cell().bytes_hash().hex())

    print("待签名数据========")
    print(tx.to_request_bytes().hex())






def mainCoinTransfer():
    """your wallet mnemonics"""
    mnemonics = ['always', 'crystal', 'grab', 'glance', 'cause', 'dismiss', 'answer', 'expose', 'once', 'session',
                 'tunnel', 'topic', 'defense', 'such', 'army', 'smile', 'exhibit', 'misery', 'runway', 'tone', 'want',
                 'primary', 'piano', 'language']
    mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2,
                                                              workchain=0)

    forward_payload = CommentPayload("12345")

    state_init = wallet.create_state_init()
    state = StateInit(code=state_init['code'], data=state_init['data'])

    tx = Transaction(Address("UQAON8ELGmF7Fa3Sdm2RsU5Lw2CNnZo9QVeXoF_07lTYqlk_"),
                     SendMode.PAY_GAS_SEPARATLY, 0, 1686176000, True, 100000000, state_init=state,
                     subwallet_id=698983191, payload=forward_payload)
    print(" 代签名数据=======")
    print(tx.to_request_bytes().hex())
    print(" 代签名hash=======")
    print(tx.transfer_cell().bytes_hash().hex())



if __name__ == '__main__':
    jettonTransferTx()
    # txTest()
    mainCoinTransfer()
    # mainCoinTransfer()
