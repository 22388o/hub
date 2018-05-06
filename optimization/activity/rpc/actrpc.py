from __future__ import print_function
import time
import json

import grpc

import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

import protobuffer.rpc_pb2 as proto
import protobuffer.rpc_pb2_grpc as proto_rpc


def actrpc_gen(file_name_inlet):
    with open(file_name_inlet) as f:
        inlet = json.load(f)

    duration = inlet['duration']

    with open(inlet['users_id_file_name']) as f:
        users_id = json.load(f)['users_id']

    with open(inlet['balances_file_name']) as f:
        balances = json.load(f)['balances']

    with open(inlet['transstream_file_name']) as f:
        transstream = json.load(f)['transstream']

    channel = grpc.insecure_channel('localhost:9393')

    stub = proto_rpc.EmulatorStub(channel)

    request = proto.SetBlockGenDurationRequest()
    request.duration = duration
    stub.SetBlockGenDuration(request)

    channels_id = dict()
    for key, user_id in users_id.items():
        request = proto.OpenChannelRequest()
        request.user_id = user_id
        request.locked_by_user = balances[key]
        response = stub.OpenChannel(request)
        channels_id[key] = response.channel_id

    with open(inlet['channels_id_file_name'], 'w') as f:
        json.dump({'channels_id': channels_id}, f,
                  sort_keys=True, indent=4 * ' ')


if __name__ == '__main__':
    actrpc_gen(file_name_inlet='actrpc_inlet.json')