import time
import json
from threading import Thread
import grpc
import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

import protobuffer.rpc_pb2 as proto
import protobuffer.rpc_pb2_grpc as proto_rpc


def set_blch_period(blch_period, stub):
    request = proto.SetBlockGenDurationRequest()
    request.duration = blch_period
    stub.SetBlockGenDuration(request)


def open_channels(users_id, balances, stub):
    channels_id = dict()
    open_request = proto.OpenChannelRequest()
    for key, user_id in users_id.items():
        open_request.user_id = user_id
        open_request.locked_by_user = balances[key]
        open_response = stub.OpenChannel(open_request)
        channels_id[key] = open_response.channel_id
    return channels_id


def set_blch_fee(fee, stub):
    request = proto.SetBlockchainFeeRequest()
    request.fee = fee
    stub.SetBlockchainFee(request)


def create_stub():
    rpc_channel = grpc.insecure_channel('localhost:9393')
    return proto_rpc.EmulatorStub(rpc_channel)


class TransactionThread(Thread):
    def __init__(self, stub, time_shift, transaction):
        Thread.__init__(self)
        self.stub = stub
        self.time_shift = time_shift
        self.transaction = transaction
        self.request = proto.SendPaymentRequest()

    def run(self):
        amount = round(self.transaction['payment']['amount'])
        if amount > 0:
            time.sleep(1.E-9 * self.transaction['time'] - self.time_shift)
            self.request.sender = self.transaction['payment']['sender']
            self.request.receiver = self.transaction['payment']['receiver']
            self.request.amount = amount
            try:
                self.stub.SendPayment(self.request)
            except Exception as er:
                print(er, 'is skipped')
            print(self.request)


def sent_transactions(stub, transseq):
    time_init = time.time()
    for i in range(len(transseq)):
        TransactionThread(stub, time.time() - time_init,
                          transseq[i]).start()


def actrpc_gen(file_name_inlet):
    with open(file_name_inlet) as f:
        inlet = json.load(f)

    blch_period = inlet['blch_period']

    blch_fee = inlet['blch_fee']

    with open(inlet['users_id_file_name']) as f:
        users_id = json.load(f)['users_id']

    del users_id['0']

    with open(inlet['user_balances_file_name']) as f:
        user_balances = json.load(f)['balances']

    with open(inlet['transseq_file_name']) as f:
        transseq = json.load(f)['transseq']

    time.sleep(1)

    stub = create_stub()

    set_blch_period(blch_period, stub)

    set_blch_fee(blch_fee, stub)

    channels_id = open_channels(users_id, user_balances, stub)

    time.sleep(1)

    sent_transactions(stub, transseq)

    with open(inlet['channels_id_file_name'], 'w') as f:
        json.dump({'channels_id': channels_id}, f,
                  sort_keys=True, indent=4 * ' ')


if __name__ == '__main__':
    actrpc_gen(file_name_inlet='actrpc_inlet.json')
